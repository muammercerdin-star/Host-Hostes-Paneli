from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_top_action_buttons_audit_v29_{TS}.md"

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

KEYS = [
    "driveModeActionsDock",
    "dma-btn",
    "dmaAiBtn",
    "dmaEndBtn",
    "Ana Sayfa",
    "Hesap",
    "Emanet",
    "AI Console",
    "Seferi Bitir",
    "url_for('index')",
    "url_for('hesap_page')",
    "url_for('consignments_page')",
    "openFinishTripModal",
    "display:none",
    "display: none",
    "visibility:hidden",
    "opacity:0",
    "height:0",
    "overflow:hidden",
    "ios-drive",
    "compact",
    "topbar",
    "route-summary",
    "top-action",
    "quick",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def rel(p):
    return str(p.relative_to(ROOT))

def esc(s):
    s = s.replace("|", "\\|").replace("`", "'")
    if len(s) > 270:
        s = s[:270] + "..."
    return s

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
md.append("# Muavin Üst Ana Sayfa / Hesap Butonları Audit V29")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir, dosya değiştirmez.")
md.append("- Amaç: Ana sayfa / hesap / emanet / AI / bitir butonları silindi mi, gizlendi mi, hangi CSS etkiliyor bulmak.")
md.append("")

md.append("## 1) Aktif CSS / JS linkleri")
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
        if "<link" in line or "<script" in line or "driveModeActionsDock" in line or "dma-btn" in line:
            md.append(f"| {i} | `{esc(line.strip())}` |")

md.append("")
md.append("## 2) Buton kaynak izleri")
for p in FILES:
    h = hits(p)
    if not h:
        continue
    md.append("")
    md.append(f"### `{rel(p)}`")
    md.append("")
    md.append("| Satır | Anahtar | İçerik |")
    md.append("| ---: | --- | --- |")
    for ln, k, line in h[:240]:
        md.append(f"| {ln} | `{esc(k)}` | `{esc(line)}` |")

md.append("")
md.append("## 3) İlk teknik yorum")
md.append("")
md.append("- `driveModeActionsDock` varsa butonlar silinmemiştir.")
md.append("- `display:none` veya sadece `body.drive-mode` şartına bağlandıysa normal görünümde kaybolur.")
md.append("- V24/V27/V28 gibi kompakt tasarım yamaları üst kartı sıkıştırırken bu dock satırını gizlemiş olabilir.")
md.append("- Çözüm büyük ihtimalle HTML değil, küçük CSS/JS görünürlük düzeltmesidir.")

OUT.write_text("\\n".join(md), encoding="utf-8")

print("✅ Üst aksiyon butonları raporu hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,420p' {OUT}")
