"""METAR archiver (WX-012): fetch recent reports for active stations, upsert idempotently.

Each run asks for the last ``hours`` hours, so a missed run (network, restart) is backfilled by
the next one. The primary key (icao, observed_at) makes re-runs no-ops; a corrected report
(COR) with the same time replaces the stored one.
"""

from __future__ import annotations

import logging
import time
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import psycopg

from aervuna_pipeline.awc import AwcClient, AwcError
from aervuna_pipeline.metar.parse import Metar, MetarParseError, parse_metar
from aervuna_pipeline.stations.catalog import active_stations

log = logging.getLogger(__name__)

RUN_INTERVAL_S = 600
LOOKBACK_HOURS = 3


@dataclass
class RunStats:
    received: int = 0
    parsed: int = 0
    written: int = 0
    skipped_unknown_station: int = 0
    parse_errors: int = 0


def parse_records(
    records: Iterable[Mapping[str, Any]], fetched_at: datetime, known: set[str], stats: RunStats
) -> list[Metar]:
    out: dict[tuple[str, datetime], Metar] = {}
    for record in records:
        stats.received += 1
        raw = record.get("rawOb")
        if not isinstance(raw, str) or not raw.strip():
            stats.parse_errors += 1
            continue
        try:
            metar = parse_metar(raw, fetched_at)
        except MetarParseError as exc:
            stats.parse_errors += 1
            log.warning("unparseable METAR skipped: %s", exc)
            continue
        if metar.icao not in known:
            stats.skipped_unknown_station += 1
            continue
        stats.parsed += 1
        key = (metar.icao, metar.observed_at)
        # Prefer a SPECI/COR that arrives later in the payload over an earlier duplicate.
        out[key] = metar
    return list(out.values())


UPSERT_SQL = """
INSERT INTO own.metar_observations (icao, observed_at, report_type, temp_c, dewpoint_c,
    wind_dir_deg, wind_speed_kt, wind_gust_kt, visibility_m, pressure_hpa, wx_codes, raw,
    fetched_at)
VALUES (%(icao)s, %(observed_at)s, %(report_type)s, %(temp_c)s, %(dewpoint_c)s,
    %(wind_dir_deg)s, %(wind_speed_kt)s, %(wind_gust_kt)s, %(visibility_m)s, %(pressure_hpa)s,
    %(wx_codes)s, %(raw)s, %(fetched_at)s)
ON CONFLICT (icao, observed_at) DO UPDATE SET
    report_type = EXCLUDED.report_type,
    temp_c = EXCLUDED.temp_c,
    dewpoint_c = EXCLUDED.dewpoint_c,
    wind_dir_deg = EXCLUDED.wind_dir_deg,
    wind_speed_kt = EXCLUDED.wind_speed_kt,
    wind_gust_kt = EXCLUDED.wind_gust_kt,
    visibility_m = EXCLUDED.visibility_m,
    pressure_hpa = EXCLUDED.pressure_hpa,
    wx_codes = EXCLUDED.wx_codes,
    raw = EXCLUDED.raw,
    fetched_at = EXCLUDED.fetched_at
WHERE own.metar_observations.raw IS DISTINCT FROM EXCLUDED.raw
"""


def write_metars(
    conn: psycopg.Connection[Any], metars: Iterable[Metar], fetched_at: datetime
) -> int:
    written = 0
    with conn.cursor() as cur:
        for m in metars:
            cur.execute(
                UPSERT_SQL,
                {
                    "icao": m.icao,
                    "observed_at": m.observed_at,
                    "report_type": m.report_type,
                    "temp_c": m.temp_c,
                    "dewpoint_c": m.dewpoint_c,
                    "wind_dir_deg": m.wind_dir_deg,
                    "wind_speed_kt": m.wind_speed_kt,
                    "wind_gust_kt": m.wind_gust_kt,
                    "visibility_m": m.visibility_m,
                    "pressure_hpa": m.pressure_hpa,
                    "wx_codes": list(m.wx_codes),
                    "raw": m.raw,
                    "fetched_at": fetched_at,
                },
            )
            written += cur.rowcount
    conn.commit()
    return written


def run_once(
    conn: psycopg.Connection[Any],
    client: AwcClient,
    *,
    now: Callable[[], datetime] = lambda: datetime.now(UTC),
    hours: int = LOOKBACK_HOURS,
) -> RunStats:
    stats = RunStats()
    stations = active_stations(conn)
    if not stations:
        log.warning("no active stations; run `aervuna-pipeline stations sync` first")
        return stats
    records = client.fetch_metars(stations, hours=hours)
    fetched_at = now()
    metars = parse_records(records, fetched_at, set(stations), stats)
    stats.written = write_metars(conn, metars, fetched_at)
    log.info("metar run: %s", stats)
    return stats


def run_forever(
    connect: Callable[[], psycopg.Connection[Any]],
    client: AwcClient,
    *,
    interval_s: int = RUN_INTERVAL_S,
    on_start: Callable[[psycopg.Connection[Any]], None] | None = None,
) -> None:
    """Run every ``interval_s`` seconds, aligned to wall-clock multiples of the interval.
    Failures are logged and retried on the next tick; the loop never exits on its own."""
    started = False
    while True:
        try:
            with connect() as conn:
                if not started and on_start is not None:
                    on_start(conn)
                started = True
                run_once(conn, client)
        except (AwcError, psycopg.Error, OSError):
            log.exception("metar run failed; next attempt at the next tick")
        sleep_s = interval_s - (time.time() % interval_s)
        time.sleep(sleep_s)
