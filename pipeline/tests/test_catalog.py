import json
from pathlib import Path
from typing import Any

import pytest

from aervuna_pipeline.stations.catalog import (
    PILOT_STATIONS,
    CatalogError,
    parse_station,
    select_stations,
)

FIXTURE = Path(__file__).parent / "fixtures" / "stations.json"


def records() -> list[dict[str, Any]]:
    data: list[dict[str, Any]] = json.loads(FIXTURE.read_text())
    return data


def test_selects_pilots_and_turkish_metar_stations_only() -> None:
    icaos = [s.icao for s in select_stations(records())]
    assert icaos == sorted([*PILOT_STATIONS, "LTCE"])


def test_string_elevation_is_parsed() -> None:
    ltce = next(s for s in select_stations(records()) if s.icao == "LTCE")
    assert ltce.elevation_m == 1757
    assert ltce.country == "TR"


def test_invalid_records_are_ignored() -> None:
    assert parse_station({"icaoId": "", "lat": 1, "lon": 1}) is None
    assert parse_station({"icaoId": "LTZZ", "lat": 123.0, "lon": 1.0}) is None
    assert parse_station({"icaoId": "LTZZ", "lat": True, "lon": 1.0}) is None


def test_missing_pilot_fails_loudly() -> None:
    without_rjtt = [r for r in records() if r.get("icaoId") != "RJTT"]
    with pytest.raises(CatalogError, match="RJTT"):
        select_stations(without_rjtt)
