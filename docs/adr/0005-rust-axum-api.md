# ADR-0005: API — Rust / Axum

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0002, ADR-0006, ADR-0007

## Bağlam
API'nin işi büyük ölçüde G/Ç: konum → grid hücresi, önbellek, sağlayıcı adaptörleri, endeks hesapları, doğrulama kaydı. Ürün sahibinin ana yığını Java/Spring; Rust/Axum'a açık ve tercih ediyor.

## Değerlendirilen seçenekler
1. **Rust / Axum** — Düşük bellek ve sunucu maliyeti, güçlü tip sistemi; sağlayıcılar trait olarak temiz modellenir. Eksi: geliştirme hızı ve öğrenme eğrisi.
2. **Java / Spring Boot (hexagonal)** — Ürün sahibinin uzmanlığı, en hızlı başlangıç. Eksi: daha yüksek bellek; ürün sahibi tercih etmedi.
3. **Python (FastAPI)** — Pipeline ile tek dil. Eksi: düşük performans ve tip güvenliği.

## Karar
**Rust / Axum.** Mimari hexagonal: `domain` (saf tipler, endeks hesapları) → `application` (use-case, portlar: `ForecastProvider`, `ForecastCache`, `VerificationSink`) → `adapters` (HTTP, sağlayıcılar, Postgres). Her `ForecastProvider` uygulaması `archive_allowed`, `shared_cache_ttl`, `attribution` değerlerini zorunlu olarak bildirir.

## Sonuçlar
- **Olumlu:** Ucuz barındırma, öngörülebilir gecikme.
- **Olumsuz:** Yavaş başlangıç; ekosistemde eksik kalan yerlerde Python worker'a iş devri.
- **Geri dönüş maliyeti:** orta — HTTP sözleşmesi (`architecture/04-api-contracts.md`) sabit kaldıkça arka uç değiştirilebilir.

## Doğrulama
Faz 1: p95 < 150 ms (önbellekten); lisans bayrakları için derleme zamanı/test zorlaması.
