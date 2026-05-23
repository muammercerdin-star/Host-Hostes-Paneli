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
    if not v:
        return None
    v = v.strip().split("?")[0].split("#")[0]
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
                if not sel or sel.startswith("@"):
                    continue
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
            units.append({
                "order": order,
                "line": line,
                "key": r,
                "kind": "missing-file",
                "text": "",
            })
            continue

        units.append({
            "order": order,
            "line": line,
            "key": rel(p),
            "kind": "file",
            "text": read(p),
        })
    else:
        attrs = m.group(2) or ""
        body = m.group(3) or ""
        idm = re.search(r"""id=['"]([^'"]+)['"]""", attrs, re.I)
        sid = idm.group(1) if idm else f"inline-{order}"

        units.append({
            "order": order,
            "line": line,
            "key": f"INLINE:{rel(TEMPLATE)}#{sid}",
            "kind": "inline",
            "text": body,
        })

decls = []
for u in units:
    for sel, prop, val in css_rules(u["text"]):
        decls.append({
            "order": u["order"],
            "line": u["line"],
            "key": u["key"],
            "selector": sel,
            "property": prop,
            "value": val,
        })

by_rule = defaultdict(list)
for d in decls:
    by_rule[(d["selector"], d["property"])].append(d)

total_by_file = defaultdict(int)
overridden_by_file = defaultdict(list)
overrides_by_file = defaultdict(list)

for d in decls:
    total_by_file[d["key"]] += 1

for rule, arr in by_rule.items():
    if len(arr) < 2:
        continue

    arr = sorted(arr, key=lambda x: x["order"])
    final = arr[-1]

    for old in arr[:-1]:
        if old["value"] == final["value"]:
            continue

        overridden_by_file[old["key"]].append({
            "selector": old["selector"],
            "property": old["property"],
            "old": old["value"],
            "later": final["key"],
            "new": final["value"],
        })

        overrides_by_file[final["key"]].append({
            "selector": old["selector"],
            "property": old["property"],
            "prev": old["key"],
            "old": old["value"],
            "new": final["value"],
        })

risk_files = [
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
lines.append("# Seats CSS Override Odak Raporu")
lines.append("")
lines.append("Bu rapor sadece `templates/seats.html` içindeki CSS yükleme sırasına göre hazırlanmıştır.")
lines.append("")

lines.append("## 1) CSS yükleme sırası")
lines.append("")
for u in units:
    lines.append(f"{u['order']:02d}. line {u['line']} — `{u['key']}`")
lines.append("")

lines.append("## 2) Riskli dosya özetleri")
lines.append("")
for f in risk_files:
    total = total_by_file.get(f, 0)
    ov = len(overridden_by_file.get(f, []))
    makes = len(overrides_by_file.get(f, []))
    rate = round((ov / total * 100), 1) if total else 0

    lines.append(f"### `{f}`")
    lines.append(f"- Toplam CSS bildirimi: **{total}**")
    lines.append(f"- Sonradan ezilen bildirim: **{ov}**")
    lines.append(f"- Ezilme oranı: **%{rate}**")
    lines.append(f"- Bu dosyanın sonradan ezdiği önceki bildirim: **{makes}**")
    lines.append("")

    samples = overridden_by_file.get(f, [])[:25]
    if samples:
        lines.append("Örnek ezilmeler:")
        for x in samples:
            lines.append(f"- `{x['selector']}` / `{x['property']}`")
            lines.append(f"  - Bu dosya: `{x['old']}`")
            lines.append(f"  - Sonradan ezen: `{x['later']}` → `{x['new']}`")
    else:
        lines.append("Ezilme detayı yok.")
    lines.append("")

lines.append("## 3) En çok sonradan ezen dosyalar")
lines.append("")
for f, arr in sorted(overrides_by_file.items(), key=lambda x: len(x[1]), reverse=True):
    lines.append(f"- `{f}` → **{len(arr)}** kuralı sonradan eziyor")
lines.append("")

Path("SEATS_CSS_OVERRIDE_REPORT.md").write_text("\n".join(lines), encoding="utf-8")

print("OK: SEATS_CSS_OVERRIDE_REPORT.md oluşturuldu")
print()
print("Riskli dosya özeti:")
for f in risk_files:
    total = total_by_file.get(f, 0)
    ov = len(overridden_by_file.get(f, []))
    makes = len(overrides_by_file.get(f, []))
    rate = round((ov / total * 100), 1) if total else 0
    print(f"- {f}: toplam={total}, ezilen={ov}, oran=%{rate}, kendisi_eziyor={makes}")
