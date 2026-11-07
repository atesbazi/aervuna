# Ufuk

Global hava durumu uygulaması. Kalbi doğruluk: mağaza ve cihazlara gömülü hava uygulamalarından daha tutarlı ve daha doğru tahmin, ölçülerek kanıtlanır. Şık, gerektiğinde sinematik. Önce Android (Flutter), sonra iOS.

| Bileşen | Yol | Teknoloji |
|---|---|---|
| Mobil | `apps/mobile` | Flutter + Kotlin/Glance widget (+ SwiftUI widget, Faz 2) |
| API | `services/api` | Rust / Axum |
| Veri hattı | `pipeline` | Python |
| Veritabanı | `db/migrations` | PostgreSQL + TimescaleDB |

Başlangıç noktası: [`docs/README.md`](docs/README.md) · Durum: [`docs/progress.md`](docs/progress.md) · Plan: [`docs/plan.md`](docs/plan.md)

Veri atıfları: ECMWF açık verisi (CC BY 4.0), Open-Meteo (CC BY 4.0), NOAA Aviation Weather Center (METAR). Ayrıntı: [`docs/research/license-notes.md`](docs/research/license-notes.md).
