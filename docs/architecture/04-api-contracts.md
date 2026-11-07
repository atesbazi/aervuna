# 04 — API Sözleşmesi (taslak, Faz 1A'da kesinleşir)

Genel: `https://api.<alan>/v1`, JSON, UTF-8, zamanlar ISO 8601 UTC + `timezone` alanı. Hata: `application/problem+json` (`type`, `title`, `status`, `code`, `retryable`, `requestId`).

## `GET /v1/forecast`
Sorgu: `lat`, `lon` (zorunlu), `lang` (`en` varsayılan \| `tr`), `units` (`metric` varsayılan \| `imperial`).

```json
{
  "cell": "grid:…",
  "timezone": "Europe/Istanbul",
  "generatedAt": "2026-11-08T09:00:00Z",
  "stale": false,
  "sources": [{ "provider": "open-meteo", "attribution": "Weather data by Open-Meteo.com (CC BY 4.0)" }],
  "current": { "time": "…", "temp": 14.2, "feelsLike": 12.9, "humidity": 71, "windSpeed": 18, "windGust": 31, "windDir": 220, "precip": 0.0, "condition": "partly_cloudy", "uvIndex": 2, "isDay": true },
  "hourly": [ { "time": "…", "temp": 14.0, "feelsLike": 12.5, "precipProb": 20, "precip": 0.0, "windSpeed": 17, "condition": "cloudy" } ],
  "daily":  [ { "date": "2026-11-08", "tempMin": 8.1, "tempMax": 16.4, "precipProb": 30, "precipSum": 0.4, "sunrise": "…", "sunset": "…", "condition": "showers" } ],
  "lifestyle": {
    "comfort": { "score": 72, "label": "comfortable" },
    "outfit":  { "layers": 2, "items": ["light_jacket"], "umbrella": false },
    "bestRun": { "from": "…", "to": "…", "reason": "low_wind_mild_temp" }
  },
  "confidence": null
}
```
- `condition`: kapalı sözlük (`clear`, `partly_cloudy`, `cloudy`, `fog`, `drizzle`, `rain`, `showers`, `snow`, `sleet`, `thunderstorm`); görsel katmanın girdisi.
- `confidence`: Faz 3'e kadar `null` (ADR-0009).
- Ham koordinat yanıtta yer almaz.

## `GET /v1/places/search?q=`
Şehir/ilçe arama. Kaynak Faz 1A'da seçilir (lisans kontrolüyle).

## `GET /v1/attributions`
Uygulamanın atıf ekranı için tüm aktif kaynaklar.

## `GET /health`
Canlılık; sağlayıcı ve DB durumları.
