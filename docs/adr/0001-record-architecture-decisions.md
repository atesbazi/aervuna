# ADR-0001: Mimari kararları ADR ile kaydetmek

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude

## Bağlam
Proje tek geliştirici ve AI ajanla, oturumlar arasında bağlam kaybı riskiyle ilerliyor. Kararların gerekçesi sohbet geçmişinde kalırsa sonraki oturumlar tutarsız kararlar verir.

## Karar
Bağlayıcı her mimari ve teknoloji kararı `docs/adr/` altında numaralı bir ADR ile kaydedilir. Küçük, geri alınabilir teknik kararlar `progress.md` → Kararlar tablosuna yazılır. İkisinden birinde yazılı olmayan karar yok sayılır.

## Sonuçlar
- **Olumlu:** Ajan her oturumda aynı kararlardan başlar; kararın neden alındığı görünür.
- **Olumsuz:** Küçük bir yazım yükü.
- **Geri dönüş maliyeti:** düşük.

## Doğrulama
Checkpoint'te bağımlılık ve teknoloji listesi ADR'lerle karşılaştırılır.
