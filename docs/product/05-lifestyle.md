# 05 — Yaşam Tarzı Katmanı

> Aervuna'nın ikinci değer ayağı. Doğru tahmin "ne olacak?" sorusunu, yaşam tarzı katmanı "**bu benim için ne demek, ne yapmalıyım?**" sorusunu yanıtlar. Opsiyonel bir eklenti değil, ürünün çekirdeğidir. Çatışmada doğruluk önce gelir (AGENTS §0), çünkü öneri ancak dayandığı tahmin kadar iyidir.
> Bağlayıcı karar: ADR-0010.

## İlkeler
1. **Karar odaklı.** Her öneri kullanıcının günlük bir sorusunu yanıtlar: Şemsiye alayım mı? Ne giyeyim? Koşuya ne zaman çıkayım? Çamaşırı asayım mı? Arabayı yıkayayım mı?
2. **Açıklanabilir.** Her önerinin yanında kısa bir "neden" vardır ("14:00'ten sonra %70 yağış, rüzgâr 30 km/h"). Kara kutu yok.
3. **Deterministik ve sürümlü.** Kurallar Rust `domain` katmanında, birim testli ve sürüm numaralı. Aynı girdi her zaman aynı öneriyi verir.
4. **Güvenle uyumlu (Faz 3+).** Öneri gücü kalibre güvene göre ayarlanır: belirsizlik yüksekse öneri bunu söyler ("yağış ihtimali düşük ama tahmin belirsiz, ince bir yağmurluk yeterli").
5. **Ölçülür.** Doğruluk ürünün kalbi olduğu için önerilerin isabeti de ölçülür: "şemsiye al" dediğimiz günlerin kaçında gerçekten yağdı (Faz 2–3).
6. **Kişisel ama gizli.** Kişiselleştirme (üşüme hassasiyeti, tercih edilen koşu saatleri) cihazda tutulur; API'ye yalnız sayısal parametre olarak gider, hesap gerekmez.
7. **Global.** Birimler, kıyafet sözlüğü ve metinler yerelleştirilir; mevsim mantığı yarımküreye göre çalışır.
8. **Sağlık ve güvenlik iddiası yok.** Sürüş, UV, hava kalitesi önerileri bilgilendirme amaçlıdır; tıbbi ya da güvenlik garantisi gibi sunulmaz.

## Öneri kataloğu ve fazlar
| Öneri | Soru | Faz | Ana girdiler |
|---|---|---|---|
| Günün özeti | Bugün beni ne bekliyor? | 1 | Tüm günlük seri → tek cümle |
| Konfor endeksi | Dışarısı nasıl hissettiriyor? | 1 | Hissedilen, nem, rüzgâr, yağış olasılığı, UV |
| Kıyafet + şemsiye | Ne giyeyim, şemsiye alayım mı? | 1 | Hissedilen, rüzgâr, yağış, gün içi aralık, kişisel üşüme ayarı |
| Koşu / yürüyüş saati | Ne zaman çıkayım? | 1 | 24 saatlik seri: sıcaklık, rüzgâr, yağış, UV, gün ışığı |
| Sabah brifingi bildirimi | Güne başlarken bilmem gereken? | 2 | Günün özeti + kıyafet; kullanıcı saati |
| Şemsiye / yağış hatırlatması | Çıkarken yağmura yakalanır mıyım? | 2 | Saatlik yağış; kayıtlı yerler |
| Çamaşır kurutma | Çamaşırı dışarı asayım mı? | 2 | Yağışsız süre, nem, rüzgâr, güneş |
| Araç yıkama | Yıkatırsam boşa gider mi? | 2 | 48–72 saat yağışsız olasılığı |
| Bisiklet | Bisikletle gidebilir miyim? | 2 | Rüzgâr, hamle, yağış, sıcaklık |
| Gün batımı / fotoğraf | Gün batımı güzel olacak mı? | 2 | Bulutluluk katmanları, görüş, gün batımı saati |
| Sürüş koşulları (bilgi) | Yollar nasıl? | 2 | Yağış tipi, sis/görüş, donma noktası çevresi |
| Kişiselleştirme v1 | Bana göre mi? | 2 | Üşüme hassasiyeti, aktivite tercihleri (cihazda) |
| Güven farkındalıklı öneriler | Bu öneriye ne kadar güveneyim? | 3 | Kalibre güven (ADR-0009) |
| Öneri isabet raporu | Önerilerin işe yaradı mı? | 3 | Öneri ↔ gerçekleşen gözlem |
| Kişiselleştirme v2 | Benden öğrenebilir mi? | 3 | "Tahminden soğuktu/sıcaktı" geri bildirimi, cihazda öğrenme |
| Alerji ve dış mekân spor (AQI, polen) | Dışarıda spor yapayım mı? | 4 | CAMS hava kalitesi ve polen |
| Güneş koruma zamanlayıcı | Ne zaman güneş kremi? | 4 | UV seri |
| Seyahat karşılaştırma | Gideceğim şehirde ne bekliyor? | 4 | Kayıtlı/aranan yerler |
| Bahçe / sulama | Bugün sulamalı mıyım? | 4 | Yağış toplamı, evapotranspirasyon |

## Uygulama yerleşimi
- **Ana ekran:** Günün özeti + kıyafet/şemsiye kartı ilk ekranda; diğer öneriler kartlar halinde, kullanıcı sıralayabilir (Faz 2).
- **Widget:** Sıcaklığın yanında tek satır öneri (Faz 1F: şemsiye/kıyafet).
- **Bildirim:** Yalnız kullanıcının açtığı türler; günde en fazla 2 (Faz 2).
- **Görsellik:** Öneri kartları sinematik arka planla yarışmaz; sakin, okunur.

## Gelir modeli ile ilişki
Temel öneriler (Faz 1 seti) ücretsiz. Gelişmiş öneriler ve kişiselleştirme Plus adayıdır (`03-monetization.md`). Öneriler kendi ürettiğimiz katma değerdir; ham sağlayıcı verisi satılmaz.

## Formül kaydı
Her önerinin girdileri, eşikleri, sürümü ve test vektörleri bu dosyanın altında "Formüller" bölümüne story kapanırken yazılır.

## Formüller
(Faz 1E ile doldurulacak.)
