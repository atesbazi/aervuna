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
| Endeks | Faz | Girdiler | Çıktı |
|---|---|---|---|
| Konfor endeksi | 1 | hissedilen, nem, rüzgâr, yağış olasılığı, UV | 0–100 + etiket |
| Kıyafet önerisi | 1 | hissedilen, rüzgâr, yağış, gün içi aralık | katman sayısı, parçalar, şemsiye |
| Koşu için en iyi saat | 1 | 24 saatlik seri: sıcaklık, rüzgâr, yağış, UV, karanlık | saat aralığı + gerekçe |
| Sürüş, seyahat, bahçe, gün batımı fotoğraf | 4+ | — | IDEA-003 |

Formüller ve eşikler Faz 1E'de bu dosyaya yazılır; her biri birim testli. Endeks çıktıları ham sağlayıcı verisini geri vermeyecek biçimde dönüştürülmüştür (katma değerli ürün).

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
