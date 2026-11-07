# ADR-0002: Veri sağlayıcıları — Open-Meteo ana, Meteoblue kıyas, Google elendi

- **Durum:** Accepted (Faz 0 yazılı teyidine bağlı; teyit olumsuzsa yeni ADR)
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0003, ADR-0007, `research/2026-11-07-data-provider-decision.md`, `research/license-notes.md`, `research/ai-reviews.md`

## Bağlam
Ürünün hedefi mağazadaki uygulamalardan ölçülebilir biçimde daha doğru olmak. Bu, tahminleri **arşivleyip gözlemle karşılaştırmayı** ve uzun vadede **kendi düzeltme katmanımızı** gerektiriyor. Dolayısıyla sağlayıcı seçiminde birinci kriter doğruluk değil, **arşiv, paylaşılan önbellek ve türev ürün hakkı**.

## Değerlendirilen seçenekler
1. **Google Weather API** — Hizmete özel şartlar madde 21.1, verinin asıl amacı hava durumu olan uygulamada kullanımını yasaklıyor. Air Quality API de rota ve risk endeksleriyle sınırlı. **Elendi.**
2. **Apple WeatherKit** — Ucuz (500 bin çağrı/ay üyeliğe dahil), ama Attachment 8 madde 1.2, 1.5, 1.6 ham veriye ücret, türetilmiş veritabanı ve paylaşılan önbelleği kısıtlıyor. Doğrulama arşivi de riskli. **Yalnız gösterim (ADR-0003).**
3. **Meteoblue** — Multi-model + ML (mLM), güçlü doğruluk iddiası; kredi bazlı fiyat ve bazı ürünlerde zorunlu destek paketi. Arşiv/önbellek hakkı yazılı sorulmalı. **Kıyas sağlayıcısı;** hak yazılı verilirse ana kaynağa terfi edebilir.
4. **Open-Meteo ticari** — Veri CC BY 4.0: arşiv, türev ve yeniden dağıtım serbest; sunucu self-host edilebilir; 30+ ulusal model. Ham model çıktısı; nowcasting yok. **Ana kaynak.**
5. **ECMWF açık verisi** — CC-BY-4.0, ticari kullanım serbest; ücretsiz alt küme 25 km. **Doğrulama arşivinin ve Faz 3 düzeltme katmanının temeli.**
6. Tomorrow.io, Rainbow.ai — fiyat kapalı/teklifle; Türkiye radar kapsamı belirsiz. **Yalnız nowcasting saha testi.**

## Karar
Ana kaynak **Open-Meteo ticari**, doğruluk kıyası **Meteoblue**, bağımsız ham model temeli **ECMWF açık verisi**, gözlem **METAR**. Google Weather ve Air Quality API kullanılmaz. Kararın kesinleşmesi Faz 0'da Open-Meteo ve Meteoblue'dan alınacak yazılı yanıtlara bağlıdır.

## Sonuçlar
- **Olumlu:** Lisans engeli olmadan "ölç, sonra seç" ve kendi düzeltme katmanı mümkün. Sağlayıcıdan bağımsızlık (self-host, ECMWF).
- **Olumsuz / kabul edilen riskler:** İlk gün doğruluk üstünlüğü yok (ham model). Nowcasting yok. Open-Meteo fiyatı teklifle.
- **Geri dönüş maliyeti:** düşük — sağlayıcılar `ForecastProvider` trait'inin arkasında (ADR-0005).

## Doğrulama
Faz 0 doğrulama raporu v0; Faz 2'de 60–90 günlük sağlayıcı karşılaştırması ve yeni ADR.
