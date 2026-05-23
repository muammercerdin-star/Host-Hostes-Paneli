from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(".").resolve()
TEMPLATE = Path("templates/seats.html")

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def clean_ref(v):
    v = (v or "").strip().split("?")[0].split("#")[0]
    if v.startswith("/static/"):
        return v.lstrip("/")
    if v.startswith("static/"):
        return v
    return None

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
                if sel and not sel.startswith("@"):
                    yield sel, prop, val

html = read(TEMPLATE)

rx = re.compile(
    r"""(?is)<link\b[^>]*href=['"]([^'"]+\.css(?:\?[^'"]*)?)['"][^>]*>|<style\b([^>]*)>(.*?)</style>"""
)

units = []
order = 0

for m in rx.finditer(html):
    order += 1
    line = html[:m.start()].count("\n") + 1

    href = m.group(1)
    if href:
        r = clean_ref(href)
        if not r:
            continue
        p = ROOT / r
        if not p.exists():
            continue
        units.append((order, line, rel(p), read(p)))
    else:
        attrs = m.group(2) or ""
        body = m.group(3) or ""
        idm = re.search(r"""id=['"]([^'"]+)['"]""", attrs, re.I)
        sid = idm.group(1) if idm else f"inline-{order}"
        units.append((order, line, f"INLINE:{rel(TEMPLATE)}#{sid}", body))

decls = []
for order, line, key, text in units:
    for sel, prop, val in css_rules(text):
        decls.append({
            "order": order,
            "line": line,
            "key": key,
            "selector": sel,
            "property": prop,
            "value": val,
        })

by_rule = defaultdict(list)
for d in decls:
    by_rule[(d["selector"], d["property"])].append(d)

external_overridden = defaultdict(list)
external_overrides = defaultdict(list)

for rule, arr in by_rule.items():
    if len(arr) < 2:
        continue

    arr = sorted(arr, key=lambda x: x["order"])
    final = arr[-1]

    for old in arr[:-1]:
        if old["value"] == final["value"]:
            continue
        if old["key"] == final["key"]:
            continue

        external_overridden[old["key"]].append((old, final))
        external_overrides[final["key"]].append((old, final))

focus = [
    "static/seats/seats-final.css",
    "static/seats/patches/manual-ticket-system.css",
    "static/seats/patches/mobile-performance-fix.css",
    "static/seats/patches/seat-layout-fab-pack.css",
    "static/seats/patches/seat-simple-ui-pack.css",
    "static/seats/patches/stop-flow-compact-mobile.css",
    "static/seats/patches/stop-flow-focus-patch.css",
    "static/seats/patches/top-sound-toggle.css",
    "static/seats/patches/unified-seat-deck-report-style.css",
]

lines = []
lines.append("# Seats Gerçek Dış Ezilme Raporu")
lines.append("")
lines.append("Aynı dosyanın kendi içindeki tekrarları sayılmadı. Sadece başka dosyanın sonradan ezdiği kurallar listelendi.")
lines.append("")

lines.append("## Özet")
lines.append("")
for f in focus:
    a = len(external_overridden.get(f, []))
    b = len(external_overrides.get(f, []))
    lines.append(f"- `{f}` → başka dosya tarafından ezilen: **{a}**, başka dosyayı ezen: **{b}**")
lines.append("")

lines.append("## Kritik detaylar")
lines.append("")
for f in focus:
    arr = external_overridden.get(f, [])
    lines.append(f"### `{f}`")
    if not arr:
        lines.append("- Dış ezilme yok.")
        lines.append("")
        continue

    for old, final in arr[:40]:
        lines.append(f"- `{old['selector']}` / `{old['property']}`")
        lines.append(f"  - Bu dosya: `{old['value']}`")
        lines.append(f"  - Sonradan ezen: `{final['key']}` → `{final['value']}`")
    lines.append("")

lines.append("## En çok sonradan ezenler")
lines.append("")
for f, arr in sorted(external_overrides.items(), key=lambda x: len(x[1]), reverse=True):
    lines.append(f"- `{f}` → **{len(arr)}** dış kural eziyor")

Path("SEATS_EXTERNAL_OVERRIDE_REPORT.md").write_text("\n".join(lines), encoding="utf-8")

print("OK: SEATS_EXTERNAL_OVERRIDE_REPORT.md oluşturuldu")
for f in focus:
    print(f"- {f}: dış_ezilen={len(external_overridden.get(f, []))}, dış_ezen={len(external_overrides.get(f, []))}")
