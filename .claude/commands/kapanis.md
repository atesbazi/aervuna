---
description: Oturum kapanışı — progress.md'yi güncelle, kararları yaz
---
Oturumu kapat:

1. `docs/progress.md`:
   - Durum Özeti (aktif faz, son tamamlanan story, sıradaki adım, engeller)
   - Story durumu tablosu
   - Kararlar: bu oturumda verilen her karar, gerekçe ve kaynakla
   - Açık soru çıktıysa: kararı ver (en mantıklı/performanslı/stabil/doğru), Kararlar'a gerekçesiyle yaz; yalnız Âkif'in yapabileceği işleri Ürün sahibi görevleri'ne ekle
   - Son oturum: `docs/templates/session-log.md` formatında en üste yeni kayıt
   - Story metrikleri (kapanan story varsa)
2. Yeni bir bağlayıcı karar verildiyse ADR yaz (`Accepted`, "Claude, Âkif'in yetki devriyle") ve `docs/adr/README.md`'ye ekle.
3. Backlog'a yeni fikir çıktıysa `IDEA-xxx` olarak ekle.
4. Değişiklikleri Conventional Commits ile commit'le (`docs(progress): …`).
5. Faz bittiyse `/checkpoint`'e geç.

Not: $ARGUMENTS
