# progress.md — İlerleme Günlüğü

> **Ajan:** Her oturum sonunda bu dosyayı güncelle. Bölümlerin sırası sabit; en yeni kayıt kendi bölümünün en üstünde.
> Oturum başında önce **Durum Özeti** ve **Son oturum**'u oku.

## Durum Özeti
| Alan | Değer |
|---|---|
| Aktif faz | **Faz 0 — Lisans, doğrulama zemini, iskelet** |
| Faz durumu | 🔨 Dokümantasyon repoda. Kod yok |
| Son tamamlanan story | — |
| Sıradaki adım | WX-010 repo yerleşimi + docker-compose → WX-011 migration → WX-017 istasyon kataloğu → WX-012 METAR arşivleyici |
| Paralelde (ürün sahibi) | WX-001 sağlayıcı soru seti, WX-002 "Ufuk" marka/mağaza araması, Q4 |
| Engeller | Sağlayıcı yazılı yanıtları yok |
| Çalışma biçimi | Scheduled task, saatsiz, Âkif elle başlatır. CI yok |
| Son checkpoint onayı | — |

## Faz durumu
| Faz | Durum | Başlangıç | Bitiş | Onay |
|---|---|---|---|---|
| 0 Lisans, doğrulama zemini, iskelet | 🔨 | 2026-11-08 | | |
| 1 Android MVP | ⏳ | | | |
| 2 iOS + sağlayıcı kararı | ⏳ | | | |
| 3 Kendi doğruluk katmanı | ⏳ | | | |

Simgeler: ⏳ başlamadı · 🔨 sürüyor · 🧪 testte · ✋ checkpoint bekliyor · ✅ onaylandı · ⛔ engelli · 💤 ertelendi

## Story durumu (aktif faz)
| ID | Sahip | Durum | Not |
|---|---|---|---|
| WX-001 | ÜS | ⏳ | Soru seti: `research/2026-11-07-data-provider-decision.md` |
| WX-002 | ÜS | ⏳ | "Ufuk" için TÜRKPATENT, EUIPO, Play, App Store |
| WX-003 | ÜS | ⏳ | |
| WX-004 | ÜS | ⏳ | |
| WX-005 | ÜS | ⏳ | |
| WX-010 | Ajan | ⏳ | |
| WX-011 | Ajan | ⏳ | |
| WX-012 | Ajan | ⏳ | Pilot: LTAC, LTFM, LTBJ, LTAI, EGLL, EDDF, KJFK, RJTT |
| WX-013 | Ajan | ⏳ | |
| WX-014 | Ajan | ⏳ | |
| WX-015 | Ajan | 💤 | CI ertelendi (Âkif, 2026-11-08) |
| WX-016 | Ajan | ⛔ | Open-Meteo ticari anahtarı bekliyor |
| WX-017 | Ajan | ⏳ | |
| WX-018 | Ajan | ⏳ | |
| WX-019 | ÜS+A | 🔨 | Yöntem önerisi yazıldı: `research/competitor-benchmark.md`; karar Q4 |

ÜS = ürün sahibi

## Açık sorular (ürün sahibine)
| # | Soru | Seçenekler + öneri | Açıldı | Durum |
|---|---|---|---|---|
| Q4 | Rakip kıyası yöntemi ve bütçesi | A bağımsız üçüncü taraf (ForecastWatch tipi) · B insan paneli · C kamuya açık benchmark'la dolaylı · D lisanslı sağlayıcı. Öneri: Faz 0–1 C, Faz 2 öncesi A için teklif | 2026-11-08 | Açık |
| Q3 | Zamanlanmış mı canlı mı? | — | 2026-11-08 | **Kapandı:** saatsiz scheduled task, Âkif elle başlatır |
| Q2 | CI nerede? | — | 2026-11-08 | **Kapandı:** şimdilik CI yok |
| Q1 | Uygulama ve repo adı | — | 2026-11-08 | **Kapandı:** Ufuk / `atesbazi/ufuk` (marka araması WX-002) |

## Kararlar
| Tarih | Karar | Gerekçe | Kaynak |
|---|---|---|---|
| 2026-11-08 | Ürünün kalbi doğruluk: mağaza ve gömülü uygulamalardan daha tutarlı ve doğru tahmin; aynı zamanda pazarlama stratejisi | Âkif'in ürün beklentisi | `product/01-vision.md` |
| 2026-11-08 | Global ürün; arayüz varsayılanı İngilizce, Türkçe uygulama içinden; cihaz diline otomatik uyum ertelendi (IDEA-006) | Âkif | `AGENTS.md §2.9` |
| 2026-11-08 | Görsel hedef: şık, tatmin edici, ihtiyaç dahilinde sinematik | Âkif | `design/01-visual-direction.md` |
| 2026-11-08 | Proje saatsiz scheduled task ile ilerler; Âkif elle başlatır | Âkif | `CLAUDE.md` → Zamanlanmış oturum modu |
| 2026-11-08 | CI şimdilik yok; yerel komutlar | Âkif | `quality/02-ci-cd.md` |
| 2026-11-08 | Doğrulama pilotu global: 4 TR + EGLL, EDDF, KJFK, RJTT | Ürün global; iddia yalnız ölçülen bölgeler için | `plan.md` Faz 0 |
| 2026-11-08 | Proje adı Ufuk, repo `atesbazi/ufuk` | Âkif | — |
| 2026-11-08 | Mobil Flutter, Android widget Kotlin/Glance, iOS widget SwiftUI | Görsel fark iki platformda tek kodla; widget'lar her durumda native | ADR-0004 |
| 2026-11-08 | API Rust/Axum, veri/ML hattı Python | Âkif tercihi; GRIB/ML ekosistemi Python'da | ADR-0005, ADR-0006 |
| 2026-11-08 | Önce Android, iOS Faz 2 | iOS widget ve derleme Mac gerektirir | ADR-0008 |
| 2026-11-08 | Ana kaynak Open-Meteo ticari, kıyas Meteoblue, WeatherKit yalnız gösterim, Google elendi | Lisans: arşiv ve türev hakkı belirleyici | ADR-0002, ADR-0003 |
| 2026-11-08 | Faz 0 doğrulama arşivi ECMWF açık verisiyle başlar | Open-Meteo ücretsiz API ticari olmayan kullanım içindir | `plan.md` Faz 0 |

## Son oturum
### 2026-11-08 — Repo kurulumu
- **Yapılan:** Dokümantasyon, 9 ADR, plan, backlog, mimari, ürün ve araştırma dosyaları, Claude Code komutları repoya yazıldı. Âkif'in beklentileri işlendi: doğruluk kalp, global/İngilizce varsayılan, ihtiyaç dahilinde sinematik görsellik, saatsiz scheduled çalışma, CI yok.
- **Sıradaki:** (1) WX-010 repo yerleşimi + `infra/docker-compose.yml`. (2) WX-011 migration aracı + ilk şema. (3) WX-017 istasyon kataloğu, ardından WX-012.
- **Açık sorular:** Q4.

## Story metrikleri
| ID | Testler ilk denemede yeşil | Düzeltme turu | ADR/kapsam ihlali | Not |
|---|---|---|---|---|

## Checkpoint raporları
(Faz sonunda `templates/checkpoint.md` formatında buraya eklenir.)
