import time, requests, math
from flask import Blueprint, request, jsonify

bp_speed = Blueprint("speed", __name__)

OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.openstreetmap.ru/api/interpreter",
]

# Basit TTL cache (RAM)
CACHE = {}  # key: (lat_b, lng_b) -> {"ts":..., "limit":..., "highway":..., "source":...}
CACHE_TTL_S = 600  # 10 dk
BUCKET_DEG = 0.001  # ~100 m (lat'a göre)

# Türkiye için makul fallback'lar
def fallback_limit_by_highway(hw: str) -> int:
    hw = (hw or "").lower()
    if hw in ("motorway", "trunk"):             # otoyol / bölünmüş ana yol
        return 120
    if hw in ("primary", "secondary", "tertiary"):
        return 90
    if hw in ("residential", "living_street", "service"):
        return 50
    return 90

def parse_maxspeed(val: str):
    if not val:
        return None
    s = val.strip().lower()
    s = s.replace("km/h", "").replace("kph", "").replace(" ", "")
    # "signals", "variable", "none" gibi değerleri ele
    if not any(ch.isdigit() for ch in s):
        return None
    try:
        return int(round(float(s)))
    except:
        return None

def overpass_query(lat, lng, radius=60):
    q = f"""
    [out:json][timeout:7];
    way(around:{radius},{lat},{lng})[highway];
    out tags center 1;
    """
    last_err = None
    for url in OVERPASS_URLS:
        try:
            r = requests.post(url, data={'data': q}, timeout=10)
            if r.status_code == 429:
                last_err = Exception("Overpass rate-limited (429)")
                continue
            r.raise_for_status()
            js = r.json()
            # En yakın yolu seç (varsa center alanına göre)
            ways = js.get("elements", [])
            if not ways:
                return {}
            # En yakınını bul
            def dist2(w):
                c = w.get("center") or {}
                return (c.get("lat", 999) - lat)**2 + (c.get("lon", 999) - lng)**2
            ways.sort(key=dist2)
            return ways[0].get("tags", {})
        except Exception as e:
            last_err = e
            continue
    # Hepsi patlarsa:
    if last_err:
        raise last_err
    return {}

def get_bucket(lat, lng):
    return (round(lat / BUCKET_DEG) * BUCKET_DEG, round(lng / BUCKET_DEG) * BUCKET_DEG)

@bp_speed.get("/api/speedlimit")
def api_speedlimit():
    try:
        lat = float(request.args["lat"])
        lng = float(request.args["lng"])
    except:
        return jsonify(ok=False, msg="lat/lng gerekli"), 400

    bucket = get_bucket(lat, lng)
    now = time.time()
    c = CACHE.get(bucket)
    if c and (now - c["ts"] < CACHE_TTL_S):
        return jsonify(ok=True, limit=c["limit"], highway=c["highway"], source=c["source"], from_cache=True, ttl=int(CACHE_TTL_S - (now - c["ts"])))

    try:
        tags = overpass_query(lat, lng)
    except Exception as e:
        # Overpass yoksa tamamen fallback
        tags = {}

    highway = (tags.get("highway") or "").lower()
    limit = parse_maxspeed(tags.get("maxspeed"))
    if not limit:
        limit = fallback_limit_by_highway(highway)
        source = "fallback"
    else:
        source = "osm:maxspeed"

    item = {"ts": now, "limit": int(limit), "highway": highway, "source": source}
    CACHE[bucket] = item
    return jsonify(ok=True, limit=item["limit"], highway=item["highway"], source=item["source"], from_cache=False, ttl=CACHE_TTL_S)
