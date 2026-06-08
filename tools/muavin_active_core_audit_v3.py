from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import hashlib
import difflib
import re
import os

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_active_core_audit_{STAMP}.md"

WEB = ROOT
ANDROID = ROOT / "android_app/app/src/main/python"
APK = ROOT / "apk_payload"

ROOTS = {
    "WEB": WEB,
    "ANDROID": ANDROID,
    "APK_PAYLOAD": APK,
}

TEXT_EXTS = {
    ".py", ".html", ".css", ".js", ".json", ".txt", ".md", ".xml",
    ".gradle", ".properties", ".cfg", ".ini", ".yml", ".yaml", ".toml", ".sh"
}

ASSET_EXTS = {
    ".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico",
    ".json", ".map", ".woff", ".woff2", ".ttf", ".otf", ".mp3", ".wav"
}

BACKUP_RE = re.compile(
    r"(\.bak|backup|backups|old|eski|copy|kopya|tmp|temp|deneme|test|audit|rapor|_unused_review)",
    re.I
)

EXCLUDE_PARTS = {
    ".git", "__pycache__", ".gradle", "build", "dist", "node_modules",
    ".venv", "venv", "reports"
}

def rel_root(p):
    try:
        return str(p.relative_to(ROOT))
    except Exception:
        return str(p)

def is_text(p):
    return p.suffix.lower() in TEXT_EXTS or p.name in {"requirements.txt", "Dockerfile", "Procfile"}

def read(p):
    try:
        if not p.exists() or p.stat().st_size > 5_000_000:
            return ""
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def sha(p):
    try:
        h = hashlib.sha256()
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 256), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""

def lines(p):
    if not is_text(p):
        return ""
    t = read(p)
    if not t:
        return 0
    return t.count("\n") + 1

def skip_rel(r):
    parts = set(Path(r).parts)
    if parts & EXCLUDE_PARTS:
        return True
    if BACKUP_RE.search(r):
        return True
    return False

def wanted_rel(r):
    if skip_rel(r):
        return False
    if r == "app.py":
        return True
    if r == "android_server.py":
        return True
    if r.startswith("templates/"):
        return True
    if r.startswith("static/"):
        return True
    if r in {"requirements.txt"}:
        return True
    return False

def collect_active(base):
    found = {}
    if not base.exists():
        return found

    for p in base.rglob("*"):
        if not p.is_file():
            continue
        try:
            r = str(p.relative_to(base))
        except Exception:
            continue
        if wanted_rel(r):
            found[r] = p
    return found

def info(p):
    if not p or not p.exists():
        return {"exists": False, "sha": "-", "size": "-", "lines": "-", "mtime": "-"}
    return {
        "exists": True,
        "sha": sha(p)[:12],
        "size": p.stat().st_size,
        "lines": lines(p),
        "mtime": datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
    }

def md_table(headers, rows, limit=None):
    if limit is not None:
        rows = rows[:limit]
    if not rows:
        return "_Kayıt yok._"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        rr = list(row)[:len(headers)]
        while len(rr) < len(headers):
            rr.append("")
        safe = [str(x).replace("|", "\\|").replace("\n", " ") for x in rr]
        out.append("| " + " | ".join(safe) + " |")
    return "\n".join(out)

def diff_preview(a, b, name_a, name_b, max_lines=90):
    if not a.exists() or not b.exists() or not is_text(a) or not is_text(b):
        return ""
    aa = read(a).splitlines()
    bb = read(b).splitlines()
    d = list(difflib.unified_diff(
        aa, bb,
        fromfile=name_a,
        tofile=name_b,
        lineterm="",
        n=3
    ))
    if not d:
        return ""
    if len(d) > max_lines:
        d = d[:max_lines] + [f"... diff kesildi, toplam satır: {len(d)}"]
    return "\n".join(d)

active = {name: collect_active(base) for name, base in ROOTS.items()}

all_rels = sorted(set().union(*(set(v.keys()) for v in active.values())))

web_android_diff = []
web_apk_diff = []
android_apk_diff = []
web_only = []
android_only = []
apk_only = []
triple_status_rows = []

for r in all_rels:
    wp = active["WEB"].get(r)
    ap = active["ANDROID"].get(r)
    pp = active["APK_PAYLOAD"].get(r)

    wi, ai, pi = info(wp), info(ap), info(pp)

    triple_status_rows.append((
        r,
        "VAR" if wi["exists"] else "-",
        wi["sha"],
        wi["lines"],
        "VAR" if ai["exists"] else "-",
        ai["sha"],
        ai["lines"],
        "VAR" if pi["exists"] else "-",
        pi["sha"],
        pi["lines"],
    ))

    if wp and ap:
        if sha(wp) != sha(ap):
            web_android_diff.append((r, wi["sha"], ai["sha"], wi["lines"], ai["lines"], wi["mtime"], ai["mtime"]))
    elif wp and not ap:
        web_only.append((r, wi["size"], wi["lines"], wi["mtime"]))
    elif ap and not wp:
        android_only.append((r, ai["size"], ai["lines"], ai["mtime"]))

    if wp and pp and sha(wp) != sha(pp):
        web_apk_diff.append((r, wi["sha"], pi["sha"], wi["lines"], pi["lines"], wi["mtime"], pi["mtime"]))

    if ap and pp and sha(ap) != sha(pp):
        android_apk_diff.append((r, ai["sha"], pi["sha"], ai["lines"], pi["lines"], ai["mtime"], pi["mtime"]))

    if pp and not wp and not ap:
        apk_only.append((r, pi["size"], pi["lines"], pi["mtime"]))

# Route / render map
ROUTE_RE = re.compile(r"""@\s*(?:\w+\.)?route\(\s*['"]([^'"]+)['"]""")
RENDER_RE = re.compile(r"""render_template\(\s*['"]([^'"]+)['"]""")

def parse_routes(app_file):
    txt = read(app_file)
    routes = []
    lines_ = txt.splitlines()
    for i, line in enumerate(lines_):
        m = ROUTE_RE.search(line)
        if m:
            fn = ""
            for j in range(i + 1, min(i + 8, len(lines_))):
                dm = re.search(r"^\s*def\s+(\w+)\s*\(", lines_[j])
                if dm:
                    fn = dm.group(1)
                    break
            routes.append((m.group(1), fn, i + 1))
    return routes

def parse_renders(app_file):
    txt = read(app_file)
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        for m in RENDER_RE.finditer(line):
            rows.append((m.group(1), i))
    return rows

web_routes = parse_routes(WEB / "app.py")
and_routes = parse_routes(ANDROID / "app.py")
web_route_set = {(r, f) for r, f, _ in web_routes}
and_route_set = {(r, f) for r, f, _ in and_routes}

web_render = parse_renders(WEB / "app.py")
and_render = parse_renders(ANDROID / "app.py")
web_render_set = {r for r, _ in web_render}
and_render_set = {r for r, _ in and_render}

# Better static ref scanner
URL_FOR_STATIC_RE = re.compile(r"""url_for\(\s*['"]static['"]\s*,\s*filename\s*=\s*['"]([^'"]+)['"]""")
URL_FOR_ANY_RE = re.compile(r"""url_for\(\s*['"]([^'"]+)['"]""")
ATTR_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.I)

def external(ref):
    ref = ref.strip()
    low = ref.lower()
    return (
        not ref or low.startswith("http://") or low.startswith("https://") or
        low.startswith("//") or low.startswith("data:") or low.startswith("mailto:") or
        low.startswith("tel:") or low.startswith("javascript:") or low.startswith("#")
    )

def clean_ref(ref):
    return ref.strip().split("#")[0].split("?")[0].strip()

def scan_template_static(base):
    missing = []
    refs = []
    endpoints = []
    if not (base / "templates").exists():
        return refs, missing, endpoints

    for html in sorted((base / "templates").rglob("*.html")):
        rhtml = str(html.relative_to(base))
        if skip_rel(rhtml):
            continue
        txt = read(html)

        for m in URL_FOR_STATIC_RE.finditer(txt):
            fn = m.group(1).strip()
            if "{{" in fn or "}}" in fn or "${" in fn:
                continue
            expected = base / "static" / fn
            refs.append((rhtml, "url_for static", "static/" + fn))
            if not expected.exists():
                missing.append((rhtml, "url_for static: " + fn, str(expected.relative_to(base))))

        for m in URL_FOR_ANY_RE.finditer(txt):
            ep = m.group(1)
            if ep != "static":
                endpoints.append((rhtml, ep))

        for m in ATTR_RE.finditer(txt):
            ref = clean_ref(m.group(1))
            if external(ref):
                continue
            if "{{" in ref or "}}" in ref or "${" in ref:
                continue

            static_rel = None
            if ref.startswith("/static/"):
                static_rel = ref.lstrip("/")
            elif ref.startswith("static/"):
                static_rel = ref
            elif ref.startswith("../static/"):
                static_rel = "static/" + ref.split("../static/", 1)[1]
            elif Path(ref).suffix.lower() in ASSET_EXTS and not ref.startswith("/"):
                try:
                    target = (html.parent / ref).resolve()
                    if str(target).startswith(str(base.resolve())):
                        static_rel = str(target.relative_to(base))
                except Exception:
                    static_rel = None

            if static_rel:
                expected = base / static_rel
                refs.append((rhtml, "attr", static_rel))
                if not expected.exists():
                    missing.append((rhtml, ref, static_rel))
    return refs, missing, endpoints

web_refs, web_missing, web_endpoints = scan_template_static(WEB)
and_refs, and_missing, and_endpoints = scan_template_static(ANDROID)

# Duplicate IDs inside same active template
ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)

def duplicate_ids(base):
    rows = []
    if not (base / "templates").exists():
        return rows
    for html in sorted((base / "templates").rglob("*.html")):
        rhtml = str(html.relative_to(base))
        if skip_rel(rhtml):
            continue
        txt = read(html)
        found = defaultdict(list)
        for m in ID_RE.finditer(txt):
            idv = m.group(1)
            line = txt.count("\n", 0, m.start()) + 1
            found[idv].append(line)
        for idv, locs in found.items():
            if len(locs) > 1:
                rows.append((rhtml, idv, len(locs), ", ".join(map(str, locs))))
    return rows

web_dup_ids = duplicate_ids(WEB)
and_dup_ids = duplicate_ids(ANDROID)

# Meaningful JS duplicate names, excluding vendor/minified and tiny helper names
JS_FUNC_DECL = re.compile(r"""^\s*(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(""", re.M)
JS_ARROW = re.compile(r"""^\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:\([^)]*\)|[A-Za-z_$][\w$]*)\s*=>""", re.M)
IGNORE_JS_NAMES = {"e", "t", "n", "i", "j", "r", "s", "d", "q", "el", "btn", "res", "data", "list", "stop", "next", "now", "msg", "map", "text"}

def js_dups(base):
    rows = []
    for js in sorted((base / "static").rglob("*.js")) if (base / "static").exists() else []:
        rjs = str(js.relative_to(base))
        if skip_rel(rjs):
            continue
        if "/vendor/" in rjs.replace("\\", "/") or js.name.endswith(".min.js"):
            continue
        txt = read(js)
        names = JS_FUNC_DECL.findall(txt) + JS_ARROW.findall(txt)
        names = [x for x in names if len(x) > 2 and x not in IGNORE_JS_NAMES]
        c = Counter(names)
        for name, count in c.items():
            if count > 1:
                rows.append((rjs, name, count))
    return rows

web_js_dups = js_dups(WEB)
and_js_dups = js_dups(ANDROID)

# Script/link order in important templates
def asset_order(base, rel_html):
    p = base / rel_html
    txt = read(p)
    rows = []
    if not txt:
        return rows
    for i, line in enumerate(txt.splitlines(), 1):
        if "<script" in line and "src=" in line:
            m = ATTR_RE.search(line)
            rows.append((rel_html, i, "script", clean_ref(m.group(1)) if m else line.strip()[:120]))
        if "<link" in line and "href=" in line:
            m = ATTR_RE.search(line)
            rows.append((rel_html, i, "link", clean_ref(m.group(1)) if m else line.strip()[:120]))
    return rows

important_templates = [
    "templates/index.html",
    "templates/seats.html",
    "templates/continue_trip.html",
    "templates/trip_report.html",
    "templates/report_archive.html",
]

web_asset_order = []
and_asset_order = []
for h in important_templates:
    web_asset_order += asset_order(WEB, h)
    and_asset_order += asset_order(ANDROID, h)

# Diff previews for most important files
priority = [
    "app.py",
    "templates/index.html",
    "templates/seats.html",
    "static/seats/seats.js",
    "templates/continue_trip.html",
    "static/continue/continue_trip_core.js",
    "templates/trip_report.html",
    "templates/report_archive.html",
    "templates/settings.html",
]

diff_blocks = []
for r in priority:
    wp = WEB / r
    ap = ANDROID / r
    if wp.exists() and ap.exists() and sha(wp) != sha(ap):
        prev = diff_preview(wp, ap, f"WEB/{r}", f"ANDROID/{r}", max_lines=100)
        if prev:
            diff_blocks.append((r, prev))

# Report
md = []
md.append("# Muavin Asistanı Canlı Çekirdek Audit V3")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append(f"- Root: `{ROOT}`")
md.append("")
md.append("## 1) Canlı Dosya Sayıları")
md.append(md_table(["Kök", "Canlı aday dosya"], [(k, len(v)) for k, v in active.items()]))
md.append("")
md.append("## 2) Asıl Kırmızı Alarm Özeti")
md.append("")
md.append(f"- WEB ↔ ANDROID farklı canlı dosya: **{len(web_android_diff)}**")
md.append(f"- WEB ↔ APK_PAYLOAD farklı canlı dosya: **{len(web_apk_diff)}**")
md.append(f"- ANDROID ↔ APK_PAYLOAD farklı canlı dosya: **{len(android_apk_diff)}**")
md.append(f"- WEB var ANDROID yok: **{len(web_only)}**")
md.append(f"- ANDROID var WEB yok: **{len(android_only)}**")
md.append(f"- APK_PAYLOAD tek başına var: **{len(apk_only)}**")
md.append(f"- WEB gerçek eksik static/ref: **{len(web_missing)}**")
md.append(f"- ANDROID gerçek eksik static/ref: **{len(and_missing)}**")
md.append(f"- WEB aynı HTML içinde duplicate ID: **{len(web_dup_ids)}**")
md.append(f"- ANDROID aynı HTML içinde duplicate ID: **{len(and_dup_ids)}**")
md.append(f"- WEB anlamlı JS tekrar adayı: **{len(web_js_dups)}**")
md.append(f"- ANDROID anlamlı JS tekrar adayı: **{len(and_js_dups)}**")
md.append("")
md.append("## 3) WEB ↔ ANDROID Farklı Canlı Dosyalar")
md.append(md_table(["Dosya", "WEB hash", "ANDROID hash", "WEB satır", "ANDROID satır", "WEB mtime", "ANDROID mtime"], web_android_diff, 200))
md.append("")
md.append("## 4) WEB ↔ APK_PAYLOAD Farklı Canlı Dosyalar")
md.append(md_table(["Dosya", "WEB hash", "APK hash", "WEB satır", "APK satır", "WEB mtime", "APK mtime"], web_apk_diff, 200))
md.append("")
md.append("## 5) Sadece WEB'de Olan Canlı Dosyalar")
md.append(md_table(["Dosya", "Byte", "Satır", "Mtime"], web_only, 200))
md.append("")
md.append("## 6) Sadece ANDROID'de Olan Canlı Dosyalar")
md.append(md_table(["Dosya", "Byte", "Satır", "Mtime"], android_only, 200))
md.append("")
md.append("## 7) Route Karşılaştırması")
md.append("")
md.append("### WEB route listesi")
md.append(md_table(["Route", "Fonksiyon", "Satır"], web_routes, 200))
md.append("")
md.append("### ANDROID route listesi")
md.append(md_table(["Route", "Fonksiyon", "Satır"], and_routes, 200))
md.append("")
md.append("### WEB'de var ANDROID'de yok")
md.append(md_table(["Route", "Fonksiyon"], sorted(web_route_set - and_route_set), 200))
md.append("")
md.append("### ANDROID'de var WEB'de yok")
md.append(md_table(["Route", "Fonksiyon"], sorted(and_route_set - web_route_set), 200))
md.append("")
md.append("## 8) render_template Karşılaştırması")
md.append("")
md.append("### WEB render_template")
md.append(md_table(["Template", "Satır"], web_render, 200))
md.append("")
md.append("### ANDROID render_template")
md.append(md_table(["Template", "Satır"], and_render, 200))
md.append("")
md.append("### WEB render ediyor ANDROID etmiyor")
md.append(md_table(["Template"], [(x,) for x in sorted(web_render_set - and_render_set)], 200))
md.append("")
md.append("### ANDROID render ediyor WEB etmiyor")
md.append(md_table(["Template"], [(x,) for x in sorted(and_render_set - web_render_set)], 200))
md.append("")
md.append("## 9) Gerçek Eksik Static Referansları")
md.append("")
md.append("### WEB")
md.append(md_table(["HTML", "Referans", "Beklenen yol"], web_missing, 200))
md.append("")
md.append("### ANDROID")
md.append(md_table(["HTML", "Referans", "Beklenen yol"], and_missing, 200))
md.append("")
md.append("## 10) Aynı HTML İçinde Duplicate ID")
md.append("")
md.append("### WEB")
md.append(md_table(["HTML", "ID", "Tekrar", "Satırlar"], web_dup_ids, 200))
md.append("")
md.append("### ANDROID")
md.append(md_table(["HTML", "ID", "Tekrar", "Satırlar"], and_dup_ids, 200))
md.append("")
md.append("## 11) Anlamlı JS Fonksiyon Tekrar Adayları")
md.append("")
md.append("### WEB")
md.append(md_table(["JS", "Fonksiyon", "Tekrar"], web_js_dups, 200))
md.append("")
md.append("### ANDROID")
md.append(md_table(["JS", "Fonksiyon", "Tekrar"], and_js_dups, 200))
md.append("")
md.append("## 12) Önemli Template Script/Link Sırası")
md.append("")
md.append("### WEB")
md.append(md_table(["HTML", "Satır", "Tür", "Referans"], web_asset_order, 250))
md.append("")
md.append("### ANDROID")
md.append(md_table(["HTML", "Satır", "Tür", "Referans"], and_asset_order, 250))
md.append("")
md.append("## 13) Öncelikli Diff Önizlemeleri")
md.append("")
if not diff_blocks:
    md.append("_Öncelikli dosyalarda diff yok._")
else:
    for r, block in diff_blocks:
        md.append(f"### {r}")
        md.append("```diff")
        md.append(block)
        md.append("```")
        md.append("")
md.append("## 14) Tüm Canlı Dosya Hash Tablosu")
md.append(md_table(
    ["Dosya", "WEB", "WEB hash", "WEB satır", "ANDROID", "ANDROID hash", "ANDROID satır", "APK", "APK hash", "APK satır"],
    triple_status_rows,
    500
))
md.append("")
md.append("## 15) Karar Notu")
md.append("""
Bu rapor da sadece tespit içindir. Hiçbir dosya silinmedi.

Bundan sonra doğru sıra:

1. `app.py` WEB/ANDROID farkı incelenecek.
2. `templates/seats.html` ve `static/seats/seats.js` WEB/ANDROID/APK farkı incelenecek.
3. `templates/index.html` içindeki `tripGuard*` duplicate ID sorunu düzeltilecek.
4. Android APK hangi dosyadan çalışıyorsa o ana kaynak kabul edilmeden kopyalama yapılmayacak.
5. `apk_payload` aktif build kaynağı mı, eski paket kalıntısı mı ayrıca belirlenecek.
6. Temizlik ancak bu çekirdek farklar sınıflandırıldıktan sonra yapılacak.
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Canlı çekirdek audit hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
print("WEB canlı aday:", len(active["WEB"]))
print("ANDROID canlı aday:", len(active["ANDROID"]))
print("APK_PAYLOAD canlı aday:", len(active["APK_PAYLOAD"]))
print("WEB ↔ ANDROID farklı:", len(web_android_diff))
print("WEB ↔ APK farklı:", len(web_apk_diff))
print("ANDROID ↔ APK farklı:", len(android_apk_diff))
print("WEB eksik static:", len(web_missing))
print("ANDROID eksik static:", len(and_missing))
print("WEB duplicate ID:", len(web_dup_ids))
print("ANDROID duplicate ID:", len(and_dup_ids))
print()
print("Raporu görmek için:")
print(f"sed -n '1,260p' {OUT}")
