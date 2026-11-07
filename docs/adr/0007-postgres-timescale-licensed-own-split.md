# ADR-0007: PostgreSQL + TimescaleDB, lisanslı/kendi veri ayrımı

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0002, ADR-0003

## Bağlam
Zaman serisi ağırlıklı veri (gözlem, tahmin anlık görüntüleri, doğrulama sonuçları). Sağlayıcı lisansları farklı saklama hakları tanıyor; lisanssız veri yanlışlıkla kalıcı bir tabloya yazılırsa ihlal olur.

## Karar
- **PostgreSQL 16 + TimescaleDB** (hypertable, sıkıştırma, sürekli agregasyon).
- İki şema:
  - `own` — kendi gözlem ve türev verimiz: istasyonlar, METAR, ECMWF anlık görüntüleri (CC-BY), sunulan tahminlerin doğrulama kaydı, düzeltme modelleri, raporlar.
  - `licensed` — yalnız `archive_allowed = true` sağlayıcıların verisi; her satırda `provider` ve `license_ref`.
- Lisanssız sağlayıcı verisi hiçbir tabloya yazılmaz; yalnız süreç belleğindeki önbellekte, `shared_cache_ttl` kadar tutulur.
- Migration'lar `db/migrations` altında tek kaynak; araç Faz 0'da seçilir (Kararlar).

## Sonuçlar
- **Olumlu:** Lisans sınırı şemada görünür; denetimi kolay.
- **Olumsuz:** Sorgularda şema ayrımı.
- **Geri dönüş maliyeti:** orta.

## Doğrulama
Veritabanı rolü: API'nin `licensed` şemasına yazma yetkisi yalnız izinli sağlayıcı tablolarında. Test: `archive_allowed = false` adaptörün verisi yazma yoluna ulaşmıyor.
