# Rakip Kıyası Yöntemi (WX-019, karar verildi)

## Neden gerekli
Ürünün kalbi ve pazarlama mesajı: Aervuna, App Store/Play uygulamalarından ve cihazlara gömülü hava uygulamalarından daha tutarlı ve daha doğru tahmin verir (`product/01-vision.md`). Bu iddia kendi doğrulamamızla tek başına kanıtlanamaz; rakiplerin aynı yer ve zamandaki tahminleriyle karşılaştırma gerekir.

## Kısıtlar
- **Apple Weather (gömülü iOS):** Verisi Apple Weather servisinden gelir. Aynı veri WeatherKit ile alınabilir, ama Attachment 8 madde 1.5 ve 1.6 arşivlemeyi ve türetilmiş veritabanını yasaklıyor (`license-notes.md`). WeatherKit ile rakip arşivi kurulmaz.
- **Uygulamaları kazımak (scraping):** Mağaza uygulamalarının ve sitelerinin kullanım şartları genellikle otomatik veri toplamayı yasaklar. Hukuki görüş alınmadan yapılmaz.
- **Reklam iddiası:** Karşılaştırmalı reklamda iddianın nesnel ve doğrulanabilir olması gerekir; yöntem ve dönem açıklanabilir olmalı. (Hukuki değerlendirme önerilir; bu doküman hukuki görüş değildir.)

## Seçenekler
| # | Yöntem | Artı | Eksi |
|---|---|---|---|
| A | **Bağımsız üçüncü taraf ölçümü** (ör. [ForecastWatch](https://forecastwatch.com/2025/07/31/new-report-analysis-of-2024-one-to-five-day-out-forecasts/) özel rapor hizmeti; Aervuna'u kendi ölçümlerine dahil ettirme) | Pazarlamada en savunulabilir; rakip verisini toplama yükü bizde değil | Ücretli; teklif gerekir; zaman alır |
| B | **İnsan panelli örnekleme** (sabit saatlerde, sabit şehirlerde gömülü uygulamaların gösterdiğini kayıt) | Ucuz; hızlı içgörü | Küçük örneklem; şartlar açısından belirsiz; pazarlama iddiası için zayıf |
| C | **Kamuya açık benchmark'larla dolaylı kıyas** (ForecastWatch yayınlarındaki metriklerle aynı metodolojiyi kendi istasyonlarımıza uygulamak) | Ücretsiz; metodoloji uyumu | İstasyon ve dönem farklı; doğrudan "daha iyi" iddiası kurulamaz |
| D | **Lisanslı sağlayıcı karşılaştırması** (rakip uygulamaların kullandığı sağlayıcılardan lisansla veri alıp kıyas) | Lisanslı ve tekrarlanabilir | Hangi uygulamanın hangi sağlayıcıyı kullandığı her zaman bilinmez; uygulama son işlemeyi kapsamaz |

## Öneri
- **Faz 0–1:** C (iç pusula) + kendi doğrulama raporlarımız. Rakip verisi toplanmaz.
- **Faz 2 öncesi:** A için teklif istenir (ÜS). Pazarlama iddiası yalnız A'nın sonuçlarıyla ve ölçülen bölge/ufuklarla sınırlı yapılır.
- B yalnız ürün içgörüsü için ve hukuki görüş sonrası.

## Karar (2026-11-08, Claude, Âkif'in yetki devriyle)
- **Faz 0–1: yöntem C** (iç pusula). Rakip verisi toplanmaz; kendi doğrulamamız ForecastWatch yayınlarındaki metodolojiyle hizalanır (WX-019).
- **Faz 2 öncesi: yöntem A** için teklif (Âkif görevi WX-006). Pazarlama iddiası yalnız A sonuçlarıyla.
- B ve D yapılmaz (B: şart/hukuk belirsizliği ve küçük örneklem; D: uygulamanın son işlemesini ölçmez).
- Gerekçe: en savunulabilir iddia (A) + bugün sıfır maliyet ve sıfır hukuki risk (C).
