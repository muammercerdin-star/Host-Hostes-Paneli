from pathlib import Path
from datetime import datetime
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

print("===== MUAVIN V99 ROUTE SYSTEM REPORT =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

FILES = {
    "WEB_TEMPLATE": ROOT / "templates/continue_trip.html",
    "WEB_CSS": ROOT / "static/continue/continue_trip_v99_clean.css",
    "WEB_JS": ROOT / "static/continue/continue_trip_v99_clean.js",
    "OLD_CSS": ROOT / "static/continue/continue_trip.css",
    "CORE_JS": ROOT / "static/continue/continue_trip_core.js",
    "UI_JS": ROOT / "static/continue/continue_trip_ui.js",
    "ANDROID_TEMPLATE": ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
    "ANDROID_CSS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
    "ANDROID_JS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
    "APP": ROOT / "app.py",
}

def sha(p):
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    except Exception:
        return "-"

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

print()
print("===== 1) DOSYA DURUMU =====")
for name, p in FILES.items():
    if p.exists():
        print(f"{name:18} VAR  size={p.stat().st_size:<8} sha={sha(p)}  {p}")
    else:
        print(f"{name:18} YOK  {p}")

print()
print("===== 2) WEB / ANDROID SENKRON =====")
pairs = [
    ("TEMPLATE", FILES["WEB_TEMPLATE"], FILES["ANDROID_TEMPLATE"]),
    ("CSS", FILES["WEB_CSS"], FILES["ANDROID_CSS"]),
    ("JS", FILES["WEB_JS"], FILES["ANDROID_JS"]),
]
for label, a, b in pairs:
    if a.exists() and b.exists():
        print(f"{label:10} {'AYNI' if sha(a)==sha(b) else 'FARKLI'}  web={sha(a)} android={sha(b)}")
    else:
        print(f"{label:10} KONTROL_EDILEMEDI")

tpl = read(FILES["WEB_TEMPLATE"])
css = read(FILES["WEB_CSS"])
js = read(FILES["WEB_JS"])
app = read(FILES["APP"])

print()
print("===== 3) TEMPLATE KRITIK IZLER =====")
for key in [
    "continue_trip_v99_clean.css",
    "continue_trip_v99_clean.js",
    "v99-prox-card",
    "v99-tl",
    "v99-tl-node {{ stop.kind }}",
    "v99-pill passed",
    "v99-pill live",
    "v99-pill next",
    "liveCurrentStopName",
    "liveDistanceValue",
    "liveOffloadMetric",
    "liveBagajMetric",
    "CONTINUE_BOOT",
    "v97_proximity_preview.css",
    "v97_real_data.css",
    "V99B_",
    "V99C_",
]:
    print(("VAR  " if key in tpl else "YOK  ") + key)

print()
print("===== 4) CSS / JS MARKER KONTROL =====")
for key in [
    "V99B_",
    "V99C_",
    ".v99-tl-node.passed",
    ".v99-tl-line.passed",
    ".v99-pill.passed",
    "passed-card",
    ".v99-tl-card.live-card",
    ".v99-tl-card.next-card",
]:
    print(("CSS VAR  " if key in css else "CSS YOK  ") + key)

for key in [
    "V99B_",
    "V99C_",
    "setRouteProgress",
    "setRing",
    "MuavinV99CleanSync",
]:
    print(("JS  VAR  " if key in js else "JS  YOK  ") + key)

print()
print("===== 5) APP.PY LIVE_STOPS / PASSED IZLERI =====")
lines = app.splitlines()
patterns = ["def continue_trip", "live_stops", "passed", "upcoming", "next", "live_current", "current_idx", "selected_stops"]
for i, line in enumerate(lines, 1):
    if any(p in line for p in patterns):
        if 1600 <= i <= 1900 or "def continue_trip" in line:
            print(f"{i:5}: {line[:180]}")

print()
print("===== 6) FLASK RENDER TEST =====")
try:
    from app import app as flask_app, get_active_trip, get_active_trip_row

    with flask_app.app_context():
        tid = get_active_trip()
        row = get_active_trip_row()
        print("ACTIVE_TRIP_ID:", tid)
        if row:
            try:
                print("ACTIVE_TRIP_ROUTE:", row["route"])
                print("ACTIVE_TRIP_PLATE:", row["plate"])
            except Exception:
                print("ACTIVE_TRIP_ROW:", dict(row))
        else:
            print("ACTIVE_TRIP_ROW: YOK")

    out = ROOT / "run_logs" / "v99_route_report_render.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    with flask_app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99_report", follow_redirects=False)
        html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(html, encoding="utf-8")

        print("STATUS:", r.status_code)
        print("LOCATION:", r.headers.get("Location", ""))
        print("HTML_SIZE:", len(html))
        print("OUT:", out)

        print()
        print("===== 7) RENDER HTML V99 IZLERI =====")
        for key in [
            "v99-prox-card",
            "v99-tl-node",
            "v99-pill passed",
            "v99-pill live",
            "v99-pill next",
            "v99-pill upcoming",
            "liveCurrentStopName",
            "liveDistanceValue",
            "ringFill",
            "CONTINUE_BOOT",
            "Traceback",
            "UndefinedError",
            "Internal Server Error",
        ]:
            print(("HTML VAR  " if key in html else "HTML YOK  ") + key)

        print()
        print("===== 8) TIMELINE KART ANALIZI =====")
        cards = re.findall(
            r'<div class="v99-tl-stop-name[^"]*">\s*([^<]+?)\s*</div>.*?<div class="v99-pill\s+([^"]+)">\s*([^<]+?)\s*</div>',
            html,
            re.S
        )

        if not cards:
            print("TIMELINE_KART_BULUNAMADI")
        else:
            counts = {}
            for name, cls, pill in cards:
                cls = cls.strip()
                counts[cls] = counts.get(cls, 0) + 1

            print("KART_SAYISI:", len(cards))
            print("STATUS_SAYILARI:", counts)

            print()
            print("ILK_20_KART:")
            for idx, (name, cls, pill) in enumerate(cards[:20], 1):
                print(f"{idx:02d}. {name.strip():30} | {cls.strip():10} | {pill.strip()}")

except Exception as e:
    print("RENDER_TEST_HATA:", repr(e))

print()
print("===== 9) BACKUP OZETI =====")
for folder in [
    ROOT / "templates",
    ROOT / "static/continue",
    ROOT / "android_app/app/src/main/python/templates",
    ROOT / "android_app/app/src/main/python/static/continue",
]:
    if not folder.exists():
        continue
    baks = sorted(folder.glob("*v99*"), key=lambda p: p.stat().st_mtime, reverse=True)[:12]
    print()
    print("KLASOR:", folder)
    for b in baks:
        print(" -", b.name)

print()
print("===== RAPOR BITTI =====")
