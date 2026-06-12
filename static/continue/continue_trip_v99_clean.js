(function(){
  "use strict";

  const CIRC = 276.46;
  const MAX_KM = 48;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(sel){
    const el = q(sel);
    return el ? (el.textContent || "").trim() : "";
  }

  function parseKm(raw){
    raw = String(raw || "").replace(",", ".").trim();
    const m = raw.match(/-?\d+(?:\.\d+)?/);
    if(!m) return null;
    const n = Number(m[0]);
    return Number.isFinite(n) ? n : null;
  }

  function cleanSpeed(raw){
    const n = parseKm(raw);
    if(n === null) return "0";
    return String(Math.max(0, Math.round(n)));
  }

  function setRing(km){
    const ring = q("#ringFill");
    const ringKm = q("#ringKm");
    if(!ring || !ringKm) return;

    let display = km;
    if(km === null){
      display = null;
    }

    let safeKm = display === null ? MAX_KM : Math.max(0, display);
    let ratio = Math.max(0, Math.min(1, 1 - safeKm / MAX_KM));
    let offset = CIRC * (1 - ratio);

    ring.style.strokeDashoffset = String(offset);

    if(display === null){
      ringKm.textContent = "—";
      ring.style.stroke = "#5a6478";
      ring.style.filter = "none";
      ring.classList.remove("urgent");
      ringKm.style.color = "#5a6478";
      ringKm.style.textShadow = "none";
      return;
    }

    let label = safeKm <= 0 ? "0" : (safeKm % 1 === 0 ? String(safeKm) : safeKm.toFixed(1));
    ringKm.textContent = label;

    if(safeKm <= 5){
      ring.style.stroke = "#e03030";
      ring.style.filter = "none";
      ring.classList.add("urgent");
      ringKm.style.color = "#e03030";
      ringKm.style.textShadow = "0 0 18px #e03030";
    }else if(safeKm <= 15){
      ring.style.stroke = "#e08820";
      ring.style.filter = "none";
      ring.classList.remove("urgent");
      ringKm.style.color = "#e08820";
      ringKm.style.textShadow = "0 0 12px #e08820";
    }else{
      ring.style.stroke = "#3a8bff";
      ring.style.filter = "none";
      ring.classList.remove("urgent");
      ringKm.style.color = "#3a8bff";
      ringKm.style.textShadow = "0 0 10px #3a8bff";
    }
  }

  function setRouteProgress(){
    const boot = window.CONTINUE_BOOT || {};
    const stops = Array.isArray(boot.routeStops) ? boot.routeStops : [];
    const current = text("#liveCurrentStopName");
    const bar = q("#routeBar");
    const pctEl = q("#distPct");

    if(!bar || !pctEl || !stops.length || !current){
      return;
    }

    let idx = stops.findIndex(s => String(s || "").trim().toLowerCase() === current.trim().toLowerCase());

    if(idx < 0){
      idx = stops.findIndex(s => String(s || "").trim().toLowerCase().includes(current.trim().toLowerCase()));
    }

    if(idx < 0) return;

    const pct = stops.length <= 1 ? 0 : Math.round((idx / (stops.length - 1)) * 100);
    bar.style.width = Math.max(0, Math.min(100, pct)) + "%";
    pctEl.textContent = "%" + pct + " tamamlandı";
  }

  function setClock(){
    const el = q("#liveClockText");
    if(!el) return;
    const now = new Date();
    const h = String(now.getHours()).padStart(2, "0");
    const m = String(now.getMinutes()).padStart(2, "0");
    el.textContent = h + ":" + m;
  }

  function sync(){
    const km = parseKm(text("#liveDistanceValue"));
    setRing(km);

    const speedVisual = q("#v99SpeedVal");
    if(speedVisual){
      speedVisual.textContent = cleanSpeed(text("#liveSpeedText"));
    }

    const status = text("#liveTopStatusText");
    const sub = q("#v99StatusSub");
    if(sub && status){
      sub.textContent = /erken|geç/i.test(status) ? "tahmini durum" : "canlı takip";
    }

    setRouteProgress();
  }

  setClock();
  sync();

  setInterval(setClock, 10000);
  setInterval(sync, 700);

  document.addEventListener("continueEtaUpdated", sync);
  window.addEventListener("storage", sync);
  window.MuavinV99CleanSync = sync;
})();





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

      distanceVal.classList.add("stop-distance-value");
      distanceVal.classList.add("v99-timeline-distance-value");
      /* V99I_DATA_STOP_BIND */
      distanceVal.classList.add("stop-distance-value");
      if(stopName) distanceVal.setAttribute("data-stop-name", stopName);

      if(status === "passed"){
        /* V99K: MESAFE yazma; GPS motoru yazacak. */
        return;
      }

      var targetIdx = indexOfName(names, stopName);

      if(status === "live"){
        /* V99K: CANLI MESAFE yazma; GPS motoru yazacak. */
        return;
      }

      var dist = computeDistance(names, currentIdx, targetIdx, runtimeKm, schedule);

      if(dist !== null){
        /* V99K: GELECEK DURAK MESAFE yazma; GPS motoru yazacak. */
      }else if(currentIdx >= 0 && targetIdx > currentIdx){
        /* V99K: MESAFE yazma; GPS motoru yazacak. */
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


/* V99G_TIMELINE_VALUE_CLEAN_START */
(function(){
  "use strict";

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function isBadArrivalText(t){
    t = norm(t);

    return (
      !t ||
      t === "geçildi" ||
      t === "simdi" ||
      t === "şimdi" ||
      t === "sırada" ||
      t === "sirada" ||
      t.indexOf("durak sonra") >= 0
    );
  }

  function cleanTimelineArrivalValues(){
    qa(".v99-tl-card").forEach(function(card){
      qa(".v99-tl-metric", card).forEach(function(metric){
        var val = q(".v99-tl-m-val", metric);
        var lbl = q(".v99-tl-m-lbl", metric);

        if(!val || !lbl) return;

        if(norm(lbl.textContent).indexOf("varış") < 0 && norm(lbl.textContent).indexOf("varis") < 0){
          return;
        }

        if(isBadArrivalText(val.textContent)){
          val.textContent = "—";
        }
      });
    });
  }

  cleanTimelineArrivalValues();
  setInterval(cleanTimelineArrivalValues, 400);
  document.addEventListener("continueEtaUpdated", cleanTimelineArrivalValues);
})();
/* V99G_TIMELINE_VALUE_CLEAN_END */

/* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_START */
(function(){
  "use strict";

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function findDistanceVal(card){
    if(!card) return null;

    var metrics = card.querySelectorAll(".v99-tl-metric");
    for(var i=0; i<metrics.length; i++){
      var lbl = metrics[i].querySelector(".v99-tl-m-lbl");
      var val = metrics[i].querySelector(".v99-tl-m-val");
      var lt = text(lbl).toLocaleLowerCase("tr-TR");

      if(val && (lt.indexOf("mesafe") >= 0)){
        return val;
      }
    }

    return null;
  }

  function bindDistanceCells(){
    var cards = document.querySelectorAll(".v99-tl-card");
    cards.forEach(function(card){
      var nameEl = card.querySelector(".v99-tl-stop-name");
      var val = findDistanceVal(card);
      var stopName = text(nameEl);

      if(!val || !stopName) return;

      val.classList.add("stop-distance-value");
      val.setAttribute("data-stop-name", stopName);

      var t = text(val);
      if(/durak|sonra|sırada|sirada/i.test(t)){
        val.textContent = "—";
      }
    });
  }

  bindDistanceCells();

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", bindDistanceCells);
  }

  window.addEventListener("load", bindDistanceCells);
  document.addEventListener("continueEtaUpdated", bindDistanceCells);

  var left = 30;
  var timer = setInterval(function(){
    bindDistanceCells();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 700);
})();
/* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_END */

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

/* V99K_DISTANCE_NO_FLICKER_GUARD_START */
(function(){
  "use strict";

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function isRealKm(t){
    return /\d/.test(t || "") && /(km|m)$/i.test(String(t || "").trim());
  }

  function isBlankDistance(t){
    t = String(t || "").trim();
    return !t || t === "—" || t === "-" || /durak|sonra|sırada|sirada/i.test(t);
  }

  function findDistanceVal(card){
    if(!card) return null;

    var metrics = card.querySelectorAll(".v99-tl-metric");
    for(var i = 0; i < metrics.length; i++){
      var lbl = metrics[i].querySelector(".v99-tl-m-lbl");
      var val = metrics[i].querySelector(".v99-tl-m-val");
      if(!lbl || !val) continue;

      var lt = text(lbl).toLocaleLowerCase("tr-TR");
      if(lt.indexOf("mesafe") >= 0){
        return val;
      }
    }

    return null;
  }

  function protectDistances(){
    document.querySelectorAll(".v99-tl-card").forEach(function(card){
      var val = findDistanceVal(card);
      if(!val) return;

      var now = text(val);
      var last = val.getAttribute("data-v99-last-real-km") || "";

      if(isRealKm(now)){
        val.setAttribute("data-v99-last-real-km", now);
        return;
      }

      if(last && isBlankDistance(now)){
        val.textContent = last;
      }
    });
  }

  protectDistances();

  var obs = new MutationObserver(function(){
    protectDistances();
  });

  try{
    obs.observe(document.body, {
      childList: true,
      subtree: true,
      characterData: true
    });
  }catch(_){}

  setInterval(protectDistances, 300);
  document.addEventListener("continueEtaUpdated", protectDistances);
  window.addEventListener("load", protectDistances);
})();
/* V99K_DISTANCE_NO_FLICKER_GUARD_END */



/* V99M_OCCUPANCY_PANEL_START */
(function(){
  "use strict";

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/ğ/g, "g")
      .replace(/ü/g, "u")
      .replace(/ş/g, "s")
      .replace(/ö/g, "o")
      .replace(/ç/g, "c")
      .replace(/\s+/g, " ")
      .trim();
  }

  function sameStop(a,b){
    var aa = norm(a);
    var bb = norm(b);
    if(!aa || !bb) return false;
    return aa === bb || aa.indexOf(bb) >= 0 || bb.indexOf(aa) >= 0;
  }

  function liveStopName(){
    return text(q("#liveCurrentStopName")) || "";
  }

  function nextStopName(){
    var el = q(".v99-tl-card.next-card .v99-tl-stop-name");
    if(el) return text(el);

    var cards = qa(".v99-tl-card");
    for(var i=0; i<cards.length; i++){
      var pill = text(q(".v99-pill", cards[i]));
      if(/sonraki|sonraki|sonra/i.test(pill)){
        return text(q(".v99-tl-stop-name", cards[i]));
      }
    }
    return "";
  }

  function ensurePanel(){
    if(q("#v99mOccSheet")) return;

    var overlay = document.createElement("div");
    overlay.id = "v99mOccOverlay";
    overlay.className = "v99m-occ-overlay";

    var sheet = document.createElement("section");
    sheet.id = "v99mOccSheet";
    sheet.className = "v99m-occ-sheet";
    sheet.innerHTML = `
      <div class="v99m-handle"></div>

      <div class="v99m-head">
        <div>
          <div class="v99m-kicker">DOLULUK PANELİ</div>
          <h3 class="v99m-title">Koltuk Haritası</h3>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <button class="v99m-refresh" id="v99mOccRefresh" type="button">YENİLE</button>
          <button class="v99m-close" id="v99mOccClose" type="button">×</button>
        </div>
      </div>

      <div class="v99m-summary-grid" id="v99mOccSummary">
        <div class="v99m-stat"><div class="v">—</div><div class="l">DOLULUK</div></div>
        <div class="v99m-stat"><div class="v">—</div><div class="l">BOŞ</div></div>
        <div class="v99m-stat"><div class="v">—</div><div class="l">İNECEK</div></div>
      </div>

      <div class="v99m-impact" id="v99mOccImpact">Veri hazırlanıyor…</div>

      <div class="v99m-section-title">
        <span>GÖRSEL KOLTUK PLANI</span>
        <span id="v99mOccLiveStop">—</span>
      </div>

      <div class="v99m-map" id="v99mSeatMap"></div>

      <div class="v99m-legend">
        <span><i class="v99m-dot free"></i> Boş</span>
        <span><i class="v99m-dot occ"></i> Dolu</span>
        <span><i class="v99m-dot off"></i> Bu durakta inecek</span>
      </div>

      <div class="v99m-detail" id="v99mSeatDetail">
        Koltuğa basınca detay burada görünür.
      </div>
    `;

    document.body.appendChild(overlay);
    document.body.appendChild(sheet);

    overlay.addEventListener("click", closePanel);
    q("#v99mOccClose").addEventListener("click", closePanel);
    q("#v99mOccRefresh").addEventListener("click", loadPanel);
  }

  function openPanel(){
    ensurePanel();
    q("#v99mOccOverlay").classList.add("open");
    q("#v99mOccSheet").classList.add("open");
    loadPanel();
  }

  function closePanel(){
    var overlay = q("#v99mOccOverlay");
    var sheet = q("#v99mOccSheet");
    if(overlay) overlay.classList.remove("open");
    if(sheet) sheet.classList.remove("open");
  }

  
  function v99uNormText(v){
    return String(v || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function v99uNearestTopCard(el){
    if(!el || !el.closest) return null;

    /*
      V99U SAFE:
      Sadece üstteki küçük bilgi kartının kendisini yakala.
      Ortak satır/container yakalanırsa HIZ ve DURUM da yanlışlıkla
      DOLULUK panelini açıyor.
    */
    return el.closest(
      ".v99-gauge-cell, .v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card"
    );
  }

  function isDolulukTarget(el){
    var card = v99uNearestTopCard(el);
    if(!card) return false;

    if(card.closest(".v99m-overlay, .v99m-panel, .v99-prox-card, .v99-tl-card, .v99-dock, nav")){
      return false;
    }

    var label = card.querySelector(
      ".v99-gauge-label, .v99-stat-label, .v99-info-label, .card-label, .label, .l"
    );

    var labelText = v99uNormText(label ? label.textContent : "");

    return labelText === "DOLULUK";
  }

  function markDolulukCards(){
    all(".v99m-occ-clickable").forEach(function(el){
      el.classList.remove("v99m-occ-clickable");
    });

    all(".v99-gauge-cell, .v99-gauge, .v99-stat, .v99-top-stat, .v99-info-cell, .v99-stat-card").forEach(function(el){
      if(isDolulukTarget(el)){
        el.classList.add("v99m-occ-clickable");
        el.setAttribute("data-v99u-doluluk-click", "1");
      }else{
        el.removeAttribute("data-v99u-doluluk-click");
      }
    });
  }

  document.addEventListener("click", function(ev){

    var el = ev.target;
    while(el && el !== document.body){
      if(isDolulukTarget(el)){
        ev.preventDefault();
        openPanel();
        return;
      }
      el = el.parentElement;
    }
  }, true);

  function num(v){
    var n = Number(v);
    return Number.isFinite(n) ? n : 0;
  }

  function seatGenderClass(s){
    var g = norm(s.gender || "");
    if(g.indexOf("bayan") >= 0 || g.indexOf("kadin") >= 0) return "female";
    if(g.indexOf("bay") >= 0 || g.indexOf("erkek") >= 0) return "male";
    return "";
  }

  function renderSummary(data, seats){
    var total = Number(data.total_seats || 40);
    var occupied = seats.filter(function(s){ return !!s.occupied; }).length;
    var free = Math.max(0, total - occupied);

    var male = seats.filter(function(s){ return !!s.occupied && seatGenderClass(s) === "male"; }).length;
    var female = seats.filter(function(s){ return !!s.occupied && seatGenderClass(s) === "female"; }).length;

    var live = liveStopName();
    var next = nextStopName();

    var offLive = seats.filter(function(s){
      return !!s.occupied && sameStop(s.to_stop, live);
    }).length;

    var offNext = seats.filter(function(s){
      return !!s.occupied && sameStop(s.to_stop, next);
    }).length;

    var bag = seats.reduce(function(a,s){
      return a + num(s.bag_count || s.bag_total || s.bagaj_count);
    }, 0);

    var summary = q("#v99mOccSummary");
    if(summary){
      summary.innerHTML = `
        <div class="v99m-stat ${free <= 2 ? "danger" : (free <= 5 ? "warn" : "")}">
          <div class="v">${occupied} / ${total}</div>
          <div class="l">DOLULUK</div>
        </div>
        <div class="v99m-stat good">
          <div class="v">${free}</div>
          <div class="l">BOŞ KOLTUK</div>
        </div>
        <div class="v99m-stat warn">
          <div class="v">${offLive}</div>
          <div class="l">BU DURAKTA İNECEK</div>
        </div>
        <div class="v99m-stat blue">
          <div class="v">${male}</div>
          <div class="l">BAY</div>
        </div>
        <div class="v99m-stat pink">
          <div class="v">${female}</div>
          <div class="l">BAYAN</div>
        </div>
        <div class="v99m-stat">
          <div class="v">${bag}</div>
          <div class="l">BAGAJ</div>
        </div>
      `;
    }

    var afterLive = Math.max(0, occupied - offLive);
    var afterNext = Math.max(0, afterLive - offNext);

    var impact = q("#v99mOccImpact");
    if(impact){
      impact.innerHTML = `
        <b>${live || "Canlı durak"}</b> durağında <b>${offLive}</b> kişi inecek → sonra <b>${afterLive}/${total}</b> kalır.<br>
        ${next ? `<b>${next}</b> durağında <b>${offNext}</b> kişi inecek → sonra <b>${afterNext}/${total}</b> kalır.` : `<span class="v99m-muted">Sıradaki durak bulunamadı.</span>`}
      `;
    }

    var liveTag = q("#v99mOccLiveStop");
    if(liveTag) liveTag.textContent = live ? ("Canlı: " + live) : "Canlı: —";
  }

  function renderSeatMap(data, seats){
    var map = q("#v99mSeatMap");
    if(!map) return;

    var positions = data.seat_positions || {};
    var byNo = {};
    seats.forEach(function(s){
      byNo[String(s.seat_no)] = s;
    });

    var maxRow = 0;
    var maxCol = 0;
    var byPos = {};

    Object.keys(positions).forEach(function(no){
      var pos = positions[no] || [];
      var r = Number(pos[0] || 0);
      var c = Number(pos[1] || 0);
      if(r > maxRow) maxRow = r;
      if(c > maxCol) maxCol = c;
      byPos[r + ":" + c] = String(no);
    });

    if(!maxRow || !maxCol){
      maxRow = Math.ceil(Number(data.total_seats || 40) / 4);
      maxCol = 4;
      for(var i=1; i<=Number(data.total_seats || 40); i++){
        var rr = Math.ceil(i / 4);
        var cc = ((i - 1) % 4) + 1;
        byPos[rr + ":" + cc] = String(i);
      }
    }

    map.style.gridTemplateColumns = "repeat(" + maxCol + ", 42px)";
    map.innerHTML = "";

    var live = liveStopName();

    for(var row=1; row<=maxRow; row++){
      for(var col=1; col<=maxCol; col++){
        var no = byPos[row + ":" + col];

        if(!no){
          var sp = document.createElement("div");
          sp.className = "v99m-seat spacer";
          map.appendChild(sp);
          continue;
        }

        var s = byNo[no] || { seat_no:no, occupied:false };
        var cell = document.createElement("button");
        cell.type = "button";
        cell.className = "v99m-seat";

        if(s.occupied){
          cell.classList.add("occ");
          var g = seatGenderClass(s);
          if(g) cell.classList.add(g);

          if(sameStop(s.to_stop, live)){
            cell.classList.add("off");
          }
        }else{
          cell.classList.add("free");
        }

        cell.textContent = no;
        cell.addEventListener("click", function(seat){
          return function(){
            showSeatDetail(seat);
          };
        }(s));

        map.appendChild(cell);
      }
    }
  }

  function showSeatDetail(s){
    var box = q("#v99mSeatDetail");
    if(!box) return;

    if(!s || !s.occupied){
      box.innerHTML = `<b>Koltuk ${s && s.seat_no ? s.seat_no : "—"}</b> boş görünüyor.`;
      return;
    }

    var g = s.gender ? String(s.gender) : "—";
    var from = s.from_stop || "—";
    var to = s.to_stop || "—";
    var bag = num(s.bag_count || s.bag_total || s.bagaj_count);

    box.innerHTML = `
      <b>Koltuk ${s.seat_no}</b> · ${g}<br>
      ${from} → ${to}<br>
      Bagaj: <b>${bag}</b>
    `;
  }

  async function loadPanel(){
    ensurePanel();

    var impact = q("#v99mOccImpact");
    var map = q("#v99mSeatMap");

    if(impact) impact.textContent = "Koltuk verisi alınıyor…";
    if(map) map.innerHTML = "";

    try{
      var res = await fetch("/api/live-seat-map?_=" + Date.now(), {
        cache:"no-store",
        headers:{ "Accept":"application/json" }
      });

      var data = await res.json();
      if(!data || data.ok === false){
        throw new Error((data && data.msg) || "API veri döndürmedi");
      }

      var seats = Array.isArray(data.seats) ? data.seats : [];
      renderSummary(data, seats);
      renderSeatMap(data, seats);

    }catch(err){
      if(impact){
        impact.innerHTML = `<b>Doluluk verisi alınamadı.</b><br><span class="v99m-muted">${String(err && err.message || err)}</span>`;
      }
    }
  }

  markDolulukCards();
  setInterval(markDolulukCards, 1500);

  window.MuavinV99OccupancyPanel = {
    open: openPanel,
    close: closePanel,
    reload: loadPanel
  };
})();
/* V99M_OCCUPANCY_PANEL_END */

/* V99O_SEAT_GENDER_SELECTED_JS_START */
(function(){
  "use strict";

  var selectedSeatNo = "";

  function q(sel){
    return document.querySelector(sel);
  }

  function qa(sel, root){
    return Array.from((root || document).querySelectorAll(sel));
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
      .replace(/\s+/g, "")
      .trim();
  }

  function sameStop(a,b){
    var na = norm(a);
    var nb = norm(b);
    if(!na || !nb) return false;
    return na === nb || na.indexOf(nb) >= 0 || nb.indexOf(na) >= 0;
  }

  function getLiveStop(){
    return text(q("#liveCurrentStopName")) || text(q("[data-live-stop]")) || "";
  }

  function genderClass(seat){
    var g = norm(seat && seat.gender);

    if(g.indexOf("bayan") >= 0 || g.indexOf("kadin") >= 0 || g.indexOf("female") >= 0){
      return "v99-seat-female";
    }

    if(g.indexOf("bay") >= 0 || g.indexOf("erkek") >= 0 || g.indexOf("male") >= 0){
      return "v99-seat-male";
    }

    return "v99-seat-unknown";
  }

  function num(x){
    var n = Number(x || 0);
    return Number.isFinite(n) ? n : 0;
  }

  function isSeatNumberText(t){
    if(!/^\d{1,2}$/.test(t)) return false;
    var n = Number(t);
    return n >= 1 && n <= 60;
  }

  function looksLikeSeatElement(el){
    if(!el) return false;

    var t = text(el);
    var dataNo = el.getAttribute("data-v99-seat-no") || el.getAttribute("data-seat-no") || el.getAttribute("data-seat") || el.dataset.seatNo || "";

    if(!isSeatNumberText(dataNo || t)) return false;

    if(el.closest(".v99-dock, .v99-bottom-dock, nav, .bottom-nav, .v99-top, .v99-stats, .v99-tl-card, .v99-prox-card")){
      return false;
    }

    var r = el.getBoundingClientRect();
    if(r.width && r.height){
      if(r.width < 28 || r.height < 28) return false;
      if(r.width > 130 || r.height > 130) return false;
    }

    return true;
  }

  function findSeatEls(){
    var direct = qa("[data-seat-no], [data-seat], .v99-seat, .v99-seat-cell, .v99-seat-btn, .v99-map-seat, .v99-bus-seat, .seat-cell, .seat-btn")
      .filter(looksLikeSeatElement);

    if(direct.length >= 10) return direct;

    return qa("button, .seat, div, span")
      .filter(looksLikeSeatElement);
  }

  function ensureBagDot(el, count){
    var old = el.querySelector(":scope > .v99-seat-bag-dot");
    if(count <= 0){
      if(old) old.remove();
      return;
    }

    if(!old){
      old = document.createElement("span");
      old.className = "v99-seat-bag-dot";
      el.appendChild(old);
    }

    old.innerHTML = "🧳" + (count > 1 ? "<b>" + count + "</b>" : "");
  }

  function applySeatClasses(seats){
    var live = getLiveStop();
    var byNo = {};

    seats.forEach(function(s){
      byNo[String(s.seat_no || "").trim()] = s;
    });

    findSeatEls().forEach(function(el){
      var no = String(
        el.getAttribute("data-seat-no") ||
        el.getAttribute("data-seat") ||
        el.dataset.seatNo ||
        text(el)
      ).trim();

      if(!isSeatNumberText(no)) return;

      var s = byNo[no] || { seat_no:no, occupied:false };

      el.classList.add("v99-seat-color-cell");
      el.setAttribute("data-v99-seat-no", no);

      el.classList.remove(
        "v99-seat-free",
        "v99-seat-male",
        "v99-seat-female",
        "v99-seat-unknown",
        "v99-seat-off-here",
        "v99-seat-has-bag",
        "v99-seat-selected"
      );

      if(s.occupied){
        el.classList.add(genderClass(s));
      }else{
        el.classList.add("v99-seat-free");
      }

      if(s.occupied && live && sameStop(s.to_stop, live)){
        el.classList.add("v99-seat-off-here");
      }

      var bag = num(s.bag_count || s.bag_total || s.bagaj_count);
      if(bag > 0){
        el.classList.add("v99-seat-has-bag");
      }

      ensureBagDot(el, bag);

      if(selectedSeatNo && String(selectedSeatNo) === String(no)){
        el.classList.add("v99-seat-selected");
      }
    });

    ensureLegend();
  }

  function ensureLegend(){
    if(q(".v99-seat-gender-legend")) return;

    var seatEls = findSeatEls();
    if(!seatEls.length) return;

    var host = seatEls[seatEls.length - 1].closest(".v99-seat-map, .v99-seat-grid, .v99-bus-map, .v99-seat-plan, .v99-occupancy-panel, .v99-seat-shell");
    if(!host){
      host = seatEls[seatEls.length - 1].parentElement;
    }

    if(!host || !host.parentElement) return;

    var legend = document.createElement("div");
    legend.className = "v99-seat-gender-legend";
    legend.innerHTML =
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot male"></i>Bay</span>' +
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot female"></i>Bayan</span>' +
      '<span class="v99-seat-legend-chip"><i class="v99-seat-legend-dot selected"></i>Seçili</span>';

    host.parentElement.insertBefore(legend, host.nextSibling);
  }

  async function refreshSeatColors(){
    try{
      var res = await fetch("/api/live-seat-map?_v=v99o_" + Date.now(), {
        credentials:"same-origin",
        cache:"no-store"
      });

      if(!res.ok) return;

      var data = await res.json();
      var seats = Array.isArray(data.seats) ? data.seats : [];

      applySeatClasses(seats);
    }catch(e){}
  }

  document.addEventListener("click", function(ev){
    var el = ev.target.closest("[data-v99-seat-no], [data-seat-no], [data-seat], .v99-seat-color-cell");

    if(!el || !looksLikeSeatElement(el)) return;

    var no = String(
      el.getAttribute("data-v99-seat-no") ||
      el.getAttribute("data-seat-no") ||
      el.getAttribute("data-seat") ||
      el.dataset.seatNo ||
      text(el)
    ).trim();

    if(!isSeatNumberText(no)) return;

    selectedSeatNo = no;

    qa(".v99-seat-color-cell.v99-seat-selected").forEach(function(x){
      x.classList.remove("v99-seat-selected");
    });

    el.classList.add("v99-seat-selected");
  }, true);

  window.MuavinV99SeatColorRefresh = refreshSeatColors;

  refreshSeatColors();

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", refreshSeatColors);
  }

  window.addEventListener("load", refreshSeatColors);
  document.addEventListener("continueEtaUpdated", refreshSeatColors);

  var left = 40;
  var timer = setInterval(function(){
    refreshSeatColors();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 900);
})();
/* V99O_SEAT_GENDER_SELECTED_JS_END */

