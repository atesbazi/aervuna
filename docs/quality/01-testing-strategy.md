# 01 — Test Stratejisi

| Katman | Araç | Kapsam |
|---|---|---|
| Rust domain | `cargo test` | Endeks formülleri, grid indirgeme, birim dönüşümleri (özellik tabanlı test: `proptest`) |
| Rust adaptör | `wiremock` | Sağlayıcı sözleşme testleri, zaman aşımı, yeniden deneme, bayat veri |
| Lisans kuralları | `cargo test` | `archive_allowed=false` adaptörün verisi `VerificationSink`'e ulaşmaz; TTL lisansı aşmaz |
| DB | testcontainers / docker | Migration'lar, hypertable, roller |
| Pipeline | `pytest` | METAR ayrıştırma (gerçek örnek METAR'lar), ECMWF enterpolasyonu, metrik hesapları (elle doğrulanmış küçük veri) |
| Flutter | `flutter test`, golden test | Widget'lar, açık/koyu tema, tr/en, boş/yükleniyor/hata |
| Android widget | Glance test | Anlık görüntüden çizim |
| Uçtan uca | Maestro (mobil) | Konum izni, şehir arama, ana ekran |
| Performans | k6 (API), Flutter DevTools (fps) | p95 < 150 ms; 60 fps |

## İlkeler
- Metrik kodu, sonucu elle hesaplanmış küçük veri setleriyle test edilir.
- Sağlayıcı yanıtları kayıtlı fixture'lardan; testler internete çıkmaz.
- Kanıtsız doğruluk iddiası yok; rapor üreten kod testli.
