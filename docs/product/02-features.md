# 02 — Özellikler

## A. Hava zekâsı
| Özellik | Faz | Not |
|---|---|---|
| Şimdi, saatlik 48 saat, 10 gün | 1 | |
| Hissedilen sıcaklık, nem, rüzgâr/hamle, UV, görüş, basınç | 1 | |
| Yağış olasılığı ve miktarı ayrı | 1 | |
| Yağışın başlama/bitiş zamanı | 4 | Nowcasting'e bağlı |
| Resmi uyarılar | 2+ | Kaynak ve lisans kararı gerekir |
| Tahmin güveni + son güncelleme zamanı | 3 | ADR-0009 |
| Hava kalitesi, polen | 4 | CAMS |

## B. Yaşam tarzı zekâsı (kendi algoritmamız)
Tam katalog, ilkeler ve faz eşlemesi: [`05-lifestyle.md`](05-lifestyle.md). Karar: ADR-0010.
Özet: Faz 1 günün özeti, konfor, kıyafet+şemsiye, koşu saati · Faz 2 bildirimler, çamaşır, araç yıkama, bisiklet, gün batımı, sürüş, kişiselleştirme v1 · Faz 3 güven farkındalıklı öneriler, isabet raporu, kişiselleştirme v2 · Faz 4 AQI/polen, UV, seyahat, bahçe.
Öneri çıktıları ham sağlayıcı verisini geri vermeyecek biçimde dönüştürülmüştür (katma değerli ürün).

## C. Görsel deneyim
| Özellik | Faz |
|---|---|
| Duruma göre shader arka plan (açık, bulutlu, yağmur, kar, gece) | 1 |
| Gün doğumu/batımı gökyüzü geçişi | 1 |
| Etkileşimli saatlik grafik | 1 |
| Radar/uydu görüntüsü | 4 |
| Hareketi azalt desteği | 1 |

## D. Platform
| Özellik | Faz |
|---|---|
| Android widget (Glance) | 1 |
| iOS widget (WidgetKit) | 2 |
| Bildirimler (yağış yaklaşıyor, sabah özeti) | 2+ |
| Live Activity, Watch, Wear OS | 4+ |

## Örnek güven ekranı (Faz 3, temsili)
```
Ankara, Çankaya · Önümüzdeki 60 dakika
Yağış olasılığı  %78      Tahmin güveni  Orta
Yaklaşık 20 dakika içinde yağış başlayabilir.
```
Değerler temsilidir; gerçek gösterim kalibrasyon verisine bağlıdır.
