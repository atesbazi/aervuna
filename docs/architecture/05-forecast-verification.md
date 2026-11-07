# 05 — Tahmin Doğrulama Metodolojisi

> Ürünün doğruluk iddiaları yalnız bu metodolojiyle üretilmiş raporlara dayanır (CLAUDE.md).

## Gözlem kaynağı
- **METAR** (NOAA AviationWeather Data API): Türkiye havalimanları. API son 30 günü verir; arşivi biz tutarız.
- Sınırlama: Havalimanı noktası şehrin tamamını temsil etmez (kıyı, rakım, kentsel ısı adası). Raporlarda istasyon bazında verilir; şehir geneline genelleme yapılmaz.
- İleride: MGM istasyonları (lisans izin verirse).

## Pilot istasyonlar
Türkiye: LTAC (Ankara Esenboğa), LTFM (İstanbul), LTBJ (İzmir), LTAI (Antalya). Global: EGLL (Londra Heathrow), EDDF (Frankfurt), KJFK (New York JFK), RJTT (Tokyo Haneda). Faz 0 sonunda tüm aktif LTxx; global liste pazar sırasına göre büyür.

## Eşleştirme
- Tahmin geçerlilik zamanı ile gözlem zamanı ±30 dk içinde en yakın; METAR saat başı/yarım raporlarıyla.
- Nokta tahmini: sağlayıcının istasyon koordinatı için verdiği değer; ECMWF'de en yakın/bilineer + rakım düzeltmesi (lapse rate 6,5 °C/km), yöntem kayıtta.
- Ufuk kovaları: 0–6, 6–12, 12–24, 24–48, 48–72, 72–120, 120–240 saat.

## Metrikler
| Değişken | Metrik |
|---|---|
| Sıcaklık, çiy noktası | MAE, bias, RMSE |
| Rüzgâr hızı | MAE, bias |
| Yağış olayı (≥ 0,1 mm/saat ya da METAR RA/SN/DZ/TS) | POD, FAR, CSI, Brier (olasılıklı tahminde) |
| Olasılıklı tahmin | Brier, güvenilirlik diyagramı (kalibrasyon) |
| Yağış başlangıcı (Faz 4) | Dakika cinsinden zamanlama hatası |
| Tahmin kararlılığı | Aynı geçerlilik zamanı için ardışık koşular arasındaki ortalama mutlak değişim (WX-018) |

## Rapor formatı
`docs/reports/phase-N/verification-YYYY-MM-DD.md` + aynı ad `.csv`. İçerik: dönem, istasyon listesi, sağlayıcılar, örnek sayısı, metrik tablosu (istasyon × ufuk × değişken), yöntem notları, sınırlamalar.

## Kurallar
- Örnek sayısı < 100 olan hücrelerde metrik gösterilmez.
- Sağlayıcı karşılaştırması yalnız aynı zaman aralığı ve aynı istasyon setinde yapılır.
- 60–90 günlük sonuç mevsimselliği kanıtlamaz; raporda yazılır.
- WeatherKit lisans gereği bu sürece dahil edilmez (ADR-0003).

## Rakip kıyası
Ürünün pazarlama iddiası "mağaza ve gömülü uygulamalardan daha tutarlı ve doğru" olduğu için rakip kıyası zorunludur. Yöntem lisans ve hukuk açısından hassastır: `research/competitor-benchmark.md`, karar Q4. Karar alınmadan rakip verisi toplanmaz.
