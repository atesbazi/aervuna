# Aervuna — Proje Dokümantasyonu

> Global, ticari hava durumu uygulaması. **Kalbi doğruluk:** mağaza ve cihazlara gömülü hava uygulamalarından daha tutarlı ve daha doğru tahmin, ölçülerek kanıtlanır. Şık ve ihtiyaç dahilinde sinematik görsellik, yaşam tarzı önerileri, kalibre tahmin güveni.
> Arayüz varsayılanı İngilizce. Android ile başlar (Faz 1), iOS Faz 2'de eklenir. Saatsiz scheduled task oturumlarıyla geliştirilir.

Bu klasör projenin **tek doğruluk kaynağıdır**. Kod ajanı (Claude Code) bağlamı buradan kurar; sohbet geçmişine dayanmaz.

## Okuma sırası (ajan için zorunlu)
| # | Dosya | Ne için |
|---|---|---|
| 1 | [`AGENTS.md`](AGENTS.md) | Çalışma kuralları. Her oturum başında okunur |
| 2 | [`progress.md`](progress.md) | Nerede kaldık, sıradaki adım, kararlar, ürün sahibi görevleri |
| 3 | [`plan.md`](plan.md) | Fazlar, kapsam, kabul kriterleri |
| 4 | [`backlog.md`](backlog.md) | `WX-xxx` story'leri |
| 5 | [`adr/`](adr/) | Bağlayıcı mimari kararlar |
| 6 | [`research/`](research/) | Sağlayıcı kararı, lisans notları, AI incelemeleri |
| 7 | [`architecture/`](architecture/) | Teknoloji, sistem, veri modeli, API, doğrulama, güvenlik |
| 8 | [`product/`](product/) | Vizyon, özellikler, gelir modeli, rakipler |
| 9 | [`design/`](design/) | Görsel yön, ekranlar |
| 10 | [`quality/`](quality/) | Test ve CI/CD |
| 11 | [`prompts/`](prompts/) | Oturum ve faz başlatma promptları |
| 12 | [`templates/`](templates/) | Checkpoint, oturum kaydı, sağlayıcı yanıtı şablonları |

## Klasör yapısı
```
docs/
├── README.md · AGENTS.md · plan.md · progress.md · backlog.md · risks.md · glossary.md
├── adr/            0000-template + 0001…0010
├── research/       2026-11-07-data-provider-decision.md · license-notes.md · competitor-benchmark.md · ai-reviews.md · provider-responses.md
├── architecture/   01-tech-stack · 02-system-architecture · 03-data-model · 04-api-contracts · 05-forecast-verification · 06-security-privacy
├── product/        01-vision · 02-features · 03-monetization · 04-competitors · 05-lifestyle
├── design/         01-visual-direction
├── quality/        01-testing-strategy · 02-ci-cd
├── prompts/        session-prompts.md
├── templates/      checkpoint.md · session-log.md · provider-response.md
└── reports/        phase-N/ ekran görüntüleri ve doğrulama raporları
```

## Kaynak doküman
Faz 0 karar dokümanının canlı sürümü: [Claude Docs](https://claude.ai/artifact/72J8iYJrrGgEHB5GKzXfsm). Repo kopyası: [`research/2026-11-07-data-provider-decision.md`](research/2026-11-07-data-provider-decision.md). İkisi ayrışırsa **repo kopyası esastır**.
