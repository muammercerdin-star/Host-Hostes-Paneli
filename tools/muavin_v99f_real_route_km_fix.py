from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP = ROOT / "app.py"
AND_APP = ROOT / "android_app/app/src/main/python/app.py"

JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

print("===== V99F REAL ROUTE KM FIX =====")

for p in [APP, AND_APP, JS, AND_JS, TPL, AND_TPL]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99f-real-km-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not APP.exists():
    raise SystemExit("❌ app.py yok")
if not JS.exists():
    raise SystemExit("❌ JS yok")

# 1) APP.PY API ekle
app_txt = APP.read_text(encoding="utf-8", errors="ignore")

api_code = r'''

# V99F_ROUTE_SEGMENT_API_START
@app.route("/api/v99-route-segments")
def api_v99_route_segments():
    from flask import jsonify, session

    def norm_route(x):
        return (
            str(x or "")
            .replace("–", "-")
            .replace("—", "-")
            .replace(" ", "")
            .lower()
            .strip()
        )

    def row_get(row, key, default=None):
        try:
            return row[key]
        except Exception:
            return default

    try:
        if not session.get("auth_ok"):
            return jsonify({"ok": False, "error": "unauthorized", "segments": []}), 401
    except Exception:
        pass

    try:
        db = get_db()
        trip = get_active_trip_row()
        route = ""
        if trip:
            try:
                route = trip["route"] or ""
            except Exception:
                route = ""

        wanted = norm_route(route)

        def candidate_routes(table):
            out = []
            try:
                rows = db.execute(f"SELECT DISTINCT route FROM {table}").fetchall()
                for r in rows:
                    rt = row_get(r, "route", "")
                    if norm_route(rt) == wanted:
                        out.append(rt)
            except Exception:
                pass

            if route and route not in out:
                out.insert(0, route)

            return out

        segments = []
        seen = set()

        def add_from_table(table):
            nonlocal segments, seen

            for rt in candidate_routes(table):
                try:
                    rows = db.execute(
                        f"""
                        SELECT from_stop, to_stop, sort_order, distance_m, duration_s, provider
                        FROM {table}
                        WHERE route=?
                        ORDER BY sort_order ASC
                        """,
                        (rt,)
                    ).fetchall()
                except Exception:
                    rows = []

                for row in rows:
                    frm = str(row_get(row, "from_stop", "") or "").strip()
                    to = str(row_get(row, "to_stop", "") or "").strip()
                    if not frm or not to:
                        continue

                    try:
                        m = float(row_get(row, "distance_m", 0) or 0)
                    except Exception:
                        m = 0

                    if m <= 0:
                        continue

                    key = (frm.lower(), to.lower())
                    if key in seen:
                        continue

                    seen.add(key)

                    segments.append({
                        "from_stop": frm,
                        "to_stop": to,
                        "sort_order": row_get(row, "sort_order", 0),
                        "distance_m": m,
                        "km": round(m / 1000.0, 3),
                        "duration_s": row_get(row, "duration_s", None),
                        "provider": row_get(row, "provider", ""),
                        "source_table": table,
                    })

        add_from_table("route_segments")

        if not segments:
            add_from_table("route_profile_segments")

        return jsonify({
            "ok": True,
            "route": route,
            "count": len(segments),
            "segments": segments
        })

    except Exception as e:
        return jsonify({"ok": False, "error": repr(e), "segments": []}), 500
# V99F_ROUTE_SEGMENT_API_END
'''

if "V99F_ROUTE_SEGMENT_API_START" not in app_txt:
    main_match = re.search(r'\nif __name__\s*==\s*[\'"]__main__[\'"]\s*:', app_txt)

    if main_match:
        app_txt = app_txt[:main_match.start()] + api_code + "\n" + app_txt[main_match.start():]
    else:
        app_txt += api_code + "\n"

    APP.write_text(app_txt, encoding="utf-8")
    print("✅ app.py route segment API eklendi")
else:
    print("ℹ️ app.py API zaten var")

# 2) JS: eski V99E timeline bloğunu kaldır, gerçek route_segments hesaplı V99F ekle
js = JS.read_text(encoding="utf-8", errors="ignore")

js = re.sub(r"/\* V99E_TIMELINE_DATA_START \*/.*?/\* V99E_TIMELINE_DATA_END \*/", "", js, flags=re.S)
js = re.sub(r"/\* V99F_REAL_ROUTE_KM_START \*/.*?/\* V99F_REAL_ROUTE_KM_END \*/", "", js, flags=re.S)

js += r'''

/* V99F_REAL_ROUTE_KM_START */
(function(){
  "use strict";

  var routeSegState = {
    loading: false,
    loaded: false,
    list: [],
    map: {}
  };

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function norm(s){
    try{
      return String(s || "")
        .toLocaleLowerCase("tr-TR")
        .replace(/ı/g, "i")
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/\s+/g, " ")
        .trim();
    }catch(_){
      return String(s || "").toLowerCase().replace(/\s+/g, " ").trim();
    }
  }

  function pairKey(a, b){
    return norm(a) + "→" + norm(b);
  }

  function parseNum(v){
    if(v === null || v === undefined) return null;
    var m = String(v).replace(",", ".").match(/-?\d+(?:\.\d+)?/);
    if(!m) return null;
    var n = Number(m[0]);
    return Number.isFinite(n) ? n : null;
  }

  function formatKm(n){
    if(n === null || n === undefined || !Number.isFinite(n)) return "—";
    n = Math.max(0, n);

    if(n >= 10) return String(Math.round(n)) + " km";
    if(n === 0) return "0 km";

    return n.toFixed(1).replace(".", ".") + " km";
  }

  function getBootArray(key){
    var boot = window.CONTINUE_BOOT || {};
    var val = boot[key];

    if(Array.isArray(val)) return val;

    if(typeof val === "string"){
      try{
        var parsed = JSON.parse(val);
        if(Array.isArray(parsed)) return parsed;
      }catch(_){}
    }

    return [];
  }

  function getStopNameFromItem(item){
    if(!item) return "";
    if(typeof item === "string") return item;
    return item.stop_name || item.stop || item.name || item.durak || "";
  }

  function getPlannedTime(item){
    if(!item || typeof item === "string") return "";
    return String(item.planned_time || item.time || item.eta || item.saat || "").trim();
  }

  function getSegmentKmFromSchedule(item){
    if(!item || typeof item === "string") return null;
    return parseNum(item.segment_km || item.km || item.distance || item.mesafe);
  }

  function buildSchedule(){
    var scheduleItems = getBootArray("scheduleItems");
    var routeStops = getBootArray("routeStops");

    scheduleItems = scheduleItems.slice().sort(function(a,b){
      var aa = Number((a && a.sort_order !== undefined) ? a.sort_order : 999999);
      var bb = Number((b && b.sort_order !== undefined) ? b.sort_order : 999999);
      return aa - bb;
    });

    var map = {};
    var order = [];

    scheduleItems.forEach(function(item){
      var name = getStopNameFromItem(item);
      if(!name) return;

      var k = norm(name);
      if(!map[k]) map[k] = item;

      if(order.indexOf(name) < 0){
        order.push(name);
      }
    });

    if(!order.length && routeStops.length){
      order = routeStops.slice();
    }

    return { map: map, order: order };
  }

  function closestScheduleItem(schedule, stopName){
    var k = norm(stopName);
    if(schedule.map[k]) return schedule.map[k];

    var keys = Object.keys(schedule.map);

    for(var i=0; i<keys.length; i++){
      if(keys[i].indexOf(k) >= 0 || k.indexOf(keys[i]) >= 0){
        return schedule.map[keys[i]];
      }
    }

    return null;
  }

  function findMetricVal(card, label){
    var want = norm(label);
    var metrics = qa(".v99-tl-metric", card);

    for(var i=0; i<metrics.length; i++){
      var lbl = q(".v99-tl-m-lbl", metrics[i]);
      var val = q(".v99-tl-m-val", metrics[i]);
      if(!lbl || !val) continue;

      if(norm(lbl.textContent).indexOf(want) >= 0){
        return val;
      }
    }

    return null;
  }

  function statusOfCard(card){
    var pill = q(".v99-pill", card);
    if(!pill) return "";

    if(pill.classList.contains("passed")) return "passed";
    if(pill.classList.contains("live")) return "live";
    if(pill.classList.contains("next")) return "next";
    if(pill.classList.contains("upcoming")) return "upcoming";

    return "";
  }

  function cardNames(){
    return qa(".v99-tl-card").map(function(card){
      var nameEl = q(".v99-tl-stop-name", card);
      return nameEl ? String(nameEl.textContent || "").trim() : "";
    }).filter(Boolean);
  }

  function indexOfName(names, stopName){
    var k = norm(stopName);

    for(var i=0; i<names.length; i++){
      if(norm(names[i]) === k) return i;
    }

    for(var j=0; j<names.length; j++){
      var nk = norm(names[j]);
      if(nk.indexOf(k) >= 0 || k.indexOf(nk) >= 0) return j;
    }

    return -1;
  }

  function addSegmentToMap(seg){
    var from = seg.from_stop || seg.from || "";
    var to = seg.to_stop || seg.to || "";
    var km = parseNum(seg.km);

    if(km === null){
      var m = parseNum(seg.distance_m);
      if(m !== null) km = m / 1000;
    }

    if(!from || !to || km === null || km <= 0) return;

    routeSegState.map[pairKey(from, to)] = km;
  }

  function segmentKmBetween(from, to, schedule){
    var direct = routeSegState.map[pairKey(from, to)];
    if(direct !== undefined) return direct;

    var nFrom = norm(from);
    var nTo = norm(to);

    for(var i=0; i<routeSegState.list.length; i++){
      var seg = routeSegState.list[i];
      var sf = norm(seg.from_stop || "");
      var st = norm(seg.to_stop || "");

      var fromOk = sf === nFrom || sf.indexOf(nFrom) >= 0 || nFrom.indexOf(sf) >= 0;
      var toOk = st === nTo || st.indexOf(nTo) >= 0 || nTo.indexOf(st) >= 0;

      if(fromOk && toOk){
        var km = parseNum(seg.km);
        if(km === null){
          var m = parseNum(seg.distance_m);
          if(m !== null) km = m / 1000;
        }
        if(km !== null && km > 0) return km;
      }
    }

    /* Son çare: schedule'daki segment_km hedef durağın önceki segmenti ise onu kullan. */
    var item = closestScheduleItem(schedule, to);
    var fallback = getSegmentKmFromSchedule(item);
    if(fallback !== null && fallback > 0) return fallback;

    return null;
  }

  function computeDistance(names, currentIdx, targetIdx, runtimeKm, schedule){
    if(targetIdx < 0 || currentIdx < 0) return null;
    if(targetIdx < currentIdx) return null;
    if(targetIdx === currentIdx) return runtimeKm !== null ? runtimeKm : 0;

    var sum = runtimeKm !== null ? runtimeKm : 0;
    var foundAny = false;

    for(var i=currentIdx; i<targetIdx; i++){
      var segKm = segmentKmBetween(names[i], names[i+1], schedule);

      if(segKm === null){
        return null;
      }

      foundAny = true;
      sum += segKm;
    }

    return foundAny ? sum : null;
  }

  function loadSegments(){
    if(routeSegState.loading || routeSegState.loaded) return;

    routeSegState.loading = true;

    fetch("/api/v99-route-segments?v=" + Date.now(), {
      credentials: "same-origin",
      cache: "no-store"
    })
    .then(function(r){ return r.json(); })
    .then(function(data){
      routeSegState.loading = false;
      routeSegState.loaded = true;

      routeSegState.list = Array.isArray(data.segments) ? data.segments : [];
      routeSegState.map = {};

      routeSegState.list.forEach(addSegmentToMap);

      hydrateTimeline();
    })
    .catch(function(){
      routeSegState.loading = false;
      routeSegState.loaded = true;
      hydrateTimeline();
    });
  }

  function hydrateTimeline(){
    var schedule = buildSchedule();
    var names = cardNames();

    var currentName = "";
    var currentEl = q("#liveCurrentStopName");
    if(currentEl) currentName = String(currentEl.textContent || "").trim();

    var currentIdx = indexOfName(names, currentName);

    var runtimeKm = parseNum((q("#liveDistanceValue") || {}).textContent);
    if(runtimeKm === null){
      runtimeKm = parseNum((window.CONTINUE_BOOT || {}).runtimeGpsKm);
    }

    qa(".v99-tl-card").forEach(function(card){
      var nameEl = q(".v99-tl-stop-name", card);
      if(!nameEl) return;

      var stopName = String(nameEl.textContent || "").trim();
      if(!stopName) return;

      var status = statusOfCard(card);
      var item = closestScheduleItem(schedule, stopName);
      var planned = getPlannedTime(item);

      var arrivalVal = findMetricVal(card, "VARIŞ");
      var distanceVal = findMetricVal(card, "MESAFE");

      if(arrivalVal && planned){
        arrivalVal.textContent = planned;
      }

      if(!distanceVal) return;

      distanceVal.classList.remove("stop-distance-value");
      distanceVal.classList.add("v99-timeline-distance-value");

      if(status === "passed"){
        distanceVal.textContent = "—";
        return;
      }

      var targetIdx = indexOfName(names, stopName);

      if(status === "live"){
        distanceVal.textContent = runtimeKm !== null ? formatKm(runtimeKm) : "0 km";
        return;
      }

      var dist = computeDistance(names, currentIdx, targetIdx, runtimeKm, schedule);

      if(dist !== null){
        distanceVal.textContent = formatKm(dist);
      }else if(currentIdx >= 0 && targetIdx > currentIdx){
        distanceVal.textContent = String(targetIdx - currentIdx) + " durak";
      }
    });
  }

  loadSegments();
  hydrateTimeline();

  setInterval(function(){
    if(!routeSegState.loaded) loadSegments();
    hydrateTimeline();
  }, 700);

  document.addEventListener("continueEtaUpdated", hydrateTimeline);

  window.MuavinV99RealKmHydrate = hydrateTimeline;
})();
/* V99F_REAL_ROUTE_KM_END */
'''

JS.write_text(js, encoding="utf-8")
print("✅ JS gerçek route km hesaplama yazıldı")

# 3) Template cache version
if TPL.exists():
    t = TPL.read_text(encoding="utf-8", errors="ignore")
    before = t

    t = re.sub(
        r"continue_trip_v99_clean\.js'\) \}\}\?v=[^\"']+",
        "continue_trip_v99_clean.js') }}?v=v99f-{{ trip['id'] }}",
        t
    )

    if t != before:
        TPL.write_text(t, encoding="utf-8")
        print("✅ template JS cache v99f yapıldı")
    else:
        print("⚠️ template JS cache değişmedi")

# 4) Android sync
if AND_APP.parent.exists():
    AND_APP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(APP, AND_APP)
    print("✅ Android app.py senkron")

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(JS, AND_JS)
    print("✅ Android JS senkron")

if AND_TPL.parent.exists() and TPL.exists():
    AND_TPL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TPL, AND_TPL)
    print("✅ Android template senkron")

print()
print("===== PYTHON SYNTAX =====")
r = subprocess.run(["python", "-m", "py_compile", "app.py"], cwd=ROOT)
if r.returncode != 0:
    raise SystemExit("❌ app.py syntax hatası")

print("✅ app.py syntax temiz")

print()
print("===== KONTROL =====")
app_check = APP.read_text(encoding="utf-8", errors="ignore")
js_check = JS.read_text(encoding="utf-8", errors="ignore")
tpl_check = TPL.read_text(encoding="utf-8", errors="ignore") if TPL.exists() else ""

for key, txt in [
    ("V99F_ROUTE_SEGMENT_API_START", app_check),
    ("V99F_REAL_ROUTE_KM_START", js_check),
    ("V99E_TIMELINE_DATA_START", js_check),
    ("v99f-", tpl_check),
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99F gerçek km düzeltmesi tamam")
