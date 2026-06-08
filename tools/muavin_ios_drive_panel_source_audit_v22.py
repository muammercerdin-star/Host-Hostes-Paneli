from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_ios_drive_panel_source_audit_v22_{TS}.md"

FILES = []

for base in [
    ROOT / "templates",
    ROOT / "static/seats",
    ROOT / "android_app/app/src/main/python/templates",
    ROOT / "android_app/app/src/main/python/static/seats",
]:
    if base.exists():
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in [".html", ".css", ".js"]:
                FILES.append(p)

VISIBLE_KEYS = [
    "sade koltuk moduna dön",
    "Sessiz",
    "Normal",
    "Sürüş",
    "driveModeToggle",
    "driveSpeedChip",
    "driveEtaChip",
    "driveEtaMain",
    "driveEtaSub",
    "Seçili durak",
    "selected-stop",
    "selectedStop",
    "Sesli Komut",
    "btnDeckAI",
    "btnDeckAIDrive",
    "voice",
    "Durak Akışı",
    "route-flow",
    "route-strip",
    "route-stop",
    "Canlı",
    "Sıradaki",
    "legend",
    "mini-chip",
    "Boş",
    "Bay",
    "Bayan",
    "Bagaj",
    "İniş",
    "Servis",
    "seat-simple",
    "drive-mode",
    "board-head",
    "board-head-right",
    "board-title",
    "board-stage",
]

STYLE_KEYS = [
    "drive-mode-actions-independent",
    "drive-mode-force-toggle",
    "drive-voice",
    "drive-speed",
    "drive-eta",
    "selected-stop-chip",
    "route-strip",
    "route-live",
    "legend",
    "mini-chip",
    "voice-command-btn",
    "board-head",
    "board-head-right",
    "seat-simple-bottom-bar",
    "bottom:",
    "position:fixed",
    "z-index",
    "grid-template",
    "border-radius",
    "backdrop-filter",
    "box-shadow",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def rel(p):
    return str(p.relative_to(ROOT))

def esc(s):
    s = s.replace("|", "\\|").replace("`", "'")
    if len(s) > 260:
        s = s[:260] + "..."
    return s

def hits(p, keys):
    arr = read(p).splitlines()
    out = []
    for i, line in enumerate(arr, 1):
        low = line.lower()
        for k in keys:
            if k.lower() in low:
                out.append((i, k, line.rstrip()))
                break
    return out

def around_first(p, keyword, before=10, after=28):
    arr = read(p).splitlines()
    lowkey = keyword.lower()
    for i, line in enumerate(arr, 1):
        if lowkey in line.lower():
            a = max(1, i - before)
            b = min(len(arr), i + after)
            return [(n, arr[n-1]) for n in range(a, b + 1)]
    return []

md = []
md.append("# Muavin iOS Tarzı Sürüş Paneli Kaynak Audit V22")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez.")
md.append("- Amaç: Üst sürüş paneli, sesli komut, durak akışı ve alt legend hangi dosyadan geliyor bulmak.")
md.append("")

md.append("## 1) Aktif seats.html yapı haritası")
for p in [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]:
    if not p.exists():
        continue

    md.append("")
    md.append(f"### `{rel(p)}`")
    md.append("")
    md.append("| Satır | İçerik |")
    md.append("| ---: | --- |")

    for i, line in enumerate(read(p).splitlines(), 1):
        if (
            "<link" in line
            or "<script" in line
            or "{% include" in line
            or "drive-mode" in line
            or "driveMode" in line
            or "Sesli Komut" in line
            or "Seçili durak" in line
            or "Durak Akışı" in line
            or "legend" in line
            or "mini-chip" in line
        ):
            md.append(f"| {i} | `{esc(line.strip())}` |")

md.append("")
md.append("## 2) Görünen ekran elemanlarının kaynak izleri")
for p in FILES:
    h = hits(p, VISIBLE_KEYS)
    if not h:
        continue

    md.append("")
    md.append(f"### `{rel(p)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")

    for ln, k, line in h[:180]:
        md.append(f"| {ln} | `{esc(k)}` | `{esc(line)}` |")

md.append("")
md.append("## 3) Tasarımı etkileyen CSS/JS izleri")
for p in FILES:
    h = hits(p, STYLE_KEYS)
    if not h:
        continue

    if not any(x in rel(p) for x in ["seats.html", "seats.css", "seats-final.css", "patches", "drive-controls", "voice"]):
        continue

    md.append("")
    md.append(f"### `{rel(p)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")

    for ln, k, line in h[:220]:
        md.append(f"| {ln} | `{esc(k)}` | `{esc(line)}` |")

md.append("")
md.append("## 4) Kritik blok çevreleri")

critical = [
    ("templates/seats.html", "drive-mode-actions-independent-style"),
    ("templates/seats.html", "drive-mode-actions-independent-js"),
    ("templates/seats.html", "drive-mode-force-toggle-js"),
    ("templates/seats.html", "seat-simple-bottom-bar-script"),
    ("templates/seats_parts/route_flow.html", "Durak"),
    ("templates/seats_parts/topbar.html", "driveModeToggle"),
    ("templates/seats_parts/deck.html", "legend"),
    ("static/seats/seats-final.css", "DRIVE MODE LEGEND"),
    ("static/seats/seats.css", "SÜRÜŞ / HIZ"),
    ("static/seats/seats.css", "SÜRÜŞ MODU ALT"),
]

for relpath, key in critical:
    p = ROOT / relpath
    sec = around_first(p, key)
    md.append("")
    md.append(f"### `{relpath}` / `{key}`")
    md.append("")
    if not sec:
        md.append("_Bulunamadı._")
        continue
    md.append("| Satır | İçerik |")
    md.append("| ---: | --- |")
    for ln, line in sec:
        md.append(f"| {ln} | `{esc(line)}` |")

md.append("")
md.append("## 5) Patron ilk karar notu")
md.append("")
md.append("- Bu ekran iOS tarzına çevrilecekse çekirdek mantığa dokunmadan, sadece görünüm ve yerleşim katmanı yapılmalı.")
md.append("- Öncelik: üstte tek cam sefer kapsülü, ortada tek sesli komut aksiyonu, durak akışında sade timeline, altta temiz legend/toolbar.")
md.append("- Mevcut fonksiyonlar korunmalı: sürüş/normal geçişi, sessiz/sesli durum, hız/ETA, seçili durak, sesli komut, durak akışı.")
md.append("- Uygulama aşamasında öneri: `ios-drive-panel-v1.css` ve gerekirse küçük `ios-drive-panel-v1.js` yaması. Ana dosyaları parça parça bozmayacağız.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ iOS sürüş paneli kaynak raporu hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,420p' {OUT}")
