# 01 — Vizyon

## Tek cümle
App Store ve Play'deki uygulamalardan ve iOS/Android'in gömülü hava uygulamalarından **daha tutarlı ve daha doğru** tahmini veren, bunu **ölçerek kanıtlayan** ve kullanıcının gününü planlamasına yardım eden, şık ve gerektiğinde sinematik bir global hava durumu uygulaması.

## Ürünün kalbi: doğruluk (Âkif, 2026-11-08)
- **En önemli özellik ve pazarlama stratejisi:** Aervuna, mağazadaki uygulamalardan ve cihazların gömülü hava uygulamalarından (Apple Weather, Android'deki Google hava) daha tutarlı ve daha iyi tahmin verir.
- Her mühendislik önceliği bu hedefe göre sıralanır: doğrulama zinciri, sağlayıcı seçimi, bias düzeltme, kalibre güven. Görsel ve yaşam tarzı katmanları doğruluğu taşıyan araçlardır, onun yerine geçmez.
- **İddia kanıtla yapılır.** "Daha doğru" mesajı ancak `architecture/05-forecast-verification.md` metodolojisiyle, rakip kıyası dahil, üretilmiş rapora dayanır. Kanıtsız iddia hem güveni hem reklam mevzuatı açısından risktir (R4).
- **Tutarlılık** da ölçülür: aynı gün için tahminin saatten saate gereksiz zıplamaması (tahmin kararlılığı) bir kalite metriğidir.
- Gerçekçi hedef: her yerde her an birinci olmak değil; ölçtüğümüz şehirlerde ve ufuklarda, kullanıcının günlük kararlarında (yağmur alacak mıyım, ne giyeyim) ölçülebilir üstünlük. Sonra genişlemek.

## Kimin için
- **Global.** Arayüz varsayılan olarak İngilizce; Türkçe uygulama içinden seçilebilir. Cihaz diline otomatik uyum ileriye bırakıldı (IDEA-006; belki hiç yapılmaz).
- Doğrulamaya Türkiye ve birkaç global pilot şehirle başlanır; pazarlama iddiası yalnız ölçülen bölgeler için yapılır.

## Deneyim
- **Şık ve görsel olarak tatmin edici.** Kullanıcı açtığında hoşuna gitmeli.
- **Sinematik, ama ihtiyaç dahilinde.** Sinematik an (fırtına yaklaşıyor, gün batımı, ilk kar) bilgiyi güçlendirdiği yerde; günlük kullanımda sakin ve okunur.
- Görsellik gerçek veriyle tutarlıdır; veri yağmur demiyorsa yağmur çizilmez.

## Neden kazanır
1. **Ölçülen doğruluk** ve bunun şeffaf gösterimi.
2. **Güven skoru:** kalibre olasılık, "yağmur olasılığı %78, güven orta" (Faz 3).
3. **Yaşam tarzı zekâsı (ikinci değer ayağı):** tahmini kullanıcının kararına çevirir: ne giyeyim, şemsiye, koşu saati, çamaşır, araç yıkama… Açıklanabilir, ölçülen ve kişiselleşen öneriler (`05-lifestyle.md`).
4. **Görsel deneyim:** gerçek veriyle tutarlı, şık ve yeri geldiğinde sinematik.

## Ne değil
- Acil durum/hayat kurtarma uygulaması değil.
- Resmi meteoroloji uyarılarının yerine geçmez; uyarılar kaynağıyla gösterilir.

## Başarı ölçütleri (taslak)
| Ölçüt | Faz 1 | Faz 2 |
|---|---|---|
| Sıcaklık MAE (24 saat, pilot istasyonlar) | Raporlanır | Kıyas sağlayıcıyla eşit ya da iyi |
| Rakip kıyası (gömülü uygulamalar dahil) | Dolaylı kıyas (yöntem C) | Bağımsız ölçüm (yöntem A) başlatıldı |
| Tahmin kararlılığı | Raporlanır | Hedef yazılır |
| D7 tutunma | Ölçülür | ≥ %25 |
| Widget ekleyen kullanıcı oranı | Ölçülür | ≥ %30 |
| Mağaza puanı | — | ≥ 4,5 |
