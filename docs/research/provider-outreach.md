# Sağlayıcı Yazışmaları (WX-001)

> Gönderilmeye hazır metinler. Gönderen: Âkif. Yanıtlar geldikçe `provider-responses.md`'ye `templates/provider-response.md` formatında işlenir.
> `[Ad Soyad]` ve `[e-posta]` alanlarını doldur. Kişisel e-posta adresleri repoya yazılmaz.
> Senaryo rakamları `2026-11-07-data-provider-decision.md` → Birim ekonomisi ile aynıdır.

## Gönderim listesi
| Sağlayıcı | Kanal | Dil | Öncelik |
|---|---|---|---|
| Open-Meteo | info@open-meteo.com — **gönderildi 2026-11-08** | EN | 1 — ana kaynak |
| Meteoblue | support@meteoblue.com ([iletişim sayfası](https://content.meteoblue.com/en/about-us/contact)) — **gönderildi 2026-11-08** | EN | 1 — kıyas |
| Tomorrow.io | tomorrow.io satış iletişim formu (e-posta bulunamadı) — Âkif | EN | 2 — nowcasting |
| Rainbow.ai | rainbow.ai/business iletişim formu (e-posta bulunamadı) — Âkif | EN | 2 — nowcasting |
| MGM | pazarlama@mgm.gov.tr ([ürünler sayfası](https://mgm.gov.tr/site/urunler.aspx?u=tum)) — **gönderildi 2026-11-08** | TR | 3 — Türkiye istasyon verisi |

İletişim formunda karakter sınırı varsa metnin "Questions" bölümü korunur, giriş kısaltılır.

---

## 1. Open-Meteo
**Konu:** Commercial API plan for a consumer weather app — licensing and pricing questions

```
Hello Open-Meteo team,

I am building Aervuna, a consumer mobile weather app (Android first, then iOS) with a global
audience. Our core promise is forecast accuracy we can measure: we archive the forecasts we
serve and verify them against METAR observations, and we derive our own lifestyle
recommendations (clothing, umbrella, best time to run) from the forecast data.

We would like to use Open-Meteo as our primary forecast source under a commercial plan and
want to confirm the following before we commit:

1. Use case: Is a commercial plan suitable for a consumer app whose primary purpose is
   showing weather forecasts?
2. Shared caching: May we cache responses per grid cell (about 5 km) and serve them to all
   users in that cell for up to 30–60 minutes?
3. Archiving: May we store the forecasts we serve, indefinitely, to verify accuracy and to
   train our own bias-correction and calibration models?
4. Derived products: May we compute and display our own indices and blended or corrected
   forecasts derived from your data, including inside a paid subscription tier?
5. Attribution: What exact attribution text and placement do you require in the app?
6. Pricing and SLA: Our estimate is about 4–5 million API calls per month at launch
   (10k DAU) and about 17 million per month at 100k DAU (grid caching applied). Which plan
   fits each stage, what are the prices, and what uptime/support terms apply?
7. Self-hosting: If we later self-host the open-source server for part of the load, are
   there commercial terms we should know about?

A written confirmation of points 1–5 would be very helpful for our licensing records.

Thank you,
[Ad Soyad]
Aervuna (pre-launch)
[e-posta]
```

---

## 2. Meteoblue
**Konu:** Weather API for a consumer weather app — licensing, caching, archiving and quote

```
Hello meteoblue team,

I am building Aervuna, a consumer mobile weather app (Android first, then iOS) with a global
audience. Accuracy is our core promise, so we measure every source we use against METAR
observations. We are considering meteoblue (Premium Weather API, multimodel/mLM) as a
primary or benchmark source and need to clarify licensing before requesting a contract.

Questions:
1. Use case: May your data be displayed in a consumer app whose primary purpose is weather
   forecasts?
2. Shared caching: May we cache responses per grid cell (about 5 km) and serve them to all
   users in that cell for 30–60 minutes?
3. Archiving and verification: May we store the forecasts we receive to verify accuracy
   over time, and to train our own bias-correction and calibration models?
4. Derived products: May we compute and display our own indices (comfort, clothing,
   umbrella advice) and blended forecasts derived from your data, including in a paid tier?
5. Attribution: Required format and placement; and the details of the discount you offer
   for displaying the meteoblue logo and link.
6. Coverage: For Turkey and Europe, what radar-based nowcasting, lightning and official
   warning data do you offer?
7. Quote: Two scenarios, hourly 7–10 day forecasts with about 15 variables:
   - Launch: about 3,000 active grid cells refreshed every 30 minutes (~4.3M calls/month)
   - Growth: about 12,000 active grid cells refreshed every 30 minutes (~17M calls/month)
   Please include the credit consumption per call, any mandatory support tier, and whether
   location-based pricing would be more suitable for this pattern.

A written confirmation of points 1–4 would be important for us.

Best regards,
[Ad Soyad]
Aervuna (pre-launch)
[e-posta]
```

---

## 3. Tomorrow.io
**Konu:** Minute-level precipitation nowcasting for a consumer weather app — coverage and terms

```
Hello Tomorrow.io team,

I am building Aervuna, a consumer mobile weather app with a global audience, starting with
Turkey and Europe. We are evaluating providers for minute-level precipitation nowcasting
(next 0–2 hours).

Questions:
1. Coverage: In Turkey (Istanbul, Ankara, Izmir, Antalya) and in Western Europe, is your
   minute-level precipitation based on radar, or on satellite/model data? Do you have a
   coverage map?
2. Use case: May your data be displayed in a consumer app whose primary purpose is weather?
3. Caching, archiving and derived products: May we cache per grid cell and share across
   users, store forecasts to verify accuracy, and derive our own alerts and indices?
4. Pricing: Plans for about 1–5M nowcast calls per month, and SLA terms.
5. Trial: Can we get a trial key to run a field test in Turkey for 30 days?

Thank you,
[Ad Soyad]
Aervuna (pre-launch)
[e-posta]
```

---

## 4. Rainbow.ai
**Konu:** Minute-by-minute precipitation API — Turkey coverage and licensing

```
Hello Rainbow.ai team,

I am building Aervuna, a consumer mobile weather app (Android first, then iOS), starting
with Turkey and Europe. Your Minute-by-Minute Forecast API and Tiles API are on our
shortlist for precipitation nowcasting and radar maps.

Questions:
1. Coverage: Is Turkey covered by real radar data in your nowcast and tiles? If not, what
   is the quality of the non-radar coverage there?
2. Use case: May your data be displayed in a consumer weather app, including within a paid
   subscription tier?
3. Caching and archiving: May we cache per grid cell and share across users, and store
   forecasts to verify accuracy over time?
4. Attribution: Required format and placement.
5. Volume pricing: About 1–5M forecast calls and 1–3M tile requests per month.
6. Trial: Could we get extended trial access for a 30-day field test in Turkey?

Thank you,
[Ad Soyad]
Aervuna (pre-launch)
[e-posta]
```

---

## 5. MGM — Meteoroloji Genel Müdürlüğü
**Konu:** Ticari mobil hava durumu uygulaması için gerçek zamanlı gözlem verisi talebi

```
Sayın Yetkili,

Aervuna adlı, Türkiye'den başlayarak global kullanıcılara yönelik ticari bir mobil hava
durumu uygulaması geliştiriyorum. Uygulamanın temel hedefi tahmin doğruluğudur. Bu amaçla
sunduğumuz tahminleri gerçekleşen gözlemlerle karşılaştırarak doğruluklarını ölçüyor ve
yerel düzeltme modelleri geliştiriyoruz.

MEVBİS üzerinden sunulan veriler hakkında aşağıdaki konularda bilgi rica ediyorum:

1. Otomatik meteoroloji gözlem istasyonlarının (OMGİ) gerçek zamanlı ya da saatlik
   verilerine API veya düzenli veri aktarımıyla erişim mümkün müdür?
2. Bu veriler ticari bir mobil uygulamada, (a) yalnız tahmin doğrulama ve model eğitimi
   için iç kullanımda, (b) kullanıcıya gösterim amacıyla kullanılabilir mi? Her iki durum
   için lisans koşulları nelerdir?
3. Verilerin arşivlenmesine ve bunlardan türetilmiş ürünler (düzeltilmiş tahmin, öneri)
   üretilmesine izin verilmekte midir?
4. Resmi meteorolojik uyarıların uygulamada kaynak gösterilerek yayımlanması için koşullar
   nelerdir?
5. İstasyon sayısı ve güncelleme sıklığına göre yıllık fiyatlandırma bilgisi alabilir miyim?

Bilgilendirmeniz için şimdiden teşekkür ederim.

Saygılarımla,
[Ad Soyad]
Aervuna
[e-posta]
```
