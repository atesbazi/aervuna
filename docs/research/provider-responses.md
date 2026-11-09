# Sağlayıcı Yanıtları

> Gönderilen metinler: [`provider-outreach.md`](provider-outreach.md).
> Takip: "Aervuna — sağlayıcı yanıt takibi" scheduled task'ı her gün 09:47 (İstanbul) Gmail'i tarar, yeni yanıtı buraya işler ve Âkif'e bildirim gönderir. Sağlayıcılara otomatik yanıt yazılmaz.
> Her yazılı yanıt `../templates/provider-response.md` formatında buraya eklenir. Yanıt gelince `license-notes.md` satırı güncellenir ve gerekiyorsa ADR revize edilir.
> E-postanın kendisi repoya konmaz (kişisel veri); özet + tarih + gönderen rolü yazılır.

| Sağlayıcı | Gönderildi | Yanıt | Özet | license-notes güncellendi |
|---|---|---|---|---|
| Open-Meteo | 2026-11-08 (e-posta, info@) | ✅ 2026-11-09 (e-posta, destek bileti) | Ticari plan uygun; saklama, arşiv, türev ve yeniden dağıtım serbest (koşul: Open-Meteo + resmi veri sağlayıcıya atıf); 4–5M çağrı/ay Professional plan, üstü 10M'lik ek Professional planlar + otomatik hacim indirimi; SLA yalnız Enterprise; self-host lisanssız ama değişiklikler açık kaynak olmalı | evet (2026-11-09) |
| Meteoblue | 2026-11-08 (e-posta, support@; satışa iletilmesi rica edildi) | Bekleniyor | | |
| Tomorrow.io | Ertelendi (Faz 4, nowcasting) | | | |
| Rainbow.ai | Ertelendi (Faz 4, nowcasting) | | | |
| MGM | 2026-11-08 (e-posta, pazarlama@) | Bekleniyor | | |

## Yanıtlar

### Open-Meteo — 2026-11-09
- **Gönderen rolü:** Open-Meteo GmbH destek ekibi (info@ destek bileti üzerinden)
- **Kanal:** e-posta (gönderdiğimiz 2026-11-08 e-postasına yanıt)

| Soru | Yanıt (özet) | Yazılı mı? | Sonuç |
|---|---|---|---|
| 1. Ticari hava uygulamasında kullanım | "A commercial plan is suitable for your use case." | Evet | ✅ |
| 2. Paylaşılan önbellek (hücre başına, 30–60 dk) | Ayrıca anılmadı; ham ve işlenmiş verinin saklanması ve yeniden dağıtımı serbest → kullanıcılar arası önbellek lisans açısından sınırsız. Süre bizim tazelik kararımız | Evet (genel izin) | ✅ |
| 3. Arşiv (süresiz), doğrulama, bias düzeltme/kalibrasyon modeli eğitimi | "use, store, and redistribute raw and processed data and analysis results" | Evet | ✅ |
| 4. Türev endeks + blend/düzeltilmiş tahmin, ücretli katman dahil | Aynı genel izin (işlenmiş veri ve analiz sonuçları); ücretli katmana kısıt anılmadı | Evet | ✅ |
| 5. Atıf biçimi | Tek koşul: hem Open-Meteo'ya hem resmi hava verisi sağlayıcısına (model sahibi ulusal servis) uygun atıf; ayrıntı [lisans sayfası](https://open-meteo.com/en/licence) | Evet (sayfaya atıf) | ⚠️ Model bazlı atıf gerekli |
| 6. Fiyat ve SLA | 4–5M çağrı/ay: **Professional API** planı. Daha fazlası için her biri 10M çağrı/ay olan ek Professional plan(lar); hacim indirimi otomatik. Tutar yanıtta yok, [fiyat sayfası](https://open-meteo.com/en/pricing). **SLA yalnız Enterprise planlarda** | Evet | ⚠️ SLA yok (Professional) |
| 7. Self-host | Open-Meteo'dan lisans gerekmez; işletme bizde. Tek yükümlülük: değişiklikler ve tescilli eklemeler açık kaynak ve herkese açık olmalı ([LICENSE](https://github.com/open-meteo/open-meteo/blob/main/LICENSE)) | Evet | ⚠️ Kaynak açma yükümlülüğü |

- **Adaptör bayrakları:** `archive_allowed=true` · `shared_cache_ttl=30 dk` (lisans sınırı yok; tazelik kararı, bkz. progress.md → Kararlar 2026-11-09) · `attribution="Weather data by Open-Meteo.com (CC BY 4.0)" + kullanılan modelin resmi sağlayıcısı`
- **Etkilenen ADR:** ADR-0002 (Open-Meteo ayağının yazılı teyidi geldi; karar değişmedi). Self-host yükümlülüğü ileride ayrı ADR konusu.
- **license-notes.md güncellendi:** evet
