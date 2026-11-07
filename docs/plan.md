# plan.md — Faz Planı

> Kural: Her faz **çalışan, denenebilir** bir çıktıyla biter. Faz sonunda ajan `templates/checkpoint.md` raporunu üretir ve ürün sahibinin **"Faz N onaylandı"** yazmasını bekler.
> Süreler tek geliştirici + AI ajan için tahmini iş günüdür.
> Çalışma biçimi: saati olmayan, Âkif'in elle başlattığı scheduled task oturumları (`CLAUDE.md` → Zamanlanmış oturum modu). CI şimdilik yok.
> Ürünün kalbi doğruluktur (`product/01-vision.md`); fazların sırası bu yüzden ölçümle başlar.

## Genel bakış
| Faz | Ad | Çıktı | Tahmini süre | Story'ler |
|---|---|---|---|---|
| 0 | Lisans, doğrulama zemini, iskelet | Yazılı sağlayıcı onayları, repo iskeleti, METAR + ECMWF arşivi, ilk doğrulama raporu | 5–7 gün (+ sağlayıcı yanıt bekleme) | WX-001…019 |
| 1 | Android MVP | Rust API, Open-Meteo adaptörü, grid önbellek, Flutter uygulaması, Glance widget, yaşam tarzı endeksleri v0, Play kapalı test | 20–25 gün | WX-020…059 |
| 2 | iOS + sağlayıcı kararı | iOS uygulaması, SwiftUI widget, 60–90 günlük doğrulamaya dayalı sağlayıcı kararı, App Store | 10–14 gün | WX-060…079 |
| 3 | Kendi doğruluk katmanı | ECMWF + istasyon verisiyle bias düzeltme, kalibre güven skoru | 15–20 gün | WX-080…099 |
| 4+ | Taslak | Nowcasting/radar, gelir modeli, genişleme (bkz. sonda) | — | — |

**Kapalı beta: Faz 1 sonu (Android). Herkese açık lansman: Faz 2 sonu.**

---

## Faz 0 — Lisans, doğrulama zemini, iskelet
**Amaç:** Para ve kod harcamadan önce lisansı kesinleştirmek; doğruluk ölçümünü ilk günden başlatmak; sonraki fazların zeminini kurmak.

**Kapsam — ürün sahibi (kod dışı)**
- Sağlayıcılara ortak soru seti gönderilir (`research/2026-11-07-data-provider-decision.md` → Sağlayıcılara sorulacaklar): Open-Meteo, Meteoblue, Tomorrow.io, Rainbow.ai, MGM. Yanıtlar `research/provider-responses.md`'ye işlenir (`templates/provider-response.md`).
- Uygulama adı için marka ve mağaza araması (TÜRKPATENT, EUIPO, Play, App Store).
- Mac edinme planı (Faz 2 için) netleşir.

**Kapsam — ajan**
- Repo yerleşimi (`AGENTS.md §4`), `.gitattributes` (LF), `.editorconfig`, `.env.example`.
- `infra/docker-compose.yml`: PostgreSQL 16 + TimescaleDB.
- Migration aracı seçimi (Kararlar'a yazılır) ve ilk migration: `licensed` ve `own` şemaları, `own.stations`, `own.metar_observations` (hypertable), `own.ecmwf_point_forecasts` (hypertable).
- `pipeline/` Python projesi (`uv`, `ruff`, `pytest`):
  - **METAR arşivleyici:** Türkiye havalimanları (LTxx) için NOAA AviationWeather Data API'den 10 dakikada bir çekim; dakikada 100 istek sınırına uyum; idempotent upsert.
  - **ECMWF anlık görüntü:** IFS açık verisi (00 ve 12 UTC koşuları), istasyon noktalarına enterpolasyon, 0–240 saat tahmin ufku. CC-BY atfı kodda ve README'de.
  - **Doğrulama raporu v0:** istasyon × tahmin ufku için sıcaklık MAE ve bias; çıktı Markdown + CSV, `docs/reports/phase-0/`.
  - **Pilot istasyonlar global:** 4 Türkiye istasyonu + 4 global (EGLL Londra, EDDF Frankfurt, KJFK New York, RJTT Tokyo). Ürün global olduğu için doğrulama baştan çok bölgeli.
- **Rakip kıyası yöntemi (WX-019):** Gömülü uygulamalar (Apple Weather, Google) ve mağaza uygulamalarıyla lisansa uygun karşılaştırma yöntemi önerilir; karar Q4.
- CI yok (Âkif, 2026-11-08); yerel komutlar `quality/02-ci-cd.md`.

**Neden Open-Meteo değil ECMWF ile başlıyoruz:** Open-Meteo'nun ücretsiz API'si ticari olmayan kullanım içindir; ticari ürün için arşiv toplamak bu kapsama girmeyebilir. ECMWF açık verisi CC-BY-4.0 ile ticari kullanıma açıktır. Open-Meteo anlık görüntüsü ticari anahtar gelince eklenir (WX-016).

**Kabul kriterleri**
- [ ] Open-Meteo ve Meteoblue'dan yazılı yanıt alındı ve `provider-responses.md`'de işlendi (ticari kullanım, paylaşılan önbellek, arşiv, türev ürün, atıf, fiyat).
- [ ] ADR-0002 yanıtlara göre `Accepted` olarak kesinleşti ya da revize ADR yazıldı.
- [ ] `docker compose up -d` + migration hatasız.
- [ ] METAR arşivleyici en az 7 gün kesintisiz çalıştı; beklenen gözlemlerin ≥ %95'i kayıtlı.
- [ ] ECMWF anlık görüntüsü en az 7 gün boyunca her 00/12 koşusunu kaydetti.
- [ ] Doğrulama raporu v0 üretildi: Ankara (LTAC), İstanbul (LTFM), İzmir (LTBJ), Antalya (LTAI) ve 4 global pilot için ufuk bazında MAE.
- [ ] Rakip kıyası yöntem önerisi `research/competitor-benchmark.md`'de; Q4 kararı alındı.
- [ ] Pipeline yerel test/lint komutları yeşil.

**Checkpoint 0** → onay.

---

## Faz 1 — Android MVP
**Amaç:** Play Store kapalı testinde gerçek kullanıcıya giden, ölçülen ve şık bir ilk sürüm.

**Kapsam (PR dilimleri)**
- **1A — API çekirdeği:** Axum servisi, `ForecastProvider` trait, Open-Meteo ticari adaptörü (`archive_allowed`, `shared_cache_ttl` bayrakları), grid hücresi modeli (H3 ya da sabit ızgara; ADR ile), bellek içi önbellek, `GET /v1/forecast` sözleşmesi (`architecture/04-api-contracts.md`), problem+json hata modeli, OpenAPI.
- **1B — Doğrulama kaydı:** sunulan tahminlerin `own.served_forecasts` tablosuna yazılması (lisans izin veriyorsa), METAR ile günlük eşleştirme işi.
- **1C — Flutter kabuğu:** proje, tema (açık/koyu), i18n (varsayılan en, uygulama içinden tr), konum izni akışı, ana ekran (şimdi, saatlik, 10 gün), şehir arama ve kayıtlı yerler, boş/yükleniyor/hata durumları.
- **1D — Görsel katman v0:** hava durumuna göre değişen shader arka planı (açık, bulutlu, yağmur, kar, gece), hareketi azalt desteği, 60 fps hedefi.
- **1E — Yaşam tarzı endeksleri v0:** konfor endeksi, kıyafet önerisi, koşu için en iyi saat. Kendi algoritmamız; girdiler sıcaklık, hissedilen, nem, rüzgâr, yağış olasılığı, UV.
- **1F — Android widget:** Kotlin + Jetpack Glance; küçük ve orta boy; veri uygulamadan paylaşılan depoyla.
- **1G — Yayın hazırlığı:** gizlilik politikası ve KVKK aydınlatma metni, veri sağlayıcı atıfları ekranı, Play Console kapalı test, crash raporlama.

**Kabul kriterleri**
- [ ] Uygulama Play kapalı test kanalında; en az 10 test kullanıcısı.
- [ ] Soğuk açılıştan ilk tahmine p95 < 2 sn (orta seviye Android, 4G).
- [ ] API p95 < 150 ms (önbellekten), sağlayıcı hatasında son geçerli veri + bayat göstergesi.
- [ ] Widget 30 dakikada bir güncelleniyor, pil etkisi Android Vitals'ta uyarı üretmiyor.
- [ ] Doğrulama kaydı çalışıyor; haftalık rapor `docs/reports/phase-1/` altında.
- [ ] Tüm metinler en (varsayılan) + tr; atıflar görünür.
- [ ] Görsel kalite: açık/koyu ve her arka plan durumu için ekran kayıtları `docs/reports/phase-1/`; Âkif'in "şık ve tatmin edici" onayı checkpoint'te.
- [ ] Yerel test/lint komutları yeşil (API, pipeline, mobil).

**Checkpoint 1** → onay.

---

## Faz 2 — iOS + sağlayıcı kararı
**Kapsam**
- Mac ortamı, Flutter iOS derlemesi, SwiftUI + WidgetKit widget (App Group ile veri).
- 60–90 günlük doğrulama verisiyle sağlayıcı karşılaştırması (lisansın izin verdiği sağlayıcılar); ana sağlayıcı kararı için yeni ADR.
- App Store ve Play herkese açık yayın.

**Kabul kriterleri**
- [ ] iOS uygulaması ve widget Faz 1 kabul kriterlerini karşılıyor.
- [ ] Doğrulama raporu: değişken × ufuk × şehir bazında sağlayıcı karşılaştırması.
- [ ] Rakip kıyası ilk raporu (Q4 yöntemiyle); pazarlama iddiası yalnız bu rapordaki bölge ve ufuklar için.
- [ ] Mağazalarda yayında.

**Checkpoint 2** → onay.

---

## Faz 3 — Kendi doğruluk katmanı
**Kapsam**
- ECMWF açık verisi + METAR (ve izin alınırsa MGM) ile istasyon ve grid bazlı bias düzeltme (mevsim, saat, ufuk).
- Kalibre güven skoru: geçmiş hata dağılımından olasılık; güvenilirlik diyagramı ile test (ADR-0009).
- Uygulamada "tahmin güveni" gösterimi.

**Kabul kriterleri**
- [ ] Düzeltilmiş tahmin, ham tahmine göre METAR doğrulamasında sıcaklık MAE'yi en az 4 pilot şehirde anlamlı ölçüde düşürüyor (eşik Faz 3 başında yazılır).
- [ ] Güven skoru kalibrasyon testini geçiyor (güvenilirlik diyagramı, Brier skor).
- [ ] 60–90 günlük ölçümün mevsimselliği kanıtlamadığı raporda açıkça yazılı; ölçüm sürüyor.

**Checkpoint 3** → onay.

---

## Faz 4+ (taslak, önceliklendirilmedi)
- Nowcasting ve radar katmanı (Türkiye kapsamı Faz 0'da teyit edilirse).
- Hava kalitesi ve polen (CAMS).
- Gelir modeli: ücretsiz + Plus (yalnızca kendi ürettiğimiz özellikler ücretli; ADR gerekir).
- Wear OS / Apple Watch, Live Activity, bildirim senaryoları.
