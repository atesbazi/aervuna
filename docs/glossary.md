# Sözlük

| Terim (TR) | Kod adı (EN) | Anlam |
|---|---|---|
| Sağlayıcı | `provider` | Tahmin verisi aldığımız dış kaynak (Open-Meteo, Meteoblue…) |
| Adaptör | `adapter` | Bir sağlayıcıyı `ForecastProvider` trait'ine bağlayan kod |
| Arşiv izni | `archive_allowed` | Sağlayıcı verisinin kalıcı saklanmasına lisansın izin verip vermediği |
| Paylaşılan önbellek süresi | `shared_cache_ttl` | Verinin kullanıcılar arasında paylaşılan önbellekte tutulabileceği süre; izin yoksa 0 |
| Grid hücresi | `grid_cell` | Konumun indirgendiği sabit alan birimi; önbellek ve gizlilik anahtarı |
| Tahmin ufku | `lead_time` | Tahminin yapıldığı an ile geçerli olduğu an arasındaki süre (saat) |
| Model koşusu | `run` | Bir NWP modelinin başlangıç zamanı (ör. ECMWF 00 UTC) |
| Nowcasting | `nowcast` | 0–2 (en çok 4) saatlik, genellikle radar tabanlı kısa vadeli tahmin |
| METAR | `metar` | Havalimanı rutin gözlem raporu; doğrulama için gerçekleşen değer |
| Doğrulama | `verification` | Tahminin gerçekleşen gözlemle karşılaştırılması |
| MAE | `mae` | Ortalama mutlak hata |
| Bias | `bias` | Ortalama işaretli hata (sistematik sapma) |
| Brier skoru | `brier` | Olasılıklı tahminin hata ölçüsü (0 en iyi) |
| POD / FAR | `pod` / `far` | Olay yakalama oranı / yanlış alarm oranı |
| Kalibrasyon | `calibration` | "%70" denen olayların gerçekten ~%70 oranında gerçekleşmesi |
| Bias düzeltme | `bias_correction` | Geçmiş hatadan öğrenilen sistematik sapmanın tahminden çıkarılması |
| Güven skoru | `confidence` | Tahminin tutma olasılığı; geçmiş doğrulamadan kalibre edilir (ADR-0009) |
| Yaşam tarzı endeksi | `lifestyle_index` | Konfor, kıyafet, koşu gibi kendi ürettiğimiz öneriler |
| Katma değerli ürün | value-added | Ham sağlayıcı verisinden geri çıkarılamayacak biçimde dönüştürülmüş çıktı |
| Lisanslı şema | `licensed` | Üçüncü taraf verisinin tutulduğu şema (yalnız izinli olanlar) |
| Kendi şemamız | `own` | Gözlem, kendi türev verimiz ve doğrulama sonuçları |
| Checkpoint | — | Faz sonu onay noktası |
