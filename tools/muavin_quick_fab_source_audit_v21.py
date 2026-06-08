from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_quick_fab_source_audit_v21_{TS}.md"

FILES = []

for base in [
    ROOT / "templates",
    ROOT / "static",
    ROOT / "android_app/app/src/main/python/templates",
    ROOT / "android_app/app/src/main/python/static",
]:
    if base.exists():
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in [".html", ".css", ".js"]:
                FILES.append(p)

KEYS = [
    "fab-column",
    "fab-left-gap-moved",
    "class=\"fab",
    "class='fab",
    "id=\"fab",
    "id='fab",
    "HIZLI",
    "Hızlı",
    "hızlı",
    "Toplu Giriş",
    "Hızlı Tahsilat",
    "Ayakta Listesi",
    "fabBulk",
    "fabCash",
    "fabStanding",
    "openStandingModalBtn",
    "seat-layout-fab-pack",
    "FAB_LEFT_GAP_MOVE",
    "querySelector(\".fab-column",
    "querySelector('.fab-column",
    "classList.add(\"fab-left-gap-moved",
    "classList.add('fab-left-gap-moved",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def rel(p):
    return str(p.relative_to(ROOT))

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

md = []
md.append("# Muavin Hızlı İşlem FAB Kaynak Audit V21")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez.")
md.append("")

md.append("## 1) Aktif seats.html link/include kontrolü")
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
            "{% include" in line
            or "seat-layout-fab-pack" in line
            or "fab" in line.lower()
            or "quick" in line.lower()
            or "hızlı" in line.lower()
            or "Hızlı" in line
        ):
            c = line.replace("|", "\\|")
            if len(c) > 240:
                c = c[:240] + "..."
            md.append(f"| {i} | `{c}` |")

md.append("")
md.append("## 2) FAB / hızlı işlem kaynak izleri")
for p in FILES:
    h = hits(p)
    if not h:
        continue

    md.append("")
    md.append(f"### `{rel(p)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")

    for ln, k, line in h[:220]:
        c = line.replace("|", "\\|")
        if len(c) > 260:
            c = c[:260] + "..."
        md.append(f"| {ln} | `{k}` | `{c}` |")

md.append("")
md.append("## 3) İlk teknik yorum")
md.append("")
md.append("- `fab-column` HTML’de üretiliyorsa asıl kaynak odur.")
md.append("- `seat-layout-fab-pack.js` sadece mevcut `.fab-column` elemanını bulup `fab-left-gap-moved` sınıfı ekliyorsa, butonu o üretmiyor; sadece yerini değiştiriyor demektir.")
md.append("- `seat-layout-fab-pack.css` ise görünüm/konum yamasıdır.")
md.append("- Gizleme veya kaldırma kararı vermeden önce asıl HTML kaynağı ile taşıyan yama ayrılmalı.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Hızlı işlem FAB kaynak raporu hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,360p' {OUT}")
