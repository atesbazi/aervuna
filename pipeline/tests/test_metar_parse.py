"""METAR parser tests. Reports follow the WMO/ICAO and US FMH-1 formats; expected values are
computed by hand from the groups (format-faithful examples, not captured live reports)."""

from datetime import UTC, datetime

import pytest

from aervuna_pipeline.metar.parse import MetarParseError, parse_metar, resolve_observation_time

REF = datetime(2026, 11, 7, 20, 5, tzinfo=UTC)


def test_cavok_report_with_trend() -> None:
    m = parse_metar("METAR LTAC 071950Z 04006KT CAVOK 08/M01 Q1024 NOSIG=", REF)
    assert m.icao == "LTAC"
    assert m.report_type == "METAR"
    assert m.observed_at == datetime(2026, 11, 7, 19, 50, tzinfo=UTC)
    assert (m.temp_c, m.dewpoint_c) == (8.0, -1.0)
    assert (m.wind_dir_deg, m.wind_speed_kt, m.wind_gust_kt) == (40.0, 6.0, None)
    assert m.visibility_m == 10000.0
    assert m.pressure_hpa == 1024.0
    assert m.wx_codes == ()
    assert m.raw == "METAR LTAC 071950Z 04006KT CAVOK 08/M01 Q1024 NOSIG"


def test_trend_weather_is_not_observed_weather() -> None:
    m = parse_metar(
        "METAR LTFM 071920Z 22012G25KT 9999 -RA FEW020 SCT040 BKN080 16/12 Q1012 TEMPO SHRA=",
        REF,
    )
    assert m.wx_codes == ("-RA",)
    assert m.wind_gust_kt == 25.0
    assert m.visibility_m == 10000.0


def test_us_report_uses_t_group_tenths_and_altimeter() -> None:
    m = parse_metar(
        "METAR KJFK 071951Z 31012G20KT 10SM FEW050 12/M03 A3012 RMK AO2 SLP200 T01171028", REF
    )
    assert (m.temp_c, m.dewpoint_c) == (11.7, -2.8)
    assert m.visibility_m == 16093.0  # 10 SM
    assert m.pressure_hpa == 1020.0  # 30.12 inHg * 33.8639 = 1019.98


def test_speci_auto_with_recent_weather_and_variable_wind() -> None:
    m = parse_metar(
        "SPECI EGLL 071935Z AUTO 25008KT 220V290 4000 RA BR BKN006 OVC012 11/10 Q1008 RERA=", REF
    )
    assert m.report_type == "SPECI"
    assert m.wx_codes == ("RA", "BR")
    assert m.visibility_m == 4000.0
    assert m.wind_dir_deg == 250.0


def test_wind_in_metres_per_second_is_converted_to_knots() -> None:
    m = parse_metar("METAR UUEE 071930Z 18005MPS 9999 OVC020 02/M01 Q1019 NOSIG", REF)
    assert m.wind_speed_kt == 9.7


def test_calm_wind_and_fractional_statute_miles() -> None:
    m = parse_metar("METAR KJFK 071951Z 00000KT 1 1/2SM BR OVC004 08/07 A2990", REF)
    assert (m.wind_dir_deg, m.wind_speed_kt) == (0.0, 0.0)
    assert m.visibility_m == 2414.0  # 1.5 SM
    assert m.wx_codes == ("BR",)


def test_variable_wind_and_thunderstorm() -> None:
    m = parse_metar("METAR LTAI 071950Z VRB03KT 6000 +TSRA FEW025CB 19/17 Q1009", REF)
    assert m.wind_dir_deg is None
    assert m.wind_speed_kt == 3.0
    assert m.wx_codes == ("+TSRA",)


def test_missing_groups_stay_null() -> None:
    m = parse_metar("METAR LTBJ 072000Z /////KT 9999 NCD ///// Q1015", REF)
    assert m.temp_c is None
    assert m.dewpoint_c is None
    assert m.wind_speed_kt is None
    assert m.visibility_m == 10000.0
    assert m.pressure_hpa == 1015.0


def test_negative_temperature_without_dewpoint() -> None:
    m = parse_metar("METAR LTCE 071950Z 27004KT 9999 SCT030 M05/ Q1028", REF)
    assert (m.temp_c, m.dewpoint_c) == (-5.0, None)


def test_correction_prefix_is_accepted() -> None:
    m = parse_metar("METAR COR LTAC 071950Z 04006KT CAVOK 08/M01 Q1024", REF)
    assert m.icao == "LTAC"


@pytest.mark.parametrize("raw", ["", "LTAC", "METAR LTAC 04006KT CAVOK", "ltac 071950Z"])
def test_reports_without_header_are_rejected(raw: str) -> None:
    with pytest.raises(MetarParseError):
        parse_metar(raw, REF)


def test_day_resolves_into_previous_month() -> None:
    ref = datetime(2026, 12, 1, 0, 5, tzinfo=UTC)
    assert resolve_observation_time(30, 23, 50, ref) == datetime(2026, 11, 30, 23, 50, tzinfo=UTC)


def test_day_31_skips_month_without_it() -> None:
    ref = datetime(2026, 12, 1, 0, 5, tzinfo=UTC)  # November has 30 days
    assert resolve_observation_time(31, 23, 0, ref) == datetime(2026, 10, 31, 23, 0, tzinfo=UTC)


def test_small_clock_skew_is_tolerated() -> None:
    ref = datetime(2026, 11, 7, 19, 45, tzinfo=UTC)
    assert resolve_observation_time(7, 19, 50, ref) == datetime(2026, 11, 7, 19, 50, tzinfo=UTC)


def test_naive_reference_is_rejected() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        resolve_observation_time(7, 19, 50, datetime(2026, 11, 7, 20, 0))
