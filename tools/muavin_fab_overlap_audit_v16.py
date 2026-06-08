from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_fab_overlap_audit_v16_{TS}.md"

FILES = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
    ROOT / "static/seats/seats.css",
    ROOT / "android_app/app/src/main/python/static/seats/seats.css",
    ROOT / "static/seats/seats-final.css",
    ROOT / "android_app/app/src/main/python/static/seats/seats-final.css",
    ROOT / "static/seats/patches/seat-layout-fab-pack.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css",
    ROOT / "static/seats/patches/seat-layout-fab-pack.js",
    ROOT / "android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js",
    ROOT / "static/seats/patches/fab-sheet-solid-fix.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/fab-sheet-solid-fix.css",
    ROOT / "static/seats/patches/seat-simple-ui-pack.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css",
]

KEYS = [
    "fab-column",
    "fab-left",
    "fab-left-gap-moved",
    "seat-layout-fab",
    "quick",
    "hızlı",
    "HIZLI",
    "seat-simple-bottom-bar",
    "board-head-right .legend",
    ".legend",
    "mini-chip",
    "z-index",
    "bottom:",
    "position:fixed",
    "pointer-events",
    "drive-mode",
    "seat-modal-open",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def context_hits(p):
    s = read(p)
    arr = s.splitlines()
    hits = []
    for i, line in enumerate(arr, 1):
        low = line.lower()
        for k in KEYS:
            if k.lower() in low:
                hits.append((i, k, line.rstrip()))
                break
    return hits

def around_first(p, pattern, before=18, after=40):
    arr = read(p).splitlines()
    for i, line in enumerate(arr, 1):
        if pattern.lower() in line.lower():
            a = max(1, i-before)
            b = min(len(arr), i+after)
            return [(n, arr[n-1]) for n in range(a,b+1)]
    return []

md = []
md.append("# Muavin FAB / Hızlı İşlem Çakışma Audit V16")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir, dosya değiştirmez.")
md.append("")
md.append("## 1) Dosya Durumu")
md.append("")
md.append("| Dosya | Var mı | Satır |")
md.append("| --- | --- | ---: |")
for p in FILES:
    rel = p.relative_to(ROOT)
    exists = p.exists()
    line_count = len(read(p).splitlines()) if exists else 0
    md.append(f"| `{rel}` | {'VAR' if exists else 'YOK'} | {line_count} |")

md.append("")
md.append("## 2) FAB / Legend / Bottom Bar İzleri")
for p in FILES:
    if not p.exists():
        continue
    hits = context_hits(p)
    if not hits:
        continue
    md.append("")
    md.append(f"### `{p.relative_to(ROOT)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")
    for ln, key, content in hits[:180]:
        c = content.replace("|", "\\|")
        if len(c) > 220:
            c = c[:220] + "..."
        md.append(f"| {ln} | `{key}` | `{c}` |")

for title, file_rel, pattern in [
    ("WEB fab-column bölgesi", "static/seats/patches/seat-layout-fab-pack.css", "fab-column"),
    ("WEB fab-left-gap bölgesi", "static/seats/patches/seat-layout-fab-pack.css", "fab-left"),
    ("WEB fab solid fix bölgesi", "static/seats/patches/fab-sheet-solid-fix.css", "fab"),
    ("WEB bottom legend bölgesi", "static/seats/seats-final.css", "board-head-right .legend"),
    ("WEB simple bottom bar bölgesi", "static/seats/patches/seat-simple-ui-pack.css", "seat-simple-bottom-bar"),
    ("TEMPLATE fab script bölgesi", "templates/seats.html", "fab"),
]:
    p = ROOT / file_rel
    md.append("")
    md.append(f"## 3) {title}")
    md.append("")
    sec = around_first(p, pattern)
    if not sec:
        md.append("_Bulunamadı._")
    else:
        md.append("| Satır | İçerik |")
        md.append("| ---: | --- |")
        for ln, content in sec:
            c = content.replace("|", "\\|")
            if len(c) > 260:
                c = c[:260] + "..."
            md.append(f"| {ln} | `{c}` |")

md.append("")
md.append("## 4) İlk Teknik Yorum")
md.append("")
md.append("- Sorun büyük ihtimalle hızlı işlem FAB grubunun `position: fixed`, `bottom` veya `z-index` değerinin alt legend bar ile çakışmasından geliyor.")
md.append("- Eğer FAB `bottom` değeri küçük, legend bar ise altta sabitse; kaydırmada FAB legend üstüne biner.")
md.append("- Temiz çözüm genelde şudur: FAB grubuna legend yüksekliği kadar `bottom` boşluğu verilir veya legend görünürken FAB yukarı taşınır.")

OUT.write_text("\\n".join(md), encoding="utf-8")

print("✅ FAB overlap audit V16 hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,280p' {OUT}")
