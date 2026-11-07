"""Database fixtures. DB tests need TEST_DATABASE_URL (a server where the user may create
databases) and the ``dbmate`` binary; otherwise they are skipped with a reason. Each test
session creates a fresh database and applies db/migrations with dbmate (the same tool and
files production uses)."""

from __future__ import annotations

import os
import shutil
import subprocess
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import psycopg
import pytest

from aervuna_pipeline.db import connect

MIGRATIONS = Path(__file__).resolve().parents[2] / "db" / "migrations"


def _with_db(url: str, name: str) -> str:
    parts = urlsplit(url)
    return urlunsplit(parts._replace(path=f"/{name}"))


@pytest.fixture(scope="session")
def database_url() -> Iterator[str]:
    admin_url = os.environ.get("TEST_DATABASE_URL")
    dbmate = shutil.which("dbmate")
    if not admin_url:
        pytest.skip("TEST_DATABASE_URL not set")
    if dbmate is None:
        pytest.skip("dbmate not on PATH")
    name = f"aervuna_test_{uuid.uuid4().hex[:8]}"
    with psycopg.connect(admin_url, autocommit=True) as admin:
        admin.execute(f'CREATE DATABASE "{name}"')
    url = _with_db(admin_url, name)
    try:
        subprocess.run(
            [dbmate, "--no-dump-schema", "--migrations-dir", str(MIGRATIONS), "up"],
            env={**os.environ, "DATABASE_URL": url},
            check=True,
            capture_output=True,
        )
        yield url
    finally:
        with psycopg.connect(admin_url, autocommit=True) as admin:
            admin.execute(f'DROP DATABASE IF EXISTS "{name}" WITH (FORCE)')


@pytest.fixture
def conn(database_url: str) -> Iterator[psycopg.Connection[Any]]:
    with connect(database_url) as c:
        c.execute("TRUNCATE own.metar_observations, own.ecmwf_point_forecasts, own.stations")
        c.commit()
        yield c
