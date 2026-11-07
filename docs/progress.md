# progress.md — İlerleme Günlüğü

> **Ajan:** Her oturum sonunda bu dosyayı güncelle. Bölümlerin sırası sabit; en yeni kayıt kendi bölümünün en üstünde.
> Oturum başında önce **Durum Özeti** ve **Son oturum**'u oku.
> Açık soru tutulmaz: ajan en doğru yolu seçer ve **Kararlar**'a yazar. Yalnız Âkif'in yapabileceği işler **Ürün sahibi görevleri**'ndedir.

## Durum Özeti
| Alan | Değer |
|---|---|
| Aktif faz | **Faz 0 — Lisans, doğrulama zemini, iskelet** |
| Faz durumu | 🔨 Dokümantasyon repoda. Kod yok |
| Son tamamlanan story | — |
| Sıradaki adım | WX-010 repo yerleşimi + docker-compose → WX-011 migration → WX-017 istasyon kataloğu → WX-012 METAR arşivleyici |
| Engeller | Sağlayıcı yazılı yanıtları yok (WX-016'yı bekletiyor; diğer işler bloklu değil) |
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
| WX-010 | Ajan | ⏳ | |
| WX-011 | Ajan | ⏳ | |
| WX-012 | Ajan | ⏳ | Pilot: LTAC, LTFM, LTBJ, LTAI, EGLL, EDDF, KJFK, RJTT |
| WX-013 | Ajan | ⏳ | |
| WX-014 | Ajan | ⏳ | |
| WX-015 | Ajan | 💤 | CI ertelendi (Âkif, 2026-11-08) |
| WX-016 | Ajan | ⛔ | Open-Meteo ticari anahtarı bekliyor (WX-001) |
| WX-017 | Ajan | ⏳ | |
| WX-018 | Ajan | ⏳ | |
| WX-019 | Ajan | ⏳ | Yöntem C kararı verildi; rapor v0'da bölüm |

## Ürün sahibi görevleri
> Soru değil; yalnız Âkif'in yapabileceği işler. Ajan bunlara takılırsa bloklanmayan işe geçer.

| ID | Görev | Neden Âkif | Durum |
|---|---|---|---|
| WX-001 | Sağlayıcı yazışmaları. Open-Meteo, Meteoblue, MGM'ye 2026-11-08'de Gmail'den gönderildi; yanıtlar günlük takip görevince işlenir. **Kalan:** Tomorrow.io ve Rainbow.ai web formları (`research/provider-outreach.md` §3–4) | Yazışma ve sözleşme | 🔨 3/5 gönderildi |
| WX-002 | "Aervuna" için TÜRKPATENT, EUIPO, Play, App Store araması | Marka | ✅ 2026-11-08: çakışma yok, ad tekil |
| WX-003 | WeatherKit'i Türkiye'de test etmek (yalnız gösterim rolü) | Apple geliştirici hesabı | ⏳ |
| WX-005 | Mac edinme (Faz 2) | Para | ⏳ |
| WX-006 | Bağımsız rakip ölçümü için teklif (ForecastWatch tipi), Faz 2 öncesi | Para + sözleşme | ⏳ |
| — | Faz checkpoint onayları ("Faz N onaylandı") | Faz kapısı | — |

WX-004 (CAMS kapsamı) ajana devredildi: kamuya açık dokümantasyondan kontrol edilir.

## Kararlar
| Tarih | Karar | Gerekçe | Kaynak |
|---|---|---|---|
| 2026-11-08 | Açık sorular Âkif'e sorulmaz; ajan en mantıklı/performanslı/stabil/doğru yolu seçer ve buraya yazar. Âkif'te kalan: faz onayı, para, yazışma/sözleşme/marka, geri alınamaz işler | Âkif | `CLAUDE.md` → Açık sorular ve kararlar |
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
### 2026-11-08 — Ad değişikliği, yaşam tarzı katmanı, karar yetkisi
- **Yapılan:** Ad Aervuna'ya çevrildi. Yaşam tarzı katmanı tasarlandı (`product/05-lifestyle.md`, ADR-0010) ve Faz 1–4'e story'leriyle dağıtıldı. "Açık soruları sorma, en doğru yolu seç" kuralı CLAUDE.md/AGENTS.md ve komutlara işlendi; Q4 (rakip kıyası) ve gelir modeli varsayımı karara bağlandı.
- **Sıradaki:** (1) WX-010 repo yerleşimi + `infra/docker-compose.yml`. (2) WX-011 migration aracı + ilk şema. (3) WX-017 istasyon kataloğu, ardından WX-012.
- **Verilen kararlar:** Kararlar tablosundaki 2026-11-08 satırları.

## Story metrikleri
| ID | Testler ilk denemede yeşil | Düzeltme turu | ADR/kapsam ihlali | Not |
|---|---|---|---|---|

## Checkpoint raporları
(Faz sonunda `templates/checkpoint.md` formatında buraya eklenir.)
