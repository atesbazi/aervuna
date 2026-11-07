---
description: Faz sonu checkpoint raporu üret ve dur
---
Aktif faz için checkpoint hazırla:

1. `docs/plan.md` → aktif fazın kabul kriterlerini tek tek kanıtla (dosya, test çıktısı, rapor, ekran görüntüsü). Kanıtı olmayanı işaretleme.
2. İlgili bileşenlerin yerel test/lint komutlarını çalıştır ve sonucu rapora yaz (CI henüz yok).
3. Bağımlılık ve teknoloji listesini ADR'lerle karşılaştır; ADR dışı bir şey varsa raporda yaz.
4. Lisans kontrolü: bu fazda eklenen sağlayıcı/saklama `docs/research/license-notes.md` ile uyumlu mu?
5. `docs/templates/checkpoint.md` formatında raporu `docs/progress.md` → Checkpoint raporları'na ekle; faz durumunu ✋ yap.
6. **Dur.** Ürün sahibinin "Faz N onaylandı" mesajını bekle.

$ARGUMENTS
