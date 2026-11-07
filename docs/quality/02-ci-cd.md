# 02 — CI/CD

> **Durum (Âkif, 2026-11-08): CI şimdilik yok.** Her oturum ilgili bileşenin yerel komutlarını çalıştırır ve özetini `progress.md`'ye yazar. Aşağıdaki tasarım, CI açıldığında uygulanacak plan olarak duruyor (WX-015 ertelendi).

## Yerel kontrol komutları (CI yerine)
| Bileşen | Komut |
|---|---|
| pipeline | `cd pipeline && uv run ruff check . && uv run ruff format --check . && uv run mypy . && uv run pytest` |
| api (Faz 1) | `cd services/api && cargo fmt --check && cargo clippy -- -D warnings && cargo test` |
| mobile (Faz 1) | `cd apps/mobile && flutter analyze && flutter test` |

## CI tasarımı (ertelendi)
Yol filtresiyle bileşen bazlı iş:
| İş | Tetik | Adımlar |
|---|---|---|
| `pipeline` | `pipeline/**`, `db/**` | `uv sync` → `ruff check` → `ruff format --check` → `mypy` → `pytest` |
| `api` (Faz 1) | `services/api/**`, `db/**` | `cargo fmt --check` → `clippy -D warnings` → `cargo test` (Postgres servisiyle) |
| `mobile` (Faz 1) | `apps/mobile/**` | `flutter analyze` → `flutter test` → `flutter build apk --debug` |
| `docs` | `docs/**` | Markdown link kontrolü |

## Runner (CI açıldığında karar verilecek)
- Ürün sahibi GitHub-hosted runner'ı yavaş buluyor ve yan projeleri için self-hosted CI planlıyor.
- Öneri: PR'da hızlı işler GitHub-hosted, ağır işler (Flutter derleme, Android emülatör, Faz 2'de macOS) self-hosted runner.

## Sürüm
- Faz kapanışında etiket `v0.N.0`.
- Android: Faz 1G'de Play Console iç test → kapalı test; imzalama anahtarı repoda değil.
- iOS: Faz 2.
