from pathlib import Path
import re
import subprocess
import shutil
from collections import defaultdict, Counter

ROOT = Path(".").resolve()

TEXT_EXTS = {
    ".html", ".css", ".js", ".py", ".json", ".txt", ".md"
}

BACKUP_PATTERNS = [
    ".bak", "_bak", "backup", ".old", "_old", ".orig", "_orig",
    "before_", "rollback", "revert"
]

PATCH_HINTS = [
    "patch", "fix", "final", "override", "pack", "tune",
    "unified", "seat", "live_map", "home", "route", "flash"
]

def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except Exception:
        return str(p)

def is_backup(p: Path) -> bool:
    s = p.name.lower()
    return any(x in s for x in BACKUP_PATTERNS)

def is_patch_like(p: Path) -> bool:
    rp = rel(p).lower()
    name = p.name.lower()
    if "static/seats/patches" in rp:
        return True
    if "patch" in rp:
        return True
    if any(x in name for x in PATCH_HINTS) and p.suffix.lower() in {".css", ".js", ".html"}:
        return True
    return False

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def all_text_files():
    skip_dirs = {
        ".git", "__pycache__", ".venv", "venv", "node_modules",
        ".mypy_cache", ".pytest_cache"
    }
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        parts = set(p.parts)
        if parts & skip_dirs:
            continue
        if p.suffix.lower() in TEXT_EXTS or p.suffix == "":
            out.append(p)
    return out

def extract_static_refs(text: str):
    refs = set()

    # url_for('static', filename='...')
    for m in re.finditer(r"url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]", text):
        refs.add("static/" + m.group(1).lstrip("/"))

    # /static/...
    for m in re.finditer(r"""['"](/static/[^'"\s)]+)['"]""", text):
        refs.add(m.group(1).lstrip("/"))

    # href/src plain static/...
    for m in re.finditer(r"""(?:href|src)\s*=\s*['"]([^'"]+)['"]""", text, re.I):
        v = m.group(1)
        if v.startswith("/static/"):
            refs.add(v.lstrip("/"))
        elif v.startswith("static/"):
            refs.add(v)

    return refs

def css_rules(text: str):
    # Basit CSS selector/property çıkarıcı. Tam CSS parser değildir ama çakışma riskini yakalar.
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    for m in re.finditer(r"([^{}]+)\{([^{}]+)\}", text, flags=re.S):
        selectors = [x.strip() for x in m.group(1).split(",") if x.strip()]
        body = m.group(2)
        for pm in re.finditer(r"([-\w]+)\s*:\s*([^;]+);", body):
            prop = pm.group(1).strip()
            val = " ".join(pm.group(2).strip().split())
            for sel in selectors:
                yield sel, prop, val

def run_cmd(cmd):
    try:
        p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=20)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:
        return 999, "", str(e)

files = all_text_files()

templates = [p for p in files if p.suffix.lower() == ".html" and rel(p).startswith("templates/")]
css_files = [p for p in files if p.suffix.lower() == ".css"]
js_files = [p for p in files if p.suffix.lower() == ".js"]
py_files = [p for p in files if p.suffix.lower() == ".py"]

patch_files = [p for p in files if is_patch_like(p)]
patch_real = [p for p in patch_files if not is_backup(p)]
patch_backup = [p for p in patch_files if is_backup(p)]

# Tüm proje içinden static referansları
all_refs = set()
ref_sources = defaultdict(list)
for p in files:
    if p.suffix.lower() not in TEXT_EXTS:
        continue
    try:
        txt = read_text(p)
    except Exception:
        continue
    refs = extract_static_refs(txt)
    for r in refs:
        all_refs.add(r)
        ref_sources[r].append(rel(p))

existing_ref_paths = set()
missing_refs = []
for r in sorted(all_refs):
    rp = ROOT / r
    if rp.exists():
        existing_ref_paths.add(rel(rp))
    else:
        missing_refs.append(r)

# Patch aktifliği
active_patches = []
orphan_patches = []
for p in patch_real:
    rp = rel(p)
    if rp in existing_ref_paths:
        active_patches.append(p)
    else:
        # Dosya adı metin olarak geçiyor mu?
        needle1 = rp
        needle2 = p.name
        mentioned = False
        for f in files:
            try:
                t = read_text(f)
            except Exception:
                continue
            if needle1 in t or needle2 in t:
                mentioned = True
                break
        if mentioned:
            active_patches.append(p)
        else:
            orphan_patches.append(p)

# Inline style/script id tekrarları
style_ids = defaultdict(list)
script_ids = defaultdict(list)
for p in templates:
    txt = read_text(p)
    for m in re.finditer(r"<style[^>]*\bid=['\"]([^'\"]+)['\"]", txt, re.I):
        style_ids[m.group(1)].append(rel(p))
    for m in re.finditer(r"<script[^>]*\bid=['\"]([^'\"]+)['\"]", txt, re.I):
        script_ids[m.group(1)].append(rel(p))

dup_style_ids = {k:v for k,v in style_ids.items() if len(v) > 1}
dup_script_ids = {k:v for k,v in script_ids.items() if len(v) > 1}

# Marker tekrarları START/END
markers = defaultdict(list)
for p in files:
    try:
        txt = read_text(p)
    except Exception:
        continue
    for m in re.finditer(r"/\*\s*=*\s*([A-Z0-9_\- ]+?(?:START|END))\s*=*\s*\*/", txt):
        markers[m.group(1).strip()].append(rel(p))

dup_markers = {k:v for k,v in markers.items() if len(v) > 1}

# CSS çakışmaları: aktif patch + ana css dosyaları
css_scan = []
for p in css_files:
    rp = rel(p)
    if rp in existing_ref_paths or p in active_patches or "static/seats" in rp or "static/live_map" in rp:
        css_scan.append(p)

css_prop_map = defaultdict(list)
for p in css_scan:
    txt = read_text(p)
    for sel, prop, val in css_rules(txt):
        key = (sel, prop)
        css_prop_map[key].append((rel(p), val))

css_conflicts = []
for (sel, prop), arr in css_prop_map.items():
    vals = {v for _, v in arr}
    if len(arr) >= 2 and len(vals) >= 2:
        css_conflicts.append((sel, prop, arr))

css_conflicts.sort(key=lambda x: len(x[2]), reverse=True)

# JS syntax check
js_syntax = []
node = shutil.which("node")
if node:
    for p in js_files:
        rp = rel(p)
        if rp in existing_ref_paths or p in active_patches or "static/seats" in rp or "static/live_map" in rp:
            code, out, err = run_cmd([node, "--check", str(p)])
            if code != 0:
                js_syntax.append((rp, err or out))
else:
    js_syntax.append(("NODE_YOK", "node kurulu değil; JS syntax kontrolü atlandı."))

# Python compile
py_compile_result = []
code, out, err = run_cmd(["python", "-m", "py_compile", "app.py"])
if code != 0:
    py_compile_result.append(("app.py", err or out))

# Rapor
lines = []
lines.append("# Muavin Asistanı Patch / Yama Audit Raporu")
lines.append("")
lines.append("## Özet")
lines.append("")
lines.append(f"- Toplam metin dosyası: **{len(files)}**")
lines.append(f"- CSS dosyası: **{len(css_files)}**")
lines.append(f"- JS dosyası: **{len(js_files)}**")
lines.append(f"- HTML template: **{len(templates)}**")
lines.append(f"- Patch/yama gibi görünen dosya: **{len(patch_files)}**")
lines.append(f"- Gerçek yama dosyası: **{len(patch_real)}**")
lines.append(f"- Backup/eski yama dosyası: **{len(patch_backup)}**")
lines.append(f"- Aktif/çağrılan yama: **{len(active_patches)}**")
lines.append(f"- Yetim/çağrılmayan yama: **{len(orphan_patches)}**")
lines.append(f"- Eksik static referansı: **{len(missing_refs)}**")
lines.append(f"- CSS çakışma riski: **{len(css_conflicts)}**")
lines.append(f"- JS syntax hatası: **{len(js_syntax) if not (len(js_syntax)==1 and js_syntax[0][0]=='NODE_YOK') else 'kontrol edilmedi'}**")
lines.append("")

lines.append("## 1) Aktif / çağrılan yamalar")
lines.append("")
if active_patches:
    for p in sorted(active_patches, key=rel):
        lines.append(f"- `{rel(p)}`")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 2) Yetim / çağrılmayan yamalar")
lines.append("")
if orphan_patches:
    for p in sorted(orphan_patches, key=rel):
        lines.append(f"- `{rel(p)}`")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 3) Backup / eski yama dosyaları")
lines.append("")
if patch_backup:
    for p in sorted(patch_backup, key=rel)[:300]:
        lines.append(f"- `{rel(p)}`")
    if len(patch_backup) > 300:
        lines.append(f"- ... {len(patch_backup)-300} dosya daha")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 4) Eksik static referansları")
lines.append("")
if missing_refs:
    for r in missing_refs:
        srcs = ", ".join(sorted(set(ref_sources[r]))[:5])
        lines.append(f"- `{r}` çağrılıyor ama dosya yok. Kaynak: {srcs}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 5) Tekrarlanan inline style id")
lines.append("")
if dup_style_ids:
    for k,v in sorted(dup_style_ids.items()):
        lines.append(f"- `{k}` -> {', '.join(sorted(set(v)))}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 6) Tekrarlanan inline script id")
lines.append("")
if dup_script_ids:
    for k,v in sorted(dup_script_ids.items()):
        lines.append(f"- `{k}` -> {', '.join(sorted(set(v)))}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 7) Tekrarlanan START/END markerları")
lines.append("")
if dup_markers:
    for k,v in sorted(dup_markers.items()):
        lines.append(f"- `{k}` -> {', '.join(sorted(set(v)))}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 8) CSS çakışma riskleri — ilk 120")
lines.append("")
if css_conflicts:
    for sel, prop, arr in css_conflicts[:120]:
        lines.append(f"### `{sel}` / `{prop}`")
        for f, val in arr[:12]:
            lines.append(f"- `{f}` => `{val}`")
        if len(arr) > 12:
            lines.append(f"- ... {len(arr)-12} kayıt daha")
        lines.append("")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 9) JS syntax kontrolü")
lines.append("")
if js_syntax:
    for f, e in js_syntax:
        lines.append(f"### `{f}`")
        lines.append("```")
        lines.append(e[:2000])
        lines.append("```")
else:
    lines.append("- Hata yok")
lines.append("")

lines.append("## 10) Python compile kontrolü")
lines.append("")
if py_compile_result:
    for f, e in py_compile_result:
        lines.append(f"### `{f}`")
        lines.append("```")
        lines.append(e[:2000])
        lines.append("```")
else:
    lines.append("- `app.py` compile OK")
lines.append("")

Path("PATCH_AUDIT_REPORT.md").write_text("\n".join(lines), encoding="utf-8")

print("OK: PATCH_AUDIT_REPORT.md oluşturuldu")
print(f"Patch/yama gibi görünen dosya: {len(patch_files)}")
print(f"Aktif/çağrılan yama: {len(active_patches)}")
print(f"Yetim/çağrılmayan yama: {len(orphan_patches)}")
print(f"Eksik static referansı: {len(missing_refs)}")
print(f"CSS çakışma riski: {len(css_conflicts)}")
print("Rapor: PATCH_AUDIT_REPORT.md")
