from pathlib import Path
from datetime import datetime
from collections import Counter
import hashlib
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_patch_inventory_v10_{STAMP}.md"

ROOTS = {
    "WEB": ROOT,
    "ANDROID": ROOT / "android_app/app/src/main/python",
    "APK_PAYLOAD": ROOT / "apk_payload",
}

ASSET_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)

PATCH_HINT_RE = re.compile(
    r"(patches/|patch|fix|hotfix|seat-simple|stop-flow|modal-bottom|manual-ticket|top-sound|bottom-voice|fab|mobile-performance|voice-commands|voice-tts|seats-final)",
    re.I
)

DANGEROUS_FOR_SEAT_MODAL = [
    "manual-ticket-system",
    "modal-bottom-nav-autohide",
    "seat-simple-ui-pack",
    "seat-layout-fab-pack",
    "mobile-performance-fix",
    "stop-flow-focus-patch",
    "stop-selected-toast",
    "top-sound-toggle",
    "bottom-voice-command",
]

BACKUP_FILE_RE = re.compile(r"(\.bak|backup|old|eski|copy|tmp|temp|deneme|audit|rapor)", re.I)
TEST_FILE_RE = re.compile(r"(^|[._-])test([._-]|$)", re.I)
DISABLED_RE = re.compile(r"(\.disabled|disabled_)", re.I)

def is_backup_like(path: Path):
    rel_parts = path.parts
    name = path.name.lower()
    if "backups" in rel_parts:
        return True
    if "_unused_review" in rel_parts:
        return True
    if BACKUP_FILE_RE.search(name):
        return True
    if TEST_FILE_RE.search(name):
        return True
    return False

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
    if not p.exists():
        return ""
    if p.suffix.lower() not in {".js", ".css", ".html", ".py"}:
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

def scan_active_assets(base):
    rows = []
    active_paths = set()

    tpl = base / "templates"
    if not tpl.exists():
        return rows, active_paths

    for html in sorted(tpl.rglob("*.html")):
        if is_backup_like(html):
            continue

        txt = read(html)
        rel_html = str(html.relative_to(base))

        for i, line in enumerate(txt.splitlines(), 1):
            for m in ASSET_RE.finditer(line):
                raw = m.group(1)
                ref = clean_ref(raw)

                if not PATCH_HINT_RE.search(ref):
                    continue

                target = resolve_ref(base, html, ref)
                if not target:
                    continue

                exists = target.exists()
                rel_target = str(target.relative_to(base)) if target.is_absolute() and str(target).startswith(str(base)) else str(target)

                rows.append((
                    rel_html,
                    i,
                    raw,
                    rel_target,
                    "VAR" if exists else "YOK",
                    "ŞÜPHELİ-MODAL" if any(x in rel_target for x in DANGEROUS_FOR_SEAT_MODAL) else ""
                ))

                if exists:
                    active_paths.add(str(target.resolve()))

    return rows, active_paths

def scan_physical_patches(base):
    rows = []
    files = []

    static = base / "static"
    if not static.exists():
        return rows, files

    for p in sorted(static.rglob("*")):
        if not p.is_file():
            continue

        rel = str(p.relative_to(base))

        if not PATCH_HINT_RE.search(rel):
            continue

        if p.suffix.lower() not in {".js", ".css"} and ".disabled" not in p.name:
            continue

        if DISABLED_RE.search(rel):
            status = "DISABLED"
        elif is_backup_like(p):
            status = "BACKUP/ESKİ"
        else:
            status = "NORMAL"

        risk = "ŞÜPHELİ-MODAL" if any(x in rel for x in DANGEROUS_FOR_SEAT_MODAL) else ""

        rows.append((rel, status, risk, p.suffix.lower() or "[yok]", p.stat().st_size, lc(p), sha(p), mt(p)))
        files.append(p)

    return rows, files

def scan_template_patch_lines(base):
    rows = []
    tpl = base / "templates"
    if not tpl.exists():
        return rows

    for html in sorted(tpl.rglob("*.html")):
        if is_backup_like(html):
            continue
        txt = read(html)
        rel = str(html.relative_to(base))
        for i, line in enumerate(txt.splitlines(), 1):
            if PATCH_HINT_RE.search(line):
                s = line.strip()
                if len(s) > 220:
                    s = s[:220] + "..."
                rows.append((rel, i, s))
    return rows

summary = []
active_by_root = {}
physical_by_root = {}
orphan_by_root = {}
template_lines_by_root = {}

for label, base in ROOTS.items():
    active_rows, active_set = scan_active_assets(base)
    physical_rows, physical_files = scan_physical_patches(base)
    template_lines = scan_template_patch_lines(base)

    orphan = []
    for p in physical_files:
        rel = str(p.relative_to(base))
        key = str(p.resolve())
        if key not in active_set and not DISABLED_RE.search(rel) and not is_backup_like(p):
            orphan.append((rel, p.suffix.lower(), p.stat().st_size, lc(p), sha(p), mt(p)))

    status_counter = Counter(r[1] for r in physical_rows)

    summary.append((
        label,
        len(active_rows),
        len(set(r[3] for r in active_rows if r[4] == "VAR")),
        sum(1 for r in active_rows if r[4] == "YOK"),
        len(physical_rows),
        status_counter.get("NORMAL", 0),
        status_counter.get("DISABLED", 0),
        status_counter.get("BACKUP/ESKİ", 0),
        len(orphan),
        sum(1 for r in active_rows if r[5] == "ŞÜPHELİ-MODAL"),
        len(template_lines),
    ))

    active_by_root[label] = active_rows
    physical_by_root[label] = physical_rows
    orphan_by_root[label] = orphan
    template_lines_by_root[label] = template_lines

# WEB/ANDROID active comparison by same relative target
web_map = {r[3]: ROOT / r[3] for r in active_by_root.get("WEB", []) if r[4] == "VAR"}
and_base = ROOTS["ANDROID"]
and_map = {r[3]: and_base / r[3] for r in active_by_root.get("ANDROID", []) if r[4] == "VAR"}

compare = []
for rel in sorted(set(web_map) | set(and_map)):
    wp = web_map.get(rel)
    ap = and_map.get(rel)
    risk = "ŞÜPHELİ-MODAL" if any(x in rel for x in DANGEROUS_FOR_SEAT_MODAL) else ""

    if wp and ap:
        compare.append((rel, "AYNI" if sha(wp) == sha(ap) else "FARKLI", risk, sha(wp), sha(ap), lc(wp), lc(ap)))
    elif wp:
        compare.append((rel, "WEB VAR ANDROID YOK", risk, sha(wp), "-", lc(wp), "-"))
    else:
        compare.append((rel, "ANDROID VAR WEB YOK", risk, "-", sha(ap), "-", lc(ap)))

recent_rows = []
for row in physical_by_root.get("WEB", []):
    rel, status, risk, ext, byte, line, h, mtime = row
    recent_rows.append((mtime, rel, status, risk, ext, line, h))
recent_rows.sort(reverse=True)

md = []
md.append("# Muavin Asistanı Yama Envanteri V10")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("- V9 hatası düzeltildi: `templates` klasörü artık `test` sanılıp atlanmıyor.")
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
    "Modal şüpheli aktif çağrı",
    "Template patch satırı",
], summary))
md.append("")
md.append("## 2) WEB ↔ ANDROID Aktif Yama Karşılaştırması")
md.append(table(["Yama dosyası", "Durum", "Risk", "WEB hash", "ANDROID hash", "WEB satır", "ANDROID satır"], compare, 200))
md.append("")
md.append("## 3) WEB Aktif Çağrılan Yamalar")
md.append(table(["Çağıran HTML", "Satır", "Ref", "Dosya", "Durum", "Risk"], active_by_root["WEB"], 260))
md.append("")
md.append("## 4) ANDROID Aktif Çağrılan Yamalar")
md.append(table(["Çağıran HTML", "Satır", "Ref", "Dosya", "Durum", "Risk"], active_by_root["ANDROID"], 260))
md.append("")
md.append("## 5) WEB Fiziksel Yama Dosyaları")
md.append(table(["Dosya", "Durum", "Risk", "Uzantı", "Byte", "Satır", "Hash", "Mtime"], physical_by_root["WEB"], 300))
md.append("")
md.append("## 6) WEB Orphan Normal Yama Dosyaları")
md.append("Dosyada var ama aktif HTML çağrısı bulunmadı. Direkt silinmez; önce dinamik kullanım kontrolü gerekir.")
md.append(table(["Dosya", "Uzantı", "Byte", "Satır", "Hash", "Mtime"], orphan_by_root["WEB"], 200))
md.append("")
md.append("## 7) WEB Son Değişen Yama Dosyaları")
md.append(table(["Mtime", "Dosya", "Durum", "Risk", "Uzantı", "Satır", "Hash"], recent_rows, 80))
md.append("")
md.append("## 8) WEB Template İçinde Patch/Yama Satırları")
md.append(table(["Template", "Satır", "İçerik"], template_lines_by_root["WEB"], 300))
md.append("")
md.append("## 9) İlk Karar Notu")
md.append("""
Bu rapordan sonra:
1. Aktif çalışan yama sayısı kesinleşecek.
2. Koltuk modalını etkileyen aktif yamalar ayrılacak.
3. Sonradan eklenen ama aktif olan dosyalar incelenecek.
4. Orphan/disabled/backuplar temizlik adayı olarak sınıflandırılacak.
5. Silme hâlâ yok; önce rapor, sonra kontrollü arşivleme.
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Yama envanteri V10 hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for r in summary:
    print(
        r[0],
        "| aktif çağrı:", r[1],
        "| aktif dosya:", r[2],
        "| fiziksel:", r[4],
        "| normal:", r[5],
        "| disabled:", r[6],
        "| orphan:", r[8],
        "| modal şüpheli:", r[9],
    )
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
