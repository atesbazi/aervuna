# 03 — Veri Modeli (taslak)

> Faz 0'da `own` şemasının ilk tabloları kesinleşir. Sütunlar migration'la birlikte bu dosyada güncellenir. Kaynak: `db/migrations`.

## Şemalar
- `own` — kendi verimiz ve açık lisanslı veri (ECMWF CC-BY, METAR).
- `licensed` — yalnız `archive_allowed = true` sağlayıcıların verisi; her satırda `provider`, `license_ref`.

## Faz 0 tabloları
### `own.stations`
| Sütun | Tip | Not |
|---|---|---|
| `icao` | `text` PK | LTAC, LTFM… |
| `name` | `text` | |
| `lat`, `lon` | `double precision` | |
| `elevation_m` | `integer` | |
| `kind` | `text` | `airport` (ileride `mgm`) |
| `active` | `boolean` | |

### `own.metar_observations` (hypertable, `observed_at`)
| Sütun | Tip | Not |
|---|---|---|
| `icao` | `text` FK | |
| `observed_at` | `timestamptz` | |
| `temp_c`, `dewpoint_c` | `real` | |
| `wind_dir_deg`, `wind_speed_kt`, `wind_gust_kt` | `real` | |
| `visibility_m` | `real` | |
| `pressure_hpa` | `real` | |
| `wx_codes` | `text[]` | RA, SN, TS… |
| `raw` | `text` | Ham METAR |
| `fetched_at` | `timestamptz` | |
PK: (`icao`, `observed_at`).

### `own.ecmwf_point_forecasts` (hypertable, `valid_at`)
| Sütun | Tip | Not |
|---|---|---|
| `icao` | `text` FK | |
| `model` | `text` | `ifs`, `aifs` |
| `run_at` | `timestamptz` | 00/12 UTC |
| `valid_at` | `timestamptz` | |
| `lead_h` | `smallint` | |
| `t2m_c`, `d2m_c` | `real` | |
| `u10`, `v10`, `gust` | `real` | |
| `tp_mm` | `real` | toplam yağış (aralık) |
| `msl_hpa` | `real` | |
| `tcc` | `real` | bulutluluk |
| `interp` | `text` | `nearest` / `bilinear` + rakım düzeltmesi |
PK: (`icao`, `model`, `run_at`, `valid_at`).

## Faz 1 tabloları (taslak)
- `own.served_forecasts` — hücre, sağlayıcı, istek zamanı, ufuk, değişkenler (yalnız `archive_allowed`).
- `own.verification_pairs` — tahmin ↔ gözlem eşleşmesi, hata.
- `own.verification_daily` — sürekli agregasyon: istasyon × sağlayıcı × ufuk × değişken.

## Faz 3 tabloları (taslak)
- `own.bias_models` — sürüm, kapsam, parametreler, eğitim dönemi, test metrikleri.
- `own.calibration_tables` — değişken × ufuk × bölge × mevsim → hata dağılımı / olasılık eşlemesi.
