# backlog.md — Ürün Birikimi

Format: `ID | Ö | Sahip | Story | Kabul (özet)`
Öncelik: **P0** olmazsa olmaz · **P1** önemli · **P2** güzel olur. Sahip: **ÜS** ürün sahibi · **A** ajan.
Durum `progress.md`'de izlenir; bu dosya kapsamı tanımlar.

## Faz 0 — Lisans, doğrulama zemini, iskelet
| ID | Ö | Sahip | Story | Kabul |
|---|---|---|---|---|
| WX-001 | P0 | ÜS | Sağlayıcılara ortak soru setini göndermek istiyorum | Open-Meteo, Meteoblue, Tomorrow.io, Rainbow.ai, MGM'ye gitti; yanıtlar `provider-responses.md`'de |
| WX-002 | P0 | ÜS | Uygulama adının marka ve mağaza uygunluğunu bilmek istiyorum | TÜRKPATENT, EUIPO, Play, App Store araması; sonuç Q1'e işlendi |
| WX-003 | P1 | ÜS | WeatherKit'i Türkiye'de test etmek istiyorum (yalnız gösterim rolü) | Dakikalık yağış ve uyarı kapsamı not edildi |
| WX-004 | P1 | ÜS | CAMS'in Türkiye kapsamını bilmek istiyorum | Avrupa alanı sınırı not edildi |
| WX-005 | P2 | ÜS | Mac edinme planı | Model ve tarih Kararlar'da |
| WX-010 | P0 | A | Repo yerleşimi ve yerel ortam | `AGENTS.md §4` klasörleri, `.gitattributes`, `.editorconfig`, `.env.example`, `infra/docker-compose.yml` (Postgres 16 + TimescaleDB) |
| WX-011 | P0 | A | Migration aracı ve ilk şema | Araç seçimi Kararlar'da; `licensed`/`own` şemaları, `own.stations`, `own.metar_observations`, `own.ecmwf_point_forecasts` hypertable |
| WX-012 | P0 | A | METAR arşivleyici | 10 dk'da bir pilot istasyonlar (4 TR + EGLL, EDDF, KJFK, RJTT), sonra tüm LTxx; 100 istek/dk sınırına uyum; idempotent; 7 gün ≥ %95 |
| WX-013 | P0 | A | ECMWF IFS açık veri anlık görüntüsü | 00/12 UTC koşuları; istasyon noktası; 0–240 saat; CC-BY atfı |
| WX-014 | P0 | A | Doğrulama raporu v0 | 8 pilot istasyonda ufuk bazında sıcaklık MAE + bias; Markdown + CSV |
| WX-015 | P2 | A | CI v0 (**ertelendi**, Âkif 2026-11-08) | Açılınca: pipeline lint + test; runner kararı |
| WX-016 | P1 | A | Open-Meteo ticari anlık görüntü | Ticari anahtar gelince; aynı istasyonlar; doğrulama raporuna ikinci sütun |
| WX-017 | P1 | A | İstasyon kataloğu | Pilot + Türkiye METAR istasyonları, koordinat, rakım, istasyon tipi; kaynak NOAA stations cache |
| WX-018 | P1 | A | Tahmin kararlılığı metriği | Aynı geçerlilik zamanı için ardışık koşular arası değişim; raporda ayrı tablo |
| WX-019 | P0 | ÜS+A | Rakip kıyası yöntemi | Seçenekler `research/competitor-benchmark.md`; karar Q4 |

## Faz 1 — Android MVP
| ID | Ö | Sahip | Story | Kabul |
|---|---|---|---|---|
| WX-020 | P0 | A | Axum API iskeleti | `/health`, yapılandırma, problem+json, tracing, OpenAPI |
| WX-021 | P0 | A | `ForecastProvider` trait ve lisans bayrakları | `archive_allowed`, `shared_cache_ttl`, `attribution` zorunlu alanlar; testle zorlanır |
| WX-022 | P0 | A | Open-Meteo ticari adaptörü | Saatlik + günlük; zaman aşımı + yeniden deneme; sözleşme testi |
| WX-023 | P0 | A | Grid hücresi modeli | ADR ile H3 ya da sabit ızgara; koordinat sunucuda hücreye indirgenir |
| WX-024 | P0 | A | Grid önbelleği | Hücre başına TTL = sağlayıcının `shared_cache_ttl`'i; bayat veri bayrağı |
| WX-025 | P0 | A | `GET /v1/forecast` | `architecture/04-api-contracts.md` ile birebir; p95 < 150 ms önbellekten |
| WX-026 | P0 | A | Sunulan tahmin kaydı | Lisans izinliyse `own.served_forecasts`; METAR eşleştirme işi |
| WX-027 | P1 | A | Haftalık doğrulama raporu | `docs/reports/phase-1/` |
| WX-030 | P0 | A | Flutter proje kabuğu | Tema, i18n (varsayılan en, uygulama içinden tr), router, durum yönetimi (ADR ile), analiz sıfır uyarı |
| WX-031 | P0 | A | Konum izni ve yer yönetimi | İzin reddinde şehir arama; kayıtlı yerler |
| WX-032 | P0 | A | Ana ekran | Şimdi, saatlik 48 saat, 10 gün; boş/yükleniyor/hata |
| WX-033 | P0 | A | Dil ve birim ayarları | Dil en/tr (varsayılan en); °C/°F, km/h/mph/m/s, 12/24 saat (varsayılan metrik) |
| WX-034 | P0 | A | Atıf ekranı | Open-Meteo, ECMWF ve diğer kaynakların atıfları |
| WX-040 | P0 | A | Shader arka plan v0 | Açık, bulutlu, yağmur, kar, gece; hareketi azalt; 60 fps |
| WX-041 | P1 | A | Gün doğumu/batımı geçişleri | Gökyüzü rengi saate göre |
| WX-045 | P0 | A | Konfor endeksi | Girdiler ve formül `product/02-features.md`'de; birim testli |
| WX-046 | P0 | A | Kıyafet önerisi | Aynı sıcaklıkta rüzgâr/nem farkını yansıtır |
| WX-047 | P1 | A | Koşu için en iyi saat | Önümüzdeki 24 saatte en uygun aralık |
| WX-050 | P0 | A | Android Glance widget | Küçük + orta; 30 dk güncelleme; Vitals uyarısı yok |
| WX-055 | P0 | A | Gizlilik politikası ve KVKK metni | Konum işleme açıklaması; uygulama içi bağlantı |
| WX-056 | P0 | A | Crash raporlama | Kişisel veri göndermez |
| WX-057 | P0 | ÜS+A | Play Console kapalı test | ≥ 10 test kullanıcısı |

## Faz 2 — iOS + sağlayıcı kararı
| ID | Ö | Sahip | Story | Kabul |
|---|---|---|---|---|
| WX-060 | P0 | ÜS | Mac ortamı | Xcode + imzalama |
| WX-061 | P0 | A | iOS derleme ve mağaza hazırlığı | TestFlight |
| WX-062 | P0 | A | SwiftUI + WidgetKit widget | App Group ile veri; küçük + orta |
| WX-065 | P0 | A | Sağlayıcı karşılaştırma raporu | Değişken × ufuk × şehir; lisansın izin verdiği sağlayıcılar |
| WX-066 | P0 | ÜS | Ana sağlayıcı kararı | Yeni ADR |
| WX-070 | P0 | ÜS+A | Herkese açık yayın | App Store + Play |

## Faz 3 — Kendi doğruluk katmanı
| ID | Ö | Sahip | Story | Kabul |
|---|---|---|---|---|
| WX-080 | P0 | A | Bias düzeltme v1 | İstasyon × saat × ufuk × mevsim; çapraz doğrulama |
| WX-081 | P0 | A | Grid'e yayma | İstasyonsuz hücrelerde düzeltme stratejisi ADR ile |
| WX-085 | P0 | A | Kalibre güven skoru | Güvenilirlik diyagramı, Brier; ADR-0009 |
| WX-086 | P0 | A | Güven gösterimi UI | "Önümüzdeki 60 dk" ve günlük kartlarda |

## Fikirler (önceliklendirilmedi)
| ID | Fikir | Kaynak |
|---|---|---|
| IDEA-001 | Nowcasting ve radar (Rainbow.ai / Tomorrow.io; Türkiye kapsamına bağlı) | Faz 0 dokümanı |
| IDEA-002 | Hava kalitesi ve polen (CAMS) | Faz 0 dokümanı |
| IDEA-003 | Sürüş, seyahat, bahçe, gün batımı fotoğraf skorları | ChatGPT önerisi, 2026-11-07 |
| IDEA-004 | Wear OS / Apple Watch, Live Activity | 2026-11-08 sohbeti |
| IDEA-005 | Plus abonelik (yalnız kendi ürettiğimiz özellikler) | Gelir modeli |
| IDEA-006 | Arayüz dilini cihaz diline göre otomatik seçmek (belki hiç yapılmaz) | Âkif, 2026-11-08 |
