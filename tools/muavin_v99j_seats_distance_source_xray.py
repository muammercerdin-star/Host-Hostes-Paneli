from pathlib import Path
from datetime import datetime
import sys, re, json
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

print("===== V99J SEATS GERCEK KM KAYNAGI RONTGEN =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

from app import app, get_active_trip, get_active_trip_row

TARGETS = [
    "Ortahan",
    "Kardeşler pide salonu",
    "Belenyaka",
    "Alaşehir Otogar",
    "Salihli Garaj",
    "Sart",
]

NEEDLES = [
    "12.5", "12,5", "12.50",
    "46.7", "46,7",
    "Alaşehir Otogar",
    "Salihli Garaj",
    "Plan/ETA",
    "Durum",
    "eta",
    "distance",
    "km",
]

def short(x, n=260):
    s = str(x)
    s = s.replace("\n", " ")
    return s[:n]

def walk(obj, path="root", hits=None):
    if hits is None:
        hits = []

    if isinstance(obj, dict):
        joined = json.dumps(obj, ensure_ascii=False, default=str)
        if any(t in joined for t in TARGETS) or any(n in joined for n in NEEDLES[:6]):
            hits.append((path, obj))
        for k, v in obj.items():
            walk(v, path + "." + str(k), hits)

    elif isinstance(obj, list):
        for i, v in enumerate(obj[:500]):
            walk(v, path + f"[{i}]", hits)

    else:
        s = str(obj)
        if any(t in s for t in TARGETS) or any(n in s for n in NEEDLES):
            hits.append((path, obj))

    return hits

def print_hits(label, data):
    hits = walk(data)
    print()
    print("===== API HIT:", label, "=====")
    print("HIT_COUNT:", len(hits))

    shown = 0
    for path, val in hits:
        if shown >= 80:
            print("... devamı kesildi")
            break

        if isinstance(val, dict):
            keys = list(val.keys())
            joined = json.dumps(val, ensure_ascii=False, default=str)
            print("PATH:", path)
            print("KEYS:", keys)
            print("VAL :", short(joined, 420))
        else:
            print("PATH:", path, "=", short(val, 300))
        shown += 1

def grep_file(p, patterns, max_lines=160):
    if not p.exists():
        return []

    out = []
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(pt.lower() in low for pt in patterns):
            out.append((i, line[:260]))
            if len(out) >= max_lines:
                break

    return out

with app.app_context():
    tid = get_active_trip()
    trip = get_active_trip_row()

    print()
    print("===== 1) AKTIF SEFER =====")
    print("ACTIVE_TRIP_ID:", tid)

    if trip:
        print("ROUTE:", trip["route"])
        print("PLATE:", trip["plate"] or "")
        print("DATE:", trip["date"] or "")

    print()
    print("===== 2) FLASK API RULES LIVE / SEAT / STOP =====")
    for r in sorted(app.url_map.iter_rules(), key=lambda x: str(x.rule)):
        s = str(r.rule)
        if any(k in s.lower() for k in ["live", "seat", "stop", "route"]):
            print(f"{s:55} -> {r.endpoint}")

    out_dir = ROOT / "run_logs"
    out_dir.mkdir(exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        urls = [
            "/api/live-seat-map",
            f"/api/live-seat-map?trip_id={tid}",
            f"/api/live-runtime-state?trip_id={tid}",
        ]

        for stop in TARGETS:
            urls.append("/api/live-stop-detail?stop=" + quote(stop))
            urls.append("/api/live-seat-destination?stop=" + quote(stop))
            urls.append("/api/live-stop-offload?stop=" + quote(stop))

        print()
        print("===== 3) API CEVAPLARI ICINDE 12.5 / ALAŞEHIR / KM ARAMA =====")

        for url in urls:
            try:
                r = c.get(url)
                raw = r.get_data().decode("utf-8", errors="ignore")
                print()
                print("URL:", url)
                print("STATUS:", r.status_code, "SIZE:", len(raw), "TYPE:", r.headers.get("Content-Type", ""))

                save = out_dir / ("v99j_" + re.sub(r"[^a-zA-Z0-9]+", "_", url).strip("_")[:90] + ".txt")
                save.write_text(raw, encoding="utf-8", errors="ignore")
                print("OUT:", save)

                try:
                    data = json.loads(raw)
                    print_hits(url, data)
                except Exception:
                    if any(n in raw for n in NEEDLES):
                        for m in re.finditer("|".join(re.escape(n) for n in NEEDLES), raw):
                            a = max(0, m.start() - 160)
                            b = min(len(raw), m.end() + 260)
                            print("TEXT_HIT:", short(raw[a:b], 500))
                            break
                    else:
                        print("JSON değil / hedef iz yok")

            except Exception as e:
                print()
                print("URL_HATA:", url, repr(e))

print()
print("===== 4) KOLTUK EKRANI JS / TEMPLATE KAYNAK TARAMA =====")

FILES = [
    ROOT / "templates/seats.html",
    ROOT / "templates/seats.htm",
    ROOT / "static/seats/seats.js",
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "app.py",
]

PATTERNS = [
    "Durak Akışı",
    "Plan/ETA",
    "live-seat-map",
    "live-stop-detail",
    "live-seat-destination",
    "distance_km",
    "distanceKm",
    "distance",
    "gps_km",
    "routeCoords",
    "runtimeGpsKm",
    "eta_sub",
    "stop-distance-value",
    "selected stop",
    "selectedStop",
    "flow",
    "km",
]

for p in FILES:
    print()
    print("DOSYA:", p)
    hits = grep_file(p, PATTERNS, 220)
    print("HIT:", len(hits))
    for i, line in hits[:220]:
        print(f"{i:5}: {line}")

print()
print("===== 5) OZEL: 12.5 / 46.7 DOSYA ARAMA =====")
for p in FILES:
    if not p.exists():
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    if "12.5" in txt or "46.7" in txt or "12,5" in txt or "46,7" in txt:
        print("BULUNDU:", p)
        for i, line in enumerate(txt.splitlines(), 1):
            if any(x in line for x in ["12.5", "46.7", "12,5", "46,7"]):
                print(f"{i:5}: {line[:260]}")

print()
print("===== RAPOR BITTI =====")
