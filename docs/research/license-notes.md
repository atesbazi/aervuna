# Lisans Notları (bağlayıcı referans)

> Her sağlayıcı için: ne serbest, ne yasak, kaynak, son kontrol tarihi. Kod yazmadan önce buraya bakılır (AGENTS.md §2.2).
> Bir sağlayıcının yazılı yanıtı geldiğinde `provider-responses.md`'ye işlenir ve buradaki satır güncellenir.

| Sağlayıcı | Ticari hava uygulaması | Paylaşılan önbellek | Arşiv / doğrulama | Türev ürün | Ham veriye ücret | Atıf | Adaptör bayrakları | Kaynak | Kontrol |
|---|---|---|---|---|---|---|---|---|---|
| Open-Meteo (ticari) | **Evet** (yazılı) | Evet (saklama + yeniden dağıtım serbest; süre sınırı yok) | **Evet** (yazılı: ham/işlenmiş veriyi saklama, analiz, model eğitimi) | **Evet** (yazılı; ücretli katman dahil, kısıt yok) | Serbest | Open-Meteo **ve** kullanılan modelin resmi sağlayıcısı ([licence](https://open-meteo.com/en/licence)) | `archive_allowed=true`, `shared_cache_ttl=30 dk` (tazelik kararı), atıf model bazlı | [pricing](https://open-meteo.com/en/pricing), [licence](https://open-meteo.com/en/licence), yazılı yanıt (`provider-responses.md`) | 2026-11-09 (yazılı yanıt) |
| Open-Meteo (ücretsiz) | **Hayır** (ticari olmayan) | — | — | — | — | — | Kullanılmaz | aynı | 2026-11-07 |
| ECMWF açık veri | Evet | Evet | Evet | Evet | Serbest | CC-BY-4.0 zorunlu, örnek metin ECMWF'de | `archive_allowed=true` | [ECMWF](https://www.ecmwf.int/node/29497) | 2026-11-07 |
| Meteoblue | Sorulacak | Sorulacak | Sorulacak | Sorulacak | Sorulacak | Logo+link karşılığı indirim seçeneği | Yanıta kadar `archive_allowed=false`, `shared_cache_ttl=0` | [pricing](https://business.meteoblue.com/pricing) | 2026-11-07 |
| Apple WeatherKit | Evet (gösterim) | **Hayır** (1.6) | **Hayır** (1.5, 1.6) | Yalnız dönüştürülmüş katma değerli ürün (1.2) | **Hayır** (1.2) | Apple Weather markası + yasal link; uyarı metni değiştirilemez (1.4); EULA uyarısı (2.2) | `archive_allowed=false`, `shared_cache_ttl=0` | [DPLA Attachment 8](https://developer.apple.com/support/terms/apple-developer-program-license-agreement) | 2026-11-08 (metin okundu) |
| Google Weather API | **Hayır** (21.1) | 1 saat | — | — | — | — | Kullanılmaz | [Maps Service Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms) | 2026-11-07 |
| Google Air Quality API | Yalnız rota ve risk endeksi (2.1) | 1 saat | — | — | — | — | Kullanılmaz | aynı | 2026-11-07 |
| CAMS | Evet | Evet | Evet | Evet | Serbest | Görünür, sonda gizlenemez | `archive_allowed=true` | [CAMS](https://atmosphere.copernicus.eu/smart-decisions) | 2026-11-07 |
| NOAA AviationWeather (METAR) | Evet (kamu verisi) | Evet | Evet (son 30 gün API; arşivi biz tutarız) | Evet | — | Kaynak belirtilir | 100 istek/dk, özel User-Agent | [Data API](https://aviationweather.gov/data/api/) | 2026-11-08 |
| RainViewer | **Hayır** (ücretsiz: kişisel/eğitim) | — | — | — | — | Zorunlu | Kullanılmaz (ticari anlaşma yoksa) | [API](https://rainviewer.com/api.html) | 2026-11-07 |
| Rainbow.ai | Ücretli plan | Sorulacak | Sorulacak | Sorulacak | — | Sorulacak | — | [business](https://rainbow.ai/business) | 2026-11-07 |
| MGM | Ücretli veri satışı | Sorulacak | Sorulacak | Sorulacak | — | Sorulacak | — | [katsayılar](https://www.mgm.gov.tr/site/urunler/katsayi.pdf) | 2026-11-07 |

## Open-Meteo — yazılı yanıt özeti (2026-11-09)
- Ticari plan tüketici hava uygulaması için uygun.
- Ham ve işlenmiş veri ile analiz sonuçları kullanılabilir, saklanabilir, yeniden dağıtılabilir. Tek koşul atıf: Open-Meteo + resmi veri sağlayıcısı (ör. ECMWF, DWD, NOAA, Météo-France; yanıtı üreten modele göre).
- SLA yalnız Enterprise planında; Professional planında uptime taahhüdü yok.
- Self-host: Open-Meteo lisansı gerekmez; sunucu kodunda yaptığımız değişiklikler ve tescilli eklemeler açık kaynak ve herkese açık yayımlanmalı (repo LICENSE). Yorum (varsayım): kendi API'miz ve pipeline'ımız bu sunucunun parçası değilse kapsam dışı; self-host kararı verilirse lisans metniyle ayrıca incelenir.

## Apple WeatherKit — Attachment 8 özet (2026-11-08 okundu)
- 1.2 Orijinal biçimdeki veriye ücret alınamaz; dönüştürülmüş katma değerli ürüne ücret alınabilir; alt lisans verilemez; dahili amaçla kullanım serbest.
- 1.3 Acil durum / hayat kurtarma amaçlı tasarlanamaz, pazarlanamaz.
- 1.4 Yalnız WeatherKit API ile erişim; atıf zorunlu; uyarılar değiştirilemez.
- 1.5 Toplu indirme/besleme, kazıma yasak; ikincil veya türetilmiş veritabanında kullanılamaz.
- 1.6 Dokümantasyonda izin yoksa önbellek/ön-yükleme/saklama yalnız geçici, sınırlı ve performans amaçlı.
- 2.2 Gerçek zamanlı rehberlik uygulamasının EULA'sında belirtilen uyarı metni zorunlu.
- ML/model eğitimi açıkça anılmıyor; 1.5 ve 1.6 kapsamında risk kabul edilir → yapılmaz.

## Google Maps Platform — Weather API (Service Specific Terms, 2026-10-15 sürümü)
- 21.1 Weather API'den alınan içerik bir Google ürününü yeniden yaratmak için kullanılamaz; örnek: asıl amacı hava durumu bilgisi olan hava uygulaması veya modeli.
- 21.2 Önbellek: anlık durum ve saatlik tahmin 1 saat; günlük tahmin 24 saat; bugünün tahmini 30 gün; saatlik geçmiş 240 saat; uyarılar 1 saat.
