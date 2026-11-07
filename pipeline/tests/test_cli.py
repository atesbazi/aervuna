from typing import Any

import psycopg
import pytest

from aervuna_pipeline.cli import main


def test_missing_database_url_is_a_config_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert main(["metar", "coverage"]) == 2


def test_coverage_fails_below_threshold(
    conn: psycopg.Connection[Any], database_url: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    conn.execute(
        "INSERT INTO own.stations (icao, name, lat, lon, active, source) "
        "VALUES ('LTAC', 'Ankara', 40, 33, true, 'test')"
    )
    conn.commit()
    monkeypatch.setenv("DATABASE_URL", database_url)
    assert main(["metar", "coverage", "--days", "1"]) == 1
