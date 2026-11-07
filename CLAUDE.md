@docs/AGENTS.md

# CLAUDE.md — Aervuna

Bu repoda Claude (Claude Code) **ana geliştiricidir**. Ürün sahibi Âkif fazları onaylar.

## Oturum ritüeli (her oturumda, kısaltmadan)
1. `docs/progress.md` → **Durum Özeti** ve **Son oturum** bölümlerini oku. Aktif fazı ve sıradaki adımı bul.
2. `docs/plan.md` → aktif fazın **Kapsam** ve **Kabul kriterleri** bölümünü oku.
3. İlgili `docs/backlog.md` story'lerini ID ile oku (`WX-xxx`).
4. Dokunacağın alanın `docs/architecture/` dosyasını ve ilgili ADR'leri oku.
5. CI henüz yok (Âkif, 2026-11-08). Kod varsa ilgili bileşenin yerel test/lint komutlarını çalıştır; kırmızıysa önce onu düzelt.
6. Âkif'e 3–6 maddelik oturum planı sun (canlı oturumda). Zamanlanmış oturumda planı `progress.md` → Son oturum'a yaz ve başla.

## Zamanlanmış oturum modu
Proje, saati olmayan ve Âkif'in elle başlattığı bir scheduled task ile ilerler. Böyle bir oturumda:
- Oturum ritüelini uygula; canlı onay bekleme.
- Yalnız aktif fazın sıradaki story'lerini yap. Bir oturumda makul büyüklükte iş bitir, yarım bırakacaksan durumu net yaz.
- Açık soru çıktığında Âkif'e sorma: `Açık sorular ve kararlar` kuralına göre kararı kendin ver, gerekçesiyle yaz ve devam et.
- Küçük, test edilmiş commit'ler at ve `main`'e push et (Faz 0). Faz 1'den itibaren `phase-N/…` dalı + PR.
- Oturum sonunda `progress.md` → Son oturum'a ne yapıldığını, sıradaki 1–3 adımı ve bu oturumda verdiğin kararları yaz; commit + push.
- Faz bittiyse checkpoint raporunu yaz ve **dur**. "Faz N onaylandı" satırı `progress.md`'de ya da sohbette Âkif'ten gelir; onaysız sonraki faza geçme.

## Oturum kapanışı
- `docs/progress.md` güncellenir: Durum Özeti, story durumu, **Kararlar**, **Son oturum** (ne yapıldı, sıradaki 1–3 adım, verilen kararlar), gerekirse **Ürün sahibi görevleri**.
- Yeni bir teknik karar verildiyse ADR ya da Kararlar satırı yazılır. İkisinden biri olmadan karar yoktur.
- Faz bittiyse `docs/templates/checkpoint.md` formatında rapor yazılır ve **durulur**.

## Bu projeye özgü bağlayıcı kurallar
- **Yaşam tarzı ikinci değer ayağıdır** (ADR-0010, `docs/product/05-lifestyle.md`): her öneri açıklanabilir, deterministik, ölçülebilir. Opsiyonel bir eklenti değildir.
- **Ürünün kalbi doğruluktur.** Mağazadaki ve cihazlara gömülü hava uygulamalarından daha tutarlı ve daha doğru tahmin, ürünün ana özelliği ve pazarlama stratejisidir. Çatışmada öncelik sırası: doğruluk → lisans/gizlilik → görsel deneyim → yaşam tarzı (`docs/AGENTS.md §0`).
- **Global ürün.** Arayüz varsayılanı İngilizce; Türkçe uygulama içinden seçilir. Cihaz diline otomatik uyum ileriye bırakıldı (IDEA-006).
- **Şık ve ihtiyaç dahilinde sinematik.** Sinematik anlar bilgiyi güçlendirdiği yerde; günlük kullanımda sakin ve okunur (`docs/design/01-visual-direction.md`).
- **Lisans önce gelir (ADR-0002, ADR-0003).** Bir sağlayıcının verisini arşive, paylaşılan önbelleğe veya modele yazmadan önce `docs/research/license-notes.md` içindeki iznine bak. İzin yoksa yazma. Her sağlayıcı adaptöründe `archive_allowed` ve `shared_cache_ttl` bayrakları zorunludur.
- **Google Weather API ve Google Air Quality API kullanılmaz** (lisans gereği, ADR-0002).
- **WeatherKit verisi** asla arşivlenmez, kullanıcılar arası paylaşılan önbelleğe girmez, olduğu gibi ücretli bir özelliğin arkasına konmaz (ADR-0003).
- **Doğruluk iddiası kanıtsız yazılmaz.** Uygulama metninde, mağaza açıklamasında veya pazarlamada "en doğru" benzeri ifade, `docs/architecture/05-forecast-verification.md` metodolojisiyle üretilmiş rapora dayanmadan kullanılmaz.
- **Güven skoru** kalibre bir olasılıktır; geçmiş doğrulama verisinden hesaplanır. Sezgisel puan "güven" diye gösterilmez (ADR-0009).
- **Kendi veri setimiz ile üçüncü taraf verisi ayrı şemalardadır** (`licensed_*` / `own_*`, ADR-0007).
- Dil: dokümanlar Türkçe; kod, identifier ve commit mesajları İngilizce (Conventional Commits).

## Açık sorular ve kararlar (Âkif, 2026-11-08)
- **Açık soruları Âkif'e sorma.** Ürün, teknik, lisans yorumu, tasarım dahil her açık soruda seçenekleri değerlendir ve **en mantıklı, en performanslı, en stabil ve doğru** yolu seç. Kararı gerekçesi ve dayanağıyla (kod, ölçüm, kaynak, ADR) `progress.md` → Kararlar'a yaz ve uygula. Bağlayıcı nitelikteyse ADR yaz ve `Accepted` olarak işaretle (Karar verenler: "Claude, Âkif'in yetki devriyle").
- Dayanak zayıfsa kararı "varsayım" diye işaretle ve en kolay geri alınan seçeneği seç.
- **Lisans belirsizliğinde** her zaman en güvenli yorumu seç (saklama yok, paylaşılan önbellek yok, ücretli özellik yok) ve öyle kodla.
- **Âkif'te kalanlar (soru değil, görev):** faz/checkpoint onayı; para harcama ve ücretli plan; sağlayıcılarla yazışma, sözleşme, marka tescili, mağaza hesapları gibi yalnız onun yapabileceği işler; geri alınamaz işler (veri/dal/etiket silme, gizli anahtar). Bunlar `progress.md` → Ürün sahibi görevleri'ne yazılır; iş bunlara takılırsa bloklanmayan sonraki işe geçilir.

## Komutlar
Henüz kod yok. Bileşenler eklendikçe buraya yazılır (`docs/architecture/01-tech-stack.md` → Komutlar).

## Proje komutları (Claude Code)
`.claude/commands/` altında: `/oturum` (başlangıç ritüeli), `/kapanis` (progress güncelleme), `/checkpoint`, `/adr`, `/story`.
