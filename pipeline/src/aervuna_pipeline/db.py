"""Database connection helper. Sessions run in UTC so date_trunc() buckets are UTC hours."""

from __future__ import annotations

import os
from typing import Any

import psycopg


class ConfigError(RuntimeError):
    pass


def database_url() -> str:
    url = os.environ.get("DATABASE_URL", "").strip()
    if not url:
        raise ConfigError("DATABASE_URL is not set (see .env.example)")
    return url


def connect(url: str | None = None) -> psycopg.Connection[Any]:
    return psycopg.connect(url or database_url(), options="-c TimeZone=UTC")
