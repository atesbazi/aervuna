# 04 — API Sözleşmesi (taslak, Faz 1A'da kesinleşir)

Genel: `https://api.<alan>/v1`, JSON, UTF-8, zamanlar ISO 8601 UTC + `timezone` alanı. Hata: `application/problem+json` (`type`, `title`, `status`, `code`, `retryable`, `requestId`).

## `GET /v1/forecast`
Sorgu: `lat`, `lon` (zorunlu), `thermalBias` (−2…+2, varsayılan 0; cihazdaki kişiselleştirme, sunucuda saklanmaz), `lang` (`en` varsayılan \| `tr`), `units` (`metric` varsayılan \| `imperial`).

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
    "rulesVersion": "1.0.0",
    "summary": { "code": "rain_after", "params": { "time": "14:00", "item": "jacket" } },
    "comfort": { "score": 72, "label": "comfortable", "why": ["mild_feels_like", "light_wind"] },
    "outfit":  { "layers": 2, "items": ["light_jacket"], "umbrella": false, "why": ["feels_like_12", "wind_18"] },
    "bestRun": { "from": "…", "to": "…", "why": ["low_wind", "mild_temp", "dry"] },
    "confidence": null
  },
  "confidence": null
}
```
- `condition`: kapalı sözlük (`clear`, `partly_cloudy`, `cloudy`, `fog`, `drizzle`, `rain`, `showers`, `snow`, `sleet`, `thunderstorm`); görsel katmanın girdisi.
- `confidence`: Faz 3'e kadar `null` (ADR-0009).
- `lifestyle`: ADR-0010. Metinler istemcide `code` + `params` ile i18n şablonlarından üretilir; sunucu dil bağımsız kod döner.
- Ham koordinat yanıtta yer almaz.

## `GET /v1/places/search?q=`
Şehir/ilçe arama. Kaynak Faz 1A'da seçilir (lisans kontrolüyle).

## `GET /v1/attributions`
Uygulamanın atıf ekranı için tüm aktif kaynaklar.

## `GET /health`
Canlılık; sağlayıcı ve DB durumları.
