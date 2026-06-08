from pathlib import Path
from datetime import datetime
import hashlib
import difflib
import re

ROOT = Path(".").resolve()
WEB = ROOT
ANDROID = ROOT / "android_app/app/src/main/python"
APK = ROOT / "apk_payload"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_target_compare_{STAMP}.md"

TARGETS = [
    "app.py",
    "templates/index.html",
    "templates/seats.html",
    "static/seats/seats.js",
    "static/seats/standing.js",
    "static/seats/bags.js",
    "static/seats/drive-controls.js",
    "static/seats/voice-commands.js",
    "static/seats/voice-tts.js",
    "templates/continue_trip.html",
    "static/continue/continue_trip_core.js",
    "static/continue/continue_trip_ui.js",
    "templates/trip_report.html",
    "templates/report_archive.html",
    "templates/settings.html",
]

def sha(p):
    if not p.exists():
        return "-"
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 256), b""):
            h.update(chunk)
    return h.hexdigest()[:12]

def read(p):
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def lc(p):
    if not p.exists():
        return "-"
    t = read(p)
    return t.count("\n") + 1 if t else 0

def size(p):
    return p.stat().st_size if p.exists() else "-"

def mtime(p):
    if not p.exists():
        return "-"
    return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

def table(headers, rows):
    if not rows:
        return "_Kayıt yok._"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        out.append("| " + " | ".join(str(x).replace("|", "\\|").replace("\n", " ") for x in r) + " |")
    return "\n".join(out)

def diff(a, b, an, bn, max_lines=180):
    if not a.exists() or not b.exists():
        return ""
    aa = read(a).splitlines()
    bb = read(b).splitlines()
    d = list(difflib.unified_diff(aa, bb, fromfile=an, tofile=bn, lineterm="", n=4))
    if len(d) > max_lines:
        d = d[:max_lines] + [f"... DIFF KESİLDİ toplam diff satırı: {len(d)}"]
    return "\n".join(d)

def important_grep(p):
    if not p.exists():
        return []
    txt = read(p)
    keys = [
        "seatModal", "save", "btnSave", "standing", "walkon",
        "fetch(", "/api/standing", "/api/walkon", "/api/stats",
        "tripGuard", "routeSheet", "unified-seat-deck-report-style",
        "CONTINUE_LIVE_FLOW_STATE_API_START",
    ]
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in keys):
            s = line.strip()
            if len(s) > 180:
                s = s[:180] + "..."
            rows.append((i, s))
    return rows[:120]

rows = []
diff_blocks = []
grep_blocks = []

for r in TARGETS:
    wp = WEB / r
    ap = ANDROID / r
    pp = APK / r

    wh, ah, ph = sha(wp), sha(ap), sha(pp)
    status_wa = "AYNI" if wh == ah and wh != "-" else "FARKLI" if wh != "-" and ah != "-" else "EKSİK"
    status_wp = "AYNI" if wh == ph and wh != "-" else "FARKLI" if wh != "-" and ph != "-" else "EKSİK"
    status_ap = "AYNI" if ah == ph and ah != "-" else "FARKLI" if ah != "-" and ph != "-" else "EKSİK"

    rows.append((
        r,
        status_wa,
        wh, ah,
        lc(wp), lc(ap),
        status_wp,
        ph,
        lc(pp),
        mtime(wp),
        mtime(ap),
    ))

    if status_wa == "FARKLI":
        d = diff(wp, ap, f"WEB/{r}", f"ANDROID/{r}", 220)
        if d:
            diff_blocks.append((r, d))

    if r in ["templates/seats.html", "static/seats/seats.js", "app.py", "templates/index.html"]:
        grep_blocks.append((f"WEB/{r}", important_grep(wp)))
        grep_blocks.append((f"ANDROID/{r}", important_grep(ap)))

md = []
md.append("# Muavin Asistanı Hedefli Dosya Karşılaştırma V4")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("")
md.append("## 1) Hedef Dosya Hash Karşılaştırması")
md.append(table(
    ["Dosya", "WEB-ANDROID", "WEB hash", "ANDROID hash", "WEB satır", "ANDROID satır", "WEB-APK", "APK hash", "APK satır", "WEB mtime", "ANDROID mtime"],
    rows
))
md.append("")
md.append("## 2) WEB ↔ ANDROID Diff Blokları")
if not diff_blocks:
    md.append("_WEB ve Android arasında hedef dosyalarda diff yok._")
else:
    for r, d in diff_blocks:
        md.append(f"### {r}")
        md.append("```diff")
        md.append(d)
        md.append("```")
        md.append("")
md.append("")
md.append("## 3) Kritik Kelime Taraması")
for name, gr in grep_blocks:
    md.append(f"### {name}")
    md.append(table(["Satır", "İçerik"], gr))
    md.append("")
md.append("## 4) Karar")
md.append("""
Bu rapor da sadece tespit içindir. Silme/kopyalama yapmadı.

Öncelik:
1. WEB-ANDROID farkı olan dosyalar gerçekten fonksiyonel mi görsel mi ayrılacak.
2. Koltuk modal kaydetme sorunu için `templates/seats.html`, `static/seats/seats.js`, `/api/standing`, `/api/walkon`, `/api/stats` akışı ayrıca incelenecek.
3. APK_PAYLOAD ana kaynak kabul edilmeyecek; eski paket çıktısı gibi duruyor.
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Hedefli karşılaştırma hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for r in rows:
    print(r[0], "WEB-ANDROID:", r[1], "WEB-APK:", r[6])
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
