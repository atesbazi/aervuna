# pipeline

Aervuna veri hattı (ADR-0006): METAR arşivi, ECMWF açık veri anlık görüntüleri, doğrulama raporları. HTTP isteği karşılamaz; API ile yalnız veritabanı üzerinden konuşur.

## Komutlar
```bash
uv sync
# yerel kontroller (CI yerine, docs/quality/02-ci-cd.md)
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```
DB entegrasyon testleri `TEST_DATABASE_URL` (veritabanı oluşturabilen bir kullanıcıyla Postgres sunucusu) ve `PATH`'te `dbmate` ister; yoksa atlanır. Her test oturumu taze bir veritabanı açar ve `db/migrations`'ı dbmate ile uygular.

```bash
# DATABASE_URL gerekir (.env.example)
uv run aervuna-pipeline stations sync     # WX-017: pilot + LTxx istasyonları (NOAA stations cache)
uv run aervuna-pipeline metar once        # WX-012: tek çekim
uv run aervuna-pipeline metar run         # katalog senkronu + 10 dakikada bir arşiv (sonsuz döngü)
uv run aervuna-pipeline metar coverage    # son 7 günde saatlik doluluk; < %95 ise çıkış kodu 1
```
Docker ile: `infra/docker-compose.yml` → `metar-archiver` servisi.

## Veri kaynakları ve atıf
- **METAR:** NOAA AviationWeather.gov Data API (ABD kamu verisi). Kaynak belirtilir. Sınır 100 istek/dk; varsayılanımız 30/dk, istasyonlar 50'şerli toplu istekle. User-Agent: `METAR_USER_AGENT` ya da varsayılan `aervuna-pipeline/<sürüm> (+https://github.com/atesbazi/aervuna)`.
- **ECMWF açık veri (WX-013, sıradaki):** CC-BY-4.0, atıf zorunlu.
