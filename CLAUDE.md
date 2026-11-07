@docs/AGENTS.md

# CLAUDE.md — Ufuk

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
- Ürün kararı gereken yerde o işi bırak, `progress.md` → Açık sorular'a seçenek + önerinle yaz ve bloklanmayan sıradaki işe geç.
- Küçük, test edilmiş commit'ler at ve `main`'e push et (Faz 0). Faz 1'den itibaren `phase-N/…` dalı + PR.
- Oturum sonunda `progress.md` → Son oturum'a ne yapıldığını, sıradaki 1–3 adımı ve açık soruları yaz; commit + push.
- Faz bittiyse checkpoint raporunu yaz ve **dur**. "Faz N onaylandı" satırı `progress.md`'de ya da sohbette Âkif'ten gelir; onaysız sonraki faza geçme.

## Oturum kapanışı
- `docs/progress.md` güncellenir: Durum Özeti, story durumu, **Kararlar**, **Son oturum** (ne yapıldı, sıradaki 1–3 adım, açık sorular).
- Yeni bir teknik karar verildiyse ADR ya da Kararlar satırı yazılır. İkisinden biri olmadan karar yoktur.
- Faz bittiyse `docs/templates/checkpoint.md` formatında rapor yazılır ve **durulur**.

## Bu projeye özgü bağlayıcı kurallar
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

## Açık sorular ve kararlar
- **Ürün, para, lisans, marka, mağaza** kararları Âkif'indir: `progress.md` → Açık sorular'a seçenek + önerinle yaz.
- **Geri alınabilir teknik kararları** kendin ver: koddan, ölçümden ve yazılı kararlardan dayanağı olsun; gerekçesiyle `progress.md` → Kararlar'a yaz. Dayanak yoksa "varsayım" diye işaretle ve kolay geri alınan seçeneği seç.
- Geri alınamaz işler (veri silme, dal/etiket silme, gizli anahtar, ücretli plan satın alma) için karar verme; not düş ve sor.

## Komutlar
Henüz kod yok. Bileşenler eklendikçe buraya yazılır (`docs/architecture/01-tech-stack.md` → Komutlar).

## Proje komutları (Claude Code)
`.claude/commands/` altında: `/oturum` (başlangıç ritüeli), `/kapanis` (progress güncelleme), `/checkpoint`, `/adr`, `/story`.
