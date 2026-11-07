# Veri Sağlayıcı Karar Dokümanı (Faz 0)

- **Tarih:** 2026-11-07, revizyon 2026-11-08
- **Canlı sürüm:** [Claude Docs](https://claude.ai/artifact/72J8iYJrrGgEHB5GKzXfsm) — ayrışırsa bu dosya esastır
- **Bağlı ADR'ler:** 0002, 0003

## Özet karar
MVP'de ana kaynak **Open-Meteo ticari paketi**, doğruluk kıyası **Meteoblue**. **Apple WeatherKit** yalnız opsiyonel gösterim kaynağı; lisansı paylaşılan önbelleği, arşivlemeyi ve türetilmiş veritabanını yasaklıyor. **Google Weather API kesin olarak elendi.**

- **Open-Meteo:** Veri CC BY 4.0; arşiv, doğrulama ve türev üretimi serbest. Sunucu self-host edilebilir. Ham model çıktısı; doğruluk üstünlüğünü bizim düzeltme katmanımız üretecek.
- **Meteoblue:** Doğruluk kıyası. Sözleşmede arşiv ve doğrulama hakkı yazılı olursa ana kaynağa geçebilir. Bazı ürünlerde zorunlu destek paketi var.
- **WeatherKit:** Attachment 8 — 1.2 ham veriye ücret yok; 1.5 toplu indirme ve türetilmiş veritabanı yasak; 1.6 önbellek yalnız geçici ve performans amaçlı. Doğrulama arşivi de riskli; "ölç, sonra seç" stratejisine uymuyor.
- **Tomorrow.io ve Rainbow.ai:** Yalnız Türkiye'de nowcasting saha testi.

**Faz 0 çıkış kriteri:** Ana kaynak ve kıyas sağlayıcısından yazılı onay: ticari hava durumu uygulamasında kullanım, paylaşılan önbellek, doğrulama arşivi, türev endeks üretimi. 100 bin DAU senaryosunda aylık maliyet teyidi.

## Değerlendirme kriterleri
Sıra: **lisans → birim ekonomisi → Türkiye kapsamı → doğruluk**. Lisansı geçemeyen sağlayıcı doğruluğundan bağımsız elenir.

| Kriter | Soru | Eşik |
|---|---|---|
| Lisans | Asıl amacı hava durumu olan uygulamada kullanım serbest mi? | Yazılı "evet" |
| Önbellek | Kullanıcılar arası paylaşılan grid önbelleği, ne kadar süre? | ≥ 15 dk |
| Arşiv | Doğrulama ve model eğitimi için saklama? | Yazılı "evet" (ana kaynak için) |
| Türev ürün | Yaşam tarzı endeksleri ve kendi blend'imiz? | Serbest |
| Atıf | Biçim ve yer | Alt bilgi düzeyinde |
| Birim ekonomisi | 100 bin DAU aylık maliyet | Gelir modeline göre |
| Türkiye kapsamı | Dakikalık yağış, uyarı, radar | Teyitli |
| Doğruluk | Bağımsız benchmark + kendi METAR doğrulamamız | Faz 2'de ölçülür |
| SLA | Uptime ve destek | ≥ %99,9 |

## Sağlayıcı karşılaştırması
| Sağlayıcı | Fiyat (kamuya açık) | Lisans ve dikkat | Türkiye / nowcasting | Rol |
|---|---|---|---|---|
| [Open-Meteo](https://open-meteo.com/en/pricing) | Standard 1M, Professional 5M, Enterprise 50M+ çağrı/ay; tutar teklifle | Ücretsiz sürüm ticari kullanıma kapalı. Veri CC BY 4.0; self-host mümkün | Nowcasting yok; 30+ ulusal model | Ana kaynak ve veri platformu |
| [Meteoblue](https://business.meteoblue.com/pricing) | Premium Weather API 400 €/ay'dan; kredi çarpanı (multi-model 1 saatlik 8x) ve zorunlu destek seviyesi | Önbellek ve arşiv hakkı yazılı sorulmalı | Radar + uydu ile yağış; yıldırım nowcast.de | Doğruluk kıyası |
| [Tomorrow.io](https://apiscout.dev/blog/best-weather-climate-apis-2026) | Kapalı | Kurumsal sözleşme | Avrupa ve Orta Doğu'nun bir kısmı [radarsız bölge](https://status.tomorrow.io/incidents/2zl0lp2px9k3) | Nowcasting saha testi |
| [Apple WeatherKit](https://developer.apple.com/weatherkit/get-started/) | 500 bin/ay dahil; 1M 49,99 $; 10M 499,99 $; 200M 9.999,99 $ | [Attachment 8](https://developer.apple.com/support/terms/apple-developer-program-license-agreement) 1.2, 1.5, 1.6; EULA uyarısı 2.2 | Dakikalık yağış seçili bölgelerde; Türkiye test edilmeli | Opsiyonel gösterim |
| [Azure Maps Weather](https://learn.microsoft.com/en-gb/Azure/azure-maps/understanding-azure-maps-transactions) | Kullanım bazlı | Lisans sorulmalı | Dakikalık tahmin var; Microsoft [ForecastWatch 2024 1–5 gün küresel 1.](https://forecastwatch.com/2025/07/31/new-report-analysis-of-2024-one-to-five-day-out-forecasts/) | Benchmark adayı |
| [Foreca](https://corporate.foreca.com/en/weather-data) | 1M istek/ay 990 €/yıl, 10M 4.950 €/yıl (üçüncü taraf kaynağı, teyit) | Tüketici paketi var | Kendi açıklaması: ForecastWatch 2024 ilk 3 | Benchmark adayı |
| [The Weather Company](https://www.weathercompany.com/weather-data-apis/weather-data-apis-packages-pricing/) | Satış ekibi | Kurumsal | Benchmark raporu TWC siparişi | Ölçek aşamasında |
| [AccuWeather](https://developer.accuweather.com/documentation/overview.md) | Core ve MinuteCast ayrı | Şartlar okunmalı | MinuteCast Türkiye sorulmalı | Opsiyonel |

## Elenenler
- **Google Weather API:** [Hizmete özel şartlar 21.1](https://cloud.google.com/maps-platform/terms/maps-service-terms) hava durumu uygulamasında kullanımı yasaklıyor; saatlik/anlık veri en çok 1 saat önbelleklenebiliyor.
- **Google Air Quality API:** Kullanım rota çözümleri ve çevresel risk endeksleriyle sınırlı.
- **Google Pollen API:** Kendi endeks ve tahminler için serbest, 24 saat önbellek; koşullu aday.
- **Weatherbit:** "2026 benchmark lideri" iddiası doğrulanamadı.

## Tamamlayıcı veri
| İhtiyaç | Kaynak | Koşul | Not |
|---|---|---|---|
| Ham model | [ECMWF açık veri](https://www.ecmwf.int/node/29497) | CC-BY-4.0, ticari serbest | Ücretsiz alt küme 25 km; 9 km'lik 2 saat gecikmeli alt küme 2026 planında |
| Hava kalitesi, polen | [CAMS](https://atmosphere.copernicus.eu/smart-decisions) | Kısıtsız, görünür atıf | Avrupa ~10 km, 4 gün; Türkiye kapsamı kontrol |
| Radar tile | [RainViewer](https://rainviewer.com/api.html) | Ücretsiz yalnız kişisel/eğitim | Ticari ayrı anlaşma |
| Radar + dakikalık yağış | [Rainbow.ai](https://rainbow.ai/business) | 0,1 $/1 bin çağrı; 5 bin ücretsiz | Türkiye kapsamı teyit |
| Doğrulama gözlemi | [NOAA AviationWeather Data API](https://aviationweather.gov/data/api/) | Kamu verisi | **Son 30 gün** sorgulanabilir; 100 istek/dk; arşivi biz tutarız |
| Türkiye istasyon/yıldırım | MGM ([MEVBİS](https://mgm.gov.tr/site/gizlilik-politikasi.aspx), [katsayılar](https://www.mgm.gov.tr/site/urunler/katsayi.pdf)) | Ürün bazlı ücret | Gerçek zamanlı API ve yeniden dağıtım belirsiz |

## Birim ekonomisi
Örnek hesap, paylaşılan grid önbelleğine izin veren sağlayıcı için; fiyatlar WeatherKit basamaklarıyla. WeatherKit'in kendisi 1.6 nedeniyle paylaşılan önbelleğe izin vermez; onun gerçek maliyeti sol taraftır.

| DAU | Kullanıcı başı çağrı/ay | Maliyet $/ay | Aktif hücre | Grid önbellekli çağrı/ay | Maliyet $/ay |
|---|---|---|---|---|---|
| 10.000 | 6M | 499,99 | 3.000 | 4,3M | 249,99 |
| 100.000 | 60M | 4.999,99 | 12.000 | 17,3M | 999,99 |
| 1.000.000 | 600M | Kurumsal | 30.000 | 43,2M | 2.499,99 |

Varsayımlar: kullanıcı başı günde 20 çağrı; hücre 30 dk'da bir yenilenir; Türkiye 5 km hücrelerle ~31 bin hücre.
- Open-Meteo sabit aylık ücret; 100 bin DAU (17,3M) Enterprise'a denk; self-host'ta yalnız sunucu.
- Meteoblue: 7 günlük saatlik temel paket çağrı başı 8.000 kredi; destek paketi eklenmeli.
- Radar ve dakikalık yağış ayrı faturalanır.

## Sağlayıcılara sorulacaklar (ortak set)
1. Veriniz, asıl amacı hava durumu olan ticari bir mobil uygulamada kullanılabilir mi?
2. Veriyi kullanıcılar arasında paylaşılan grid bazlı bir önbellekte ne kadar süre tutabiliriz?
3. Verinizden kendi yaşam tarzı endekslerimizi ve kendi blend tahminimizi üretip gösterebilir miyiz? Tahminlerinizi doğrulama ve model eğitimi için arşivleyebilir miyiz?
4. Zorunlu atfın biçimi nedir? Logo mu, metin mi, nerede?
5. Türkiye'de dakikalık yağış, yıldırım ve resmi uyarı kapsamınız nedir? Radar mı, uydu mu?
6. 100 bin DAU tablosu için aylık teklif ve SLA nedir?

Yanıtlar: [`provider-responses.md`](provider-responses.md).

## Teknoloji yığını ve faz planı
Bkz. `../plan.md` ve ADR 0004–0008.
