from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import hashlib
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_patch_inventory_{STAMP}.md"

ROOTS = {
    "WEB": ROOT,
    "ANDROID": ROOT / "android_app/app/src/main/python",
    "APK_PAYLOAD": ROOT / "apk_payload",
}

PATCH_NAME_RE = re.compile(
    r"(patch|fix|hotfix|step|final|mobile|voice|modal|seat-simple|stop-flow|bottom|fab|toggle|sync|disabled|bak)",
    re.I
)

BACKUP_RE = re.compile(r"(\.bak|backup|old|eski|copy|tmp|temp|deneme|test|audit|rapor)", re.I)
DISABLED_RE = re.compile(r"(\.disabled|disabled_)", re.I)

ASSET_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
STYLE_ID_RE = re.compile(r"""<style[^>]*\bid\s*=\s*["']([^"']+)["']""", re.I)
SCRIPT_ID_RE = re.compile(r"""<script[^>]*\bid\s*=\s*["']([^"']+)["']""", re.I)

def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def sha(p):
    try:
        h = hashlib.sha256()
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 256), b""):
                h.update(chunk)
        return h.hexdigest()[:12]
    except Exception:
        return "-"

def lc(p):
    if not p.exists() or p.suffix.lower() not in {".js", ".css", ".html", ".py"}:
        return ""
    t = read(p)
    return t.count("\n") + 1 if t else 0

def mt(p):
    try:
        return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "-"

def table(headers, rows, limit=None):
    if limit is not None:
        rows = rows[:limit]
    if not rows:
        return "_Kayıt yok._"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        out.append("| " + " | ".join(str(x).replace("|", "\\|").replace("\n", " ") for x in r) + " |")
    return "\n".join(out)

def clean_ref(ref):
    return ref.strip().split("?")[0].split("#")[0].strip()

def is_patch_ref(ref):
    low = ref.lower()
    return (
        "/patches/" in low or
        "patch" in low or
        "fix" in low or
        "hotfix" in low or
        "seat-simple" in low or
        "stop-flow" in low or
        "modal-bottom" in low or
        "manual-ticket" in low or
        "top-sound" in low or
        "bottom-voice" in low
    )

def resolve_ref(base, html, ref):
    ref = clean_ref(ref)
    if not ref:
        return None
    if ref.startswith("http://") or ref.startswith("https://") or ref.startswith("//"):
        return None
    if ref.startswith("/"):
        return base / ref.lstrip("/")
    if ref.startswith("static/"):
        return base / ref
    return html.parent / ref

def active_refs_for_root(base):
    rows = []
    refs = set()
    templates = base / "templates"
    if not templates.exists():
        return rows, refs

    for html in sorted(templates.rglob("*.html")):
        rel_html = str(html.relative_to(base))
        if BACKUP_RE.search(rel_html) or DISABLED_RE.search(rel_html):
            continue

        txt = read(html)
        for i, line in enumerate(txt.splitlines(), 1):
            for m in ASSET_RE.finditer(line):
                raw = m.group(1)
                ref = clean_ref(raw)
                if not is_patch_ref(ref):
                    continue
                target = resolve_ref(base, html, ref)
                exists = target.exists() if target else False
                rel_target = str(target.relative_to(base)) if target and exists else str(target.relative_to(base)) if target else "-"
                rows.append((rel_html, i, ref, rel_target, "VAR" if exists else "YOK"))
                if target:
                    try:
                        refs.add(str(target.resolve()))
                    except Exception:
                        refs.add(str(target))
    return rows, refs

def physical_patch_files_for_root(base):
    rows = []
    files = []

    static = base / "static"
    if not static.exists():
        return rows, files

    for p in sorted(static.rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(base))
        if not PATCH_NAME_RE.search(rel):
            continue
        if p.suffix.lower() not in {".js", ".css", ".html", ".txt", ".md"} and ".disabled" not in p.name:
            continue

        if DISABLED_RE.search(rel):
            status = "DISABLED"
        elif BACKUP_RE.search(rel):
            status = "BACKUP/ESKİ"
        else:
            status = "NORMAL"

        files.append(p)
        rows.append((rel, status, p.suffix.lower() or "[yok]", p.stat().st_size, lc(p), sha(p), mt(p)))
    return rows, files

def inline_patch_blocks(base):
    rows = []
    templates = base / "templates"
    if not templates.exists():
        return rows

    for html in sorted(templates.rglob("*.html")):
        rel_html = str(html.relative_to(base))
        if BACKUP_RE.search(rel_html) or DISABLED_RE.search(rel_html):
            continue

        txt = read(html)
        for m in STYLE_ID_RE.finditer(txt):
            sid = m.group(1)
            if PATCH_NAME_RE.search(sid):
                line = txt.count("\n", 0, m.start()) + 1
                rows.append((rel_html, line, "style", sid))
        for m in SCRIPT_ID_RE.finditer(txt):
            sid = m.group(1)
            if PATCH_NAME_RE.search(sid):
                line = txt.count("\n", 0, m.start()) + 1
                rows.append((rel_html, line, "script", sid))
    return rows

def patch_markers(base):
    rows = []
    for folder in ["templates", "static"]:
        root = base / folder
        if not root.exists():
            continue
        for p in sorted(root.rglob("*")):
            if not p.is_file():
                continue
            rel = str(p.relative_to(base))
            if BACKUP_RE.search(rel) or DISABLED_RE.search(rel):
                continue
            if p.suffix.lower() not in {".html", ".js", ".css"}:
                continue
            txt = read(p)
            for i, line in enumerate(txt.splitlines(), 1):
                if re.search(r"(PATCH|HOTFIX|FIX|STEP|YAMA|FINAL|V\d+)", line, re.I):
                    s = line.strip()
                    if len(s) > 180:
                        s = s[:180] + "..."
                    rows.append((rel, i, s))
    return rows

all_summary = []
all_active = {}
all_physical = {}
all_inline = {}
all_markers = {}
all_orphan = {}

for label, base in ROOTS.items():
    active_rows, active_refs = active_refs_for_root(base)
    physical_rows, physical_files = physical_patch_files_for_root(base)
    inline_rows = inline_patch_blocks(base)
    marker_rows = patch_markers(base)

    orphan_rows = []
    for p in physical_files:
        try:
            key = str(p.resolve())
        except Exception:
            key = str(p)
        rel = str(p.relative_to(base))
        if key not in active_refs and not DISABLED_RE.search(rel) and not BACKUP_RE.search(rel):
            orphan_rows.append((rel, p.suffix.lower(), p.stat().st_size, lc(p), sha(p), mt(p)))

    status_counter = Counter(r[1] for r in physical_rows)

    all_summary.append((
        label,
        len(active_rows),
        len(set(r[3] for r in active_rows if r[4] == "VAR")),
        sum(1 for r in active_rows if r[4] == "YOK"),
        len(physical_rows),
        status_counter.get("NORMAL", 0),
        status_counter.get("DISABLED", 0),
        status_counter.get("BACKUP/ESKİ", 0),
        len(orphan_rows),
        len(inline_rows),
        len(marker_rows),
    ))

    all_active[label] = active_rows
    all_physical[label] = physical_rows
    all_inline[label] = inline_rows
    all_markers[label] = marker_rows
    all_orphan[label] = orphan_rows

# WEB/ANDROID active linked patch hash comparison
web_active_map = {r[3]: ROOT / r[3] for r in all_active.get("WEB", []) if r[4] == "VAR"}
and_active_map = {r[3]: ROOTS["ANDROID"] / r[3] for r in all_active.get("ANDROID", []) if r[4] == "VAR"}

active_compare = []
for rel in sorted(set(web_active_map.keys()) | set(and_active_map.keys())):
    wp = web_active_map.get(rel)
    ap = and_active_map.get(rel)
    if wp and ap:
        status = "AYNI" if sha(wp) == sha(ap) else "FARKLI"
        active_compare.append((rel, status, sha(wp), sha(ap), lc(wp), lc(ap)))
    elif wp and not ap:
        active_compare.append((rel, "WEB VAR ANDROID YOK", sha(wp), "-", lc(wp), "-"))
    elif ap and not wp:
        active_compare.append((rel, "ANDROID VAR WEB YOK", "-", sha(ap), "-", lc(ap)))

md = []
md.append("# Muavin Asistanı Yama Envanteri V9")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("- Bu rapor sadece tespittir. Hiçbir dosya silinmedi/değiştirilmedi.")
md.append("")
md.append("## 1) Genel Yama Sayıları")
md.append(table([
    "Kök",
    "Aktif çağrı satırı",
    "Aktif benzersiz dosya",
    "Aktif ama dosya yok",
    "Fiziksel yama dosyası",
    "Normal",
    "Disabled",
    "Backup/Eski",
    "Orphan normal",
    "Inline yama",
    "Marker satırı",
], all_summary))
md.append("")
md.append("## 2) WEB ↔ ANDROID Aktif Yama Dosyası Karşılaştırması")
md.append(table(["Yama dosyası", "Durum", "WEB hash", "ANDROID hash", "WEB satır", "ANDROID satır"], active_compare, 200))
md.append("")

for label in ROOTS:
    md.append(f"## 3) {label} Aktif Çağrılan Yamalar")
    md.append(table(["Çağıran HTML", "Satır", "Ref", "Dosya", "Durum"], all_active[label], 250))
    md.append("")

    md.append(f"## 4) {label} Fiziksel Yama Dosyaları")
    md.append(table(["Dosya", "Durum", "Uzantı", "Byte", "Satır", "Hash", "Mtime"], all_physical[label], 300))
    md.append("")

    md.append(f"## 5) {label} Orphan Normal Yama Dosyaları")
    md.append("Bunlar dosyada var ama aktif template içinde çağrısı görünmedi. Direkt silinmez; JS dinamik çağırıyor olabilir.")
    md.append(table(["Dosya", "Uzantı", "Byte", "Satır", "Hash", "Mtime"], all_orphan[label], 200))
    md.append("")

    md.append(f"## 6) {label} Inline Yama Script/Style Blokları")
    md.append(table(["HTML", "Satır", "Tür", "ID"], all_inline[label], 200))
    md.append("")

    md.append(f"## 7) {label} Patch/Fix/Step Marker Satırları")
    md.append(table(["Dosya", "Satır", "İçerik"], all_markers[label], 300))
    md.append("")

md.append("## 8) İlk Karar Notu")
md.append("""
Bu rapordan sonra karar sırası:

1. Aktif çağrılan yama sayısı kaç?
2. WEB ve ANDROID aktif yamaları birebir aynı mı?
3. Son dönemde eklenen aktif yamalar hangileri?
4. Koltuk modalını etkileyen yamalar hangileri?
5. Disabled/orphan/backup yamalar temizlik adayı mı, yoksa arşive mi alınacak?

Şimdilik silme yok. Önce sayım ve sınıflandırma.
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Yama envanteri hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for r in all_summary:
    print(
        r[0],
        "| aktif çağrı:", r[1],
        "| aktif dosya:", r[2],
        "| fiziksel:", r[4],
        "| normal:", r[5],
        "| disabled:", r[6],
        "| backup/eski:", r[7],
        "| orphan:", r[8],
        "| inline:", r[9],
        "| marker:", r[10],
    )
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
