# ADR-0008: Önce Android, iOS Faz 2

- **Durum:** Accepted
- **Tarih:** 2026-11-08
- **Karar verenler:** Âkif (ürün sahibi), Claude
- **İlgili:** ADR-0004

## Bağlam
Geliştirme makinesi Windows (WSL2). iOS derleme, imzalama ve özellikle SwiftUI widget geliştirme pratikte Mac gerektiriyor. Türkiye'de Android payı yüksek.

## Karar
Faz 1 yalnız Android (Flutter + Glance widget), tamamen Windows'ta. iOS ve SwiftUI widget Faz 2'de, Mac edinildikten sonra. Bulut derleme (Codemagic, GitHub Actions macOS) yalnız yedek.

## Sonuçlar
- **Olumlu:** Mac beklemeden başlanır; ilk kullanıcı geri bildirimi erken.
- **Olumsuz:** iOS kullanıcıları lansmanı bekler.
- **Geri dönüş maliyeti:** düşük.

## Doğrulama
Faz 1 checkpoint'i Mac olmadan geçilebiliyor.
