# 02 — Sistem Mimarisi

## Bileşenler ve veri akışı
```
                 ┌──────────────────────────── Mobil (Flutter) ───────────────────────────┐
                 │  UI + shader arka plan + endeks kartları   │  Glance / WidgetKit widget │
                 └───────────────┬────────────────────────────┴──────────────▲────────────┘
                                 │ HTTPS /v1/forecast?lat&lon                 │ JSON anlık görüntü
                                 ▼                                            │ (uygulama yazar)
┌──────────────────────────────── API (Rust / Axum) ─────────────────────────────────────────┐
│ adapters/http ─▶ application ─▶ domain (endeksler, grid, birimler)                          │
│                    │ ports: ForecastProvider · ForecastCache · VerificationSink              │
│                    ▼                                                                         │
│ adapters/providers: open_meteo (archive=yes) · meteoblue (yanıta göre) · weatherkit (yok)   │
│ adapters/cache: moka (TTL = shared_cache_ttl)       adapters/db: sqlx → own.served_forecasts │
└──────────────────────────────────────────┬──────────────────────────────────────────────────┘
                                           │
                     ┌─────────────────────▼──────────────────────┐
                     │ PostgreSQL + TimescaleDB                    │
                     │  own.*      : stations, metar_observations, │
                     │               ecmwf_point_forecasts,        │
                     │               served_forecasts, verification│
                     │  licensed.* : yalnız archive_allowed        │
                     └─────────────────────▲──────────────────────┘
                                           │
┌──────────────────────── Pipeline (Python, zamanlanmış) ─────────────────────────────────────┐
│ metar_archiver (10 dk) · ecmwf_snapshot (00/12 UTC) · verify (günlük) · bias_fit (Faz 3)    │
│ Kaynaklar: aviationweather.gov · data.ecmwf.int · (Open-Meteo ticari)                        │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Temel ilkeler
1. **Lisans bayrakları tipte.** Her `ForecastProvider` `archive_allowed`, `shared_cache_ttl`, `attribution` bildirir; önbellek TTL'i ve `VerificationSink` yazımı bu değerlerden türetilir, elle verilmez.
2. **Gizlilik sınırı API'de.** Koordinat ilk adımda grid hücresine indirgenir; sonraki katmanlar ve loglar ham koordinat görmez.
3. **Bayat ama erişilebilir.** Sağlayıcı hatasında önbellekteki son geçerli veri `stale: true` ile döner; TTL lisans sınırını aşamaz.
4. **Sağlayıcıdan bağımsız sözleşme.** Mobil yalnız `04-api-contracts.md` şemasını bilir; sağlayıcı değişimi istemciyi etkilemez.
5. **Doğrulama zinciri.** Sunulan her tahmin (izinliyse) kaydedilir; pipeline METAR ile eşleştirir; rapor ve Faz 3 kalibrasyonu buradan beslenir.

## Açık tasarım kararları
| Konu | Seçenekler | Ne zaman |
|---|---|---|
| Grid | H3 (çözünürlük 6–7) / sabit lat-lon ızgara | Faz 1A başında ADR |
| Dağıtım | Tek VPS (docker compose) / yönetilen Postgres + konteyner | Faz 1G |
| Pipeline zamanlayıcı | cron (systemd timer) / APScheduler / Timescale job | Faz 0 (Kararlar) |
| Widget güncelleme | Uygulama anlık görüntüsü / widget kendi çağrısı | Faz 1F |
