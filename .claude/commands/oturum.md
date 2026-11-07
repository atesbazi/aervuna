---
description: Oturum başlangıç ritüeli — bağlamı docs/'tan kur ve oturum planı sun
---
CLAUDE.md → "Oturum ritüeli"ni eksiksiz uygula:

1. `docs/progress.md` → Durum Özeti, Açık sorular, Son oturum.
2. `docs/plan.md` → aktif fazın Kapsam ve Kabul kriterleri.
3. `docs/backlog.md` → sıradaki story'ler (ID).
4. İlgili `docs/architecture/` dosyaları ve ADR'ler; veri/sağlayıcıya dokunacaksan `docs/research/license-notes.md`.
5. Kod varsa ilgili bileşenin yerel test/lint komutlarını çalıştır (CI henüz yok); kırmızıysa önce onu düzelt.

Çıktı (kısa):
- Aktif faz ve son durum (2 satır)
- Bu oturumun planı (3–6 madde, story ID'leriyle)
- Engel veya açık soru varsa (seçenek + öneri)

Ek odak (varsa): $ARGUMENTS
