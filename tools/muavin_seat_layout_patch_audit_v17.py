from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_seat_layout_patch_audit_v17_{TS}.md"

FILES = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
    ROOT / "static/seats/seats.css",
    ROOT / "android_app/app/src/main/python/static/seats/seats.css",
    ROOT / "static/seats/seats-final.css",
    ROOT / "android_app/app/src/main/python/static/seats/seats-final.css",
]

PATCH_DIRS = [
    ROOT / "static/seats/patches",
    ROOT / "android_app/app/src/main/python/static/seats/patches",
]

KEYS = [
    "seat-layout",
    "right-seat-column",
    "bottom-row",
    "only-54",
    "51-54",
    "51",
    "54",
    "43",
    "49",
    "grid-row",
    "grid-column",
    "right-seat-column-shift",
    "translateX",
    "corr",
    "koridor",
    "KORİDOR",
    "KAPI",
    "deck",
    "cell",
    "label",
    "seat-smaller",
    "ghost",
    "unified-seat",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def active_links(tpl):
    s = read(tpl)
    out = []
    for i, line in enumerate(s.splitlines(), 1):
        if "static/seats/patches" in line or "seats-final.css" in line or "seats.css" in line:
            out.append((i, line.strip()))
    return out

def hits(p):
    arr = read(p).splitlines()
    out = []
    for i, line in enumerate(arr, 1):
        low = line.lower()
        for k in KEYS:
            if k.lower() in low:
                out.append((i, k, line.rstrip()))
                break
    return out

def around(p, pattern, before=12, after=35):
    arr = read(p).splitlines()
    for i, line in enumerate(arr, 1):
        if pattern.lower() in line.lower():
            a = max(1, i-before)
            b = min(len(arr), i+after)
            return [(n, arr[n-1]) for n in range(a,b+1)]
    return []

md = []
md.append("# Muavin Koltuk Yerleşimi Yama Audit V17")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir, dosya değiştirmez.")
md.append("")

md.append("## 1) Aktif CSS / JS Linkleri")
for tpl in [ROOT / "templates/seats.html", ROOT / "android_app/app/src/main/python/templates/seats.html"]:
    md.append("")
    md.append(f"### `{tpl.relative_to(ROOT)}`")
    md.append("")
    md.append("| Satır | Link |")
    md.append("| ---: | --- |")
    for ln, line in active_links(tpl):
        md.append(f"| {ln} | `{line.replace('|','\\|')}` |")

md.append("")
md.append("## 2) Fiziksel Patch Dosyaları")
for d in PATCH_DIRS:
    md.append("")
    md.append(f"### `{d.relative_to(ROOT)}`")
    md.append("")
    if not d.exists():
        md.append("_Yok._")
        continue
    for p in sorted(d.glob("*")):
        if p.is_file():
            mark = ""
            name = p.name.lower()
            if any(x in name for x in ["seat", "row", "54", "right", "layout", "deck", "ghost", "unified"]):
                mark = "  ⭐"
            md.append(f"- `{p.name}`{mark}")

md.append("")
md.append("## 3) Koltuk Yerleşimiyle İlgili Satırlar")
scan_files = FILES[:]
for d in PATCH_DIRS:
    if d.exists():
        scan_files += sorted([p for p in d.glob("*") if p.is_file() and p.suffix in [".css", ".js"]])

for p in scan_files:
    if not p.exists():
        continue
    h = hits(p)
    if not h:
        continue

    md.append("")
    md.append(f"### `{p.relative_to(ROOT)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")
    for ln, k, line in h[:220]:
        c = line.replace("|", "\\|")
        if len(c) > 230:
            c = c[:230] + "..."
        md.append(f"| {ln} | `{k}` | `{c}` |")

for title, rel, pattern in [
    ("seat-layout-fab-pack kritik bölge", "static/seats/patches/seat-layout-fab-pack.css", "RIGHT_SEAT_COLUMN"),
    ("51-54 / alt sıra bölgesi", "static/seats/patches/seat-layout-fab-pack.css", "51"),
    ("right-seat-column dosyası", "static/seats/patches/right-seat-column-spacing-fix.css", "right"),
    ("bottom-row dosyası", "static/seats/patches/bottom-row-51-54-equal-spacing.css", "51"),
    ("only-54 dosyası", "static/seats/patches/only-54-reapply-right-shift.css", "54"),
    ("unified seat deck", "static/seats/patches/unified-seat-deck-report-style.css", "seat"),
    ("seat label ghost", "static/seats/patches/seat-label-ghost-clean.css", "label"),
]:
    p = ROOT / rel
    md.append("")
    md.append(f"## 4) {title}")
    md.append("")
    sec = around(p, pattern)
    if not sec:
        md.append("_Bulunamadı veya dosya aktif değil._")
    else:
        md.append("| Satır | İçerik |")
        md.append("| ---: | --- |")
        for ln, line in sec:
            c = line.replace("|", "\\|")
            if len(c) > 260:
                c = c[:260] + "..."
            md.append(f"| {ln} | `{c}` |")

md.append("")
md.append("## 5) İlk Yorum")
md.append("")
md.append("- Koltuk aralığı, koridor, 51-54 hizası, sağ sütun kayması gibi işler büyük ihtimalle `seat-layout-fab-pack.css` ve eski yetim patch dosyaları içinde.")
md.append("- Aktif linkte olmayan dosya varsa, fiziksel dosya duruyor ama sayfaya uygulanmıyor demektir.")
md.append("- Özellikle `right-seat-column-spacing-fix.css`, `bottom-row-51-54-equal-spacing.css`, `only-54-reapply-right-shift.css` daha önce yetim görünmüştü; tekrar kontrol edilmeli.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Koltuk yerleşimi yama raporu hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,320p' {OUT}")
