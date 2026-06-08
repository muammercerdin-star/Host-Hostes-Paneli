from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import hashlib
import re
import subprocess
import os

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
REPORT = REPORTS / f"muavin_full_audit_{STAMP}.md"

EXCLUDE_DIRS = {
    ".git", "__pycache__", ".gradle", "build", "dist", "node_modules",
    ".venv", "venv", ".idea", ".vscode", "reports"
}

TEXT_EXTS = {
    ".py", ".html", ".css", ".js", ".json", ".txt", ".md", ".xml",
    ".gradle", ".properties", ".cfg", ".ini", ".yml", ".yaml", ".toml",
    ".sh", ".kt", ".java"
}

MAX_READ = 3_000_000


def rel(p):
    try:
        return str(p.relative_to(ROOT))
    except Exception:
        return str(p)


def skip_path(p):
    parts = set(p.relative_to(ROOT).parts)
    return bool(parts & EXCLUDE_DIRS)


def is_text_file(p):
    if p.name in {"requirements.txt", "Dockerfile", "Procfile"}:
        return True
    return p.suffix.lower() in TEXT_EXTS


def read_text(p):
    try:
        if p.stat().st_size > MAX_READ:
            return ""
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def sha256(p):
    h = hashlib.sha256()
    try:
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 256), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "ERR"


def line_count(p):
    if not is_text_file(p):
        return None
    txt = read_text(p)
    if txt == "":
        return 0
    return txt.count("\n") + 1


def run_cmd(cmd):
    try:
        r = subprocess.run(
            cmd, cwd=ROOT, text=True, capture_output=True, timeout=8
        )
        out = (r.stdout or "").strip()
        err = (r.stderr or "").strip()
        return out if out else err
    except Exception as e:
        return f"Komut çalışmadı: {e}"


def esc(x):
    return str(x).replace("|", "\\|").replace("\n", " ").strip()


def table(headers, rows, limit=None):
    if limit is not None:
        rows = rows[:limit]
    out = []
    out.append("| " + " | ".join(esc(h) for h in headers) + " |")
    out.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        out.append("| " + " | ".join(esc(c) for c in row) + " |")
    return "\n".join(out) if rows else "_Kayıt yok._"


print("===== MUAVİN ASİSTANI FULL AUDIT V1 =====")
print("ROOT:", ROOT)
print("Rapor hazırlanıyor...")

all_files = []
for p in ROOT.rglob("*"):
    if p.is_file() and not skip_path(p):
        all_files.append(p)

text_files = [p for p in all_files if is_text_file(p)]
py_files = [p for p in text_files if p.suffix.lower() == ".py"]
html_files = [p for p in text_files if p.suffix.lower() == ".html"]
css_files = [p for p in text_files if p.suffix.lower() == ".css"]
js_files = [p for p in text_files if p.suffix.lower() == ".js"]

ext_counter = Counter(p.suffix.lower() or "[uzantısız]" for p in all_files)
dir_counter = Counter()
for p in all_files:
    parts = p.relative_to(ROOT).parts
    top = parts[0] if parts else "."
    dir_counter[top] += 1

size_rows = []
for p in all_files:
    try:
        size_rows.append((rel(p), p.stat().st_size, line_count(p)))
    except Exception:
        pass
size_rows_sorted = sorted(size_rows, key=lambda x: x[1], reverse=True)

line_rows = []
for p in text_files:
    lc = line_count(p)
    try:
        line_rows.append((rel(p), lc or 0, p.stat().st_size))
    except Exception:
        pass
line_rows_sorted = sorted(line_rows, key=lambda x: x[1], reverse=True)

# Hash / duplicate content
hash_groups = defaultdict(list)
for p in all_files:
    h = sha256(p)
    hash_groups[h].append(p)

duplicate_content = []
for h, group in hash_groups.items():
    if h != "ERR" and len(group) > 1:
        duplicate_content.append((h[:12], len(group), ", ".join(rel(x) for x in group[:8])))

duplicate_content = sorted(duplicate_content, key=lambda x: x[1], reverse=True)

# Same basename, different locations
name_groups = defaultdict(list)
for p in all_files:
    name_groups[p.name].append(p)

same_name_rows = []
for name, group in name_groups.items():
    if len(group) > 1:
        hashes = {sha256(x) for x in group}
        status = "AYNI" if len(hashes) == 1 else "FARKLI / ÇAKIŞMA ADAYI"
        same_name_rows.append((name, len(group), status, ", ".join(rel(x) for x in group[:10])))

same_name_rows = sorted(same_name_rows, key=lambda x: (x[2] != "FARKLI / ÇAKIŞMA ADAYI", -x[1], x[0]))

# Backup / old / test candidates
BACKUP_RE = re.compile(r"(\.bak|backup|back-up|old|eski|copy|kopya|tmp|temp|deneme|test|orig|step\d|audit|rapor)", re.I)
backup_rows = []
for p in all_files:
    rp = rel(p)
    if BACKUP_RE.search(rp):
        try:
            backup_rows.append((rp, p.stat().st_size, line_count(p)))
        except Exception:
            backup_rows.append((rp, "", ""))

backup_rows = sorted(backup_rows, key=lambda x: x[0].lower())

# Android/web shadow copies
android_prefix = Path("android_app/app/src/main/python")
shadow_rows = []
for p in all_files:
    rp = p.relative_to(ROOT)
    try:
        sub = rp.relative_to(android_prefix)
    except ValueError:
        continue

    counterpart = ROOT / sub
    if counterpart.exists() and counterpart.is_file():
        same = sha256(p) == sha256(counterpart)
        status = "AYNI" if same else "FARKLI / SENKRON ÇAKIŞMASI"
        shadow_rows.append((str(sub), status, rel(counterpart), rel(p)))
    else:
        shadow_rows.append((str(sub), "ANA KOPYA YOK", "-", rel(p)))

shadow_rows = sorted(shadow_rows, key=lambda x: (x[1] == "AYNI", x[0]))

# Flask routes and render_template
ROUTE_RE = re.compile(r"""@\s*(?:\w+\.)?route\(\s*['"]([^'"]+)['"]""")
RENDER_RE = re.compile(r"""render_template\(\s*['"]([^'"]+)['"]""")
IMPORT_RE = re.compile(r"""^\s*(?:from\s+([\w.]+)\s+import\s+(.+)|import\s+(.+))""", re.M)

route_rows = []
render_rows = []
import_rows = []

for p in py_files:
    txt = read_text(p)
    lines = txt.splitlines()

    for i, line in enumerate(lines):
        m = ROUTE_RE.search(line)
        if m:
            fn = ""
            for j in range(i + 1, min(i + 8, len(lines))):
                dm = re.search(r"^\s*def\s+(\w+)\s*\(", lines[j])
                if dm:
                    fn = dm.group(1)
                    break
            route_rows.append((m.group(1), fn, rel(p), i + 1))

    for i, line in enumerate(lines):
        for m in RENDER_RE.finditer(line):
            render_rows.append((m.group(1), rel(p), i + 1))

    for m in IMPORT_RE.finditer(txt):
        mod = m.group(1) or m.group(3) or ""
        what = m.group(2) or ""
        import_rows.append((rel(p), mod, what[:100]))

route_rows = sorted(route_rows, key=lambda x: x[0])
render_rows = sorted(render_rows, key=lambda x: x[0])

# Template dependencies
ATTR_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.I)
URL_FOR_STATIC_RE = re.compile(r"""url_for\(\s*['"]static['"]\s*,\s*filename\s*=\s*['"]([^'"]+)['"]""")
INCLUDE_RE = re.compile(r"""{%\s*(?:include|extends)\s+['"]([^'"]+)['"]""")
ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)

def clean_ref(ref):
    ref = ref.strip()
    ref = ref.split("#")[0].split("?")[0]
    return ref.strip()

def is_external(ref):
    low = ref.lower()
    return (
        low.startswith("http://") or low.startswith("https://") or
        low.startswith("//") or low.startswith("data:") or
        low.startswith("mailto:") or low.startswith("tel:") or
        low.startswith("javascript:") or
        low == "" or low.startswith("#")
    )

def resolve_local_ref(html_file, ref):
    ref = clean_ref(ref)
    if is_external(ref):
        return None

    if ref.startswith("/static/"):
        return ROOT / ref.lstrip("/")
    if ref.startswith("static/"):
        return ROOT / ref
    if ref.startswith("../static/"):
        return ROOT / "static" / ref.split("../static/", 1)[1]
    if ref.startswith("/"):
        return ROOT / ref.lstrip("/")

    return html_file.parent / ref

template_dep_rows = []
missing_static_rows = []
all_referenced_static = set()
inline_rows = []
duplicate_id_rows = []
global_ids = defaultdict(list)

for p in html_files:
    txt = read_text(p)

    attr_refs = [clean_ref(x) for x in ATTR_RE.findall(txt)]
    static_refs = [clean_ref(x) for x in URL_FOR_STATIC_RE.findall(txt)]
    includes = INCLUDE_RE.findall(txt)

    inline_style_count = len(re.findall(r"<style\b", txt, re.I))
    inline_script_count = len(re.findall(r"<script\b(?![^>]*\bsrc=)", txt, re.I))
    inline_rows.append((rel(p), inline_style_count, inline_script_count))

    ids = ID_RE.findall(txt)
    c = Counter(ids)
    for idv, n in c.items():
        global_ids[idv].append(rel(p))
        if n > 1:
            duplicate_id_rows.append((idv, n, rel(p)))

    refs_for_row = []
    for ref in attr_refs:
        if is_external(ref):
            continue
        refs_for_row.append(ref)

        target = resolve_local_ref(p, ref)
        if target:
            if "/static/" in str(target).replace("\\", "/"):
                try:
                    all_referenced_static.add(target.resolve())
                except Exception:
                    pass
            if not target.exists():
                missing_static_rows.append((rel(p), ref, rel(target)))

    for ref in static_refs:
        refs_for_row.append("url_for static: " + ref)
        target = ROOT / "static" / ref
        try:
            all_referenced_static.add(target.resolve())
        except Exception:
            pass
        if not target.exists():
            missing_static_rows.append((rel(p), "url_for static: " + ref, rel(target)))

    template_dep_rows.append((
        rel(p),
        len(refs_for_row),
        ", ".join(refs_for_row[:12]),
        ", ".join(includes[:8])
    ))

global_duplicate_id_rows = []
for idv, files in global_ids.items():
    unique_files = sorted(set(files))
    if len(unique_files) > 1:
        global_duplicate_id_rows.append((idv, len(unique_files), ", ".join(unique_files[:10])))

global_duplicate_id_rows = sorted(global_duplicate_id_rows, key=lambda x: (-x[1], x[0]))

# Orphan static candidates
static_roots = [ROOT / "static"]
static_files = []
for sr in static_roots:
    if sr.exists():
        for p in sr.rglob("*"):
            if p.is_file() and not skip_path(p):
                static_files.append(p)

orphan_static_rows = []
for p in static_files:
    try:
        rp = p.resolve()
    except Exception:
        rp = p
    if rp not in all_referenced_static:
        orphan_static_rows.append((rel(p), p.stat().st_size, p.suffix.lower()))

orphan_static_rows = sorted(orphan_static_rows, key=lambda x: x[0].lower())

# JS / Python function duplicates
JS_FUNC_RE = re.compile(
    r"""\bfunction\s+([A-Za-z_$][\w$]*)\s*\(|(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function\s*)?\(?"""
)
PY_FUNC_RE = re.compile(r"""^\s*def\s+([A-Za-z_]\w*)\s*\(""", re.M)

js_func_global = defaultdict(list)
js_func_file_dups = []
for p in js_files + html_files:
    txt = read_text(p)
    names = []
    for m in JS_FUNC_RE.finditer(txt):
        name = m.group(1) or m.group(2)
        if name:
            names.append(name)
            js_func_global[name].append(rel(p))
    c = Counter(names)
    for name, n in c.items():
        if n > 1:
            js_func_file_dups.append((name, n, rel(p)))

js_func_global_dups = []
for name, files in js_func_global.items():
    u = sorted(set(files))
    if len(u) > 1:
        js_func_global_dups.append((name, len(u), ", ".join(u[:10])))

py_func_global = defaultdict(list)
py_func_file_dups = []
for p in py_files:
    txt = read_text(p)
    names = PY_FUNC_RE.findall(txt)
    for name in names:
        py_func_global[name].append(rel(p))
    c = Counter(names)
    for name, n in c.items():
        if n > 1:
            py_func_file_dups.append((name, n, rel(p)))

py_func_global_dups = []
for name, files in py_func_global.items():
    u = sorted(set(files))
    if len(u) > 1:
        py_func_global_dups.append((name, len(u), ", ".join(u[:10])))

js_func_file_dups = sorted(js_func_file_dups, key=lambda x: (-x[1], x[0]))
js_func_global_dups = sorted(js_func_global_dups, key=lambda x: (-x[1], x[0]))
py_func_file_dups = sorted(py_func_file_dups, key=lambda x: (-x[1], x[0]))
py_func_global_dups = sorted(py_func_global_dups, key=lambda x: (-x[1], x[0]))

# Patch / yama traces
PATCH_LINE_RE = re.compile(r"(patch|hotfix|fix|step[-_ ]?\d+|audit|debug|todo|fixme|v\d+)", re.I)
PATCH_TOKEN_RE = re.compile(r"([A-ZÇĞİÖŞÜ0-9][A-ZÇĞİÖŞÜ0-9_-]{3,}(?:PATCH|FIX|HOTFIX|STEP|AUDIT|V[0-9])[A-ZÇĞİÖŞÜ0-9_-]*)", re.I)

patch_tokens = defaultdict(lambda: {"count": 0, "files": set()})
patch_lines = []
debug_rows = []

DEBUG_RE = re.compile(r"(console\.log|debugger|alert\(|TODO|FIXME)", re.I)

for p in text_files:
    txt = read_text(p)
    if not txt:
        continue

    for i, line in enumerate(txt.splitlines(), 1):
        if PATCH_LINE_RE.search(line):
            short = line.strip()
            if len(short) > 180:
                short = short[:180] + "..."
            patch_lines.append((rel(p), i, short))

            for tm in PATCH_TOKEN_RE.findall(line):
                key = tm.strip()
                patch_tokens[key]["count"] += 1
                patch_tokens[key]["files"].add(rel(p))

        if DEBUG_RE.search(line):
            short = line.strip()
            if len(short) > 180:
                short = short[:180] + "..."
            debug_rows.append((rel(p), i, short))

patch_token_rows = []
for token, data in patch_tokens.items():
    patch_token_rows.append((token, data["count"], ", ".join(sorted(data["files"])[:8])))

patch_token_rows = sorted(patch_token_rows, key=lambda x: (-x[1], x[0]))
patch_lines = patch_lines[:250]
debug_rows = debug_rows[:250]

# CSS selector duplicate rough scan
CSS_SELECTOR_RE = re.compile(r"([.#][A-Za-z0-9_-]+)\s*\{")
selector_global = defaultdict(list)

for p in css_files + html_files:
    txt = read_text(p)
    for m in CSS_SELECTOR_RE.finditer(txt):
        selector_global[m.group(1)].append(rel(p))

selector_dup_rows = []
for sel, files in selector_global.items():
    if len(files) >= 3:
        selector_dup_rows.append((sel, len(files), ", ".join(sorted(set(files))[:8])))

selector_dup_rows = sorted(selector_dup_rows, key=lambda x: (-x[1], x[0]))

# Git info
git_status = run_cmd(["git", "status", "--short"])
git_branch = run_cmd(["git", "branch", "--show-current"])
git_last = run_cmd(["git", "log", "--oneline", "-5"])

# Report
md = []
md.append(f"# Muavin Asistanı Full Audit Raporu\n")
md.append(f"- Tarih: `{STAMP}`")
md.append(f"- Root: `{ROOT}`")
md.append(f"- Toplam dosya: **{len(all_files)}**")
md.append(f"- Text dosya: **{len(text_files)}**")
md.append(f"- Python: **{len(py_files)}**")
md.append(f"- HTML template/dosya: **{len(html_files)}**")
md.append(f"- CSS: **{len(css_files)}**")
md.append(f"- JS: **{len(js_files)}**")
md.append("")

md.append("## 1) Git Durumu")
md.append(f"Branch: `{git_branch}`")
md.append("```")
md.append(git_status or "Temiz ya da git bilgisi alınamadı.")
md.append("```")
md.append("Son commitler:")
md.append("```")
md.append(git_last or "Git log alınamadı.")
md.append("```")

md.append("\n## 2) Ana Klasörlere Göre Dosya Sayısı")
md.append(table(["Klasör", "Dosya sayısı"], sorted(dir_counter.items(), key=lambda x: (-x[1], x[0]))))

md.append("\n## 3) Uzantıya Göre Dosya Sayısı")
md.append(table(["Uzantı", "Dosya sayısı"], sorted(ext_counter.items(), key=lambda x: (-x[1], x[0]))))

md.append("\n## 4) En Büyük 40 Dosya")
md.append(table(["Dosya", "Byte", "Satır"], size_rows_sorted, limit=40))

md.append("\n## 5) En Uzun 40 Text Dosya")
md.append(table(["Dosya", "Satır", "Byte"], line_rows_sorted, limit=40))

md.append("\n## 6) Aynı İçeriğe Sahip Dosyalar")
md.append("Bunlar birebir aynı dosyalar. Silme adayı olabilir ama şimdilik sadece rapor.")
md.append(table(["Hash", "Adet", "Dosyalar"], duplicate_content, limit=80))

md.append("\n## 7) Aynı İsimli Dosyalar")
md.append("Aynı isim farklı klasördeyse özellikle web/android senkron çakışması olabilir.")
md.append(table(["Dosya adı", "Adet", "Durum", "Konumlar"], same_name_rows, limit=120))

md.append("\n## 8) Android/Web Gölge Kopya Kontrolü")
md.append("Android içindeki kopya ile ana web kopyası aynı mı farklı mı?")
md.append(table(["Alt yol", "Durum", "Ana kopya", "Android kopya"], shadow_rows, limit=160))

md.append("\n## 9) Backup / Eski / Test / Audit Dosya Adayları")
md.append("Bunlar otomatik silinmeyecek. Sadece temizlik adayı olarak listeleniyor.")
md.append(table(["Dosya", "Byte", "Satır"], backup_rows, limit=200))

md.append("\n## 10) Flask Route Haritası")
md.append(table(["Route", "Fonksiyon", "Dosya", "Satır"], route_rows, limit=200))

md.append("\n## 11) render_template Haritası")
md.append(table(["Template", "Çağıran Python dosyası", "Satır"], render_rows, limit=200))

md.append("\n## 12) Template → Static / Include Haritası")
md.append(table(["HTML", "Local ref sayısı", "İlk referanslar", "Include/Extends"], template_dep_rows, limit=200))

md.append("\n## 13) Eksik Local Static / Dosya Referansları")
md.append("HTML içinde çağrılıp fiziksel olarak bulunamayan dosyalar.")
md.append(table(["Çağıran HTML", "Referans", "Beklenen yol"], missing_static_rows, limit=200))

md.append("\n## 14) Referans Verilmeyen Static Dosyalar")
md.append("Bunlar gereksiz olabilir ama JS dinamik çağırıyor olabilir. Silmeden önce tek tek bakılmalı.")
md.append(table(["Static dosya", "Byte", "Uzantı"], orphan_static_rows, limit=200))

md.append("\n## 15) Inline Style / Script Sayısı")
md.append("Büyük HTML şişkinliği ve yama üstüne yama riskini gösterir.")
md.append(table(["HTML", "Inline style", "Inline script"], inline_rows, limit=200))

md.append("\n## 16) Aynı HTML Dosyası İçinde Duplicate ID")
md.append(table(["ID", "Tekrar", "Dosya"], duplicate_id_rows, limit=200))

md.append("\n## 17) Farklı Dosyalarda Aynı ID")
md.append("Her zaman hata değildir ama modal/JS seçici çakışması yapabilir.")
md.append(table(["ID", "Dosya sayısı", "Dosyalar"], global_duplicate_id_rows, limit=200))

md.append("\n## 18) Aynı Dosya İçinde Tekrar Eden JS Fonksiyonları")
md.append(table(["Fonksiyon", "Tekrar", "Dosya"], js_func_file_dups, limit=200))

md.append("\n## 19) Farklı Dosyalarda Aynı JS Fonksiyonları")
md.append(table(["Fonksiyon", "Dosya sayısı", "Dosyalar"], js_func_global_dups, limit=200))

md.append("\n## 20) Aynı Dosya İçinde Tekrar Eden Python Fonksiyonları")
md.append(table(["Fonksiyon", "Tekrar", "Dosya"], py_func_file_dups, limit=200))

md.append("\n## 21) Farklı Dosyalarda Aynı Python Fonksiyonları")
md.append(table(["Fonksiyon", "Dosya sayısı", "Dosyalar"], py_func_global_dups, limit=200))

md.append("\n## 22) CSS Selector Tekrarları")
md.append("3 ve üzeri tekrar eden selectorlar. CSS çakışması için ilk sinyal.")
md.append(table(["Selector", "Tekrar", "Dosyalar"], selector_dup_rows, limit=200))

md.append("\n## 23) Yama / Patch / Fix İzleri - Özet Tokenlar")
md.append(f"Yakalanan benzersiz yama token sayısı: **{len(patch_token_rows)}**")
md.append(table(["Yama token", "Geçiş", "Dosyalar"], patch_token_rows, limit=200))

md.append("\n## 24) Yama / Patch / Fix Satırlarından İlk 250 Kayıt")
md.append(table(["Dosya", "Satır", "Satır içeriği"], patch_lines, limit=250))

md.append("\n## 25) Debug / TODO / Alert İzleri")
md.append(table(["Dosya", "Satır", "Satır içeriği"], debug_rows, limit=250))

md.append("\n## 26) İlk Karar Notu")
md.append("""
Bu rapor sadece tespit içindir. Şu aşamada hiçbir dosya silinmedi.
Silme kararı için ayrı bir liste hazırlanmalı:

1. Birebir aynı içerikte olan backup dosyalar
2. Ana uygulama tarafından çağrılmayan eski patch dosyaları
3. Android/web kopyasında eski kalmış farklı dosyalar
4. Eksik static referansları yüzünden boşa duran bağlantılar
5. Büyük HTML içine gömülmüş tekrar eden inline script/style blokları

Önce bu rapordaki çakışmaları okuyup sınıflandıracağız. Sonra silinecekleri tek tek onaylı listeye alacağız.
""")

REPORT.write_text("\n".join(md), encoding="utf-8")

print()
print("✅ RAPOR HAZIR:")
print(REPORT)
print()
print("===== KISA ÖZET =====")
print("Toplam dosya:", len(all_files))
print("Text dosya:", len(text_files))
print("Python:", len(py_files))
print("HTML:", len(html_files))
print("CSS:", len(css_files))
print("JS:", len(js_files))
print("Aynı içerikli dosya grubu:", len(duplicate_content))
print("Aynı isimli dosya grubu:", len(same_name_rows))
print("Android/Web farklı kopya:", sum(1 for x in shadow_rows if "FARKLI" in x[1]))
print("Eksik static/ref:", len(missing_static_rows))
print("Backup/eski/test adayı:", len(backup_rows))
print("Duplicate ID:", len(duplicate_id_rows))
print("Yama token:", len(patch_token_rows))
print()
print("Raporun ilk kısmını görmek için:")
print(f"sed -n '1,220p' {REPORT}")
