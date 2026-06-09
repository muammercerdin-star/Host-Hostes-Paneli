from pathlib import Path
import importlib.util
import json
import math

ROOT = Path(".").resolve()

# IMPORT_PATH_FIX_V68B
# Bu script tools/ klasöründen çalıştığı için app.py içindeki yerel modülleri bulsun.
import sys
for _p in [
    ROOT,
    ROOT / "modules",
    ROOT / "blueprints",
    ROOT / "routes",
    ROOT / "utils",
]:
    _sp = str(_p)
    if _sp not in sys.path:
        sys.path.insert(0, _sp)
APP_PATH = ROOT / "app.py"

print("===== ROUTE COORDS DEEP CHECK V68 =====")
print("ROOT:", ROOT)
print()

def norm(v):
    s = (v or "").strip().lower()
    for ch in ["–", "-", "_", "/", "\\", ".", ",", "(", ")", "[", "]"]:
        s = s.replace(ch, " ")
    return " ".join(s.split())

def dist_km(a, b):
    R = 6371
    lat1 = math.radians(float(a["lat"]))
    lat2 = math.radians(float(b["lat"]))
    dlat = math.radians(float(b["lat"]) - float(a["lat"]))
    dlng = math.radians(float(b["lng"]) - float(a["lng"]))
    h = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng/2)**2
    return 2 * R * math.asin(math.sqrt(h))

if not APP_PATH.exists():
    print("❌ app.py yok")
    raise SystemExit

spec = importlib.util.spec_from_file_location("muavin_app_for_check", APP_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

app = getattr(mod, "app", None)
if app is None:
    print("❌ app nesnesi bulunamadı")
    raise SystemExit

with app.app_context():
    db = mod.get_db()

    print("===== 1) AKTİF SEFER =====")
    tid = mod.get_active_trip()
    print("active_trip_id:", tid)

    if not tid:
        print("❌ Aktif sefer yok")
        raise SystemExit

    trip = db.execute("SELECT * FROM trips WHERE id=?", (tid,)).fetchone()
    if not trip:
        print("❌ trips kaydı yok")
        raise SystemExit

    route = trip["route"]
    print("route:", route)
    print("plate:", trip["plate"])
    print("date:", trip["date"])

    stops = mod.get_stops(route)
    print()
    print("===== 2) ROTA DURAK SIRASI get_stops(route) =====")
    print("durak adedi:", len(stops))
    for i, s in enumerate(stops, 1):
        print(f"{i:02d}. {s}")

    print()
    print("===== 3) route_stop_coords TABLO VAR MI =====")
    tables = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
    print("route_stop_coords var mı:", "route_stop_coords" in tables)

    if "route_stop_coords" not in tables:
        print("❌ route_stop_coords tablosu yok. GPS canlı durak sağlıklı çalışamaz.")
        raise SystemExit

    cols = [c["name"] for c in db.execute("PRAGMA table_info(route_stop_coords)").fetchall()]
    print("kolonlar:", cols)

    print()
    print("===== 4) BU ROTA İÇİN KOORDİNATLAR =====")
    rows = db.execute(
        """
        SELECT rowid, route, stop, lat, lng
        FROM route_stop_coords
        WHERE route=?
        """,
        (route,),
    ).fetchall()

    print("koordinat satırı:", len(rows))

    stop_index = {norm(s): i for i, s in enumerate(stops, 1)}
    coord_by_stop = {}

    for n, r in enumerate(rows, 1):
        stop = r["stop"] or ""
        key = norm(stop)
        idx = stop_index.get(key)
        lat = r["lat"]
        lng = r["lng"]

        coord_by_stop[key] = {
            "stop": stop,
            "lat": lat,
            "lng": lng,
            "route_idx": idx,
            "rowid": r["rowid"],
        }

        flag = "✅" if idx else "⚠️ ROTA LİSTESİNDE YOK"
        print(f"{n:02d}. rowid={r['rowid']} route_idx={idx} {flag} | {stop} | lat={lat} lng={lng}")

    print()
    print("===== 5) KOORDİNATI EKSİK ROTA DURAKLARI =====")
    missing = []
    for i, s in enumerate(stops, 1):
        if norm(s) not in coord_by_stop:
            missing.append((i, s))

    if not missing:
        print("✅ Rota duraklarının hepsinde koordinat var gibi görünüyor.")
    else:
        for i, s in missing:
            print(f"❌ {i:02d}. {s}")

    print()
    print("===== 6) ROTA SIRASINA GÖRE KOORDİNAT MESAFELERİ =====")
    ordered = []
    for i, s in enumerate(stops, 1):
        item = coord_by_stop.get(norm(s))
        if item:
            ordered.append({
                "idx": i,
                "stop": s,
                "lat": item["lat"],
                "lng": item["lng"],
            })

    for a, b in zip(ordered, ordered[1:]):
        try:
            km = dist_km(a, b)
            warn = ""
            if km < 0.2:
                warn = " ⚠️ çok yakın/aynı koordinat olabilir"
            elif km > 180:
                warn = " ⚠️ çok uzak, koordinat yanlış olabilir"
            print(f"{a['idx']:02d}->{b['idx']:02d} {a['stop']} -> {b['stop']} = {km:.2f} km{warn}")
        except Exception as e:
            print(f"HATA {a['stop']} -> {b['stop']}: {e}")

    print()
    print("===== 7) live_runtime_state SON DURUM =====")
    try:
        state = db.execute(
            "SELECT * FROM live_runtime_state WHERE trip_id=?",
            (tid,),
        ).fetchone()

        if state:
            print(dict(state))
        else:
            print("live_runtime_state kaydı yok")
    except Exception as e:
        print("live_runtime_state okunamadı:", e)

    print()
    print("===== 8) ŞU AN APP.PY'NİN TEMPLATE'E GÖNDERDİĞİ routeCoords SIRASI =====")
    app_style = []
    for r in rows:
        try:
            app_style.append({
                "stop": r["stop"] or "",
                "lat": float(r["lat"]),
                "lng": float(r["lng"]),
            })
        except Exception:
            pass

    for i, x in enumerate(app_style, 1):
        print(f"{i:02d}. {x}")

    print()
    print("✅ V68 teşhis bitti.")
