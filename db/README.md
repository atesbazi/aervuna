# db

`migrations/` — tek kaynak SQL migration'lar (API ve pipeline ortak, ADR-0007). Araç: **dbmate** (`-- migrate:up` / `-- migrate:down`, tablo `schema_migrations`). Çalıştırma: `infra/README.md`. Şema açıklaması: `docs/architecture/03-data-model.md`.
