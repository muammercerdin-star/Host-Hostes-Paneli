from pathlib import Path
import re
from datetime import datetime

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = ROOT / "tools" / "reports" / f"live_stop_source_audit_{STAMP}.txt"

EXTS = {".html", ".js", ".css", ".py", ".java", ".json"}

KEYWORDS = [
    "Canlı Durak",
    "Canli Durak",
    "liveStop",
    "live-stop",
    "live_stop",
    "currentStop",
    "nextStop",
    "selectedStop",
    "activeStop",
    "remainingKm",
    "remaining",
    "kalan",
    "Kalan mesafe",
    "km",
    "durak",
    "Durak",
    "Ortahan",
    "Belenyaka",
    "Alaşehir",
    "Alasehir",
    "OTOGAR",
    "erken",
    "geç",
    "gec",
    "ETA",
    "eta",
]

SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".gradle", "build",
    "dist", ".idea", ".vscode"
}

def iter_files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in EXTS:
            yield p

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def rel(p):
    return str(p.relative_to(ROOT))

def line_hits(text, terms):
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        for t in terms:
            if t.lower() in low:
                hits.append((i, line.rstrip()))
                break
    return hits

def context(lines, idx, before=3, after=5):
    start = max(1, idx - before)
    end = min(len(lines), idx + after)
    return start, end

report = []
report.append("===== MUAVİN CANLI DURAK KAYNAK DENETİMİ =====")
report.append(f"ROOT: {ROOT}")
report.append(f"RAPOR: {OUT}")
report.append("")
report.append("NOT: Bu script sadece okuma/tarama yapar. Kaynak dosyalara yama uygulamaz.")
report.append("")

files = list(iter_files())

# 1) Ana keyword hitleri
report.append("===== 1) CANLI DURAK / KM / DURAK METNİ GEÇEN DOSYALAR =====")
for p in files:
    txt = read(p)
    hits = line_hits(txt, KEYWORDS)
    if hits:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, line in hits[:80]:
            report.append(f"{ln}: {line[:220]}")
        if len(hits) > 80:
            report.append(f"... toplam {len(hits)} hit, ilk 80 gösterildi")

# 2) HTML id/class adayları
report.append("")
report.append("===== 2) HTML ID / CLASS ADAYLARI =====")
html_terms = ["live", "stop", "durak", "km", "eta", "route", "card", "next", "current"]
for p in files:
    if p.suffix.lower() != ".html":
        continue
    txt = read(p)
    candidates = []
    for m in re.finditer(r'\b(id|class)=["\']([^"\']+)["\']', txt, re.I):
        attr, val = m.group(1), m.group(2)
        low = val.lower()
        if any(t in low for t in html_terms):
            line_no = txt[:m.start()].count("\n") + 1
            candidates.append((line_no, attr, val))
    if candidates:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, attr, val in candidates[:120]:
            report.append(f"{ln}: {attr}=\"{val}\"")
        if len(candidates) > 120:
            report.append(f"... toplam {len(candidates)} aday, ilk 120 gösterildi")

# 3) JS fonksiyon adayları
report.append("")
report.append("===== 3) JS FONKSİYON / RENDER ADAYLARI =====")
js_terms = [
    "liveStop", "live-stop", "currentStop", "nextStop", "remainingKm",
    "kalan", "durak", "render", "update", "eta", "km"
]
for p in files:
    if p.suffix.lower() not in {".js", ".html"}:
        continue
    txt = read(p)
    lines = txt.splitlines()
    hits = line_hits(txt, js_terms)
    if not hits:
        continue

    interesting = []
    for ln, line in hits:
        if re.search(r'\bfunction\b|=>|render|update|liveStop|currentStop|nextStop|remainingKm|Kalan mesafe|km', line, re.I):
            interesting.append((ln, line))

    if interesting:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, line in interesting[:120]:
            report.append(f"{ln}: {line[:240]}")
        if len(interesting) > 120:
            report.append(f"... toplam {len(interesting)} aday, ilk 120 gösterildi")

# 4) CSS blok adayları
report.append("")
report.append("===== 4) CSS KART / BORDER / GLOW ADAYLARI =====")
css_terms = [
    "live", "stop", "durak", "card", "border", "box-shadow",
    "glow", "pulse", "animation", "keyframes", "red", "pink"
]
for p in files:
    if p.suffix.lower() not in {".css", ".html"}:
        continue
    txt = read(p)
    hits = []
    for i, line in enumerate(txt.splitlines(), 1):
        low = line.lower()
        if any(t in low for t in css_terms):
            hits.append((i, line.rstrip()))
    if hits:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, line in hits[:140]:
            report.append(f"{ln}: {line[:240]}")
        if len(hits) > 140:
            report.append(f"... toplam {len(hits)} hit, ilk 140 gösterildi")

# 5) Durak listesi / JSON / rota kaynakları
report.append("")
report.append("===== 5) DURAK LİSTESİ / ROTA VERİ KAYNAĞI ADAYLARI =====")
data_terms = [
    "Ortahan", "Belenyaka", "Alaşehir", "Alasehir", "Denizli",
    "İstanbul", "Istanbul", "Vardön", "Vardon", "stops", "route",
    "duraklar", "routes"
]
for p in files:
    if p.suffix.lower() not in {".json", ".js", ".py", ".html"}:
        continue
    txt = read(p)
    hits = line_hits(txt, data_terms)
    if hits:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, line in hits[:100]:
            report.append(f"{ln}: {line[:240]}")
        if len(hits) > 100:
            report.append(f"... toplam {len(hits)} hit, ilk 100 gösterildi")

# 6) Flask/API route adayları
report.append("")
report.append("===== 6) PYTHON FLASK / API ROUTE ADAYLARI =====")
for p in files:
    if p.suffix.lower() != ".py":
        continue
    txt = read(p)
    hits = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "@app.route" in line or "def " in line and any(t in line.lower() for t in ["stop", "durak", "route", "trip", "live"]):
            hits.append((i, line.rstrip()))
    if hits:
        report.append("")
        report.append(f"--- {rel(p)} ---")
        for ln, line in hits[:120]:
            report.append(f"{ln}: {line[:240]}")

# 7) Web / Android kopya karşılaştırma adayları
report.append("")
report.append("===== 7) WEB - ANDROID AYNI İSİMLİ DOSYA KONTROLÜ =====")
pairs = [
    ("templates", "android_app/app/src/main/python/templates"),
    ("static", "android_app/app/src/main/python/static"),
]
for a, b in pairs:
    A = ROOT / a
    B = ROOT / b
    if not A.exists() or not B.exists():
        report.append(f"Eksik klasör: {a} veya {b}")
        continue

    for fp in A.rglob("*"):
        if not fp.is_file() or fp.suffix.lower() not in EXTS:
            continue
        relp = fp.relative_to(A)
        gp = B / relp
        if gp.exists():
            ta = read(fp)
            tb = read(gp)
            if ta == tb:
                state = "AYNI"
            else:
                state = "FARKLI"
            if any(k.lower() in ta.lower() or k.lower() in tb.lower() for k in KEYWORDS):
                report.append(f"{state}: {a}/{relp}  <->  {b}/{relp}")
        else:
            if any(k.lower() in read(fp).lower() for k in KEYWORDS):
                report.append(f"ANDROID KOPYA YOK: {a}/{relp}")

OUT.write_text("\n".join(report), encoding="utf-8")

print("\n".join(report[:260]))
print("")
print("===== RAPOR DOSYASI =====")
print(OUT)
print("")
print("Şimdi şu raporu da görmek için:")
print(f"sed -n '1,260p' {OUT}")
