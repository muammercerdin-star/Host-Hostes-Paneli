from pathlib import Path
import re

ROOT = Path(".").resolve()

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def line_no(text, idx):
    return text.count("\n", 0, idx) + 1

def print_header(title):
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)

def context_lines(path, text, pattern, before=14, after=28, max_hits=8):
    rx = re.compile(pattern, re.I | re.S)
    hits = list(rx.finditer(text))
    if not hits:
        return False

    print(f"\n--- {rel(path)} | {len(hits)} eşleşme | pattern: {pattern} ---")
    lines = text.splitlines()
    shown = 0

    for m in hits[:max_hits]:
        ln = line_no(text, m.start())
        a = max(1, ln - before)
        b = min(len(lines), ln + after)
        print(f"\n[Satır {ln} civarı]")
        for i in range(a, b + 1):
            print(f"{i:5d}: {lines[i-1]}")
        shown += 1

    if len(hits) > shown:
        print(f"\n... {len(hits) - shown} eşleşme daha var, rapor kısa tutuldu.")
    return True

def walk_files():
    roots = [
        Path("templates"),
        Path("static"),
        Path("modules"),
    ]
    exts = {".html", ".css", ".js", ".py"}
    skip_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", "env"}

    files = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if p.suffix.lower() not in exts:
                continue
            if any(part in skip_dirs for part in p.parts):
                continue
            files.append(p)
    return sorted(files, key=lambda x: rel(x))

files = walk_files()

V2_COLORS = {
    "--ink": "#0a0a0f",
    "--card": "#13131a",
    "--card2": "#1a1a24",
    "--line": "rgba(255,255,255,.06)",
    "--red": "#ff2d55",
    "--amber": "#ffcc00",
    "--blue": "#0a84ff",
    "--green": "#30d158",
    "--white": "#ffffff",
    "--dim": "rgba(255,255,255,.42)",
}

print_header("0) HEDEF V2 RENK PALETİ")
for k, v in V2_COLORS.items():
    print(f"{k:10s} = {v}")

print_header("1) seats.html ve base.html içinde CSS / JS yüklenme sırası")

for target in [Path("templates/base.html"), Path("templates/seats.html")]:
    if not target.exists():
        print(f"{rel(target)} yok")
        continue

    text = read(target)
    print(f"\n--- {rel(target)} ---")

    rx = re.compile(
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]*>|<script[^>]+src=["\']([^"\']+)["\'][^>]*>',
        re.I
    )

    found = False
    for m in rx.finditer(text):
        found = True
        ln = line_no(text, m.start())
        href = m.group(1)
        src = m.group(2)
        if href:
            print(f"{ln:5d}: CSS    {href}")
        if src:
            print(f"{ln:5d}: SCRIPT {src}")

    if not found:
        print("CSS/JS linki bulunamadı.")

print_header("2) seats.html içindeki inline <style> blokları")

seats = Path("templates/seats.html")
if seats.exists():
    text = read(seats)
    style_rx = re.compile(r'<style\b([^>]*)>', re.I)
    for m in style_rx.finditer(text):
        start_ln = line_no(text, m.start())
        end = text.find("</style>", m.end())
        end_ln = line_no(text, end) if end != -1 else "?"
        attrs = m.group(1) or ""
        idm = re.search(r'id=["\']([^"\']+)["\']', attrs, re.I)
        sid = idm.group(1) if idm else "-"
        print(f"{start_ln:5d}-{end_ln}: style id={sid}")

print_header("3) Canlı Durak Akışı HTML kaynağı nerede?")

UI_PATTERNS = [
    r"Canlı\s+Durak\s+Akışı",
    r"Canlı\s+Akış",
    r"Şu\s*Anki\s*Durak",
    r"Şu\s+anki\s+durak",
    r"Sıradaki\s+duraklar",
    r"Sıradaki\s+Durak",
    r"Kalan\s+mesafe",
    r"İnecek",
    r"Bagaj",
    r"Planında",
    r"Plan\s*dışı",
]

if seats.exists():
    text = read(seats)
    any_hit = False
    for pat in UI_PATTERNS:
        if context_lines(seats, text, pat, before=10, after=22, max_hits=4):
            any_hit = True
    if not any_hit:
        print("seats.html içinde görünen metinlerle doğrudan eşleşme bulunamadı.")
        print("Muhtemelen JS ile render ediliyor veya metin farklı yazılmış.")

print_header("4) Durak akışıyla ilgili tüm dosya eşleşmeleri")

TERMS = [
    "Canlı Durak Akışı",
    "Canlı Akış",
    "Şu Anki Durak",
    "Şu anki durak",
    "Sıradaki duraklar",
    "Kalan mesafe",
    "Planında",
    "Plan dışı",
    "liveStop",
    "speedState",
    "currentStop",
    "nextStop",
    "route-flow",
    "routeFlow",
    "stop-flow",
    "stopFlow",
    "route-stop",
    "stop-card",
    "current-card",
    "next-card",
    "timeline",
    "buildActualSchedule",
    "scheduleOffsetsForRoute",
    "planMap",
    "route_stop_coords",
    "stop_logs",
    "bag-badge",
    "bag-count",
    "bag-dir",
]

compiled = [(t, re.compile(re.escape(t), re.I)) for t in TERMS]

for p in files:
    text = read(p)
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        for term, rx in compiled:
            if rx.search(line):
                hits.append((i, term, line.strip()))
                break

    if not hits:
        continue

    print(f"\n--- {rel(p)} | {len(hits)} ilgili satır ---")
    for i, term, line in hits[:90]:
        print(f"{i:5d}: [{term}] {line[:220]}")
    if len(hits) > 90:
        print(f"... {len(hits)-90} satır daha var.")

print_header("5) CSS tarafında muhtemel selector / override kaynakları")

CSS_HINTS = [
    ".current-card",
    ".current-stop",
    ".next-card",
    ".next-stop",
    ".route-flow",
    ".route-stop",
    ".stop-flow",
    ".stop-card",
    ".timeline",
    ".flow",
    ".live",
    ".bag",
    ".route",
    ".status",
    ".stat",
    ".badge",
    ".chip",
]

for p in files:
    if p.suffix.lower() not in {".css", ".html"}:
        continue

    text = read(p)
    lines = text.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(h.lower() in low for h in CSS_HINTS):
            if "{" in line or "}" in line or ":" in line or "." in line or "#" in line:
                hits.append((i, line.rstrip()))

    if not hits:
        continue

    print(f"\n--- {rel(p)} | CSS aday satır: {len(hits)} ---")
    for i, line in hits[:120]:
        print(f"{i:5d}: {line[:240]}")
    if len(hits) > 120:
        print(f"... {len(hits)-120} satır daha var.")

print_header("6) JS tarafında canlı durak / mesafe / render kaynakları")

JS_HINTS = [
    "liveStop",
    "speedState",
    "currentStop",
    "nextStop",
    "render",
    "buildActualSchedule",
    "scheduleOffsetsForRoute",
    "planMap",
    "distance",
    "distKm",
    "stop_logs",
    "route_stop_coords",
    "bag",
    "tts",
    "speak",
]

for p in files:
    if p.suffix.lower() not in {".js", ".html"}:
        continue

    text = read(p)
    lines = text.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(h.lower() in low for h in JS_HINTS):
            hits.append((i, line.rstrip()))

    if not hits:
        continue

    print(f"\n--- {rel(p)} | JS aday satır: {len(hits)} ---")
    for i, line in hits[:140]:
        print(f"{i:5d}: {line[:260]}")
    if len(hits) > 140:
        print(f"... {len(hits)-140} satır daha var.")

print_header("7) Mevcut renk kodları envanteri")

color_rx = re.compile(
    r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]+\)|hsla?\([^)]+\)',
    re.I
)

for p in files:
    if p.suffix.lower() not in {".css", ".html", ".js"}:
        continue

    text = read(p)
    colors = []
    for m in color_rx.finditer(text):
        ln = line_no(text, m.start())
        colors.append((ln, m.group(0)))

    if not colors:
        continue

    unique = []
    seen = set()
    for ln, c in colors:
        key = c.lower().replace(" ", "")
        if key not in seen:
            seen.add(key)
            unique.append((ln, c))

    if not unique:
        continue

    # Çok alakasız dosyaları şişirmemek için sadece durak/seat/live/map geçenleri öne çıkar
    name = rel(p).lower()
    if not any(x in name for x in ["seat", "live", "map", "base", "continue"]):
        continue

    print(f"\n--- {rel(p)} | benzersiz renk: {len(unique)} ---")
    for ln, c in unique[:90]:
        print(f"{ln:5d}: {c}")
    if len(unique) > 90:
        print(f"... {len(unique)-90} renk daha var.")

print_header("8) SONUÇ İPUCU")
print("Bu rapora göre şunları belirleyeceğiz:")
print("1) Canlı Durak Akışı HTML'i templates/seats.html içinde mi, JS ile mi üretiliyor?")
print("2) Görünümü hangi CSS dosyası yönetiyor?")
print("3) En son hangi yama dosyası override ediyor?")
print("4) V2 renkleri ayrı bir scoped blokla mı eklenmeli, mevcut dosya mı düzenlenmeli?")
print("5) Koltuk planına dokunmadan sadece canlı akış bölümü hedeflenebilir mi?")
