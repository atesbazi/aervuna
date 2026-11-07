# AI İncelemeleri ve Doğrulanan Düzeltmeler

> Ürün sahibi aynı soruyu Gemini, ChatGPT ve Claude'a sordu (2026-11-07/08). Bu dosya yalnız **kalıcı sonuçları** ve **birincil kaynakla doğrulanan** düzeltmeleri tutar. Bir iddia burada "doğrulandı" değilse karar dayanağı yapılmaz.

## 1. Gemini (2026-11-07) — ilk öneri
- Önerdiği sağlayıcılar: Open-Meteo, OpenWeather, Google Weather, Meteoblue, AccuWeather, Weatherbit, Tomorrow.io.
- **Hatalı:** Google Weather API'yi hava uygulaması için önerdi → şartlar 21.1 yasaklıyor (doğrulandı).
- **Doğrulanamadı:** "Weatherbit 2026 benchmark lideri".
- **Doğrulanamadı:** Tomorrow.io'nun her bölgede hücresel sinyal ve sokak kamerası kullandığı.
- Faydalı: MGM verisiyle Türkiye harmanlama fikri (lisans koşuluyla), lifestyle katmanları.

## 2. ChatGPT (2026-11-07) — ilk değerlendirme
- Meteoblue ana + Google Weather ikinci kaynak + Tomorrow.io nowcasting + Open-Meteo alternatif.
- **Hatalı:** Google Weather ikinci kaynak (21.1). ChatGPT daha sonra kabul etti.
- Faydalı: Doğruluk laboratuvarı (MAE, Brier, POD, FAR), 60–90 gün pilot, lifestyle özellik listesi (→ IDEA-003).

## 3. Claude (2026-11-07) — Faz 0 dokümanı v1
- Google'ı eledi (doğrulandı), WeatherKit'i ucuz ana kaynak adayı gösterdi, ECMWF açık veriyi ve METAR doğrulamasını ekledi, grid önbellek birim ekonomisini hesapladı.
- **Hatalı (düzeltildi):** WeatherKit'in paylaşılan grid önbelleğine uygun olduğunu varsaydı → Attachment 8 madde 1.6.
- **Hatalı (düzeltildi):** METAR API geçmişi 15 gün yazıldı → 30 gün.
- **Eksik (düzeltildi):** Meteoblue zorunlu destek paketi.

## 4. ChatGPT (2026-11-08) — Claude dokümanına eleştiri
Doğrulanan:
- WeatherKit Attachment 8 madde 1.2, 1.5, 1.6 (DPLA metni okundu) → ADR-0003.
- METAR 30 gün (aviationweather.gov) → düzeltildi.
- Open-Meteo'yu birinci sıraya alma (lisans gerekçesiyle) → ADR-0002.
- Sağlayıcı bazında arşiv bayrağı, lisanslı/kendi veri ayrımı → ADR-0005, ADR-0007.
- Güven skoru kalibre olmalı → ADR-0009.
Düzeltilen / reddedilen:
- "Claude'un mimarisi WeatherKit → arşiv → ML" iddiası dokümanla örtüşmüyor (ML ECMWF + istasyon üzerineydi); ama WeatherKit akıştan açıkça ayrılmamıştı → ayrıldı.
- "Sabit 400 €/ay varsayımı" doküman "400 €'dan başlıyor, kredi bazlı" diyordu.
- Rust/Axum + Flutter: ChatGPT gerekçesiz önermişti; ürün sahibi kendi tercihi olarak onayladı → ADR-0004, ADR-0005.

## 5. Claude (2026-11-08) — ek tespit
- WeatherKit tahminlerini METAR ile karşılaştırmak için arşivlemek de 1.5/1.6 ile çatışabilir → WeatherKit'in doğruluğu bizim yöntemimizle ölçülemez.
- Faz 0 arşivi Open-Meteo **ücretsiz** API ile toplanmamalı (ticari olmayan kullanım şartı) → ECMWF açık verisiyle başlanır.
