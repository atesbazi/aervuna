# 06 — Güvenlik ve Gizlilik

## Konum verisi (KVKK)
- İstemci koordinatı yalnız HTTPS ile API'ye gelir; API ilk adımda grid hücresine indirger.
- Ham koordinat loglanmaz, saklanmaz, üçüncü tarafa iletilmez. Sağlayıcıya hücre merkezi gönderilir.
- Kayıtlı yerler cihazda tutulur (Faz 1). Hesap sistemi Faz 1'de yok.
- Crash raporlamada konum, IP ve cihaz tanımlayıcısı kapalı.
- Aydınlatma metni ve gizlilik politikası Faz 1G'de; uygulama içinden erişilir.

## Gizli bilgiler
- Sağlayıcı anahtarları yalnız API sunucusunda, ortam değişkeninde. İstemciye gömülmez.
- `.env` commit'lenmez; `.env.example` güncel.
- WeatherKit kullanılırsa JWT sunucuda imzalanır, istemciye kısa ömürlü token verilir (Faz 2).

## API
- Oran sınırlama (IP + cihaz başına), istek boyutu sınırı, zaman aşımı her dış çağrıda.
- Hata yanıtında iç ayrıntı yok; `requestId` ile log eşleşmesi.

## Mağaza gereksinimleri
- Play: Data safety formu konum işleme ile tutarlı.
- Apple (Faz 2): Privacy manifest; WeatherKit EULA uyarı metni (Attachment 8, 2.2).
- Uygulama acil durum/hayat kurtarma amaçlı olarak pazarlanmaz (Attachment 8, 1.3; genel sorumluluk).
