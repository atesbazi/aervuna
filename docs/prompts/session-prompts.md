# Oturum ve Faz Promptları

Kullanım: Claude Code'da repo kökünde aç. Kısa yol: `.claude/commands/` altındaki `/oturum`, `/kapanis`, `/checkpoint`, `/adr`, `/story`.

---

## İlk oturum (bir kez)
```
Bu repo Aervuna hava durumu uygulamasının tek doğruluk kaynağı. Sırasıyla oku:
docs/AGENTS.md, CLAUDE.md, docs/README.md, docs/progress.md, docs/plan.md,
docs/adr/README.md ve tüm ADR'ler, docs/research/ altındaki tüm dosyalar, docs/architecture/.
Sonra:
- Projeyi 5 maddede özetle.
- Çelişkili ya da belirsiz gördüğün en fazla 5 noktayı önerinle listele.
- Belirsizlikleri kendin karara bağla ve Kararlar'a yaz; kod yazmaya Faz 0 promptuyla başla.
```

## Her oturum
```
/oturum
```
(ya da: "CLAUDE.md oturum ritüelini uygula ve oturum planını sun.")

## Faz 0
```
Faz 0'a başla. Kapsam ve kabul kriterleri docs/plan.md "Faz 0", story'ler WX-010…017.
Sıra: WX-010 → WX-011 → WX-017 → WX-012 → WX-013 → WX-014 → WX-018. WX-016 Open-Meteo ticari anahtarı gelince. CI yok (WX-015 ertelendi).
Kurallar: ECMWF verisi CC-BY atfıyla; METAR'da dakikada 100 istek sınırı ve özel User-Agent;
her story sonunda progress.md. Faz sonunda checkpoint raporu ver ve dur.
```

## Faz 1
```
Faz 0 onaylandı. Faz 1'e başla: docs/plan.md "Faz 1", PR dilimleri 1A…1G, story'ler WX-020…057.
Önce 1A başında grid kararını ver ve ADR olarak yaz (H3 / sabit ızgara).
Her PR dilimi ayrı dal: phase-1/a-api-core, phase-1/b-verification, … Checkpoint 1G sonunda.
```

## Checkpoint incelemesi (ürün sahibi için)
```
/checkpoint
```
Rapor `progress.md` → Checkpoint raporları altında. Uygunsa: "Faz N onaylandı".

## Zamanlanmış oturum (birincil çalışma biçimi)
Claude'da "Aervuna — geliştirme oturumu" adlı scheduled task; saati yok, Âkif elle çalıştırır. Prompt'u task ayarlarında. Özet:
```
atesbazi/aervuna reposunda CLAUDE.md → Oturum ritüeli ve Zamanlanmış oturum modunu uygula.
Aktif fazın sıradaki story'lerini yap, yerel testleri çalıştır, commit + push et, progress.md'yi güncelle.
Açık soruları sorma; en doğru yolu seç ve Kararlar'a yaz. Faz bittiyse checkpoint yaz ve dur.
```
