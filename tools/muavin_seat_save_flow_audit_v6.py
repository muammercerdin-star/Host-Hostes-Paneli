from pathlib import Path
from datetime import datetime
import re
from collections import Counter, defaultdict

ROOT = Path(".").resolve()
ANDROID = ROOT / "android_app/app/src/main/python"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_seat_save_flow_audit_{STAMP}.md"

FILES = {
    "WEB seats.html": ROOT / "templates/seats.html",
    "WEB modals.html": ROOT / "templates/seats_parts/modals.html",
    "WEB seats.js": ROOT / "static/seats/seats.js",
    "WEB standing.js": ROOT / "static/seats/standing.js",
    "WEB manual-ticket-system.js": ROOT / "static/seats/patches/manual-ticket-system.js",
    "WEB seat-simple-ui-pack.js": ROOT / "static/seats/patches/seat-simple-ui-pack.js",
    "WEB modal-bottom-nav-autohide.js": ROOT / "static/seats/patches/modal-bottom-nav-autohide.js",
    "ANDROID seats.html": ANDROID / "templates/seats.html",
    "ANDROID modals.html": ANDROID / "templates/seats_parts/modals.html",
    "ANDROID seats.js": ANDROID / "static/seats/seats.js",
    "ANDROID standing.js": ANDROID / "static/seats/standing.js",
    "ANDROID manual-ticket-system.js": ANDROID / "static/seats/patches/manual-ticket-system.js",
    "ANDROID seat-simple-ui-pack.js": ANDROID / "static/seats/patches/seat-simple-ui-pack.js",
    "ANDROID modal-bottom-nav-autohide.js": ANDROID / "static/seats/patches/modal-bottom-nav-autohide.js",
}

KEYS = [
    "seatModal", "modal", "save", "Save", "kaydet", "Kaydet",
    "btnSave", "saveBtn", "submit", "preventDefault",
    "addEventListener", "onclick", "fetch(", "/api/",
    "/api/walkon", "/api/standing", "/api/stats", "/api/stoplog",
    "selectedSeat", "currentSeat", "seatNo", "trip_id", "tripId",
    "disabled", "classList", "show", "hide"
]

ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)
FETCH_RE = re.compile(r"""fetch\(\s*["'`]([^"'`]+)["'`]""")
EVENT_RE = re.compile(r"""(?:addEventListener\s*\(\s*["'`]([^"'`]+)["'`]|\.onclick\s*=|onsubmit\s*=)""")
QUERY_RE = re.compile(r"""(?:getElementById|querySelector|querySelectorAll)\(\s*["'`]([^"'`]+)["'`]""")
FUNC_RE = re.compile(r"""^\s*(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(|^\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function|\([^)]*\)\s*=>|[A-Za-z_$][\w$]*\s*=>)""", re.M)

def read(p):
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

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

def grep_keys(name, txt):
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in KEYS):
            s = line.strip()
            if len(s) > 220:
                s = s[:220] + "..."
            rows.append((name, i, s))
    return rows

summary = []
id_rows = []
dup_id_rows = []
fetch_rows = []
event_rows = []
query_rows = []
func_rows = []
key_rows = []

for name, path in FILES.items():
    txt = read(path)
    exists = path.exists()
    summary.append((name, "VAR" if exists else "YOK", str(path.relative_to(ROOT)) if exists else "-", txt.count("\n") + 1 if txt else 0))

    if not txt:
        continue

    ids = ID_RE.findall(txt)
    c = Counter(ids)
    for idv, count in c.items():
        id_rows.append((name, idv, count))
        if count > 1:
            dup_id_rows.append((name, idv, count))

    for m in FETCH_RE.finditer(txt):
        line = txt.count("\n", 0, m.start()) + 1
        fetch_rows.append((name, line, m.group(1)))

    for m in EVENT_RE.finditer(txt):
        line = txt.count("\n", 0, m.start()) + 1
        event_rows.append((name, line, m.group(1) or "onclick/onsubmit"))

    for m in QUERY_RE.finditer(txt):
        q = m.group(1)
        if any(x in q.lower() for x in ["save", "seat", "modal", "standing", "walkon", "trip", "btn"]):
            line = txt.count("\n", 0, m.start()) + 1
            query_rows.append((name, line, q))

    for m in FUNC_RE.finditer(txt):
        fn = m.group(1) or m.group(2)
        if fn and any(x in fn.lower() for x in ["seat", "save", "modal", "standing", "walk", "ticket", "submit", "stats"]):
            line = txt.count("\n", 0, m.start()) + 1
            func_rows.append((name, line, fn))

    key_rows.extend(grep_keys(name, txt))

# Cross-file ID use count
global_id = defaultdict(list)
for name, idv, count in id_rows:
    global_id[idv].append((name, count))

interesting_ids = []
for idv, places in global_id.items():
    low = idv.lower()
    if any(x in low for x in ["seat", "modal", "save", "standing", "walk", "trip", "btn"]):
        interesting_ids.append((idv, len(places), ", ".join(f"{n}({c})" for n, c in places)))

interesting_ids.sort(key=lambda x: (-x[1], x[0]))

# Endpoint counts
endpoint_counter = Counter(x[2] for x in fetch_rows)

md = []
md.append("# Muavin Asistanı Koltuk Kaydetme Akışı Audit V6")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez.")
md.append("")
md.append("## 1) İncelenen Dosyalar")
md.append(table(["Dosya etiketi", "Durum", "Yol", "Satır"], summary))
md.append("")
md.append("## 2) Fetch Endpointleri")
md.append(table(["Endpoint", "Geçiş"], endpoint_counter.most_common(80)))
md.append("")
md.append("## 3) Fetch Satırları")
md.append(table(["Dosya", "Satır", "Endpoint"], fetch_rows, 200))
md.append("")
md.append("## 4) Event Listener / Submit İzleri")
md.append(table(["Dosya", "Satır", "Event"], event_rows, 240))
md.append("")
md.append("## 5) Koltuk/Modal/Kaydet Query Selector İzleri")
md.append(table(["Dosya", "Satır", "Selector/ID"], query_rows, 240))
md.append("")
md.append("## 6) İlgili Fonksiyon Adayları")
md.append(table(["Dosya", "Satır", "Fonksiyon"], func_rows, 200))
md.append("")
md.append("## 7) Aynı Dosya İçinde Duplicate ID")
md.append(table(["Dosya", "ID", "Tekrar"], dup_id_rows, 120))
md.append("")
md.append("## 8) Koltuk/Modal/Kaydet ile İlgili ID'lerin Dosyalara Dağılımı")
md.append(table(["ID", "Dosya sayısı", "Yerler"], interesting_ids, 200))
md.append("")
md.append("## 9) Kritik Satır Taraması")
md.append(table(["Dosya", "Satır", "İçerik"], key_rows, 400))
md.append("")
md.append("## 10) İlk Teşhis Notu")
md.append("""
Bu rapordan sonra bakılacaklar:
1. Kaydet butonunun gerçek ID'si nedir?
2. Butona kaç farklı JS dosyası event bağlıyor?
3. Modal açılırken seçili koltuk değişkeni hangi isimle tutuluyor?
4. Kaydetme işlemi `/api/walkon`, `/api/standing` veya başka endpoint'e mi gidiyor?
5. İlk tıklamada endpoint çağrısı hiç gidiyor mu, yoksa çağrı gidip cevap mı hatalı?
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Koltuk kaydetme akışı audit hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
print("Fetch endpoint sayısı:", len(fetch_rows))
print("Event listener sayısı:", len(event_rows))
print("İlgili selector sayısı:", len(query_rows))
print("İlgili fonksiyon sayısı:", len(func_rows))
print("Duplicate ID:", len(dup_id_rows))
print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
