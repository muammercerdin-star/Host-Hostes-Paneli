from pathlib import Path
from datetime import datetime
import hashlib
import difflib
import re

ROOT = Path(".").resolve()
WEB = ROOT
ANDROID = ROOT / "android_app/app/src/main/python"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_functional_diff_{STAMP}.md"

TARGET_FUNCS = [
    "trip_start",
    "continue_trip",
    "api_walkon",
    "api_standing",
    "api_standing_list",
    "api_stats",
    "api_stoplog",
    "trip_report_page",
    "api_trip_report",
    "latest_trip_report_redirect",
    "report_archive_page",
    "end_trip",
]

TARGET_HTML_KEYS = [
    "seatModal",
    "btnSave",
    "save",
    "modal",
    "standing",
    "walkon",
    "pillTotal",
    "routeSheet",
    "tripGuard",
    "unified-seat-deck-report-style",
    "manual-ticket-system",
    "seat-simple-ui-pack",
    "mobile-performance-fix",
]

FILES = [
    "app.py",
    "templates/seats.html",
    "templates/index.html",
    "templates/trip_report.html",
    "templates/report_archive.html",
    "templates/settings.html",
]

def read(p):
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def sha_text(t):
    return hashlib.sha256(t.encode("utf-8", errors="ignore")).hexdigest()[:12]

def normalize_py(t):
    out = []
    for line in t.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        out.append(re.sub(r"\s+", " ", s))
    return "\n".join(out)

def normalize_html(t):
    out = []
    for line in t.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("<!--"):
            continue
        out.append(re.sub(r"\s+", " ", s))
    return "\n".join(out)

def extract_func(txt, func):
    lines = txt.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^\s*def\s+{re.escape(func)}\s*\(", line):
            start = i
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^\s*def\s+\w+\s*\(", lines[j]) or re.match(r"^\s*@app\.route", lines[j]):
            end = j
            break

    route_start = start
    for k in range(start - 1, max(-1, start - 8), -1):
        if "@app.route" in lines[k]:
            route_start = k
        elif lines[k].strip() and not lines[k].lstrip().startswith("@"):
            break

    return "\n".join(lines[route_start:end])

def table(headers, rows):
    if not rows:
        return "_Kayıt yok._"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        out.append("| " + " | ".join(str(x).replace("|", "\\|").replace("\n", " ") for x in r) + " |")
    return "\n".join(out)

def diff_text(a, b, an, bn, max_lines=180):
    d = list(difflib.unified_diff(
        a.splitlines(),
        b.splitlines(),
        fromfile=an,
        tofile=bn,
        lineterm="",
        n=4
    ))
    if len(d) > max_lines:
        d = d[:max_lines] + [f"... DIFF KESİLDİ toplam diff satırı: {len(d)}"]
    return "\n".join(d)

def grep_keys(txt, keys):
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in keys):
            s = line.strip()
            if len(s) > 180:
                s = s[:180] + "..."
            rows.append((i, s))
    return rows

# 1) File normalized comparison
file_rows = []
file_diffs = []
for r in FILES:
    wt = read(WEB / r)
    at = read(ANDROID / r)

    if r.endswith(".py"):
        wn = normalize_py(wt)
        an = normalize_py(at)
    else:
        wn = normalize_html(wt)
        an = normalize_html(at)

    same_raw = sha_text(wt) == sha_text(at)
    same_norm = sha_text(wn) == sha_text(an)

    file_rows.append((
        r,
        "AYNI" if same_raw else "FARKLI",
        "AYNI" if same_norm else "FARKLI",
        len(wt.splitlines()),
        len(at.splitlines()),
        sha_text(wt),
        sha_text(at),
        sha_text(wn),
        sha_text(an),
    ))

    if not same_norm:
        d = diff_text(wn, an, f"WEB normalized {r}", f"ANDROID normalized {r}", 220)
        if d:
            file_diffs.append((r, d))

# 2) App function comparison
app_web = read(WEB / "app.py")
app_and = read(ANDROID / "app.py")
func_rows = []
func_diffs = []

for fn in TARGET_FUNCS:
    wb = extract_func(app_web, fn)
    ab = extract_func(app_and, fn)
    wn = normalize_py(wb)
    an = normalize_py(ab)

    status_raw = "AYNI" if sha_text(wb) == sha_text(ab) else "FARKLI"
    status_norm = "AYNI" if sha_text(wn) == sha_text(an) else "FARKLI"

    func_rows.append((
        fn,
        "VAR" if wb else "YOK",
        "VAR" if ab else "YOK",
        status_raw,
        status_norm,
        len(wb.splitlines()) if wb else 0,
        len(ab.splitlines()) if ab else 0,
        sha_text(wn),
        sha_text(an),
    ))

    if wb and ab and status_norm == "FARKLI":
        d = diff_text(wn, an, f"WEB app.py::{fn}", f"ANDROID app.py::{fn}", 180)
        func_diffs.append((fn, d))

# 3) Routes
ROUTE_RE = re.compile(r"""@\s*(?:\w+\.)?route\(\s*['"]([^'"]+)['"]""")
def routes(txt):
    found = []
    lines = txt.splitlines()
    for i, line in enumerate(lines):
        m = ROUTE_RE.search(line)
        if m:
            fn = ""
            for j in range(i+1, min(i+8, len(lines))):
                dm = re.search(r"^\s*def\s+(\w+)\s*\(", lines[j])
                if dm:
                    fn = dm.group(1)
                    break
            found.append((m.group(1), fn))
    return found

wr = set(routes(app_web))
ar = set(routes(app_and))

# 4) Seats html key grep
seats_web = read(WEB / "templates/seats.html")
seats_and = read(ANDROID / "templates/seats.html")
index_web = read(WEB / "templates/index.html")
index_and = read(ANDROID / "templates/index.html")

# 5) Asset links in seats.html
ASSET_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
def assets(txt):
    return [m.group(1) for m in ASSET_RE.finditer(txt) if "/static/" in m.group(1)]

wa = assets(seats_web)
aa = assets(seats_and)
asset_rows = []
for x in sorted(set(wa) | set(aa)):
    asset_rows.append((x, "VAR" if x in wa else "-", "VAR" if x in aa else "-"))

md = []
md.append("# Muavin Asistanı Fonksiyonel Fark Raporu V5")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("")
md.append("## 1) Dosya Bazlı Ham / Normalize Karşılaştırma")
md.append("")
md.append("Normalize karşılaştırma boş satır ve yorum farklarını ayıklar. Ham farklı ama normalize aynıysa çoğu zaman fonksiyonel fark yoktur.")
md.append("")
md.append(table(
    ["Dosya", "Ham", "Normalize", "WEB satır", "ANDROID satır", "WEB hash", "ANDROID hash", "WEB norm", "ANDROID norm"],
    file_rows
))
md.append("")
md.append("## 2) app.py Kritik Fonksiyon Karşılaştırması")
md.append(table(
    ["Fonksiyon", "WEB", "ANDROID", "Ham", "Normalize", "WEB satır", "ANDROID satır", "WEB norm", "ANDROID norm"],
    func_rows
))
md.append("")
md.append("## 3) Route Farkları")
md.append("")
md.append("### WEB'de var ANDROID'de yok")
md.append(table(["Route", "Fonksiyon"], sorted(wr - ar)))
md.append("")
md.append("### ANDROID'de var WEB'de yok")
md.append(table(["Route", "Fonksiyon"], sorted(ar - wr)))
md.append("")
md.append("## 4) seats.html Static Link Karşılaştırması")
md.append(table(["Static link", "WEB", "ANDROID"], asset_rows))
md.append("")
md.append("## 5) seats.html Kritik Kelime Satırları")
md.append("")
md.append("### WEB templates/seats.html")
md.append(table(["Satır", "İçerik"], grep_keys(seats_web, TARGET_HTML_KEYS)))
md.append("")
md.append("### ANDROID templates/seats.html")
md.append(table(["Satır", "İçerik"], grep_keys(seats_and, TARGET_HTML_KEYS)))
md.append("")
md.append("## 6) index.html Kritik Kelime Satırları")
md.append("")
md.append("### WEB templates/index.html")
md.append(table(["Satır", "İçerik"], grep_keys(index_web, TARGET_HTML_KEYS)))
md.append("")
md.append("### ANDROID templates/index.html")
md.append(table(["Satır", "İçerik"], grep_keys(index_and, TARGET_HTML_KEYS)))
md.append("")
md.append("## 7) app.py Fonksiyonel Diff")
if not func_diffs:
    md.append("_Kritik app.py fonksiyonlarında normalize edilmiş fonksiyonel diff yok._")
else:
    for fn, d in func_diffs:
        md.append(f"### {fn}")
        md.append("```diff")
        md.append(d)
        md.append("```")
        md.append("")
md.append("")
md.append("## 8) Dosya Normalize Diff")
if not file_diffs:
    md.append("_Normalize dosya diff yok._")
else:
    for r, d in file_diffs:
        md.append(f"### {r}")
        md.append("```diff")
        md.append(d)
        md.append("```")
        md.append("")
md.append("")
md.append("## 9) Karar Notu")
md.append("""
Bu rapor sadece tespit içindir. Hiçbir dosya değiştirilmedi.

Okuma mantığı:
- `app.py` kritik fonksiyonları normalize AYNI çıkarsa, kayıt API tarafında web/android farkı yoktur.
- `seats.js` zaten WEB/ANDROID AYNI çıktı. Bu yüzden koltuk modal kayıt sorunu büyük ihtimalle dosya senkron farkından değil; olay sırası, tarayıcı cache, modal kapanma/submit çakışması veya API cevabı yönetiminden olabilir.
- `templates/seats.html` farkı sadece CSS/link ise işlevsel değil görsel kabul edilir.
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Fonksiyonel fark raporu hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for r in file_rows:
    print(r[0], "Ham:", r[1], "Normalize:", r[2])
print()
print("Kritik app fonksiyonları:")
for r in func_rows:
    print(r[0], "Ham:", r[3], "Normalize:", r[4])
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
