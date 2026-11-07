# infra

Yerel ortam: `docker-compose.yml` (WX-010).

| Servis | Ne | Not |
|---|---|---|
| `db` | PostgreSQL 16 + TimescaleDB (`timescale/timescaledb:2.17.2-pg16`) | Yalnız `127.0.0.1:5432` |
| `migrate` | dbmate, `db/migrations` | `tools` profili; elle çalıştırılır |
| `metar-archiver` | `pipeline` imajı: katalog senkronu + 10 dk'da bir METAR arşivi (WX-012, WX-017) | `restart: unless-stopped` |

```bash
cp .env.example .env    # POSTGRES_PASSWORD ve DATABASE_URL'i ayarla
docker compose -f infra/docker-compose.yml --env-file .env up -d db
docker compose -f infra/docker-compose.yml --env-file .env run --rm migrate
docker compose -f infra/docker-compose.yml --env-file .env up -d --build metar-archiver
docker compose -f infra/docker-compose.yml --env-file .env logs -f metar-archiver
# 7 gün sonra doluluk (WX-012 kabulü, >= %95):
docker compose -f infra/docker-compose.yml --env-file .env run --rm metar-archiver metar coverage
```
Yeni migration: `dbmate new <ad>` (dosya `db/migrations/<zaman>_<ad>.sql`, `-- migrate:up` / `-- migrate:down`).
