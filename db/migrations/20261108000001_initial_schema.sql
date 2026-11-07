-- migrate:up
-- WX-011: initial schema (ADR-0007, docs/architecture/03-data-model.md).
-- own      : our own observations and openly licensed data (METAR, ECMWF CC-BY-4.0).
-- licensed : only providers with archive_allowed = true; every row carries provider + license_ref.

CREATE SCHEMA IF NOT EXISTS own;
CREATE SCHEMA IF NOT EXISTS licensed;

COMMENT ON SCHEMA own IS 'Own data and openly licensed data (METAR public data, ECMWF open data CC-BY-4.0).';
COMMENT ON SCHEMA licensed IS 'Third-party data from providers whose licence allows archiving (archive_allowed = true). Each row must carry provider and license_ref.';

CREATE TABLE own.stations (
    icao         text PRIMARY KEY CHECK (icao ~ '^[A-Z0-9]{4}$'),
    name         text NOT NULL,
    lat          double precision NOT NULL CHECK (lat BETWEEN -90 AND 90),
    lon          double precision NOT NULL CHECK (lon BETWEEN -180 AND 180),
    elevation_m  integer,
    country      text,
    kind         text NOT NULL DEFAULT 'airport' CHECK (kind IN ('airport', 'mgm')),
    active       boolean NOT NULL DEFAULT false,
    source       text NOT NULL,
    updated_at   timestamptz NOT NULL DEFAULT now()
);

COMMENT ON COLUMN own.stations.active IS 'Archived by the METAR archiver when true.';
COMMENT ON COLUMN own.stations.source IS 'Catalogue source, e.g. noaa-awc-stations-cache.';

CREATE TABLE own.metar_observations (
    icao           text NOT NULL REFERENCES own.stations (icao),
    observed_at    timestamptz NOT NULL,
    report_type    text NOT NULL DEFAULT 'METAR' CHECK (report_type IN ('METAR', 'SPECI')),
    temp_c         real,
    dewpoint_c     real,
    wind_dir_deg   real CHECK (wind_dir_deg IS NULL OR wind_dir_deg BETWEEN 0 AND 360),
    wind_speed_kt  real CHECK (wind_speed_kt IS NULL OR wind_speed_kt >= 0),
    wind_gust_kt   real CHECK (wind_gust_kt IS NULL OR wind_gust_kt >= 0),
    visibility_m   real CHECK (visibility_m IS NULL OR visibility_m >= 0),
    pressure_hpa   real,
    wx_codes       text[] NOT NULL DEFAULT '{}',
    raw            text NOT NULL,
    fetched_at     timestamptz NOT NULL,
    PRIMARY KEY (icao, observed_at)
);

COMMENT ON COLUMN own.metar_observations.temp_c IS 'Tenths from the RMK T-group when present, otherwise whole degrees from the body.';
COMMENT ON COLUMN own.metar_observations.visibility_m IS 'Prevailing visibility; 10000 for CAVOK/9999 (means >= 10 km).';

CREATE TABLE own.ecmwf_point_forecasts (
    icao       text NOT NULL REFERENCES own.stations (icao),
    model      text NOT NULL CHECK (model IN ('ifs', 'aifs')),
    run_at     timestamptz NOT NULL,
    valid_at   timestamptz NOT NULL,
    lead_h     smallint NOT NULL CHECK (lead_h BETWEEN 0 AND 360),
    t2m_c      real,
    d2m_c      real,
    u10        real,
    v10        real,
    gust       real,
    tp_mm      real,
    msl_hpa    real,
    tcc        real,
    interp     text NOT NULL,
    fetched_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (icao, model, run_at, valid_at),
    CHECK (valid_at = run_at + make_interval(hours => lead_h))
);

COMMENT ON TABLE own.ecmwf_point_forecasts IS 'ECMWF open data (CC-BY-4.0) interpolated to station points. Attribution required.';

CREATE INDEX metar_observations_observed_at_idx ON own.metar_observations (observed_at DESC);
CREATE INDEX ecmwf_point_forecasts_valid_at_idx ON own.ecmwf_point_forecasts (valid_at DESC);

-- Hypertables (ADR-0007). infra/docker-compose.yml always ships TimescaleDB.
-- Where the extension is not installed (plain PostgreSQL in a throwaway test
-- database) the tables stay regular tables and a WARNING is raised; see
-- docs/progress.md -> Kararlar (2026-11-07).
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_available_extensions WHERE name = 'timescaledb') THEN
        CREATE EXTENSION IF NOT EXISTS timescaledb;
        PERFORM create_hypertable('own.metar_observations', by_range('observed_at', INTERVAL '30 days'));
        PERFORM create_hypertable('own.ecmwf_point_forecasts', by_range('valid_at', INTERVAL '30 days'));
    ELSE
        RAISE WARNING 'timescaledb is not available: own.metar_observations and own.ecmwf_point_forecasts are plain tables';
    END IF;
END
$$;

-- migrate:down
DROP TABLE IF EXISTS own.ecmwf_point_forecasts;
DROP TABLE IF EXISTS own.metar_observations;
DROP TABLE IF EXISTS own.stations;
DROP SCHEMA IF EXISTS licensed;
DROP SCHEMA IF EXISTS own;
