"""Archive completeness (WX-012 acceptance: >= 95 % of expected observations over 7 days).

Expected observations are counted per UTC hour: a station is complete for an hour when at
least one METAR/SPECI was stored for it. This is cadence-neutral (LTxx/EGLL/RJTT report
every 30 min, KJFK hourly) and matches the verification pairing window of +/- 30 min
(docs/architecture/05-forecast-verification.md). Decision recorded in docs/progress.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import psycopg

COVERAGE_SQL = """
WITH hours AS (
    SELECT generate_series(date_trunc('hour', %(start)s::timestamptz),
                           %(end)s::timestamptz - interval '1 hour',
                           interval '1 hour') AS h
),
obs AS (
    SELECT DISTINCT m.icao, hours.h
    FROM own.metar_observations m
    JOIN hours ON date_trunc('hour', m.observed_at) = hours.h
    WHERE m.observed_at >= date_trunc('hour', %(start)s::timestamptz)
      AND m.observed_at < %(end)s
)
SELECT s.icao,
       (SELECT count(*) FROM hours) AS expected,
       count(o.h) AS observed
FROM own.stations s
LEFT JOIN obs o ON o.icao = s.icao
WHERE s.active
GROUP BY s.icao
ORDER BY s.icao
"""


@dataclass(frozen=True)
class Coverage:
    icao: str
    expected_hours: int
    observed_hours: int

    @property
    def ratio(self) -> float:
        return self.observed_hours / self.expected_hours if self.expected_hours else 0.0


def coverage(conn: psycopg.Connection[Any], start: datetime, end: datetime) -> list[Coverage]:
    if start.tzinfo is None or end.tzinfo is None:
        raise ValueError("start and end must be timezone-aware")
    if end <= start:
        raise ValueError("end must be after start")
    with conn.cursor() as cur:
        cur.execute(COVERAGE_SQL, {"start": start, "end": end})
        return [Coverage(icao, int(exp), int(obs)) for icao, exp, obs in cur.fetchall()]


def format_table(rows: list[Coverage], threshold: float) -> str:
    lines = ["| ICAO | Expected h | Observed h | Coverage | OK |", "|---|---|---|---|---|"]
    for r in rows:
        ok = "yes" if r.ratio >= threshold else "NO"
        lines.append(
            f"| {r.icao} | {r.expected_hours} | {r.observed_hours} | {r.ratio:.1%} | {ok} |"
        )
    return "\n".join(lines)
