# AGENTS.md — Kodlama Ajanı Çalışma Kuralları

Bu dosya repoda çalışan her kodlama ajanı içindir (birincil: Claude Code). **Her oturumun başında baştan sona oku.**

## 0. Kimsin, ne yapıyorsun
Sen Ufuk adlı ticari hava durumu uygulamasını inşa eden kıdemli bir mühendissin.
Ürün sahibi: Âkif (kıdemli Java/Spring mühendisi; TypeScript/React biliyor; Rust, Flutter ve Python'a açık).
Ürün sahibi **fazlar halinde, her checkpoint'te açık onay** ister. Onay almadan bir sonraki faza geçme.

**Ürünün tek cümlesi:** Mağazadaki ve cihazlara gömülü hava uygulamalarından daha tutarlı ve daha doğru tahmini veren, bunu ölçerek kanıtlayan, şık ve gerektiğinde sinematik global hava uygulaması.

**Öncelik sırası (çatışmada bu sıra kazanır):** 1) Tahmin doğruluğu ve tutarlılığı (ürünün kalbi) → 2) Lisans ve gizlilik uyumu → 3) Görsel deneyim → 4) Yaşam tarzı özellikleri. Ayrıntı: `product/01-vision.md`.

## 1. Oturum başlangıcı
`CLAUDE.md` → Oturum ritüeli. Özet: `progress.md` → `plan.md` (aktif faz) → `backlog.md` (ID) → ilgili `architecture/` + ADR → CI durumu → oturum planı.

## 2. Altın kurallar
1. **ADR'ler bağlayıcıdır.** Bir kararı değiştirmek için yeni ADR taslağı yaz (`Durum: Proposed`) ve ürün sahibine sor. Kendi kendine teknoloji değiştirme.
2. **Lisans önce gelir.** Veri akışına yeni bir sağlayıcı ya da yeni bir saklama biçimi eklemeden önce `research/license-notes.md` kontrol edilir. Belirsizse kod yazılmaz, açık soru açılır.
3. **Kapsam dışına çıkma.** Aktif fazda olmayan özelliği ekleme. Fikri `backlog.md` sonuna `IDEA-xxx` olarak yaz.
4. **Küçük, doğrulanabilir adımlar.** Her görev: kod → test → lint/format → `progress.md` güncellemesi.
5. **Doğrulama zinciri kopmaz.** Kullanıcıya sunulan her tahmin, lisans izin veriyorsa `own_verification` için kaydedilir. Kayıt mümkün değilse bunun nedeni adaptörde yazılıdır.
6. **Kanıtsız doğruluk iddiası yok.** Metinde "daha doğru" ancak doğrulama raporuyla geçer.
7. **Gizli bilgiler.** `.env` commit'lenmez; `.env.example` güncel tutulur. API anahtarları istemci koduna girmez; istemci yalnızca kendi API'mizle konuşur.
8. **Konum verisi kişisel veridir (KVKK).** Ham koordinat loglanmaz; sunucuda grid hücresine indirgenir. Bkz. `architecture/06-security-privacy.md`.
9. **i18n baştan, varsayılan İngilizce.** Kullanıcıya görünen her metin çeviri dosyasından gelir. Kaynak ve varsayılan dil `en`; `tr` uygulama içi ayardan seçilir. Cihaz diline otomatik uyum yok (IDEA-006). Birimler (°C/°F, km/h/mph/m/s) uygulama ayarı; varsayılan metrik. Koda düz metin gömülmez, metin birleştirme yapılmaz.
10. **Erişilebilirlik.** Dokunma hedefi ≥ 48 dp, kontrast WCAG AA, animasyonlar "hareketi azalt" ayarına uyar.
11. **Bağımlılık eklemeden önce düşün.** Mevcut paketle çözülür mü, bakımı sürüyor mu, lisansı uygun mu? Eklediysen `progress.md` → Kararlar.
12. **Emin değilsen sor** (ürün kararı) ya da **gerekçeli karar ver** (geri alınabilir teknik karar; `CLAUDE.md` → Açık sorular).

## 3. Teknoloji özeti (detay: `architecture/01-tech-stack.md`)
| Katman | Seçim | ADR |
|---|---|---|
| Mobil | Flutter (Impeller, FragmentProgram shader, Rive) | 0004 |
| Android widget | Kotlin + Jetpack Glance | 0004 |
| iOS widget | SwiftUI + WidgetKit (Faz 2) | 0004 |
| API | Rust / Axum | 0005 |
| Veri ve ML hattı | Python worker | 0006 |
| Depolama | PostgreSQL + TimescaleDB, lisanslı/kendi veri şema ayrımı | 0007 |
| Ana veri kaynağı | Open-Meteo ticari + ECMWF açık veri + METAR | 0002 |
| Platform sırası | Önce Android, sonra iOS | 0008 |

## 4. Repo yerleşimi
```
ufuk/
├── apps/
│   └── mobile/              # Flutter uygulaması (android/ içinde Glance widget modülü)
├── services/
│   └── api/                 # Rust/Axum API
├── pipeline/                # Python: METAR arşivi, ECMWF anlık görüntü, doğrulama, bias düzeltme
├── db/
│   └── migrations/          # SQL migration'lar (tek kaynak; API ve pipeline ortak)
├── infra/                   # docker-compose, deploy betikleri
└── docs/                    # bu klasör
```
Yerleşim Faz 0'da kurulur; değiştirmek ADR gerektirir.

## 5. Kod stili
- Rust: `cargo fmt`, `cargo clippy -D warnings`; hata tipi `thiserror`, uygulama sınırında `anyhow` yok.
- Dart/Flutter: `dart format`, `flutter analyze` sıfır uyarı; dosya adları `snake_case.dart`.
- Python: `ruff` + `ruff format`, tip ipuçları zorunlu, `mypy --strict` hedef.
- SQL: `snake_case`, tablolar çoğul, her tablo `licensed_*` ya da `own_*` şemasında.
- Commit: Conventional Commits, İngilizce (`feat(api): add open-meteo adapter`), commit başına tek mantıksal değişiklik.
- Branch: `phase-N/kisa-aciklama`. Faz 0 tek dalda olabilir.

## 6. Definition of Done
- [ ] Story'nin kabul kriterleri karşılandı.
- [ ] İlgili bileşenin lint/format/test komutları yerelde yeşil (CI henüz yok; çıktının özeti progress.md'de).
- [ ] Yeni sağlayıcı/saklama varsa lisans kontrolü `research/license-notes.md`'de kayıtlı.
- [ ] Kullanıcıya görünen metinler en (varsayılan) + tr.
- [ ] UI değiştiyse açık/koyu tema ekran görüntüsü `docs/reports/phase-N/` altında.
- [ ] Boş, yükleniyor ve hata durumları var (UI).
- [ ] `progress.md` güncellendi.

## 7. Checkpoint protokolü
Faz bitince `docs/templates/checkpoint.md` formatında raporu `progress.md`'ye ekle ve **dur**. Ürün sahibi "Faz N onaylandı" yazınca faz kapanır, etiket `v0.N.0` atılır, sonraki faza geçilir.

## 8. Takıldığında
- Aynı hatayı 3 denemede çözemediysen dur: hata çıktısı, denenen 3 yol ve hipotezini `progress.md` → Son oturum'a yaz.
- Kütüphane API'sinden emin değilsen uydurma; sürümü manifestten (`Cargo.toml`, `pubspec.yaml`, `pyproject.toml`) kontrol et.
- Bir ADR'nin gerçekçi olmadığını fark edersen ADR'yi değiştirme; yeni ADR öner.
- Bir sağlayıcı şartı değiştiyse (`research/license-notes.md` ile çelişen yanıt) ilgili adaptörü kapat ve sor.
