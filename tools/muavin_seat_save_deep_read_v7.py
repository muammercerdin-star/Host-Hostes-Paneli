from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
ANDROID = ROOT / "android_app/app/src/main/python"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_seat_save_deep_read_{STAMP}.md"

TARGETS = {
    "WEB modals.html": ROOT / "templates/seats_parts/modals.html",
    "WEB seats.js": ROOT / "static/seats/seats.js",
    "ANDROID modals.html": ANDROID / "templates/seats_parts/modals.html",
    "ANDROID seats.js": ANDROID / "static/seats/seats.js",
}

KEYS = [
    "btnSeatSave",
    "saveSeat",
    "openSeat",
    "closeSeat",
    "clearSeatUI",
    "offloadSeat",
    "seatModal",
    "seatBackdrop",
    "seatTitle",
    "currentSeat",
    "selectedSeat",
    "seatNo",
    "passenger",
    "from",
    "to",
    "price",
    "phone",
    "note",
    "dataset",
    "disabled",
    "localStorage",
    "persist",
    "render",
    "updateStats",
    "setSeatVisual",
    "addEventListener",
    "onclick",
]

LINE_WINDOWS = {
    "WEB modals.html": [(1, 120)],
    "ANDROID modals.html": [(1, 120)],
    "WEB seats.js": [(70, 125), (1160, 1210), (1360, 1475), (1475, 1545), (1545, 1615), (2400, 2510), (2790, 2850)],
    "ANDROID seats.js": [(70, 125), (1160, 1210), (1360, 1475), (1475, 1545), (1545, 1615), (2400, 2510), (2790, 2850)],
}

FUNC_NAMES = [
    "openModal",
    "closeModal",
    "openSeat",
    "closeSeat",
    "saveSeat",
    "clearSeatUI",
    "offloadSeat",
    "toggleSeatPick",
    "saveBulk",
    "updateStats",
    "setSeatVisual",
]

def read(p):
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def code_block(title, body, lang="js"):
    return f"### {title}\n```{lang}\n{body.rstrip()}\n```\n"

def numbered_slice(txt, start, end):
    lines = txt.splitlines()
    out = []
    for i in range(max(1, start), min(len(lines), end) + 1):
        out.append(f"{i:04d}: {lines[i-1]}")
    return "\n".join(out)

def grep_keys(txt):
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(k in line for k in KEYS):
            s = line.rstrip()
            if len(s) > 240:
                s = s[:240] + "..."
            rows.append((i, s))
    return rows

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

def extract_function(txt, name):
    lines = txt.splitlines()
    patterns = [
        re.compile(rf"^\s*(?:async\s+)?function\s+{re.escape(name)}\s*\("),
        re.compile(rf"^\s*(?:const|let|var)\s+{re.escape(name)}\s*="),
    ]

    start = None
    for i, line in enumerate(lines):
        if any(p.search(line) for p in patterns):
            start = i
            break

    if start is None:
        return ""

    brace_count = 0
    seen_brace = False
    end = start

    for j in range(start, len(lines)):
        line = lines[j]
        brace_count += line.count("{")
        brace_count -= line.count("}")
        if "{" in line:
            seen_brace = True
        end = j
        if seen_brace and brace_count <= 0 and j > start:
            break

    out = []
    for k in range(start, end + 1):
        out.append(f"{k+1:04d}: {lines[k]}")
    return "\n".join(out)

def analyze_save_logic(txt):
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        low = line.lower()
        if (
            "btnseatsave" in low or
            "saveseat" in low or
            "openseat" in low or
            "currentseat" in low or
            "selectedseat" in low or
            "passengers" in low or
            "updateStats" in line or
            "setSeatVisual" in line or
            "disabled" in low
        ):
            s = line.strip()
            if len(s) > 220:
                s = s[:220] + "..."
            rows.append((i, s))
    return rows

md = []
md.append("# Muavin Asistanı Koltuk Kaydetme Derin Okuma V7")
md.append("")
md.append(f"- Tarih: `{STAMP}`")
md.append("- Bu rapor sadece okuma/tespittir. Dosya değiştirmez.")
md.append("")

for label, path in TARGETS.items():
    txt = read(path)
    md.append(f"## {label}")
    md.append(f"- Yol: `{path.relative_to(ROOT)}`")
    md.append(f"- Satır: `{txt.count(chr(10)) + 1 if txt else 0}`")
    md.append("")

    md.append("### Kritik kelime satırları")
    md.append(table(["Satır", "İçerik"], grep_keys(txt), 200))
    md.append("")

    for a, b in LINE_WINDOWS.get(label, []):
        lang = "html" if "html" in label else "js"
        md.append(code_block(f"{label} satır {a}-{b}", numbered_slice(txt, a, b), lang))

    if label.endswith("seats.js"):
        md.append("### Fonksiyon gövdeleri")
        for fn in FUNC_NAMES:
            body = extract_function(txt, fn)
            if body:
                md.append(code_block(f"{label} :: {fn}", body, "js"))

        md.append("### Kayıt akışı özet satırları")
        md.append(table(["Satır", "İçerik"], analyze_save_logic(txt), 260))
        md.append("")

md.append("## İlk Okuma Soruları")
md.append("""
Bu raporda özellikle şunlara bakacağız:

1. `btnSeatSave` hangi satırda hangi fonksiyona bağlı?
2. `openSeat` seçili koltuğu hangi değişkende tutuyor?
3. `saveSeat` ilk satırlarında “koltuk yoksa çık” gibi erken return var mı?
4. Kaydet butonu tıklanınca buton disabled oluyor mu?
5. Kayıt yaptıktan sonra `closeSeat`, `render`, `updateStats`, `setSeatVisual` sırası doğru mu?
6. `manual-ticket-system.js` koltuk görseline ayrıca müdahale edip state’i geciktiriyor mu?
""")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Derin okuma raporu hazır:")
print(OUT)
print()
print("Görmek için:")
print(f"sed -n '1,360p' {OUT}")
