"""Station catalogue (WX-017): pilot stations + every Turkish (LTxx) METAR station.

Source: NOAA AviationWeather stations cache. Coordinates and elevation come from the source,
never from hand-written tables, so interpolation (WX-013) uses audited station metadata.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

import psycopg

log = logging.getLogger(__name__)

SOURCE = "noaa-awc-stations-cache"
PILOT_STATIONS: tuple[str, ...] = (
    # Turkey
    "LTAC",  # Ankara Esenboga
    "LTFM",  # Istanbul
    "LTBJ",  # Izmir Adnan Menderes
    "LTAI",  # Antalya
    # Global
    "EGLL",  # London Heathrow
    "EDDF",  # Frankfurt
    "KJFK",  # New York JFK
    "RJTT",  # Tokyo Haneda
)
TURKEY_PREFIX = "LT"


class CatalogError(RuntimeError):
    pass


@dataclass(frozen=True)
class Station:
    icao: str
    name: str
    lat: float
    lon: float
    elevation_m: int | None
    country: str | None


def _float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None


def _reports_metar(record: Mapping[str, Any]) -> bool:
    site_type = record.get("siteType")
    if site_type is None:
        return True  # field absent: do not exclude
    if isinstance(site_type, str):
        site_type = [site_type]
    return isinstance(site_type, list) and any(str(t).upper() == "METAR" for t in site_type)


def parse_station(record: Mapping[str, Any]) -> Station | None:
    icao = str(record.get("icaoId") or "").strip().upper()
    lat, lon = _float(record.get("lat")), _float(record.get("lon"))
    if len(icao) != 4 or not icao.isalnum() or lat is None or lon is None:
        return None
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        return None
    elev = _float(record.get("elev"))
    name = str(record.get("site") or icao).strip()
    raw_country = record.get("country")
    country = str(raw_country).strip() if raw_country is not None else ""
    return Station(
        icao=icao,
        name=name,
        lat=lat,
        lon=lon,
        elevation_m=round(elev) if elev is not None else None,
        country=country or None,
    )


def select_stations(
    records: Iterable[Mapping[str, Any]], pilots: Iterable[str] = PILOT_STATIONS
) -> list[Station]:
    """Pilot stations plus every LTxx station that reports METAR. Fails if a pilot is missing."""
    wanted = {p.upper() for p in pilots}
    selected: dict[str, Station] = {}
    for record in records:
        station = parse_station(record)
        if station is None:
            continue
        is_turkish = station.icao.startswith(TURKEY_PREFIX) and _reports_metar(record)
        if station.icao in wanted or is_turkish:
            selected[station.icao] = station
    missing = sorted(wanted - selected.keys())
    if missing:
        raise CatalogError(f"pilot stations missing from catalogue: {', '.join(missing)}")
    return sorted(selected.values(), key=lambda s: s.icao)


UPSERT_SQL = """
INSERT INTO own.stations (icao, name, lat, lon, elevation_m, country, kind, active, source,
                          updated_at)
VALUES (%(icao)s, %(name)s, %(lat)s, %(lon)s, %(elevation_m)s, %(country)s, 'airport', true,
        %(source)s, now())
ON CONFLICT (icao) DO UPDATE SET
    name = EXCLUDED.name,
    lat = EXCLUDED.lat,
    lon = EXCLUDED.lon,
    elevation_m = EXCLUDED.elevation_m,
    country = EXCLUDED.country,
    source = EXCLUDED.source,
    updated_at = now()
WHERE (own.stations.name, own.stations.lat, own.stations.lon, own.stations.elevation_m,
       own.stations.country)
      IS DISTINCT FROM
      (EXCLUDED.name, EXCLUDED.lat, EXCLUDED.lon, EXCLUDED.elevation_m, EXCLUDED.country)
"""


def upsert_stations(conn: psycopg.Connection[Any], stations: Iterable[Station]) -> int:
    """Insert new stations as active; update metadata of existing ones without touching
    ``active`` (an operator may have disabled a station). Returns rows inserted or changed."""
    rows = [
        {
            "icao": s.icao,
            "name": s.name,
            "lat": s.lat,
            "lon": s.lon,
            "elevation_m": s.elevation_m,
            "country": s.country,
            "source": SOURCE,
        }
        for s in stations
    ]
    changed = 0
    with conn.cursor() as cur:
        for row in rows:
            cur.execute(UPSERT_SQL, row)
            changed += cur.rowcount
    conn.commit()
    log.info("station catalogue: %d stations, %d inserted/updated", len(rows), changed)
    return changed


def active_stations(conn: psycopg.Connection[Any]) -> list[str]:
    with conn.cursor() as cur:
        cur.execute("SELECT icao FROM own.stations WHERE active ORDER BY icao")
        return [row[0] for row in cur.fetchall()]
