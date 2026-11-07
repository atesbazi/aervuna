"""Command line entry point: ``aervuna-pipeline <command>``."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
from typing import Any

import psycopg

from aervuna_pipeline.awc import AwcClient, AwcError
from aervuna_pipeline.db import ConfigError, connect
from aervuna_pipeline.metar import archive
from aervuna_pipeline.metar.coverage import coverage, format_table
from aervuna_pipeline.stations.catalog import CatalogError, select_stations, upsert_stations

log = logging.getLogger("aervuna_pipeline")


def _client() -> AwcClient:
    return AwcClient(os.environ.get("METAR_USER_AGENT") or None)


def sync_stations(conn: psycopg.Connection[Any], client: AwcClient) -> int:
    stations = select_stations(client.fetch_stations_cache())
    return upsert_stations(conn, stations)


def _sync_best_effort(conn: psycopg.Connection[Any], client: AwcClient) -> None:
    try:
        sync_stations(conn, client)
    except (AwcError, CatalogError):
        log.exception("station catalogue sync failed; archiving the stations already stored")
        conn.rollback()


def _hour_floor(value: datetime) -> datetime:
    return value.replace(minute=0, second=0, microsecond=0)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="aervuna-pipeline")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="group", required=True)

    stations = sub.add_parser("stations", help="station catalogue (WX-017)")
    stations.add_subparsers(dest="action", required=True).add_parser(
        "sync", help="load pilot + LTxx stations from the NOAA stations cache"
    )

    metar = sub.add_parser("metar", help="METAR archive (WX-012)")
    metar_sub = metar.add_subparsers(dest="action", required=True)
    metar_sub.add_parser("once", help="fetch and store once")
    run = metar_sub.add_parser("run", help="sync stations, then archive every 10 minutes")
    run.add_argument("--interval", type=int, default=archive.RUN_INTERVAL_S)
    cov = metar_sub.add_parser("coverage", help="hourly completeness per active station")
    cov.add_argument("--days", type=int, default=7)
    cov.add_argument("--threshold", type=float, default=0.95)

    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    try:
        if args.group == "stations":
            with _client() as client, connect() as conn:
                changed = sync_stations(conn, client)
            print(f"stations inserted/updated: {changed}")
            return 0
        if args.action == "once":
            with _client() as client, connect() as conn:
                stats = archive.run_once(conn, client)
            print(stats)
            return 0
        if args.action == "run":
            with _client() as client:
                archive.run_forever(
                    connect,
                    client,
                    interval_s=args.interval,
                    on_start=lambda conn: _sync_best_effort(conn, client),
                )
            return 0  # pragma: no cover - run_forever does not return
        if args.action == "coverage":
            end = _hour_floor(datetime.now(UTC))
            start = end - timedelta(days=args.days)
            with connect() as conn:
                rows = coverage(conn, start, end)
            print(f"METAR coverage {start:%Y-%m-%dT%H:%MZ} .. {end:%Y-%m-%dT%H:%MZ}")
            print(format_table(rows, args.threshold))
            return 0 if rows and all(r.ratio >= args.threshold for r in rows) else 1
    except (ConfigError, AwcError, CatalogError, psycopg.Error) as exc:
        log.error("%s", exc)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
