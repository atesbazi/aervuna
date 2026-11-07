import gzip
import json
from pathlib import Path

import httpx
import pytest

from aervuna_pipeline.awc import DEFAULT_USER_AGENT, AwcClient, AwcError
from aervuna_pipeline.ratelimit import RateLimiter


def make_client(handler: httpx.MockTransport, sleeps: list[float]) -> AwcClient:
    return AwcClient(transport=handler, sleep=sleeps.append)


def test_metar_request_batches_ids_and_sends_user_agent() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        ids = request.url.params["ids"].split(",")
        return httpx.Response(200, json=[{"icaoId": i, "rawOb": f"METAR {i}"} for i in ids])

    icaos = [f"LT{chr(65 + i // 26)}{chr(65 + i % 26)}" for i in range(60)]
    with make_client(httpx.MockTransport(handler), []) as client:
        records = client.fetch_metars(icaos, hours=3)
    assert len(records) == 60
    assert [len(r.url.params["ids"].split(",")) for r in seen] == [50, 10]
    assert all(r.url.params["format"] == "json" and r.url.params["hours"] == "3" for r in seen)
    assert seen[0].headers["User-Agent"] == DEFAULT_USER_AGENT


def test_no_content_is_empty() -> None:
    transport = httpx.MockTransport(lambda _: httpx.Response(204))
    with make_client(transport, []) as client:
        assert client.fetch_metars(["LTAC"]) == []


def test_retries_on_429_then_succeeds() -> None:
    calls = {"n": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(429) if calls["n"] < 3 else httpx.Response(200, json=[])

    sleeps: list[float] = []
    with make_client(httpx.MockTransport(handler), sleeps) as client:
        assert client.fetch_metars(["LTAC"]) == []
    assert calls["n"] == 3
    assert sleeps == [2.0, 4.0]


def test_client_errors_are_not_retried() -> None:
    calls = {"n": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(400)

    with make_client(httpx.MockTransport(handler), []) as client, pytest.raises(AwcError):
        client.fetch_metars(["LTAC"])
    assert calls["n"] == 1


def test_gives_up_after_max_attempts_on_timeouts() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectTimeout("timeout", request=request)

    sleeps: list[float] = []
    with make_client(httpx.MockTransport(handler), sleeps) as client, pytest.raises(AwcError):
        client.fetch_metars(["LTAC"])
    assert len(sleeps) == 3


def test_stations_cache_is_gunzipped() -> None:
    fixture = (Path(__file__).parent / "fixtures" / "stations.json").read_bytes()
    transport = httpx.MockTransport(lambda _: httpx.Response(200, content=gzip.compress(fixture)))
    with make_client(transport, []) as client:
        stations = client.fetch_stations_cache()
    assert stations == json.loads(fixture)


def test_rate_limit_above_provider_maximum_is_refused() -> None:
    with pytest.raises(ValueError, match="100"):
        AwcClient(requests_per_minute=101)


def test_rate_limiter_waits_when_window_is_full() -> None:
    now = {"t": 0.0}
    sleeps: list[float] = []

    def sleep(seconds: float) -> None:
        sleeps.append(seconds)
        now["t"] += seconds

    limiter = RateLimiter(2, clock=lambda: now["t"], sleep=sleep)
    limiter.acquire()
    now["t"] = 10.0
    limiter.acquire()
    limiter.acquire()  # third call within 60 s must wait until t = 60
    assert sleeps == [50.0]
