from pathlib import Path
import re
import subprocess
import shutil
from collections import defaultdict, Counter

ROOT = Path(".").resolve()

IGNORE_DIRS = {
    ".git", "__pycache__", ".venv", "venv", "node_modules",
    "android_app", "apk_payload", "backups", "_unused_review",
    ".pytest_cache", ".mypy_cache"
}

TEXT_EXTS = {".html", ".css", ".js", ".py", ".json", ".txt", ".md"}

PATCH_HINTS = [
    "patch", "fix", "final", "override", "pack", "tune",
    "unified", "extra", "marquee", "toast", "voice", "modal",
    "mobile", "focus", "compact", "manual", "ghost"
]

def rel(p):
    p = Path(p)
    try:
        return str(p.resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def ignored(p):
    try:
        parts = p.resolve().relative_to(ROOT).parts
    except Exception:
        parts = p.parts
    return any(x in IGNORE_DIRS for x in parts)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def clean_static_ref(v):
    if not v:
        return None
    v = v.strip().replace("&amp;", "&")
    if v.startswith("http://") or v.startswith("https://") or v.startswith("//"):
        return None
    if "{{" in v or "{%" in v:
        return None
    v = v.split("?")[0].split("#")[0]
    if v.startswith("/static/"):
        return v.lstrip("/")
    if v.startswith("static/"):
        return v
    return None

def all_files():
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if ignored(p):
            continue
        if p.suffix.lower() in TEXT_EXTS:
            out.append(p)
    return out

def source_files(files):
    out = []
    for p in files:
        rp = rel(p)
        if rp.startswith("tools/"):
            continue
        if rp.startswith("templates/") and p.suffix.lower() == ".html":
            out.append(p)
        elif rp == "app.py":
            out.append(p)
        elif rp.startswith("modules/") and p.suffix.lower() == ".py":
            out.append(p)
    return out

def extract_static_refs(text):
    refs = set()

    for m in re.finditer(r"url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]", text):
        refs.add("static/" + m.group(1).lstrip("/"))

    for m in re.finditer(r"""(?:href|src)\s*=\s*['"]([^'"]+)['"]""", text, re.I):
        r = clean_static_ref(m.group(1))
        if r:
            refs.add(r)

    for m in re.finditer(r"""['"](/static/[^'"\s)]+)['"]""", text):
        r = clean_static_ref(m.group(1))
        if r:
            refs.add(r)

    return refs

def is_patch_like(p):
    rp = rel(p).lower()
    name = p.name.lower()
    if not rp.startswith("static/"):
        return False
    if p.suffix.lower() not in {".css", ".js"}:
        return False
    if "/patches/" in rp:
        return True
    if any(h in name for h in PATCH_HINTS):
        return True
    return False

def css_rules(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"@keyframes\s+[^{]+\{.*?\}\s*\}", "", text, flags=re.S)
    for m in re.finditer(r"([^{}]+)\{([^{}]+)\}", text, flags=re.S):
        selectors = [x.strip() for x in m.group(1).split(",") if x.strip()]
        body = m.group(2)
        for pm in re.finditer(r"([-\w]+)\s*:\s*([^;]+);", body):
            prop = pm.group(1).strip()
            val = " ".join(pm.group(2).strip().split())
            for sel in selectors:
                if sel.startswith("@"):
                    continue
                yield sel, prop, val

def html_css_units(template_path):
    html = read(template_path)
    units = []
    order = 0

    rx = re.compile(
        r"""(?is)<link\b[^>]*href=['"]([^'"]+\.css(?:\?[^'"]*)?)['"][^>]*>|<style\b([^>]*)>(.*?)</style>"""
    )

    for m in rx.finditer(html):
        order += 1

        href = m.group(1)
        if href:
            r = clean_static_ref(href)
            if r:
                p = ROOT / r
                if p.exists():
                    units.append({
                        "kind": "file",
                        "key": rel(p),
                        "order": order,
                        "text": read(p),
                    })
            continue

        attrs = m.group(2) or ""
        body = m.group(3) or ""
        idm = re.search(r"""id=['"]([^'"]+)['"]""", attrs, re.I)
        sid = idm.group(1) if idm else f"inline-{order}"
        units.append({
            "kind": "inline",
            "key": f"INLINE:{rel(template_path)}#{sid}",
            "order": order,
            "text": body,
        })

    return units

def is_candidate_key(key, candidates):
    if key in candidates:
        return True
    low = key.lower()
    if low.startswith("inline:") and any(h in low for h in PATCH_HINTS):
        return True
    return False

def run_cmd(cmd):
    try:
        p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=25)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:
        return 999, "", str(e)

files = all_files()
sources = source_files(files)

css_files = [p for p in files if p.suffix.lower() == ".css" and rel(p).startswith("static/")]
js_files = [p for p in files if p.suffix.lower() == ".js" and rel(p).startswith("static/")]
templates = [p for p in files if p.suffix.lower() == ".html" and rel(p).startswith("templates/")]

patch_candidates = sorted([p for p in css_files + js_files if is_patch_like(p)], key=rel)
candidate_keys = {rel(p) for p in patch_candidates}

all_refs = set()
ref_sources = defaultdict(list)

for p in sources:
    txt = read(p)
    for r in extract_static_refs(txt):
        all_refs.add(r)
        ref_sources[r].append(rel(p))

existing_refs = set()
missing_refs = []

for r in sorted(all_refs):
    p = ROOT / r
    if p.exists():
        existing_refs.add(rel(p))
    else:
        missing_refs.append(r)

active_candidates = []
orphan_candidates = []

source_text_blob = "\n".join(read(p) for p in sources)

for p in patch_candidates:
    rp = rel(p)
    if rp in existing_refs or rp in source_text_blob or p.name in source_text_blob:
        active_candidates.append(p)
    else:
        orphan_candidates.append(p)

# JS syntax
node = shutil.which("node")
js_errors = []
if node:
    for p in active_candidates:
        if p.suffix.lower() != ".js":
            continue
        code, out, err = run_cmd([node, "--check", str(p)])
        if code != 0:
            js_errors.append((rel(p), err or out))
else:
    js_errors.append(("NODE_YOK", "node kurulu değil; JS syntax kontrolü atlandı."))

# Python compile
py_errors = []
code, out, err = run_cmd(["python", "-m", "py_compile", "app.py"])
if code != 0:
    py_errors.append(("app.py", err or out))

# Inline duplicate IDs — aynı template içinde
dup_inline = []
for tpl in templates:
    txt = read(tpl)
    style_ids = re.findall(r"""<style[^>]*\bid=['"]([^'"]+)['"]""", txt, re.I)
    script_ids = re.findall(r"""<script[^>]*\bid=['"]([^'"]+)['"]""", txt, re.I)

    for sid, count in Counter(style_ids).items():
        if count > 1:
            dup_inline.append((rel(tpl), "style", sid, count))

    for sid, count in Counter(script_ids).items():
        if count > 1:
            dup_inline.append((rel(tpl), "script", sid, count))

# CSS exact override audit
overridden_by_later = defaultdict(list)
overwrites_previous = defaultdict(list)

for tpl in templates:
    units = html_css_units(tpl)
    rule_map = defaultdict(list)

    for u in units:
        for sel, prop, val in css_rules(u["text"]):
            rule_map[(sel, prop)].append((u["order"], u["key"], val))

    for (sel, prop), arr in rule_map.items():
        vals = {x[2] for x in arr}
        if len(arr) < 2 or len(vals) < 2:
            continue

        arr_sorted = sorted(arr, key=lambda x: x[0])
        last_order, last_key, last_val = arr_sorted[-1]

        for order, key, val in arr_sorted[:-1]:
            if val == last_val:
                continue

            if is_candidate_key(key, candidate_keys):
                overridden_by_later[key].append({
                    "template": rel(tpl),
                    "selector": sel,
                    "property": prop,
                    "old": val,
                    "later": last_key,
                    "new": last_val,
                })

            if is_candidate_key(last_key, candidate_keys):
                overwrites_previous[last_key].append({
                    "template": rel(tpl),
                    "selector": sel,
                    "property": prop,
                    "prev": key,
                    "old": val,
                    "new": last_val,
                })

stable_pre = []
risk_pre = []

js_error_files = {x[0] for x in js_errors if x[0] != "NODE_YOK"}

for p in active_candidates:
    rp = rel(p)
    if rp in js_error_files:
        risk_pre.append((rp, "JS syntax hatası"))
    elif rp in overridden_by_later:
        risk_pre.append((rp, f"{len(overridden_by_later[rp])} CSS kuralı daha sonra eziliyor"))
    else:
        stable_pre.append(rp)

lines = []
lines.append("# Muavin Asistanı Canlı Patch Audit Raporu")
lines.append("")
lines.append("Bu rapor sadece canlı çalışan proje alanını tarar: `templates/`, `static/`, `app.py`, `modules/`.")
lines.append("")
lines.append("## 1) Özet")
lines.append("")
lines.append(f"- Canlı template sayısı: **{len(templates)}**")
lines.append(f"- Canlı CSS dosyası: **{len(css_files)}**")
lines.append(f"- Canlı JS dosyası: **{len(js_files)}**")
lines.append(f"- Patch/yama adayı CSS/JS: **{len(patch_candidates)}**")
lines.append(f"- Aktif/çağrılan yama adayı: **{len(active_candidates)}**")
lines.append(f"- Yetim/çağrılmayan yama adayı: **{len(orphan_candidates)}**")
lines.append(f"- Ön-stabil görünen aktif yama: **{len(stable_pre)}**")
lines.append(f"- Riskli/eziliyor olabilir: **{len(risk_pre)}**")
lines.append(f"- Eksik static referansı: **{len(missing_refs)}**")
lines.append(f"- Inline duplicate id: **{len(dup_inline)}**")
lines.append(f"- JS syntax sonucu: **{'node yok, kontrol edilmedi' if (len(js_errors)==1 and js_errors[0][0]=='NODE_YOK') else str(len(js_errors)) + ' hata'}**")
lines.append(f"- Python compile: **{'OK' if not py_errors else 'HATA'}**")
lines.append("")

lines.append("## 2) Ön-stabil görünen aktif yamalar")
lines.append("")
if stable_pre:
    for x in sorted(stable_pre):
        lines.append(f"- `{x}`")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 3) Riskli / eziliyor olabilir")
lines.append("")
if risk_pre:
    for f, reason in sorted(risk_pre):
        lines.append(f"- `{f}` — {reason}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 4) Yetim / çağrılmayan yama adayları")
lines.append("")
if orphan_candidates:
    for p in sorted(orphan_candidates, key=rel):
        lines.append(f"- `{rel(p)}`")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 5) Eksik static referansları")
lines.append("")
if missing_refs:
    for r in missing_refs:
        src = ", ".join(sorted(set(ref_sources[r]))[:5])
        lines.append(f"- `{r}` çağrılıyor ama dosya yok. Kaynak: {src}")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 6) Inline duplicate style/script id")
lines.append("")
if dup_inline:
    for tpl, kind, sid, count in dup_inline:
        lines.append(f"- `{tpl}` içinde `{kind} id=\"{sid}\"` {count} kez geçiyor")
else:
    lines.append("- Yok")
lines.append("")

lines.append("## 7) Ezilen CSS detayları — ilk 120")
lines.append("")
count = 0
for f in sorted(overridden_by_later):
    lines.append(f"### `{f}`")
    for item in overridden_by_later[f][:20]:
        lines.append(f"- `{item['template']}` → `{item['selector']}` / `{item['property']}`")
        lines.append(f"  - Eski: `{item['old']}`")
        lines.append(f"  - Daha sonra ezen: `{item['later']}` → `{item['new']}`")
        count += 1
        if count >= 120:
            break
    lines.append("")
    if count >= 120:
        break
if count == 0:
    lines.append("- Yok")
lines.append("")

lines.append("## 8) Başka kuralları ezen yamalar — ilk 80")
lines.append("")
count = 0
for f in sorted(overwrites_previous):
    lines.append(f"### `{f}`")
    for item in overwrites_previous[f][:15]:
        lines.append(f"- `{item['template']}` → `{item['selector']}` / `{item['property']}`")
        lines.append(f"  - Önceki: `{item['prev']}` → `{item['old']}`")
        lines.append(f"  - Bu yama: `{item['new']}`")
        count += 1
        if count >= 80:
            break
    lines.append("")
    if count >= 80:
        break
if count == 0:
    lines.append("- Yok")
lines.append("")

lines.append("## 9) JS syntax kontrolü")
lines.append("")
if js_errors:
    for f, e in js_errors:
        lines.append(f"### `{f}`")
        lines.append("```")
        lines.append(e[:2000])
        lines.append("```")
else:
    lines.append("- Hata yok")
lines.append("")

lines.append("## 10) Python compile kontrolü")
lines.append("")
if py_errors:
    for f, e in py_errors:
        lines.append(f"### `{f}`")
        lines.append("```")
        lines.append(e[:2000])
        lines.append("```")
else:
    lines.append("- `app.py` compile OK")
lines.append("")

Path("PATCH_LIVE_AUDIT_REPORT.md").write_text("\n".join(lines), encoding="utf-8")

print("OK: PATCH_LIVE_AUDIT_REPORT.md oluşturuldu")
print(f"Canlı patch/yama adayı: {len(patch_candidates)}")
print(f"Aktif/çağrılan: {len(active_candidates)}")
print(f"Ön-stabil: {len(stable_pre)}")
print(f"Riskli/eziliyor olabilir: {len(risk_pre)}")
print(f"Yetim/çağrılmayan: {len(orphan_candidates)}")
print(f"Eksik static referansı: {len(missing_refs)}")
print(f"Inline duplicate id: {len(dup_inline)}")
