from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99J DIREKT GPS MESAFE MOTORU =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99j-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski V99J bloğu varsa temizle
s = re.sub(
    r"\n?/\* V99J_DIRECT_GPS_DISTANCE_START \*/.*?/\* V99J_DIRECT_GPS_DISTANCE_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

block = r'''

/* V99J_DIRECT_GPS_DISTANCE_START */
(function(){
  "use strict";

  /*
    V99J:
    Mesafe artık segment toplamından değil,
    koltuk ekranındaki mantık gibi mevcut GPS konumu -> durak koordinatı
    direkt kuş uçuşu / canlı yaklaşım mesafesi üzerinden yazılır.
  */

  var lastPoint = null;
  var BOOT = window.CONTINUE_BOOT || {};
  var routeCoords = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];

  function q(sel){
    return document.querySelector(sel);
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .replace(/İ/g, "i")
      .replace(/I/g, "i")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/ğ/g, "g")
      .replace(/ü/g, "u")
      .replace(/ş/g, "s")
      .replace(/ö/g, "o")
      .replace(/ç/g, "c")
      .replace(/[^\w]+/g, "")
      .trim();
  }

  function findCoord(stopName){
    var n = norm(stopName);
    if(!n) return null;

    for(var i=0; i<routeCoords.length; i++){
      var item = routeCoords[i] || {};
      var s = item.stop || item.stop_name || item.name || "";
      if(norm(s) === n){
        var lat = Number(item.lat);
        var lng = Number(item.lng);
        if(Number.isFinite(lat) && Number.isFinite(lng)){
          return { lat:lat, lng:lng };
        }
      }
    }

    // Yumuşak eşleşme: Alaşehir OTOGAR / Alaşehir Otogar gibi farklar için
    for(var j=0; j<routeCoords.length; j++){
      var it = routeCoords[j] || {};
      var st = it.stop || it.stop_name || it.name || "";
      var ns = norm(st);
      if(n && ns && (n.indexOf(ns) >= 0 || ns.indexOf(n) >= 0)){
        var lat2 = Number(it.lat);
        var lng2 = Number(it.lng);
        if(Number.isFinite(lat2) && Number.isFinite(lng2)){
          return { lat:lat2, lng:lng2 };
        }
      }
    }

    return null;
  }

  function distKm(a, b){
    if(!a || !b) return NaN;

    var R = 6371;
    var toRad = function(d){ return d * Math.PI / 180; };

    var dLat = toRad(b.lat - a.lat);
    var dLng = toRad(b.lng - a.lng);
    var la1 = toRad(a.lat);
    var la2 = toRad(b.lat);

    var h =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(la1) * Math.cos(la2) *
      Math.sin(dLng / 2) * Math.sin(dLng / 2);

    return 2 * R * Math.asin(Math.sqrt(h));
  }

  function fmtKm(km){
    if(!Number.isFinite(km) || km < 0) return "—";
    if(km < 0.05) return "0 km";
    if(km < 1) return Math.round(km * 1000) + " m";
    if(km < 100) return km.toFixed(1).replace(".", ".") + " km";
    return Math.round(km) + " km";
  }

  function findMetricVal(card, wanted){
    if(!card) return null;

    var metrics = card.querySelectorAll(".v99-tl-metric");
    var want = norm(wanted);

    for(var i=0; i<metrics.length; i++){
      var lbl = metrics[i].querySelector(".v99-tl-m-lbl");
      var val = metrics[i].querySelector(".v99-tl-m-val");
      if(!lbl || !val) continue;

      if(norm(lbl.textContent).indexOf(want) >= 0){
        return val;
      }
    }

    return null;
  }

  function bindCells(){
    document.querySelectorAll(".v99-tl-card").forEach(function(card){
      var nameEl = card.querySelector(".v99-tl-stop-name");
      var stopName = text(nameEl);
      var distanceVal = findMetricVal(card, "MESAFE");

      if(!stopName || !distanceVal) return;

      distanceVal.classList.add("stop-distance-value");
      distanceVal.classList.add("v99-timeline-distance-value");
      distanceVal.setAttribute("data-stop-name", stopName);
    });
  }

  function updateRingForLive(km){
    var liveDist = document.getElementById("liveDistanceValue");
    if(liveDist && Number.isFinite(km)){
      liveDist.textContent = fmtKm(km);
    }

    if(typeof window.MuavinV99CleanSync === "function"){
      try{ window.MuavinV99CleanSync(); }catch(_){}
    }
  }

  function hydrateGpsDistances(){
    if(!lastPoint) return;

    bindCells();

    var currentName = text(document.getElementById("liveCurrentStopName"));
    var currentCoord = findCoord(currentName);

    if(currentCoord){
      updateRingForLive(distKm(lastPoint, currentCoord));
    }

    document.querySelectorAll(".v99-tl-card").forEach(function(card){
      var nameEl = card.querySelector(".v99-tl-stop-name");
      var stopName = text(nameEl);
      var distanceVal = findMetricVal(card, "MESAFE");
      var coord = findCoord(stopName);

      if(!distanceVal || !coord) return;

      var km = distKm(lastPoint, coord);
      distanceVal.textContent = fmtKm(km);
    });
  }

  function onPos(pos){
    if(!pos || !pos.coords) return;

    lastPoint = {
      lat: Number(pos.coords.latitude),
      lng: Number(pos.coords.longitude)
    };

    if(!Number.isFinite(lastPoint.lat) || !Number.isFinite(lastPoint.lng)){
      lastPoint = null;
      return;
    }

    hydrateGpsDistances();
  }

  bindCells();

  if(navigator.geolocation){
    navigator.geolocation.watchPosition(
      onPos,
      function(){ bindCells(); },
      {
        enableHighAccuracy: true,
        maximumAge: 3000,
        timeout: 12000
      }
    );

    navigator.geolocation.getCurrentPosition(
      onPos,
      function(){ bindCells(); },
      {
        enableHighAccuracy: true,
        maximumAge: 3000,
        timeout: 12000
      }
    );
  }

  // V99F eski toplam mesafe yazarsa tekrar gerçek GPS mesafesiyle ez.
  setInterval(hydrateGpsDistances, 900);
  document.addEventListener("continueEtaUpdated", hydrateGpsDistances);
  window.addEventListener("load", hydrateGpsDistances);

  window.MuavinV99DirectGpsDistance = hydrateGpsDistances;
})();
/* V99J_DIRECT_GPS_DISTANCE_END */
'''

s = s.rstrip() + block + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")
for key in [
    "V99J_DIRECT_GPS_DISTANCE_START",
    "MuavinV99DirectGpsDistance",
    "navigator.geolocation.watchPosition",
    "routeCoords",
    "stop-distance-value",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99J tamam. Tarayıcıda /continue-trip?v=v99jgps ile yenile.")
