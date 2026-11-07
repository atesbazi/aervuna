"""Minimal blocking rate limiter: at most ``per_minute`` calls in any 60 s window."""

from __future__ import annotations

import time
from collections import deque
from collections.abc import Callable


class RateLimiter:
    def __init__(
        self,
        per_minute: int,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        if per_minute < 1:
            raise ValueError("per_minute must be >= 1")
        self._limit = per_minute
        self._clock = clock
        self._sleep = sleep
        self._calls: deque[float] = deque()

    def acquire(self) -> None:
        while True:
            now = self._clock()
            while self._calls and now - self._calls[0] >= 60.0:
                self._calls.popleft()
            if len(self._calls) < self._limit:
                self._calls.append(now)
                return
            self._sleep(60.0 - (now - self._calls[0]))
