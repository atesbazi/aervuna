"""Raw METAR/SPECI parser (WMO FM 15 / FM 16, ICAO Annex 3, US FMH-1 remarks).

We parse the raw report ourselves instead of trusting derived JSON fields so that the
archive stores values whose origin is auditable (docs/architecture/05-forecast-verification.md).
Only the main body is parsed; trend groups (NOSIG/TEMPO/BECMG) and recent weather (RExx)
never contribute to observed values. From RMK only the US T-group (tenths of a degree) is used.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta

KT_PER_MPS = 1.0 / 0.514444
KT_PER_KMH = 1.0 / 1.852
M_PER_SM = 1609.344
HPA_PER_INHG = 33.8639
CAVOK_VISIBILITY_M = 10000.0

_STATION = re.compile(r"^[A-Z][A-Z0-9]{3}$")
_TIME = re.compile(r"^(\d{2})(\d{2})(\d{2})Z$")
_WIND = re.compile(r"^(\d{3}|VRB)(\d{2,3})(?:G(\d{2,3}))?(KT|MPS|KMH)$")
_WIND_VAR = re.compile(r"^\d{3}V\d{3}$")
_VIS_M = re.compile(r"^(\d{4})(?:NDV)?$")
_VIS_SM = re.compile(r"^(M|P)?(?:(\d+)|(\d+)/(\d+))SM$")
_VIS_WHOLE = re.compile(r"^\d$")
_RVR = re.compile(r"^R\d{2}[LCR]?/")
_WX = re.compile(
    r"^(?:[+-]|VC)?(?:MI|PR|BC|DR|BL|SH|TS|FZ)?"
    r"(?:(?:DZ|RA|SN|SG|IC|PL|GR|GS|UP)+|BR|FG|FU|VA|DU|SA|HZ|PY|PO|SQ|FC|SS|DS)?$"
)
_CLOUD = re.compile(r"^(?:FEW|SCT|BKN|OVC|VV)(?:\d{3}|///)(?:CB|TCU|///)?$")
_TEMP = re.compile(r"^(M?\d{2})/(M?\d{2})?$")
_Q = re.compile(r"^Q(\d{4})$")
_A = re.compile(r"^A(\d{4})$")
_T_GROUP = re.compile(r"^T([01])(\d{3})([01])(\d{3})$")

_TREND_MARKERS = frozenset({"NOSIG", "TEMPO", "BECMG"})
_NO_CLOUD = frozenset({"SKC", "CLR", "NSC", "NCD"})


class MetarParseError(ValueError):
    """Raised when a report lacks the mandatory station/time header."""


@dataclass(frozen=True)
class Metar:
    icao: str
    observed_at: datetime
    report_type: str
    temp_c: float | None = None
    dewpoint_c: float | None = None
    wind_dir_deg: float | None = None
    wind_speed_kt: float | None = None
    wind_gust_kt: float | None = None
    visibility_m: float | None = None
    pressure_hpa: float | None = None
    wx_codes: tuple[str, ...] = field(default_factory=tuple)
    raw: str = ""


def resolve_observation_time(day: int, hour: int, minute: int, reference: datetime) -> datetime:
    """Resolve DDHHMMZ against a UTC reference (fetch time).

    Picks the latest candidate in the reference month or the months before it that is not
    later than reference + 1 h (allows small clock skew). Raises ValueError if none is valid.
    """
    if reference.tzinfo is None:
        raise ValueError("reference must be timezone-aware")
    ref = reference.astimezone(UTC)
    limit = ref + timedelta(hours=1)
    year, month = ref.year, ref.month
    for _ in range(3):
        try:
            candidate = datetime(year, month, day, hour, minute, tzinfo=UTC)
        except ValueError:
            candidate = None
        if candidate is not None and candidate <= limit:
            return candidate
        month -= 1
        if month == 0:
            year, month = year - 1, 12
    raise ValueError(f"cannot resolve day {day:02d} {hour:02d}:{minute:02d}Z against {ref}")


def _signed(grp: str) -> float:
    return -float(grp[1:]) if grp.startswith("M") else float(grp)


def _parse_wind(match: re.Match[str]) -> tuple[float | None, float, float | None]:
    direction, speed, gust, unit = match.groups()
    factor = {"KT": 1.0, "MPS": KT_PER_MPS, "KMH": KT_PER_KMH}[unit]
    dir_deg = None if direction == "VRB" else float(direction)
    gust_kt = round(float(gust) * factor, 1) if gust else None
    return dir_deg, round(float(speed) * factor, 1), gust_kt


def _parse_sm(match: re.Match[str], whole: str | None) -> float:
    _, integer, num, den = match.groups()
    miles = float(integer) if integer is not None else float(num) / float(den)
    if whole is not None:
        miles += float(whole)
    return round(miles * M_PER_SM, 0)


def parse_metar(raw: str, reference: datetime) -> Metar:
    """Parse a raw METAR/SPECI. ``reference`` is the UTC time the report was fetched."""
    text = " ".join(raw.replace("=", " ").split())
    tokens = text.split(" ")
    report_type = "METAR"
    if tokens and tokens[0] in ("METAR", "SPECI"):
        report_type = tokens.pop(0)
    if tokens and tokens[0] == "COR":
        tokens.pop(0)
    if len(tokens) < 2 or not _STATION.match(tokens[0]):
        raise MetarParseError(f"missing station identifier: {raw!r}")
    icao = tokens[0]
    time_match = _TIME.match(tokens[1])
    if not time_match:
        raise MetarParseError(f"missing DDHHMMZ group: {raw!r}")
    day, hour, minute = (int(g) for g in time_match.groups())
    try:
        observed_at = resolve_observation_time(day, hour, minute, reference)
    except ValueError as exc:
        raise MetarParseError(str(exc)) from exc

    body: list[str] = []
    remarks: list[str] = []
    in_remarks = False
    for grp in tokens[2:]:
        if grp == "RMK":
            in_remarks = True
            continue
        if in_remarks:
            remarks.append(grp)
        elif grp in _TREND_MARKERS:
            in_remarks = True  # trend section: skip, but keep scanning for RMK
        else:
            body.append(grp)

    temp_c: float | None = None
    dewpoint_c: float | None = None
    wind_dir: float | None = None
    wind_speed: float | None = None
    wind_gust: float | None = None
    visibility: float | None = None
    pressure: float | None = None
    wx: list[str] = []
    pending_whole: str | None = None

    for grp in body:
        if grp in ("AUTO", "COR") or _WIND_VAR.match(grp) or _RVR.match(grp):
            continue
        if grp in _NO_CLOUD or _CLOUD.match(grp) or grp.startswith("RE"):
            continue
        if (m := _WIND.match(grp)) and wind_speed is None:
            wind_dir, wind_speed, wind_gust = _parse_wind(m)
        elif grp == "CAVOK":
            visibility = CAVOK_VISIBILITY_M
        elif _VIS_WHOLE.match(grp) and visibility is None:
            pending_whole = grp
        elif (m := _VIS_SM.match(grp)) and visibility is None:
            visibility = _parse_sm(m, pending_whole)
            pending_whole = None
        elif (m := _VIS_M.match(grp)) and visibility is None:
            meters = float(m.group(1))
            visibility = CAVOK_VISIBILITY_M if meters >= 9999 else meters
        elif m := _TEMP.match(grp):
            temp_c = _signed(m.group(1))
            dewpoint_c = _signed(m.group(2)) if m.group(2) else None
        elif m := _Q.match(grp):
            pressure = float(m.group(1))
        elif m := _A.match(grp):
            pressure = round(float(m.group(1)) / 100.0 * HPA_PER_INHG, 1)
        elif grp and _WX.match(grp) and grp not in ("+", "-", "VC"):
            wx.append(grp)

    for grp in remarks:
        if m := _T_GROUP.match(grp):
            sign_t, t, sign_d, d = m.groups()
            temp_c = (-1 if sign_t == "1" else 1) * int(t) / 10.0
            dewpoint_c = (-1 if sign_d == "1" else 1) * int(d) / 10.0
            break

    return Metar(
        icao=icao,
        observed_at=observed_at,
        report_type=report_type,
        temp_c=temp_c,
        dewpoint_c=dewpoint_c,
        wind_dir_deg=wind_dir,
        wind_speed_kt=wind_speed,
        wind_gust_kt=wind_gust,
        visibility_m=visibility,
        pressure_hpa=pressure,
        wx_codes=tuple(wx),
        raw=text,
    )
