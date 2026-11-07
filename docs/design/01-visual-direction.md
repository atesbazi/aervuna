# 01 — Görsel Yön (taslak, Faz 1C öncesi kesinleşir)

## Hedef (Âkif, 2026-11-08)
Kullanıcı uygulamayı açtığında hoşuna gitmeli: şık, görsel olarak tatmin edici ve **ihtiyaç dahilinde sinematik**.

## İlkeler
0. **Sinematik an, gerektiğinde.** Fırtına yaklaşıyor, ilk kar, gün batımı, uzun yağmurun bitişi gibi anlarda sahne zenginleşir. Sıradan bir günde arka plan sakin kalır ve bilgi öndedir.
1. **Veriyle tutarlı görsellik.** Arka plan animasyonu `condition` ve `isDay` alanından türetilir; veri yağmur demiyorsa yağmur çizilmez.
2. **Önce okunurluk.** Sıcaklık ve sonraki 2 saat bir bakışta okunur; dekor bilgiyi örtmez.
3. **Sakin hareket.** 60 fps, yumuşak geçişler; "hareketi azalt" açıksa statik görsel.
4. **Token'lardan stil.** Renk, tipografi, boşluk, radius Flutter `ThemeExtension` token'larında; ekranda sabit değer yok.

## Arka plan durumları (Faz 1D)
| Durum | Gündüz | Gece |
|---|---|---|
| clear | Gradyan gökyüzü, güneş halesi | Yıldız alanı |
| partly_cloudy / cloudy | Parallax bulut katmanları | Koyu bulut, ay ışığı |
| rain / showers / drizzle | Shader yağmur çizgileri, cam damlası (P2) | Aynı, düşük kontrast |
| snow / sleet | Partikül kar | Aynı |
| thunderstorm | Yağmur + aralıklı şimşek (hareketi azalt'ta kapalı) | Aynı |
| fog | Hacimsel sis | Aynı |

## Açık kararlar
- Tipografi ve renk paleti (Faz 1C).
- Tasarım aracı ve referans moodboard (Âkif).
- Widget görsel dili (Faz 1F).
