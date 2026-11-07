# 03 — Gelir Modeli (taslak, karar Faz 2'de ADR ile)

## Kısıtlar
- WeatherKit kullanılırsa: olduğu gibi gösterilen Apple verisine ücret alınamaz (Attachment 8, 1.2).
- Diğer sağlayıcılarda yeniden satış ve ücretli erişim koşulları `research/license-notes.md`'den kontrol edilir.
- Kural: **Ücretli katman yalnız kendi ürettiğimiz değeri satar** (endeksler, güven, kişiselleştirilmiş bildirimler, gelişmiş widget/tema), ham tahmini değil.

## Seçenekler
1. Ücretsiz + Plus abonelik (aylık/yıllık).
2. Ücretsiz + reklam (görsel deneyimle çelişir; önerilmez).
3. Tek seferlik "pro" satın alma.

## Açık sorular
- Türkiye fiyat seviyesi; yıllık deneme.
- IAP altyapısı (RevenueCat vb.) — ADR gerekir.
