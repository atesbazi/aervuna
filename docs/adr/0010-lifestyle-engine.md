# ADR-0010: Yaşam tarzı motoru — deterministik, açıklanabilir, sunucuda

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Claude (Âkif'in yetki devriyle), Âkif bilgilendirildi
- **İlgili:** ADR-0003, ADR-0005, ADR-0009, `product/05-lifestyle.md`

## Bağlam
Yaşam tarzı önerileri (kıyafet, şemsiye, koşu saati, çamaşır…) ürünün ikinci değer ayağı. Aynı öneriler uygulamada, widget'ta ve bildirimde tutarlı olmalı; ölçülebilir ve açıklanabilir olmalı; kişiselleştirilebilmeli ama hesap ve konum geçmişi gerektirmemeli.

## Değerlendirilen seçenekler
1. **Sunucuda (Rust domain) deterministik kural motoru** — tek mantık her yüzeyde; test ve sürümleme kolay; çıktı katma değerli ürün olarak lisans dostu. Eksi: kişiselleştirme istekle parametre taşımalı.
2. **Cihazda (Dart) hesaplama** — çevrimdışı çalışır, kişiselleştirme doğal. Eksi: Android widget (Kotlin) ve iOS widget (Swift) için mantık kopyalanır; bildirim sunucudan tetiklenecekse yine sunucu gerekir.
3. **ML tabanlı öneri** — Eksi: veri yok, açıklanamaz, test edilemez; Faz 3 öncesi anlamsız.

## Karar
**Seçenek 1.** Öneriler Rust `domain` katmanında saf fonksiyonlar olarak, sürüm numaralı (`lifestyle_rules_version`) kurallarla hesaplanır ve `/v1/forecast` yanıtında `lifestyle` bloğunda döner. Her öneri `value`, `why` (girdi ve eşiklerden üretilen kısa gerekçe kodu + parametreleri) ve Faz 3'ten itibaren `confidence` taşır. Kişiselleştirme parametreleri (ör. `thermalBias` −2…+2) cihazda tutulur ve sorgu parametresi olarak gelir; sunucu bunları saklamaz. Widget'lar uygulamanın yazdığı anlık görüntüyü okur (ADR-0004). ML, Faz 3 sonrasında ayrı bir ADR ile değerlendirilir.

## Sonuçlar
- **Olumlu:** Tek doğruluk kaynağı; birim testli; isabet ölçümü sunucuda mümkün; WeatherKit ve diğer lisanslarda "dönüştürülmüş katma değerli ürün" sınıfında.
- **Olumsuz:** Çevrimdışında son önbelleklenmiş öneri gösterilir; yeni hesap yapılamaz.
- **Geri dönüş maliyeti:** düşük — kurallar saf fonksiyon; gerekirse Dart'a port edilebilir.

## Doğrulama
Her öneri için formül ve test vektörleri `product/05-lifestyle.md` → Formüller'de. Faz 2–3'te şemsiye önerisinin isabeti (POD/FAR) doğrulama raporunda.
