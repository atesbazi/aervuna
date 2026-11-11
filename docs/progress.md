# progress.md — İlerleme Günlüğü

> **Ajan:** Her oturum sonunda bu dosyayı güncelle. Bölümlerin sırası sabit; en yeni kayıt kendi bölümünün en üstünde.
> Oturum başında önce **Durum Özeti** ve **Son oturum**'u oku.
> Açık soru tutulmaz: ajan en doğru yolu seçer ve **Kararlar**'a yazar. Yalnız Âkif'in yapabileceği işler **Ürün sahibi görevleri**'ndedir.

## Durum Özeti
| Alan | Değer |
|---|---|
| Aktif faz | **Faz 0 — Lisans, doğrulama zemini, iskelet** |
| Faz durumu | 🔨 İskelet, şema, istasyon kataloğu ve METAR arşivleyici kodda; 7 günlük çalışma başlamadı |
| Son tamamlanan story | WX-010, WX-011 (2026-11-08) |
| Sıradaki adım | WX-013 ECMWF IFS anlık görüntü → WX-014 doğrulama raporu v0 iskeleti → WX-018 kararlılık metriği |
| Engeller | Open-Meteo yazılı yanıtı geldi (2026-11-09, lisans ✅); WX-016 ticari anahtar alımını bekliyor (ÜS-009). MGM yanıtladı (2026-11-11): MY-55 arşivlenemez/paylaşılamaz → kullanılmaz. Meteoblue yanıtı yok. 7 günlük METAR/ECMWF sayacı arşivleyici sürekli çalışan bir makinede başlatılınca başlar (ÜS-007) |
| Çalışma biçimi | Saatsiz scheduled task, Âkif elle başlatır. CI yok. Açık sorular ajan tarafından karara bağlanır |
| Son checkpoint onayı | — |

## Faz durumu
| Faz | Durum | Başlangıç | Bitiş | Onay |
|---|---|---|---|---|
| 0 Lisans, doğrulama zemini, iskelet | 🔨 | 2026-11-08 | | |
| 1 Android MVP + yaşam tarzı v0 | ⏳ | | | |
| 2 iOS + sağlayıcı kararı + yaşam tarzı v1 | ⏳ | | | |
| 3 Kendi doğruluk katmanı + güven farkındalıklı öneriler | ⏳ | | | |

Simgeler: ⏳ başlamadı · 🔨 sürüyor · 🧪 testte · ✋ checkpoint bekliyor · ✅ onaylandı · ⛔ engelli · 💤 ertelendi

## Story durumu (aktif faz)
| ID | Sahip | Durum | Not |
|---|---|---|---|
| WX-010 | Ajan | ✅ | `infra/docker-compose.yml` (db, migrate, metar-archiver); `.gitattributes`/`.editorconfig`/`.env.example` mevcuttu. `compose config` geçerli; imajlar bu ortamda çekilemedi |
| WX-011 | Ajan | ✅ | dbmate; `own`/`licensed`, 3 tablo; düz PG16'da up/down/up test edildi. Hypertable yolu TimescaleDB'li ortamda ilk `migrate`'te doğrulanacak |
| WX-012 | Ajan | 🧪 | Kod + test hazır (ham METAR ayrıştırıcı, 30 istek/dk, 3 saat geri bakış, idempotent upsert, `metar coverage`). 7 gün ≥ %95 sayacı ÜS-007 ile başlar |
| WX-013 | Ajan | ⏳ | |
| WX-014 | Ajan | ⏳ | |
| WX-015 | Ajan | 💤 | CI ertelendi (Âkif, 2026-11-08) |
| WX-016 | Ajan | ⛔ | Lisans yazılı teyitli (2026-11-09); Professional plan anahtarı bekliyor (ÜS-009) |
| WX-017 | Ajan | 🧪 | Pilot 8 + tüm METAR veren LTxx, NOAA stations cache'ten. Canlı yanıtla ilk senkron bekliyor (alan adları `VERIFY`) |
| WX-018 | Ajan | ⏳ | |
| WX-019 | Ajan | ⏳ | Yöntem C kararı verildi; rapor v0'da bölüm |

## Ürün sahibi görevleri
> Soru değil; yalnız Âkif'in yapabileceği işler. Ajan bunlara takılırsa bloklanmayan işe geçer.

| ID | Görev | Neden Âkif | Durum |
|---|---|---|---|
| WX-001 | Sağlayıcı yazışmaları. Open-Meteo, Meteoblue, MGM'ye 2026-11-08'de Gmail'den gönderildi; yanıtlar günlük takip görevince işlenir. Tomorrow.io ve Rainbow.ai ertelendi (nowcasting Faz 4; IDEA-001) | Yazışma ve sözleşme | 🔨 Open-Meteo ✅ yanıtladı (2026-11-09); MGM ⚠️ yanıtladı (2026-11-11: yalnız MY-55, arşiv ve 3. kişi paylaşımı yasak → kullanılmaz; bkz. ÜS-010); Meteoblue bekleniyor. Ayrıntı `research/provider-responses.md` |
| WX-002 | "Aervuna" için TÜRKPATENT, EUIPO, Play, App Store araması | Marka | ✅ 2026-11-08: çakışma yok, ad tekil |
| WX-003 | WeatherKit'i Türkiye'de test etmek (yalnız gösterim rolü) | Apple geliştirici hesabı | ⏳ |
| WX-005 | Mac edinme (Faz 2) | Para | ⏳ |
| WX-006 | Bağımsız rakip ölçümü için teklif (ForecastWatch tipi), Faz 2 öncesi | Para + sözleşme | ⏳ |
| ÜS-007 | METAR arşivleyiciyi sürekli açık bir makinede başlatmak: `infra/README.md` komutları (db → migrate → metar-archiver). 7 günlük WX-012/WX-013 sayacı bununla başlar; ilk `migrate` çıktısında WARNING olmamalı (TimescaleDB). Zamanlanmış oturumların kalıcı sunucusu yok | Makine/sunucu (Faz 0 maliyeti "Yerel") | ⏳ |
| ÜS-008 | (İsteğe bağlı) Claude ayarları → Capabilities'te `aviationweather.gov`, `data.ecmwf.int`, `registry-1.docker.io`, `ghcr.io` alanlarına izin: oturumlar canlı yanıtla doğrulama ve compose imajlarını deneyebilir. Bu oturumda üçü de proxy tarafından reddedildi | Hesap ayarı | ⏳ |
| ÜS-009 | Open-Meteo **Professional API** planını satın almak ve API anahtarını ortam değişkeni olarak sağlamak (repoya değil). Yazılı yanıt: 4–5M çağrı/ay bu plan; fazlası 10M'lik ek Professional planlar, hacim indirimi otomatik; SLA yalnız Enterprise. WX-016'yı açar | Para + hesap | ⏳ |
| ÜS-010 | (İsteğe bağlı) MGM'ye takip: yanıtta anılan ürün listesi linki e-postada yok; 2027 ürün değişiklikleri, OMGİ erişimi, resmi uyarıların kaynak gösterilerek yayımı ve yalnız iç doğrulama için arşivli bir ürün/lisans olup olmadığı sorulabilir. Yanıt gelmezse plan değişmez (MGM'siz) | Yazışma | ⏳ |
| — | Faz checkpoint onayları ("Faz N onaylandı") | Faz kapısı | — |

WX-004 (CAMS kapsamı) ajana devredildi: kamuya açık dokümantasyondan kontrol edilir.

## Kararlar
| Tarih | Karar | Gerekçe | Kaynak |
|---|---|---|---|
| 2026-11-11 | MGM MY-55 kullanılmaz; MGM adaptörü yazılmaz. Doğrulama ve bias düzeltme METAR + ECMWF açık veriyle sürer; ADR-0002 değişmez. Lisans yeniden açılırsa yeni karar | Yazılı yanıt: veriler arşivlenemez ve 3. kişilerle paylaşılamaz. Doğrulama/model eğitimi saklama gerektirir (AGENTS §2.5); gösterim için en güvenli yorum: son kullanıcı 3. kişidir (CLAUDE.md lisans belirsizliği kuralı). MGM ADR-0002'de ana kaynak değil (`plan.md`: "izin alınırsa MGM") | `research/provider-responses.md` → MGM 2026-11-11 |
| 2026-11-11 | MGM uyarılarının uygulamada yayımı belirsiz kabul edilir; resmi uyarı kaynağı olarak MGM kullanılmaz | Soru 4 yanıtsız; en güvenli yorum (izin yok) | aynı |
| 2026-11-09 | ADR-0002'nin Open-Meteo ayağı yazılı teyit aldı; karar aynen geçerli, ADR değişmez. Meteoblue/MGM teyidi bekleniyor | Yazılı yanıt: ticari plan uygun; saklama, arşiv, türev ve yeniden dağıtım serbest; tek koşul atıf | `research/provider-responses.md` → Open-Meteo 2026-11-09 |
| 2026-11-09 | Open-Meteo adaptör bayrakları: `archive_allowed=true`, `shared_cache_ttl=30 dk` | Lisans süre sınırı koymuyor; süre tazelik kararı. 30 dk, sağlayıcılara bildirdiğimiz çağrı tahmininin (hücre başına 30 dk yenileme) temeli ve doğruluk önceliğine uygun. Varsayım: tek sabit, ölçümle değiştirilebilir | `research/license-notes.md` |
| 2026-11-09 | Atıf model bazlı: yanıtta Open-Meteo **ve** tahmini üreten modelin resmi sağlayıcısı gösterilir; `attribution` alanı sabit metin değil, kullanılan modele göre üretilir (WX-021) | Open-Meteo'nun tek lisans koşulu; `04-api-contracts.md` örneği yalnız Open-Meteo'yu anıyor, WX-021'de genişletilir | Open-Meteo yanıtı, [licence](https://open-meteo.com/en/licence) |
| 2026-11-09 | Başlangıçta Open-Meteo Professional plan, SLA'sız; kesinti riski ECMWF açık veri yedeği + grid önbelleğinde bayat veri bayrağıyla (WX-024) karşılanır. Enterprise (SLA) değerlendirmesi büyüme aşamasında Âkif'e (para) | SLA yalnız Enterprise planında; Professional maliyet açısından lansman için yeterli | Open-Meteo yanıtı |
| 2026-11-09 | Self-host şimdilik yok; yapılırsa sunucu kodundaki değişiklikler açık kaynak yayımlanır (yeni ADR ile) | Open-Meteo: self-host lisansız, tek yükümlülük değişiklikleri açık kaynak yapmak | Open-Meteo yanıtı, repo LICENSE |
| 2026-11-08 | Migration aracı **dbmate** (düz SQL, `-- migrate:up/down`, compose'da `migrate` servisi, imaj etiketi sabit) | Dilden bağımsız tek ikili; Faz 0'da Rust araç zinciri gerektirmez (sqlx-cli gerektirirdi); API ve pipeline aynı dosyaları kullanır; testler de aynı araçla taze DB'ye uygular | WX-011, `db/README.md` |
| 2026-11-08 | Hypertable oluşturma TimescaleDB varsa yapılır; eklentisiz düz Postgres'te tablolar düz kalır ve migration WARNING verir | Compose her zaman TimescaleDB sağlar; düz Postgres'li test/geliştirme ortamında şema yine uygulanabilir. Risk (üretimde sessizce düz tablo) WARNING + TimescaleDB varken hypertable'ı doğrulayan test + ÜS-007 kontrolüyle kapatılır. Varsayım: kolay geri alınır (koşul kaldırılır) | `db/migrations/20261108000001_initial_schema.sql` |
| 2026-11-08 | Gözlem değerleri API'nin türetilmiş JSON alanlarından değil, ham METAR'ın kendi ayrıştırıcımızla okunmasından gelir; trend (NOSIG/TEMPO/BECMG) ve RExx gözleme sayılmaz; ABD RMK T-grubu varsa sıcaklık/çiy onda bir hassasiyetle | Doğrulama verisinin kaynağı denetlenebilir olmalı (doğruluk önceliği); JSON alan anlamları bu ortamdan canlı doğrulanamadı | `pipeline/.../metar/parse.py` |
| 2026-11-08 | METAR çekimi: 50 istasyonluk toplu istek, 30 istek/dk (sınırın %30'u), her çalışmada son 3 saat, `(icao, observed_at)` upsert; COR aynı zamanı değiştirir | Kaçan çalışmalar sonraki çalışmada kendiliğinden doldurulur (≥ %95 hedefi), sağlayıcı sınırına geniş pay | WX-012 |
| 2026-11-08 | WX-012 doluluk ölçüsü **saatlik**: istasyon bir UTC saatinde ≥ 1 rapor varsa o saat tam; oran = dolu saat / beklenen saat | Kadanstan bağımsız (LTxx/EGLL/RJTT 30 dk, KJFK 60 dk); doğrulama eşleştirmesinin ±30 dk penceresiyle uyumlu | `pipeline/.../metar/coverage.py` |
| 2026-11-08 | Pilot 8'e ek olarak METAR veren tüm LTxx istasyonları ilk günden aktif | Arşiv geriye doldurulamaz (API yalnız 30 gün); maliyet 10 dk'da ~2 istek; plan "Faz 0 sonunda tüm aktif LTxx" diyor | WX-017 |
| 2026-11-08 | İstasyon senkronu koordinat/ad/rakımı günceller, `active`'e dokunmaz; eksik pilot istasyon hata | Operatörün kapattığı istasyon geri açılmaz; koordinatlar elle yazılmaz, kaynaktan gelir | WX-017 |
| 2026-11-08 | Varsayılan User-Agent `aervuna-pipeline/<sürüm> (+https://github.com/atesbazi/aervuna)`; e-posta yok | NOAA özel UA istiyor; repo bağlantısı iletişim için yeterli, kişisel veri yayımlanmaz | `pipeline/README.md` |
| 2026-11-08 | Açık sorular Âkif'e sorulmaz; ajan en mantıklı/performanslı/stabil/doğru yolu seçer ve buraya yazar. Âkif'te kalan: faz onayı, para, yazışma/sözleşme/marka, geri alınamaz işler | Âkif | `CLAUDE.md` → Açık sorular ve kararlar |
| 2026-11-08 | Tomorrow.io ve Rainbow.ai yazışması Faz 4'e ertelendi | Yalnız nowcasting için gerekli; Faz 0–3 kapsamını etkilemiyor; ikisi de e-posta yayınlamıyor (yalnız web formu) | IDEA-001 |
| 2026-11-08 | Sağlayıcı e-postaları hazırlandı; Open-Meteo ve Meteoblue öncelikli, MGM Türkçe | WX-001'i Âkif için gönderilmeye hazır hale getirmek | `research/provider-outreach.md` |
| 2026-11-08 | Uygulama adı **Aervuna**, repo `atesbazi/aervuna` (eski: Ufuk); marka araması temiz (WX-002) | Âkif | — |
| 2026-11-08 | Yaşam tarzı ikinci değer ayağı; her fazda planlı: F1 v0, F2 v1 + bildirim + kişiselleştirme, F3 güven farkındalıklı + isabet raporu, F4 AQI/polen/UV/seyahat/bahçe | Âkif'in beklentisi; öneri ancak tahmin kadar iyi olduğu için doğruluğa bağlı | `product/05-lifestyle.md`, ADR-0010 |
| 2026-11-08 | Yaşam tarzı motoru Rust domain'de, deterministik, sürümlü, `why` gerekçeli; kişiselleştirme cihazda | Tek mantık her yüzeyde, test edilebilir, lisans dostu, hesap gerektirmez | ADR-0010 |
| 2026-11-08 | Rakip kıyası: Faz 0–1 dolaylı yöntem (C), Faz 2 öncesi bağımsız üçüncü taraf (A); kazıma ve panel yok | En savunulabilir iddia + bugün sıfır maliyet ve hukuki risk | `research/competitor-benchmark.md` |
| 2026-11-08 | Gelir modeli varsayımı: ücretsiz + Plus, reklamsız; IAP RevenueCat (Faz 2'de ADR) | Reklam şık deneyimle çelişir; Plus yalnız kendi değerimizi satar | `product/03-monetization.md` |
| 2026-11-08 | Ürünün kalbi doğruluk: mağaza ve gömülü uygulamalardan daha tutarlı ve doğru tahmin; aynı zamanda pazarlama stratejisi | Âkif | `product/01-vision.md` |
| 2026-11-08 | Global ürün; arayüz varsayılanı İngilizce, Türkçe uygulama içinden; cihaz diline otomatik uyum ertelendi (IDEA-006) | Âkif | `AGENTS.md §2.9` |
| 2026-11-08 | Görsel hedef: şık, tatmin edici, ihtiyaç dahilinde sinematik | Âkif | `design/01-visual-direction.md` |
| 2026-11-08 | Saatsiz scheduled task; Âkif elle başlatır. CI şimdilik yok | Âkif | `CLAUDE.md`, `quality/02-ci-cd.md` |
| 2026-11-08 | Doğrulama pilotu global: 4 TR + EGLL, EDDF, KJFK, RJTT | Ürün global; iddia yalnız ölçülen bölgeler için | `plan.md` Faz 0 |
| 2026-11-08 | Mobil Flutter, Android widget Kotlin/Glance, iOS widget SwiftUI | Görsel fark iki platformda tek kodla; widget'lar her durumda native | ADR-0004 |
| 2026-11-08 | API Rust/Axum, veri/ML hattı Python | Âkif tercihi; GRIB/ML ekosistemi Python'da | ADR-0005, ADR-0006 |
| 2026-11-08 | Önce Android, iOS Faz 2 | iOS widget ve derleme Mac gerektirir | ADR-0008 |
| 2026-11-08 | Ana kaynak Open-Meteo ticari, kıyas Meteoblue, WeatherKit yalnız gösterim, Google elendi | Lisans: arşiv ve türev hakkı belirleyici | ADR-0002, ADR-0003 |
| 2026-11-08 | Faz 0 doğrulama arşivi ECMWF açık verisiyle başlar | Open-Meteo ücretsiz API ticari olmayan kullanım içindir | `plan.md` Faz 0 |

## Son oturum
### 2026-11-08 (2) — Faz 0 iskelet, şema, istasyon kataloğu, METAR arşivleyici
- **Plan:** (1) WX-010 compose. (2) WX-011 migration aracı + ilk şema. (3) WX-017 istasyon kataloğu. (4) WX-012 METAR arşivleyici + doluluk ölçümü. (5) progress güncellemesi.
- **Yapılan:** Plan tamamlandı. `infra/docker-compose.yml` (TimescaleDB 2.17.2-pg16, dbmate 2.37.0, `metar-archiver`), `db/migrations/20261108000001_initial_schema.sql`, `pipeline/` (uv, httpx, psycopg 3; `stations sync`, `metar once|run|coverage`, Dockerfile).
- **Yerel kontroller:** `ruff check` ✅, `ruff format --check` ✅, `mypy --strict` ✅ (18 dosya), `pytest` 37 geçti / 1 atlandı (hypertable testi: bu ortamda TimescaleDB yok). DB testleri düz PostgreSQL 16 + dbmate ile koştu.
- **Bu ortamda doğrulanamayanlar:** aviationweather.gov, data.ecmwf.int, Docker Hub ve ghcr.io'ya çıkış proxy tarafından reddedildi (ÜS-008). Bu yüzden canlı NOAA yanıtı (alan adları `VERIFY` notlu), compose imajlarının çekilmesi, pipeline imaj derlemesi ve TimescaleDB hypertable yolu ilk kez ÜS-007 çalıştırmasında doğrulanacak. Testlerdeki METAR'lar format-sadık örnekler, canlı kayıt değil.
- **Sıradaki:** (1) WX-013 ECMWF IFS açık veri anlık görüntüsü (00/12 UTC, istasyon noktası, 0–240 sa, CC-BY atfı). (2) WX-014 doğrulama raporu v0 kodu (MAE/bias, ufuk kovaları, n < 100 gizleme) + WX-018 kararlılık metriği. (3) WX-004 CAMS kapsamı (doküman taraması).
- **Verilen kararlar:** Kararlar tablosundaki ilk sekiz 2026-11-08 satırı (dbmate, koşullu hypertable, ham METAR ayrıştırma, çekim politikası, saatlik doluluk, tüm LTxx aktif, senkron kuralları, User-Agent).

### 2026-11-08 — Ad değişikliği, yaşam tarzı katmanı, karar yetkisi
- **Yapılan:** Ad Aervuna'ya çevrildi. Yaşam tarzı katmanı tasarlandı (`product/05-lifestyle.md`, ADR-0010) ve Faz 1–4'e story'leriyle dağıtıldı. "Açık soruları sorma, en doğru yolu seç" kuralı CLAUDE.md/AGENTS.md ve komutlara işlendi; Q4 (rakip kıyası) ve gelir modeli varsayımı karara bağlandı.
- **Sıradaki:** (1) WX-010 repo yerleşimi + `infra/docker-compose.yml`. (2) WX-011 migration aracı + ilk şema. (3) WX-017 istasyon kataloğu, ardından WX-012.
- **Verilen kararlar:** Kararlar tablosundaki 2026-11-08 satırları.

## Story metrikleri
| ID | Testler ilk denemede yeşil | Düzeltme turu | ADR/kapsam ihlali | Not |
|---|---|---|---|---|
| WX-010 | — (yapılandırma) | 0 | Yok | `compose config` geçerli |
| WX-011 | Evet | 0 | Yok | up/down/up |
| WX-017 | Evet | 0 | Yok | |
| WX-012 | Evet | 1 (ruff S105 yanlış pozitif → değişken adı) | Yok | |

## Checkpoint raporları
(Faz sonunda `templates/checkpoint.md` formatında buraya eklenir.)
