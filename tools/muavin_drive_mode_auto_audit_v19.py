from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_drive_mode_auto_audit_v19_{TS}.md"

FILES = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
    ROOT / "static/seats/seats.js",
    ROOT / "android_app/app/src/main/python/static/seats/seats.js",
    ROOT / "static/seats/drive-controls.js",
    ROOT / "android_app/app/src/main/python/static/seats/drive-controls.js",
]

PATCH_DIRS = [
    ROOT / "static/seats/patches",
    ROOT / "android_app/app/src/main/python/static/seats/patches",
]

KEYS = [
    "drive-mode",
    "driveMode",
    "driveModeToggle",
    "drive-mode-force",
    "classList.add",
    "classList.remove",
    "classList.toggle",
    "document.body.classList",
    "document.documentElement.classList",
    "localStorage",
    "sessionStorage",
    "setInterval",
    "setTimeout",
    "requestAnimationFrame",
    "Normal",
    "Sürüş",
    "auto",
    "force",
    "watch",
    "sync",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

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

def section(p, start, end):
    arr = read(p).splitlines()
    return [(i, arr[i-1]) for i in range(max(1,start), min(len(arr),end)+1)]

scan = FILES[:]
for d in PATCH_DIRS:
    if d.exists():
        scan += sorted([p for p in d.glob("*") if p.is_file() and p.suffix in [".js", ".css"]])

md = []
md.append("# Muavin Drive Mode Otomatik Geri Dönme Audit V19")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez.")
md.append("")

md.append("## 1) Drive Mode İzleri")
for p in scan:
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
    for ln, k, line in h[:240]:
        c = line.replace("|", "\\|")
        if len(c) > 260:
            c = c[:260] + "..."
        md.append(f"| {ln} | `{k}` | `{c}` |")

md.append("")
md.append("## 2) Şüpheli Template Blokları")
for rel, ranges in [
    ("templates/seats.html", [(830, 880), (880, 930)]),
    ("android_app/app/src/main/python/templates/seats.html", [(829, 879), (879, 929)]),
]:
    p = ROOT / rel
    if not p.exists():
        continue
    for a,b in ranges:
        md.append("")
        md.append(f"### `{rel}` satır {a}-{b}")
        md.append("")
        md.append("| Satır | İçerik |")
        md.append("| ---: | --- |")
        for ln, line in section(p, a, b):
            c = line.replace("|", "\\|")
            md.append(f"| {ln} | `{c}` |")

md.append("")
md.append("## 3) İlk Teknik Yorum")
md.append("")
md.append("- Eğer `setInterval` veya `setTimeout` içinde `drive-mode` tekrar ekleniyorsa, normal moda geçtikten sonra ekran tekrar sürüş moduna döner.")
md.append("- Eğer `localStorage` içinde eski değer sürüş modu olarak kalıyorsa, sen normal yapsan bile senkron script onu geri basabilir.")
md.append("- Temiz çözüm: Drive mode için tek kaynak bırakmak. Normal butonuna basılınca hem class hem localStorage aynı anda `false` yapılmalı; otomatik script normal tercihini ezmemeli.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Drive mode otomatik geri dönme audit V19 hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,360p' {OUT}")
