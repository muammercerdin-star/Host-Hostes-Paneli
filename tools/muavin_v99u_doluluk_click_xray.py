from pathlib import Path
from datetime import datetime
import re
import sys

ROOT = Path(".").resolve()

print("===== V99U DOLULUK CLICK RÖNTGEN =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "static/continue/continue_trip_v99_clean.css",
    ROOT / "static/continue/continue_doluluk_click_guard_v99t.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_doluluk_click_guard_v99t.js",
]

PATTERNS = [
    "doluluk",
    "DOLULUK",
    "occupancy",
    "seat-map",
    "seat map",
    "Koltuk Haritası",
    "Koltuk Haritasi",
    "openSeat",
    "openDoluluk",
    "openOccupancy",
    "showSeat",
    "showDoluluk",
    "addEventListener",
    "onclick",
    ".onclick",
    "click",
    "v99-stat",
    "v99-top",
    "v99-metric",
    "stat-grid",
    "metric-grid",
    "doluluk",
    "HIZ",
    "DURUM",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def show_lines(label, p, patterns=PATTERNS, max_lines=260):
    print()
    print("===== DOSYA:", label, "=====")
    print("PATH:", p)
    print("EXISTS:", p.exists(), "SIZE:", p.stat().st_size if p.exists() else "-")

    if not p.exists():
        return

    txt = read(p)
    hits = []

    for i, line in enumerate(txt.splitlines(), 1):
        low = line.lower()
        if any(x.lower() in low for x in patterns):
            hits.append((i, line.rstrip()))

    print("HIT_COUNT:", len(hits))

    for i, line in hits[:max_lines]:
        print(f"{i:5}: {line[:260]}")

    if len(hits) > max_lines:
        print("... kesildi, toplam:", len(hits))

print()
print("===== 1) DOSYA DURUMU =====")
for p in FILES:
    print(("VAR " if p.exists() else "YOK "), p, "size=", p.stat().st_size if p.exists() else "-")

print()
print("===== 2) TEMPLATE SCRIPT SIRASI =====")
tpl = read(ROOT / "templates/continue_trip.html")
for i, line in enumerate(tpl.splitlines(), 1):
    if "<script" in line and "src=" in line:
        print(f"{i:5}: {line.strip()}")

print()
print("===== 3) TEMPLATE ÜST KUTU / DOLULUK / PANEL SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    low = line.lower()
    if any(k.lower() in low for k in [
        "hiz", "hız", "doluluk", "durum",
        "v99-stat", "v99-top", "metric",
        "seat", "koltuk", "panel",
        "onclick", "data-"
    ]):
        print(f"{i:5}: {line[:260]}")

print()
print("===== 4) STATIC/CONTINUE JS DOSYALARINDA CLICK ARAMA =====")
js_files = sorted((ROOT / "static/continue").glob("*.js"))
for p in js_files:
    txt = read(p)
    if not txt:
        continue

    low = txt.lower()
    if any(k in low for k in [
        "doluluk", "occupancy", "seat-map", "koltuk haritas",
        "addEventListener(\"click".lower(),
        "addEventListener('click".lower(),
        ".onclick",
        "onclick"
    ]):
        print()
        print("JS:", p, "size=", p.stat().st_size)
        count = 0
        for i, line in enumerate(txt.splitlines(), 1):
            l = line.lower()
            if any(k.lower() in l for k in [
                "doluluk", "occupancy", "seat-map", "koltuk haritas",
                "addEventListener", ".onclick", "onclick", "click",
                "closest", "matches", "querySelector"
            ]):
                print(f"{i:5}: {line[:260]}")
                count += 1
                if count >= 220:
                    print("... kesildi")
                    break

print()
print("===== 5) ÖZEL: DOLULUK PANELİ AÇAN FONKSİYON ADAYLARI =====")
all_txt = ""
for p in [ROOT / "templates/continue_trip.html"] + js_files:
    all_txt += "\n/* FILE: " + str(p) + " */\n" + read(p)

funcs = re.findall(
    r"(function\s+[A-Za-z0-9_$]*?(?:Doluluk|Occupancy|Seat|Koltuk)[A-Za-z0-9_$]*\s*\([^)]*\)|const\s+[A-Za-z0-9_$]*?(?:Doluluk|Occupancy|Seat|Koltuk)[A-Za-z0-9_$]*\s*=\s*\([^)]*\)\s*=>|var\s+[A-Za-z0-9_$]*?(?:Doluluk|Occupancy|Seat|Koltuk)[A-Za-z0-9_$]*\s*=)",
    all_txt,
    flags=re.I
)

print("FUNC_ADAY_COUNT:", len(funcs))
for f in funcs[:80]:
    print("-", f[:200])

print()
print("===== 6) CLICK HANDLER BAĞLANDIĞI SELECTOR ADAYLARI =====")
selector_hits = re.findall(
    r"(querySelector(?:All)?\([^)]{0,120}\)|closest\([^)]{0,120}\)|matches\([^)]{0,120}\))",
    all_txt,
    flags=re.I
)

wanted = []
for h in selector_hits:
    low = h.lower()
    if any(k in low for k in ["doluluk", "occup", "seat", "koltuk", "stat", "metric", "top"]):
        wanted.append(h)

print("SELECTOR_HIT_COUNT:", len(wanted))
for h in wanted[:160]:
    print("-", h[:220])

print()
print("===== 7) RENDER HTML KONTROL =====")
try:
    sys.path.insert(0, str(ROOT))
    from app import app

    out = ROOT / "run_logs" / "v99u_doluluk_click_render.html"
    out.parent.mkdir(exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99u_xray", follow_redirects=False)
        html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(html, encoding="utf-8")

        print("STATUS:", r.status_code)
        print("HTML_SIZE:", len(html))
        print("OUT:", out)

        print()
        print("HTML içinde üst stat / doluluk adayları:")
        for i, line in enumerate(html.splitlines(), 1):
            low = line.lower()
            if any(k.lower() in low for k in [
                "doluluk", "hiz", "hız", "durum",
                "v99-stat", "v99-top", "metric",
                "onclick", "data-"
            ]):
                print(f"{i:5}: {line[:260]}")

except Exception as e:
    print("RENDER HATA:", repr(e))

print()
print("===== 8) SONUÇ OKUMA REHBERİ =====")
print("Eğer click handler .v99-stat-grid / .v99-stats / üst satır parent elemana bağlıysa sorun bu.")
print("Doğru hedef sadece DOLULUK kutusunun kendi class/id'si olmalı.")
print("Bu röntgen dosyaya dokunmadı.")

print()
print("===== RAPOR BİTTİ =====")
