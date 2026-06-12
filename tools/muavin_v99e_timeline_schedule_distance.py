from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

print("===== V99E TIMELINE SCHEDULE / DISTANCE =====")

for p in [WEB_JS, AND_JS, TPL, AND_TPL]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99e-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
js = re.sub(r"/\* V99E_TIMELINE_DATA_START \*/.*?/\* V99E_TIMELINE_DATA_END \*/", "", js, flags=re.S)

js += r'''

/* V99E_TIMELINE_DATA_START */
(function(){
  "use strict";

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

  function getSegmentKm(item){
    if(!item || typeof item === "string") return null;
    return parseNum(item.segment_km || item.km || item.distance || item.mesafe);
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

  function buildSchedule(){
    var boot = window.CONTINUE_BOOT || {};
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
      routeStops.forEach(function(name){
        var k = norm(name);
        if(!map[k]) map[k] = { stop_name:name, planned_time:"", segment_km:null };
      });
    }

    return {
      map: map,
      order: order
    };
  }

  function closestScheduleItem(schedule, stopName){
    var k = norm(stopName);
    if(schedule.map[k]) return schedule.map[k];

    var keys = Object.keys(schedule.map);

    for(var i=0; i<keys.length; i++){
      if(keys[i] === k) return schedule.map[keys[i]];
    }

    for(var j=0; j<keys.length; j++){
      if(keys[j].indexOf(k) >= 0 || k.indexOf(keys[j]) >= 0){
        return schedule.map[keys[j]];
      }
    }

    return null;
  }

  function findOrderIndex(order, stopName){
    var k = norm(stopName);

    for(var i=0; i<order.length; i++){
      if(norm(order[i]) === k) return i;
    }

    for(var j=0; j<order.length; j++){
      var ok = norm(order[j]);
      if(ok.indexOf(k) >= 0 || k.indexOf(ok) >= 0) return j;
    }

    return -1;
  }

  function buildCumulative(schedule){
    var cum = {};
    var total = 0;

    for(var i=0; i<schedule.order.length; i++){
      var name = schedule.order[i];
      var item = closestScheduleItem(schedule, name);

      if(i === 0){
        total = 0;
      }else{
        var seg = getSegmentKm(item);
        if(seg !== null && seg > 0){
          total += seg;
        }
      }

      cum[norm(name)] = total;
    }

    return cum;
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

  function hydrateTimeline(){
    var schedule = buildSchedule();
    var cumulative = buildCumulative(schedule);

    var currentName = "";
    var currentEl = q("#liveCurrentStopName");
    if(currentEl) currentName = String(currentEl.textContent || "").trim();

    var currentIdx = findOrderIndex(schedule.order, currentName);
    var currentCum = currentIdx >= 0 ? cumulative[norm(schedule.order[currentIdx])] : null;

    var runtimeKm = parseNum((q("#liveDistanceValue") || {}).textContent);
    if(runtimeKm === null){
      runtimeKm = parseNum((window.CONTINUE_BOOT || {}).runtimeGpsKm);
    }

    var cards = qa(".v99-tl-card");

    cards.forEach(function(card){
      var nameEl = q(".v99-tl-stop-name", card);
      if(!nameEl) return;

      var stopName = String(nameEl.textContent || "").trim();
      if(!stopName) return;

      var item = closestScheduleItem(schedule, stopName);
      var planned = getPlannedTime(item);
      var status = statusOfCard(card);

      var arrivalVal = findMetricVal(card, "VARIŞ");
      var distanceVal = findMetricVal(card, "MESAFE");

      if(arrivalVal && planned){
        arrivalVal.textContent = planned;
      }

      if(distanceVal){
        /* Eski core timeline mesafesini ezmesin; üstteki gizli liveDistanceValue kalsın. */
        if(card.contains(distanceVal)){
          distanceVal.classList.remove("stop-distance-value");
          distanceVal.classList.add("v99-timeline-distance-value");
        }

        if(status === "passed"){
          distanceVal.textContent = "—";
        }else if(status === "live"){
          distanceVal.textContent = runtimeKm !== null ? formatKm(runtimeKm) : "0 km";
        }else{
          var stopIdx = findOrderIndex(schedule.order, stopName);
          var stopCum = stopIdx >= 0 ? cumulative[norm(schedule.order[stopIdx])] : null;

          if(currentCum !== null && stopCum !== null){
            var dist = (stopCum - currentCum) + (runtimeKm || 0);
            distanceVal.textContent = dist >= 0 ? formatKm(dist) : "—";
          }else if(currentIdx >= 0 && stopIdx >= 0){
            var diff = stopIdx - currentIdx;
            distanceVal.textContent = diff > 0 ? (diff + " durak") : "—";
          }
        }
      }
    });
  }

  hydrateTimeline();

  setInterval(hydrateTimeline, 700);
  document.addEventListener("continueEtaUpdated", hydrateTimeline);
  window.MuavinV99TimelineHydrate = hydrateTimeline;
})();
/* V99E_TIMELINE_DATA_END */
'''

WEB_JS.write_text(js, encoding="utf-8")
print("✅ V99E JS eklendi:", WEB_JS)

# Template JS cache versiyonunu yükselt
if TPL.exists():
    t = TPL.read_text(encoding="utf-8", errors="ignore")
    before = t

    t = re.sub(
        r"continue_trip_v99_clean\.js'\) \}\}\?v=[^\"']+",
        "continue_trip_v99_clean.js') }}?v=v99e-{{ trip['id'] }}",
        t
    )

    if t != before:
      TPL.write_text(t, encoding="utf-8")
      print("✅ template JS cache versiyonu v99e yapıldı")
    else:
      print("⚠️ template JS version değişmedi; mevcut hali korunuyor")

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS senkron:", AND_JS)

if AND_TPL.parent.exists() and TPL.exists():
    AND_TPL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TPL, AND_TPL)
    print("✅ Android template senkron:", AND_TPL)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")
print("V99E JS marker:", "VAR" if "V99E_TIMELINE_DATA_START" in txt else "YOK")

if TPL.exists():
    tt = TPL.read_text(encoding="utf-8", errors="ignore")
    print("template v99e:", "VAR" if "v99e-" in tt else "YOK")

print()
print("✅ V99E timeline saat/mesafe bağlama tamam")
