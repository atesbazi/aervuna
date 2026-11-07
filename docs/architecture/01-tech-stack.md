# 01 — Teknoloji Yığını

| Katman | Seçim | Sürüm politikası | ADR |
|---|---|---|---|
| Mobil | Flutter, Dart | Kararlı kanal; sürüm Faz 1 başında `pubspec.yaml`'da sabitlenir | 0004 |
| Görsel | Impeller, `FragmentProgram` (GLSL shader), Rive | — | 0004 |
| Android widget | Kotlin, Jetpack Glance | — | 0004 |
| iOS widget | Swift, SwiftUI, WidgetKit (Faz 2) | — | 0004 |
| API | Rust (stable), Axum, Tokio, `reqwest`, `sqlx`, `serde`, `tracing`, `utoipa` (OpenAPI) | `rust-toolchain.toml` ile sabit | 0005 |
| Önbellek | Süreç içi (`moka`); çoklu örnekte gerekirse Redis (ADR) | — | 0005 |
| Veri hattı | Python 3.12+, `uv`, `ecmwf-opendata`, `cfgrib`/`eccodes`, `xarray`, `pandas`/`polars`, `httpx`, `ruff`, `pytest`, `mypy` | `pyproject.toml` + `uv.lock` | 0006 |
| Veritabanı | PostgreSQL 16 + TimescaleDB | docker imajı etiketle sabit | 0007 |
| Migration | Faz 0'da seçilir (aday: `sqlx-cli`, `dbmate`) | — | 0007 |
| Yerel ortam | Windows + WSL2 Ubuntu, Docker | — | — |
| CI | Şimdilik yok (Âkif, 2026-11-08); yerel komutlar | — | — |

## Bileşen sorumlulukları
- **API (Rust):** istemcinin konuştuğu tek yer. Sağlayıcı anahtarları yalnız burada.
- **Pipeline (Python):** zamanlanmış işler; HTTP isteği karşılamaz.
- **Mobil:** yalnız kendi API'mizle konuşur (WeatherKit hariç; ADR-0003).

## Komutlar
Faz 0'da kod geldikçe doldurulur:
```
# yerel ortam
docker compose -f infra/docker-compose.yml up -d
# pipeline
cd pipeline && uv sync && uv run pytest && uv run ruff check .
# api (Faz 1)
cd services/api && cargo test && cargo clippy -- -D warnings
# mobil (Faz 1)
cd apps/mobile && flutter analyze && flutter test
```

## Maliyet (taslak)
| Kalem | Faz 0 | Faz 1 kapalı test |
|---|---|---|
| Open-Meteo ticari | 0 (anahtar bekleniyor) | Teklif |
| Sunucu (API + DB + pipeline) | Yerel | Küçük VPS; Faz 1'de karar |
| Google Play geliştirici hesabı | — | Tek seferlik ücret |
| Apple Developer Program | — | Faz 2 |
