"""Integration tests against a migrated database (skipped without TEST_DATABASE_URL)."""

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import psycopg
import pytest

from aervuna_pipeline.metar.archive import run_once
from aervuna_pipeline.metar.coverage import coverage
from aervuna_pipeline.stations.catalog import active_stations, select_stations, upsert_stations

FIXTURE = Path(__file__).parent / "fixtures" / "stations.json"
NOW = datetime(2026, 11, 7, 20, 5, tzinfo=UTC)


class FakeAwc:
    def __init__(self, records: list[dict[str, Any]]) -> None:
        self.records = records
        self.requested: list[str] = []

    def fetch_metars(self, icaos: list[str], hours: int = 3) -> list[dict[str, Any]]:
        self.requested = list(icaos)
        return self.records


def load_stations(conn: psycopg.Connection[Any]) -> None:
    upsert_stations(conn, select_stations(json.loads(FIXTURE.read_text())))


def run(conn: psycopg.Connection[Any], records: list[dict[str, Any]]) -> Any:
    return run_once(conn, FakeAwc(records), now=lambda: NOW)  # type: ignore[arg-type]


def test_schemas_and_tables_exist(conn: psycopg.Connection[Any]) -> None:
    rows = conn.execute(
        "SELECT table_schema || '.' || table_name FROM information_schema.tables "
        "WHERE table_schema IN ('own', 'licensed') ORDER BY 1"
    ).fetchall()
    assert [r[0] for r in rows] == [
        "own.ecmwf_point_forecasts",
        "own.metar_observations",
        "own.stations",
    ]
    schemas = conn.execute(
        "SELECT nspname FROM pg_namespace WHERE nspname IN ('own', 'licensed') ORDER BY 1"
    ).fetchall()
    assert [r[0] for r in schemas] == ["licensed", "own"]


def test_hypertables_when_timescaledb_is_installed(conn: psycopg.Connection[Any]) -> None:
    installed = conn.execute("SELECT 1 FROM pg_extension WHERE extname = 'timescaledb'").fetchone()
    if installed is None:
        pytest.skip("timescaledb not installed on the test server")
    rows = conn.execute(
        "SELECT hypertable_schema || '.' || hypertable_name "
        "FROM timescaledb_information.hypertables ORDER BY 1"
    ).fetchall()
    assert [r[0] for r in rows] == ["own.ecmwf_point_forecasts", "own.metar_observations"]


def test_station_sync_is_idempotent_and_keeps_operator_deactivation(
    conn: psycopg.Connection[Any],
) -> None:
    load_stations(conn)
    assert len(active_stations(conn)) == 9
    conn.execute("UPDATE own.stations SET active = false WHERE icao = 'LTCE'")
    conn.commit()
    assert upsert_stations(conn, select_stations(json.loads(FIXTURE.read_text()))) == 0
    assert "LTCE" not in active_stations(conn)


def test_archive_run_is_idempotent(conn: psycopg.Connection[Any]) -> None:
    load_stations(conn)
    records = [
        {"icaoId": "LTAC", "rawOb": "METAR LTAC 071950Z 04006KT CAVOK 08/M01 Q1024 NOSIG"},
        {"icaoId": "LTAC", "rawOb": "METAR LTAC 071920Z 04005KT CAVOK 09/M01 Q1024 NOSIG"},
        {"icaoId": "KJFK", "rawOb": "METAR KJFK 071951Z 31012KT 10SM FEW050 12/M03 A3012"},
        {"icaoId": "EHAM", "rawOb": "METAR EHAM 071955Z 24010KT 9999 FEW030 10/07 Q1015"},
        {"icaoId": "LTFM", "rawOb": "garbage"},
    ]
    first = run(conn, records)
    assert (first.received, first.parsed, first.written) == (5, 3, 3)
    assert first.skipped_unknown_station == 1
    assert first.parse_errors == 1
    second = run(conn, records)
    assert second.written == 0
    count = conn.execute("SELECT count(*) FROM own.metar_observations").fetchone()
    assert count == (3,)
    temp = conn.execute(
        "SELECT temp_c, wx_codes FROM own.metar_observations "
        "WHERE icao = 'LTAC' AND observed_at = '2026-11-07T19:50Z'"
    ).fetchone()
    assert temp == (8.0, [])


def test_correction_replaces_report(conn: psycopg.Connection[Any]) -> None:
    load_stations(conn)
    run(conn, [{"rawOb": "METAR LTAC 071950Z 04006KT CAVOK 08/M01 Q1024"}])
    stats = run(conn, [{"rawOb": "METAR COR LTAC 071950Z 04006KT CAVOK 07/M01 Q1024"}])
    assert stats.written == 1
    row = conn.execute("SELECT temp_c FROM own.metar_observations").fetchone()
    assert row == (7.0,)


def test_coverage_counts_hours_with_at_least_one_report(conn: psycopg.Connection[Any]) -> None:
    load_stations(conn)
    start = datetime(2026, 11, 7, 16, 0, tzinfo=UTC)
    records = [  # LTAC: 16:20, 16:50 (same hour), 17:50, 19:50 -> 3 of 4 hours
        {"rawOb": f"METAR LTAC 07{hh}{mm}Z 04006KT CAVOK 08/M01 Q1024"}
        for hh, mm in (("16", "20"), ("16", "50"), ("17", "50"), ("19", "50"))
    ]
    run(conn, records)
    rows = {r.icao: r for r in coverage(conn, start, start + timedelta(hours=4))}
    assert (rows["LTAC"].expected_hours, rows["LTAC"].observed_hours) == (4, 3)
    assert rows["LTAC"].ratio == 0.75
    assert rows["KJFK"].observed_hours == 0
    assert len(rows) == 9
