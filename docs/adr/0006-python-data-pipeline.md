# ADR-0006: Veri ve ML hattı — Python

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0005, ADR-0007, `architecture/05-forecast-verification.md`

## Bağlam
GRIB işleme (eccodes, cfgrib, xarray), ECMWF açık veri istemcisi, istatistik ve ML (bias düzeltme, kalibrasyon) ekosistemi Python'da. Bunları Rust'ta yeniden yazmak Faz 0–3'ü uzatır.

## Karar
Toplu ve zamanlanmış veri işleri **Python worker**'da: METAR arşivi, ECMWF anlık görüntü, doğrulama raporları, bias düzeltme, kalibrasyon. Araçlar: `uv`, `ruff`, `pytest`, `mypy`. API ile iletişim yalnız veritabanı üzerinden (paylaşılan şema, `db/migrations` tek kaynak). Python servis HTTP isteği karşılamaz.

## Sonuçlar
- **Olumlu:** Hazır meteoroloji kütüphaneleri; hızlı deneme.
- **Olumsuz:** İkinci çalışma zamanı ve bağımlılık seti.
- **Geri dönüş maliyeti:** düşük — sınır veritabanı şeması.

## Doğrulama
Faz 0 kabul kriterleri (7 gün kesintisiz arşiv, rapor v0).
