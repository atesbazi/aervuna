# ADR-0004: Mobil Flutter, widget'lar native

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0008

## Bağlam
Ürünün farkı görsellik (sinematik arka planlar, shader, animasyonlu grafikler) ve iki platform. Geliştirici tek kişi, makine Windows. Ana ekran widget'ı, kilit ekranı ve Live Activity hiçbir çapraz platform aracıyla çizilemiyor: iOS'ta WidgetKit yalnız SwiftUI, Android'de Jetpack Glance (Kotlin).

## Değerlendirilen seçenekler
1. **Flutter + native widget'lar** — Impeller ile iki platformda aynı piksel; `FragmentProgram` shader'ları ve Rive iki platformda çalışır; iOS'a geçiş büyük ölçüde derleme işi. Eksi: widget'lar ayrıca Swift/Kotlin.
2. **Tamamen native (SwiftUI + Compose)** — En iyi platform hissi, widget/Live Activity/Watch doğal. Eksi: iki kat iş; iOS tarafı Mac olmadan başlayamaz.
3. **Kotlin Multiplatform + native UI** — Ortak iş mantığı. Eksi: öğrenme eğrisi; Compose shader desteği (AGSL) Android 13+; iOS yine Mac.
4. **React Native** — Ürün sahibi React biliyor; Android widget JSX ile mümkün. Eksi: özel GPU çizimi Flutter kadar olgun değil; iOS widget yine SwiftUI.

## Karar
**Flutter.** Android widget **Kotlin + Jetpack Glance**, iOS widget **SwiftUI + WidgetKit** (Faz 2). Widget'lar uygulamanın yazdığı tek bir JSON anlık görüntüsünü okur; kendi ağ çağrısı yapmaz (Faz 1'de; gerekirse yeni ADR).

## Sonuçlar
- **Olumlu:** Görsel katman bir kez yazılır; Faz 1 tamamen Windows'ta.
- **Olumsuz:** Üç dil (Dart, Kotlin, Swift) — ama widget kodu küçük.
- **Geri dönüş maliyeti:** yüksek (UI yeniden yazımı); bu yüzden iş mantığı ve veri sözleşmesi API'de tutulur.

## Doğrulama
Faz 1: 60 fps arka plan, soğuk açılış p95 < 2 sn; widget Vitals uyarısı yok.
