# Risk Kaydı

| # | Risk | Olasılık | Etki | Azaltma | Sahip |
|---|---|---|---|---|---|
| R1 | Sağlayıcı lisansı arşiv, paylaşılan önbellek veya türev ürüne izin vermez | Orta | Çok yüksek | Faz 0 yazılı onay; adaptörde `archive_allowed` bayrağı; ECMWF açık verisi bağımsız yedek | ÜS |
| R2 | WeatherKit Attachment 8 ihlali (arşiv, paylaşılan önbellek, ham veriye ücret) | Düşük | Yüksek | ADR-0003; kod incelemesinde kontrol; WeatherKit yalnız istemci tarafında gösterim | Ajan |
| R3 | Türkiye'de nowcasting/radar kapsamı yetersiz | Yüksek | Orta | Faz 0'da yazılı teyit; nowcasting Faz 4+'a bırakıldı | ÜS |
| R4 | "En doğru" iddiası kanıtsız kalır; reklam mevzuatı riski | Orta | Yüksek | Doğrulama metodolojisi ve rapor; kanıtsız iddia yasak (CLAUDE.md) | Ajan + ÜS |
| R5 | Open-Meteo ham model çıktısı mağaza uygulamalarından daha az doğru çıkar | Orta | Yüksek | Doğrulama raporu; Meteoblue kıyası; Faz 3 bias düzeltme | Ajan |
| R6 | Mac yokluğu iOS'u geciktirir | Orta | Orta | Önce Android (ADR-0008); bulut derleme yedek | ÜS |
| R7 | Maliyet artışı (API çağrısı, sunucu) | Orta | Orta | Grid önbelleği; sabit ücretli plan; self-host seçeneği; aylık maliyet kontrolü | ÜS |
| R8 | İsim/marka çakışması | Orta | Yüksek | WX-002 araması; yedek isimler | ÜS |
| R9 | MGM verisine ticari erişim yok ya da pahalı | Yüksek | Düşük | METAR + ECMWF yeterli zemin; MGM opsiyonel | ÜS |
| R10 | KVKK: konum verisinin işlenmesi | Orta | Yüksek | Koordinat sunucuda hücreye indirgenir, ham konum loglanmaz; aydınlatma metni | Ajan |
| R11 | Tek geliştirici bant genişliği (paralel yan projeler) | Yüksek | Orta | Küçük fazlar, `progress.md` ile kesintisiz devam, zamanlanmış oturumlar | ÜS |
| R12 | Flutter + native widget ikiliği bakım yükü yaratır | Orta | Düşük | Widget'lar küçük ve yalnız okuma yapar; veri sözleşmesi tek JSON | Ajan |
| R13 | 60–90 günlük doğrulama mevsimselliği yansıtmaz | Yüksek | Orta | Ölçüm sürekli; kararlar yıllık veriyle yeniden gözden geçirilir | Ajan |

ÜS = ürün sahibi
