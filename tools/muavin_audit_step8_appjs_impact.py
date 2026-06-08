from pathlib import Path
import re

ROOT = Path(".").resolve()

print("===== MUAVİN ASİSTANI STEP-8 app.js ETKİ ALANI DENETİMİ =====")
print("ROOT:", ROOT)
print()

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def section(t):
    print()
    print("===== " + t + " =====")

def line_hits(path, patterns):
    txt = read(path)
    lines = txt.splitlines()
    out = []
    for i, line in enumerate(lines, 1):
        for pat in patterns:
            if pat in line:
                out.append((i, pat, line.strip()[:220]))
    return out

templates = []
for folder in ["templates", "android_app/app/src/main/python/templates"]:
    base = ROOT / folder
    if base.exists():
        templates += sorted(base.rglob("*.html"))

section("1) base.html kullanan ve .seat izi taşıyan sayfalar")

for p in templates:
    txt = read(p)
    uses_base = 'extends "base.html"' in txt or "extends 'base.html'" in txt
    has_seat_data_num = "data-num" in txt or ".seat[data-num]" in txt or 'class="seat' in txt or "class='seat" in txt
    has_static_seats_js = "seats.js" in txt or "/static/seats" in txt
    has_block_scripts = "block scripts" in txt

    if uses_base or has_seat_data_num or has_static_seats_js:
        print()
        print(f"--- {rel(p)} ---")
        print("uses_base:", uses_base)
        print("has_seat_marker:", has_seat_data_num)
        print("has_static_seats_js:", has_static_seats_js)
        print("has_block_scripts:", has_block_scripts)

        for i, pat, line in line_hits(p, [
            'extends "base.html"',
            "extends 'base.html'",
            "data-num",
            ".seat[data-num]",
            'class="seat',
            "class='seat",
            "seats.js",
            "/static/seats",
            "block scripts",
        ])[:80]:
            print(f"{i:5}: [{pat}] {line}")

section("2) static/app.js otomatik çalışan kısım")

for path in ["static/app.js", "android_app/app/src/main/python/static/app.js"]:
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if not p.exists():
        print("yok")
        continue

    lines = read(p).splitlines()
    for i, line in enumerate(lines, 1):
        if "DOMContentLoaded" in line or "bindSeats" in line or "apiLoad" in line or "querySelectorAll" in line or "addEventListener" in line:
            s = max(1, i-4)
            e = min(len(lines), i+8)
            print()
            print(f"### satır {i}")
            for j in range(s, e+1):
                mark = ">>" if j == i else "  "
                print(f"{mark} {j:5}: {lines[j-1]}")

section("3) seats.html script yükleme sırası")

for path in ["templates/seats.html", "android_app/app/src/main/python/templates/seats.html"]:
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if not p.exists():
        print("yok")
        continue

    for i, pat, line in line_hits(p, [
        "extends",
        "block scripts",
        "app.js",
        "seats.js",
        "voice-commands.js",
        "DOMContentLoaded",
        "data-num",
        "seat_no",
    ]):
        print(f"{i:5}: [{pat}] {line}")

section("4) base.html script yükleme sırası")

for path in ["templates/base.html", "android_app/app/src/main/python/templates/base.html"]:
    p = ROOT / path
    print()
    print(f"--- {path} ---")
    if not p.exists():
        print("yok")
        continue

    lines = read(p).splitlines()
    for i, line in enumerate(lines, 1):
        if "<script" in line or "block scripts" in line or "jquery" in line.lower() or "app.js" in line:
            print(f"{i:5}: {line}")

section("5) Eksik / eski endpointleri gerçek kullanan aktif dosyalar")

patterns = [
    "/api/seats",
    "/api/seat/clear",
    "/api/report/seat-detail",
    "/api/consignments/${id}/status",
    "/api/route-stop",
]

skip_dirs = {".git", "__pycache__", "audit_reports", "node_modules", ".gradle", "build", "dist"}
for p in ROOT.rglob("*"):
    if any(part in skip_dirs for part in p.parts):
        continue
    if not p.is_file() or p.suffix.lower() not in {".html", ".js", ".py"}:
        continue

    s = str(p).replace("\\", "/")
    if "/vendor/" in s or "/backups/" in s or "/apk_payload/" in s or "/tools/" in s:
        continue

    txt = read(p)
    found = False
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        for pat in patterns:
            if pat in line:
                rows.append((i, pat, line.strip()[:220]))
                found = True

    if found:
        print()
        print(f"--- {rel(p)} ---")
        for i, pat, line in rows:
            print(f"{i:5}: [{pat}] {line}")

print()
print("===== STEP-8 BİTTİ =====")
