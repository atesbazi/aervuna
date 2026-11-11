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
| MGM | 2026-11-08 (e-posta, pazarlama@) | ⚠️ 2026-11-11 (e-posta, Döner Sermaye İşletmesi) | Yalnız MY-55 "İl ve İlçe Merkezleri Son Durum" (saatlik, web servis, yıllık sözleşme) önerildi; **veriler arşivlenemez, 3. kişilerle paylaşılamaz**. Fiyat, OMGİ, türev ürün ve uyarı soruları yanıtsız; ürün listesi linki e-postada yok; 2027 ürünlerinde değişiklik olacak | evet (2026-11-11) |

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

### MGM — 2026-11-11
- **Gönderen rolü:** Meteoroloji Genel Müdürlüğü Döner Sermaye İşletmesi (talep pazarlama@ adresinden ilgili birime iletilmiş)
- **Kanal:** e-posta (gönderdiğimiz 2026-11-08 e-postasına yanıt)

| Soru | Yanıt (özet) | Yazılı mı? | Sonuç |
|---|---|---|---|
| 1. OMGİ gerçek zamanlı/saatlik veriye API ile erişim | OMGİ'den söz edilmedi. Önerilen ürün **MY-55 İl ve İlçe Merkezleri Son Durum**: il merkezleri ve belirli ilçelerin saatlik son durumu, web servis, **yıllık sözleşme** | Evet | ⚠️ Yalnız il/ilçe merkezi son durum; OMGİ ağı yanıtsız |
| 2a. İç kullanım (doğrulama, model eğitimi) | Doğrudan yanıt yok; genel koşul "veriler arşivlenemez" → doğrulama ve model eğitimi için gereken saklama yapılamaz | Evet (genel koşul) | ❌ |
| 2b. Kullanıcıya gösterim | Doğrudan yanıt yok; genel koşul "3. kişiler ile paylaşılamaz". En güvenli yorum: son kullanıcıya gösterim de yeniden dağıtımdır | Evet (genel koşul) | ❌ (en güvenli yorum) |
| 3. Arşiv ve türev ürün (düzeltilmiş tahmin, öneri) | "Veriler arşivlenemez." Türev ürün ayrıca anılmadı | Evet | ❌ Arşiv yasak; türev belirsiz |
| 4. Resmi uyarıların kaynak gösterilerek yayımlanması | Yanıtsız | — | ⚠️ Belirsiz |
| 5. Yıllık fiyat | Tutar yok; ürün listesine link verildiği yazıyor ama e-postada link/ek yok. "2027 ürünlerimizde değişiklikler olacaktır" | Kısmen | ⚠️ Fiyat bilinmiyor |

- **Adaptör bayrakları:** `archive_allowed=false` · `shared_cache_ttl=0` · `attribution="Meteoroloji Genel Müdürlüğü"` (kullanılırsa). Adaptör yazılmaz (bkz. `progress.md` → Kararlar 2026-11-11).
- **Etkilenen ADR:** ADR-0002 değişmez (MGM ana kaynak değil; `plan.md` "izin alınırsa MGM"). Doğrulama ve bias düzeltme METAR + ECMWF açık veri ile sürer.
- **license-notes.md güncellendi:** evet
