# ADR-0003: WeatherKit yalnız opsiyonel gösterim kaynağı

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0002, `research/license-notes.md` → Apple

## Bağlam
WeatherKit en ucuz ciddi seçenek. Ancak Apple Developer Program License Agreement, Attachment 8:
- **1.2** Ham Apple Weather verisine ücret alınamaz; ücret yalnız ham verinin geri çıkarılamayacağı biçimde dönüştürülmüş katma değerli ürünler için alınabilir.
- **1.5** Toplu indirme/besleme yasak; veri ikincil veya türetilmiş bir veritabanının parçası olamaz.
- **1.6** Dokümantasyonda açıkça izin verilmedikçe veri yalnız geçici, sınırlı ve performans amaçlı önbelleklenebilir.
- **2.2** Gerçek zamanlı hava rehberliği sunan uygulamanın EULA'sında belirli uyarı metni zorunlu.

## Karar
WeatherKit kullanılacaksa:
- Yalnız **kullanıcı başına, istemci tarafında gösterim** için.
- **Arşivlenmez**, `own`/`licensed` şemalarına yazılmaz, kullanıcılar arası paylaşılan önbelleğe girmez, model eğitiminde kullanılmaz.
- Olduğu gibi gösterilen WeatherKit verisi ücretli bir özelliğin arkasına konmaz.
- Adaptörü varsa `archive_allowed = false`, `shared_cache_ttl = 0`.

## Sonuçlar
- **Olumlu:** Lisans ihlali riski sıfıra yakın; gerekirse ucuz ikinci görüş.
- **Olumsuz:** Ucuzluk avantajı büyük ölçüde kaybolur; WeatherKit'in doğruluğunu kendi yöntemimizle ölçemeyiz.
- **Geri dönüş maliyeti:** düşük.

## Doğrulama
Kod incelemesinde: WeatherKit kaynaklı hiçbir alan veritabanı yazma yoluna ya da paylaşılan önbelleğe ulaşmıyor (test ile zorlanır).
