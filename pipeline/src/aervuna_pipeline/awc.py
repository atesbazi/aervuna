"""NOAA AviationWeather.gov Data API client (https://aviationweather.gov/data/api/).

Licence: US public data; cite the source (docs/research/license-notes.md). Limits: at most
100 requests per minute and a custom User-Agent. We stay well below the limit (default 30/min),
batch station ids, retry with backoff on 429/5xx/timeouts and never retry other 4xx.

VERIFY: response field names (``icaoId``, ``rawOb``, ``site``, ``lat``, ``lon``, ``elev``,
``country``, ``siteType``) follow the public API documentation; they could not be checked
against a live response from the development sandbox (no egress to aviationweather.gov).
Parsing is defensive and observed values come from the raw report, not from these fields.
"""

from __future__ import annotations

import gzip
import json
import logging
import time
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any

import httpx

from aervuna_pipeline import __version__
from aervuna_pipeline.ratelimit import RateLimiter

log = logging.getLogger(__name__)

BASE_URL = "https://aviationweather.gov"
METAR_PATH = "/api/data/metar"
STATIONS_CACHE_PATH = "/data/cache/stations.cache.json.gz"
DEFAULT_USER_AGENT = f"aervuna-pipeline/{__version__} (+https://github.com/atesbazi/aervuna)"
MAX_IDS_PER_REQUEST = 50
DEFAULT_REQUESTS_PER_MINUTE = 30
RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})


class AwcError(RuntimeError):
    """Non-retryable or exhausted AviationWeather request failure."""


def chunked(items: Sequence[str], size: int) -> Iterator[list[str]]:
    for start in range(0, len(items), size):
        yield list(items[start : start + size])


class AwcClient:
    def __init__(
        self,
        user_agent: str | None = None,
        *,
        base_url: str = BASE_URL,
        requests_per_minute: int = DEFAULT_REQUESTS_PER_MINUTE,
        transport: httpx.BaseTransport | None = None,
        timeout_s: float = 20.0,
        max_attempts: int = 4,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        if requests_per_minute > 100:
            raise ValueError("AviationWeather allows at most 100 requests per minute")
        self._client = httpx.Client(
            base_url=base_url,
            headers={"User-Agent": user_agent or DEFAULT_USER_AGENT},
            timeout=timeout_s,
            transport=transport,
            follow_redirects=True,
        )
        self._limiter = RateLimiter(requests_per_minute, sleep=sleep)
        self._max_attempts = max_attempts
        self._sleep = sleep

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> AwcClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _get(self, path: str, params: dict[str, str] | None = None) -> httpx.Response:
        last_error: str = ""
        for attempt in range(1, self._max_attempts + 1):
            self._limiter.acquire()
            try:
                response = self._client.get(path, params=params)
            except httpx.TransportError as exc:
                last_error = f"{type(exc).__name__}: {exc}"
            else:
                if response.status_code < 400:
                    return response
                if response.status_code not in RETRY_STATUSES:
                    raise AwcError(f"GET {path} -> HTTP {response.status_code}")
                last_error = f"HTTP {response.status_code}"
            if attempt < self._max_attempts:
                delay = min(60.0, 2.0**attempt)
                log.warning(
                    "GET %s failed (%s); retry %d in %.0fs", path, last_error, attempt, delay
                )
                self._sleep(delay)
        raise AwcError(f"GET {path} failed after {self._max_attempts} attempts: {last_error}")

    def fetch_metars(self, icaos: Iterable[str], hours: int = 3) -> list[dict[str, Any]]:
        """Return METAR/SPECI records for ``icaos`` from the last ``hours`` hours."""
        ids = sorted({i.upper() for i in icaos})
        records: list[dict[str, Any]] = []
        for batch in chunked(ids, MAX_IDS_PER_REQUEST):
            response = self._get(
                METAR_PATH, {"ids": ",".join(batch), "format": "json", "hours": str(hours)}
            )
            if response.status_code == 204 or not response.content.strip():
                continue
            payload = response.json()
            if not isinstance(payload, list):
                raise AwcError(f"unexpected METAR payload type: {type(payload).__name__}")
            records.extend(r for r in payload if isinstance(r, dict))
        return records

    def fetch_stations_cache(self) -> list[dict[str, Any]]:
        """Return the full station catalogue (gzipped JSON cache file)."""
        response = self._get(STATIONS_CACHE_PATH)
        body = response.content
        if body[:2] == b"\x1f\x8b":
            body = gzip.decompress(body)
        payload = json.loads(body)
        if not isinstance(payload, list):
            raise AwcError(f"unexpected stations payload type: {type(payload).__name__}")
        return [r for r in payload if isinstance(r, dict)]
