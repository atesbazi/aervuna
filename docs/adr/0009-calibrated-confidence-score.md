# ADR-0009: Güven skoru kalibre bir olasılıktır

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** `architecture/05-forecast-verification.md`, `product/02-features.md`

## Bağlam
Ürünün ana farkı "tahmine ne kadar güvenilebileceğini" söylemek. Bir modelin sezgisel yorumu ya da keyfi bir puan "güven" diye gösterilirse kullanıcıyı yanıltır ve iddia savunulamaz.

## Karar
- "Güven" yalnız geçmiş doğrulama verisinden türetilmiş, **kalibre** bir değerdir: değişken × tahmin ufku × yer × mevsim için hata dağılımı ya da olay olasılığı.
- Kategorik gösterim (Yüksek/Orta/Düşük) kalibre olasılık aralıklarından türetilir; aralıklar dokümante edilir.
- Yeterli doğrulama verisi olmayan durumda güven **gösterilmez** ("henüz ölçülmedi").
- Faz 3'ten önce güven gösterimi yoktur.

## Sonuçlar
- **Olumlu:** Savunulabilir ve test edilebilir fark.
- **Olumsuz:** Veri birikene kadar özellik yok.
- **Geri dönüş maliyeti:** düşük.

## Doğrulama
Güvenilirlik diyagramı ve Brier skoru; ayrılmış test döneminde kalibrasyon hatası eşiği (Faz 3 başında yazılır).
