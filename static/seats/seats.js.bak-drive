const BOOT = window.SEATS_BOOT || {};
const URLS = BOOT.urls || {};

const csrf = BOOT.csrf || "";
const ROUTE_NAME = BOOT.routeName || "";
const TRIP_DATE = BOOT.tripDate || "";
const TRIP_DEPARTURE_TIME = BOOT.departureTime || "";
const TRIP_KEY = BOOT.tripKey || "";

const seatPositions = BOOT.seatPositions || {};
const assigned = BOOT.assigned || {};
const stopsMap = BOOT.stopsMap || {};
const boardsMapServer = BOOT.boardsMapServer || {};
const genders = BOOT.genders || {};
const serviceMap = BOOT.serviceMap || {};
const serviceNotes = BOOT.serviceNotes || {};
const serverStops = BOOT.serverStops || [];

const BAG_TRIP = TRIP_KEY;
  window.BAG_TRIP = BAG_TRIP;

  let ROUTE_SCHEDULES = {
    "Denizli – İstanbul": [
      { stop: "Denizli otogar", time: "20:00" },
      { stop: "Alaşehir Otogar", time: "23:10" },
      { stop: "Salihli Garaj", time: "23:50" },
      { stop: "Turgutlu Garaj", time: "00:25" },
      { stop: "Manisa Otogar", time: "01:05" },
      { stop: "Balıkesir", time: "03:10" },
      { stop: "Bursa Otogar", time: "04:30" },
      { stop: "Harem", time: "07:30" },
      { stop: "Esenler Otogar", time: "08:00" }
    ],
    "İstanbul – Denizli": [
      { stop: "Esenler Otogar", time: "20:00" },
      { stop: "Harem", time: "20:35" },
      { stop: "Bursa Otogar", time: "23:15" },
      { stop: "Balıkesir", time: "00:35" },
      { stop: "Manisa Otogar", time: "02:40" },
      { stop: "Turgutlu Garaj", time: "03:15" },
      { stop: "Salihli Garaj", time: "03:55" },
      { stop: "Alaşehir Otogar", time: "04:40" },
      { stop: "Denizli otogar", time: "07:20" }
    ],
    "Denizli – İzmir": [
      { stop: "Denizli otogar", time: "20:00" },
      { stop: "Alaşehir Otogar", time: "22:10" },
      { stop: "Salihli Garaj", time: "22:50" },
      { stop: "Turgutlu Garaj", time: "23:25" },
      { stop: "Manisa Otogar", time: "00:00" },
      { stop: "İzmir Otogar", time: "01:10" }
    ],
    "İzmir – Denizli": [
      { stop: "İzmir Otogar", time: "20:00" },
      { stop: "Manisa Otogar", time: "21:00" },
      { stop: "Turgutlu Garaj", time: "21:35" },
      { stop: "Salihli Garaj", time: "22:10" },
      { stop: "Alaşehir Otogar", time: "22:50" },
      { stop: "Denizli otogar", time: "01:00" }
    ]
  };

  const VOICE_HELP = [
    "kaç yolcu var",
    "ayakta kaç kişi var",
    "hesap aç",
    "emanet aç",
    "sıradaki durak [durak adı]",
    "durak seç [durak adı]",
    "[durak adı] kaç yolcu var",
    "bir sonraki durak",
    "rötar kaç",
    "hangi duraktayız",
    "sesli yardım"
  ];

  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));

  function onClick(sel, fn){
    const el = $(sel);
    if(el) el.addEventListener("click", fn);
  }

  function onChange(sel, fn){
    const el = $(sel);
    if(el) el.addEventListener("change", fn);
  }

  function setText(sel, val){
    const el = $(sel);
    if(el) el.textContent = val;
  }

  function setValue(sel, val){
    const el = $(sel);
    if(el) el.value = val;
  }

  function show(el){
    if(el) el.style.display = "block";
  }

  function hide(el){
    if(el) el.style.display = "none";
  }

  const boardsMap = Object.assign(
    {},
    boardsMapServer || {},
    JSON.parse(localStorage.getItem("boardsMap:" + TRIP_KEY) || "{}")
  );

  let cachedStops = null;
  let currentSeat = null;
  let multiMode = false;
  let standingCount = 0;
  let standingRevenue = 0;
  let standingItems = [];
  let parcelItems = [];
  let geoWatchId = null;
  let speedWatchId = null;
  let lastAlertAt = 0;
  let snoozeUntil = 0;
  let lastApproach = { stop:null, seats:[] };
  let currentCoords = null;
  let lastApproachVoiceStop = "";
  let lastRouteStripCenteredStop = "";

// Bagaj göz bilgisi sesli uyarıda kullanılacak.
// Örnek: bagMetaCache["3"] = {count:1, right:0, left_front:1, left_back:0, eyes:["LF"]}
const bagMetaCache = {};

  const multiSelected = new Set();
  const ALERT_COOLDOWN_MS = 3 * 60 * 1000;

  const speedState = {
    current: 0,
    history: [],
    lastLimitObj: null,
    lastLimitFetchTs: 0,
    lastLimitValue: null,
    lastWarnOverAt: 0,
    lastWarnNearAt: 0,
    liveStop: "",
    passedStops: new Set(),
    etaItems: []
  };

  function toast(msg, ms=2400){
    const t = $("#toast");
    if(!t) return;
    t.textContent = msg;
    t.style.display = "block";
    clearTimeout(toast._timer);
    toast._timer = setTimeout(() => {
      t.style.display = "none";
    }, ms);
  }

  function fmtTL(v){
    return "₺" + Number(v || 0).toFixed(2);
  }

  function parseMoney(v){
    const s = String(v ?? "").replace(",", ".").trim();
    const n = parseFloat(s);
    return Number.isFinite(n) ? n : 0;
  }

  function numTR(v){
    const n = parseFloat(String(v ?? "").replace(",", "."));
    return Number.isFinite(n) ? n : NaN;
  }

  function norm(s){
    return (s || "")
      .toString()
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .trim()
      .toLowerCase();
  }

  function safeDate(dateStr, fallback=new Date()){
    const d = new Date(dateStr);
    return Number.isNaN(d.getTime()) ? fallback : d;
  }

  async function safeJsonFetch(url, opt){
    const res = await fetch(url, opt || {});
    const ct = res.headers.get("content-type") || "";
    if(!ct.includes("application/json")){
      const txt = await res.text();
      throw new Error(txt || "JSON bekleniyordu");
    }
    return await res.json();
  }

  function persistBoards(){
    localStorage.setItem("boardsMap:" + TRIP_KEY, JSON.stringify(boardsMap || {}));
  }

  function persistVoiceState(){
    localStorage.setItem("liveStop:" + TRIP_KEY, speedState.liveStop || "");
    localStorage.setItem("passedStops:" + TRIP_KEY, JSON.stringify([...speedState.passedStops]));
  }

  function loadVoiceState(){
    speedState.liveStop = localStorage.getItem("liveStop:" + TRIP_KEY) || "";
    try{
      speedState.passedStops = new Set(JSON.parse(localStorage.getItem("passedStops:" + TRIP_KEY) || "[]"));
    }catch(_){
      speedState.passedStops = new Set();
    }
  }

  function persistStandingTotals(){
    localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({
      count: standingCount,
      revenue: standingRevenue
    }));
  }

  function persistStandingItems(){
    localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems || []));
  }

  function sampleRandom(arr, count){
    const a = arr.slice();
    for(let i = a.length - 1; i > 0; i--){
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a.slice(0, Math.max(0, Math.min(count, a.length)));
  }

  function allStopsList(){
    if(Array.isArray(cachedStops) && cachedStops.length) return cachedStops.map(x => x.name);
    return Array.isArray(serverStops) ? serverStops.slice() : [];
  }

  function indexOfStopByName(name){
    const list = allStopsList();
    const t = norm(name);
    return list.findIndex(x => norm(x) === t);
  }

  function findStopByName(name){
    const t = norm(name);
    const list = Array.isArray(cachedStops)
      ? cachedStops
      : (Array.isArray(serverStops) ? serverStops.map(s => ({ name:s, lat:null, lng:null })) : []);
    return list.find(x => norm(x?.name) === t) || null;
  }

  function findCanonicalStopName(name){
    const s = findStopByName(name);
    return s?.name || "";
  }

  function hasCoord(stop){
    if(!stop) return false;
    const lat = parseFloat(stop.lat);
    const lng = parseFloat(stop.lng);
    return Number.isFinite(lat) && Number.isFinite(lng);
  }

  function distKm(a, b){
    const R = 6371;
    const toRad = d => d * Math.PI / 180;
    const dLat = toRad(b.lat - a.lat);
    const dLng = toRad(b.lng - a.lng);
    const la1 = toRad(a.lat);
    const la2 = toRad(b.lat);
    const h = Math.sin(dLat/2)**2 + Math.cos(la1) * Math.cos(la2) * Math.sin(dLng/2)**2;
    return 2 * R * Math.asin(Math.sqrt(h));
  }

function nearestStopByGps(maxKm = 15){
  if(!currentCoords || !Array.isArray(cachedStops)) return "";

  let best = null;

  for(const s of cachedStops){
    if(!s || !hasCoord(s)) continue;

    const km = distKm(currentCoords, {
      lat: Number(s.lat),
      lng: Number(s.lng)
    });

    if(!best || km < best.km){
      best = {
        name: s.name,
        km
      };
    }
  }

  if(!best) return "";

  // Çok uzaktaysa canlı durak göstermesin
  if(best.km > maxKm) return "";

  return best.name || "";
}

function getDisplayLiveStop(){
  return speedState.liveStop || nearestStopByGps(15) || "";
}

function stopDistanceKmByName(name){
  if(!name || !currentCoords) return NaN;

  const stopObj = findStopByName(name);
  if(!stopObj || !hasCoord(stopObj)) return NaN;

  return distKm(currentCoords, {
    lat: Number(stopObj.lat),
    lng: Number(stopObj.lng)
  });
}

function bagSeatsForStop(stopName){
  const seats = seatsForStop(stopName).map(Number).filter(Boolean);
  const bagSeats = [];

  seats.forEach(seatNo => {
    const el = document.querySelector(`.seat[data-seat="${seatNo}"]`);
    if(!el) return;

    const cntText = el.querySelector(".bag-count")?.textContent || "0";
    const cnt = parseInt(cntText, 10) || 0;
    const hasBag = el.classList.contains("has-bag") || cnt > 0;

    if(hasBag){
      bagSeats.push(seatNo);
    }
  });

  return bagSeats;
}

function formatSeatListForVoice(seats){
  const list = seats.map(String);

  if(list.length === 0) return "";
  if(list.length === 1) return `${list[0]} numaralı koltukta`;

  const last = list.pop();
  return `${list.join(", ")} ve ${last} numaralı koltuklarda`;
}


function bagEyeVoicePartsForSeat(seatNo){
  const meta = bagMetaCache[String(seatNo)] || {};
  const parts = [];

  const right = Number(meta.right || 0);
  const leftFront = Number(meta.left_front || 0);
  const leftBack = Number(meta.left_back || 0);

  function add(label, count){
    if(count <= 0) return;
    if(count === 1) parts.push(`${label} gözde bagaj`);
    else parts.push(`${label} gözde ${count} bagaj`);
  }

  add("sağ", right);
  add("sol ön", leftFront);
  add("sol arka", leftBack);

  // Eğer detaylı adet yok ama göz kodu varsa yine göz adını söyle.
  if(!parts.length && Array.isArray(meta.eyes)){
    if(meta.eyes.includes("R")) parts.push("sağ gözde bagaj");
    if(meta.eyes.includes("LF")) parts.push("sol ön gözde bagaj");
    if(meta.eyes.includes("LB")) parts.push("sol arka gözde bagaj");
  }

  return parts;
}

function bagVoiceSummaryForStop(stopName){
  const seats = bagSeatsForStop(stopName).map(Number).filter(Boolean);
  if(!seats.length) return "";

  const chunks = seats.map(seatNo => {
    const parts = bagEyeVoicePartsForSeat(seatNo);

    if(parts.length){
      return `${seatNo} numarada ${parts.join(", ")}`;
    }

    return `${seatNo} numarada bagaj`;
  });

  return `Bagaj uyarısı: ${chunks.join(". ")} var.`;
}


function maybeSpeakApproachStop(stopName, km){
  if(!stopName) return;
  if(!Number.isFinite(km)) return;
  if(km > 5) return;

  const key = `${TRIP_KEY}:${stopName}`;
  if(lastApproachVoiceStop === key) return;

  lastApproachVoiceStop = key;
  speak(`${stopName} durağına yaklaşılıyor. ${stopHumanVoiceSummary(stopName)}`);
}

function tripStartDate(){
  const datePart = TRIP_DATE || new Date().toISOString().slice(0,10);

  // Öncelik: Saat yönetimindeki profilin ilk saatli durağı
  const routeSchedule = getRouteSchedule();
  const firstTimedStop = Array.isArray(routeSchedule)
    ? routeSchedule.find(x => x && String(x.time || "").trim())
    : null;

  const rawTime = firstTimedStop?.time || TRIP_DEPARTURE_TIME || "00:00";
  const timePart = String(rawTime).trim();

  const iso = `${datePart}T${timePart.length === 5 ? timePart + ":00" : timePart}`;
  return safeDate(iso, new Date());
}

  function getRouteSchedule(){
    return ROUTE_SCHEDULES[ROUTE_NAME] || [];
  }

async function loadRouteScheduleFromApi(){
  try{
    const url = `/api/route-schedule?route=${encodeURIComponent(ROUTE_NAME)}&direction=gidis&_=${Date.now()}`;
    const j = await safeJsonFetch(url);

    if(!j || !j.ok || !Array.isArray(j.items) || !j.items.length){
      console.warn("Saat profili bulunamadı, gömülü liste kullanılacak.");
      return false;
    }

    const apiSchedule = j.items
      .filter(x => Number(x.is_timed) === 1 && String(x.planned_time || "").trim())
      .map(x => ({
        stop: x.stop_name,
        time: String(x.planned_time || "").trim(),
        segment_km: x.segment_km,
        sort_order: x.sort_order
      }));

    if(apiSchedule.length){
      ROUTE_SCHEDULES[ROUTE_NAME] = apiSchedule;
      console.log("Saat profili API'den yüklendi:", apiSchedule);
      return true;
    }

    return false;
  }catch(err){
    console.warn("Saat profili API hatası:", err);
    return false;
  }
}

  function scheduleOffsetsForRoute(){
    const sample = getRouteSchedule();
    if(!sample.length) return [];

    let prev = null;
    let carry = 0;
    let firstAbs = null;

    return sample.map(item => {
      const parts = String(item.time || "00:00").split(":");
      const hh = parseInt(parts[0], 10) || 0;
      const mm = parseInt(parts[1], 10) || 0;
      let cur = hh * 60 + mm + carry;

      if(prev !== null && cur < prev){
        carry += 1440;
        cur = hh * 60 + mm + carry;
      }

      if(firstAbs === null) firstAbs = cur;
      prev = cur;

      return {
        stop:item.stop,
        sampleTime:item.time,
        offsetMin: cur - firstAbs
      };
    });
  }

  function buildActualSchedule(){
    const start = tripStartDate();
    const offsets = scheduleOffsetsForRoute();

    return offsets.map(x => ({
      stop: x.stop,
      plan: x.sampleTime,
      planDate: new Date(start.getTime() + x.offsetMin * 60000),
      offsetMin: x.offsetMin,
      routeIndex: indexOfStopByName(x.stop)
    }));
  }

  function minutesDiff(a, b){
    return Math.round((a - b) / 60000);
  }

  function fmtHour(d){
    if(!d || Number.isNaN(d.getTime())) return "—";
    return d.toLocaleTimeString("tr-TR", { hour:"2-digit", minute:"2-digit" });
  }

  function fmtSignedMin(mins){
    if(!Number.isFinite(mins)) return "—";
    if(Math.abs(mins) > 720) return "Plan dışı";
    if(mins === 0) return "Tam saat";
    if(mins < 0) return `${Math.abs(mins)} dk erken`;
    return `${mins} dk rötar`;
  }

  function getSelectedStopName(){
    return ($("#alertStop")?.value || "").trim();
  }

  function isTimedStop(name){
    return getRouteSchedule().some(x => norm(x.stop) === norm(name));
  }

  function hasPassengersFor(stopName){
    return seatsForStop(stopName).length > 0;
  }

  function isFinalStop(name){
    const list = allStopsList();
    const idx = indexOfStopByName(name);
    return idx >= 0 && idx === list.length - 1;
  }

  async function fetchStops(){
    const j = await safeJsonFetch("/api/stops");
    if(!j.ok) throw new Error(j.msg || "Duraklar alınamadı");

    let stops = (j.stops || []).map(name => ({ name, lat:null, lng:null }));

    try{
      const c = await safeJsonFetch("/api/coords");
      if(c.ok){
        const coordMap = new Map((c.items || []).map(i => [i.stop, { lat:i.lat, lng:i.lng }]));
        stops = stops.map(s => coordMap.has(s.name) ? { ...s, ...coordMap.get(s.name) } : s);
      }
    }catch(_){}

    cachedStops = stops;
    return stops;
  }

  async function populateStops(){
    if(!cachedStops) await fetchStops();

    const ids = ["alertStop","pickup","dropoff","bulkFrom","bulkTo","cashFrom","cashTo"];
    for(const id of ids){
      const el = $("#" + id);
      if(!el) continue;

      const prev = el.value;
      el.innerHTML = "";

      const o0 = document.createElement("option");
      o0.value = "";
      o0.textContent = "—";
      el.appendChild(o0);

      for(const s of cachedStops){
        const o = document.createElement("option");
        o.value = s.name;
        o.dataset.label = s.name;
        o.textContent = s.name + (hasCoord(s) ? " •" : "");
        el.appendChild(o);
      }

      if(prev && [...el.options].some(x => x.value === prev)){
        el.value = prev;
      }
    }
  }

  function computeSeatCountsByStop(){
    const out = {};
    Object.values(stopsMap || {}).forEach(stop => {
      if(stop) out[stop] = (out[stop] || 0) + 1;
    });
    return out;
  }

  function computeStandingCountsByStop(){
    const out = {};
    (standingItems || []).forEach(it => {
      const raw = (it?.to || "").trim();
      if(!raw) return;
      const key = (findStopByName(raw)?.name || raw).trim();
      const c = Number(it?.count || 0);
      if(!c) return;
      out[key] = (out[key] || 0) + c;
    });
    return out;
  }

  function computeParcelCountsByStop(){
    const out = {};
    (parcelItems || []).forEach(it => {
      const raw = (it?.to || "").trim();
      if(!raw) return;
      const key = (findStopByName(raw)?.name || raw).trim();
      const c = Number(it?.count || 0);
      if(!c) return;
      out[key] = (out[key] || 0) + c;
    });
    return out;
  }

  function totalParcelCount(){
    return (parcelItems || []).reduce((a,b) => a + Number(b?.count || 0), 0);
  }

  function totalServiceCount(){
    return Object.keys(assigned || {}).filter(k => assigned[k] && serviceMap[k]).length;
  }

  function seatsForStop(stop){
    const out = [];
    for(const [seat, st] of Object.entries(stopsMap || {})){
      if(norm(st) === norm(stop)) out.push(Number(seat));
    }
    return out.sort((a,b) => a - b);
  }

  
function stopHumanVoiceSummary(stopName){
  const stop = String(stopName || "").trim();
  if(!stop) return "Durak bilgisi bulunamadı.";

  let seats = [];
  let parcelCt = 0;
  let standingCt = 0;
  let bagSeats = [];

  try{
    seats = seatsForStop(stop).map(Number).filter(Boolean);
  }catch(_){
    seats = [];
  }

  try{
    parcelCt = computeParcelCountsByStop()[stop] || 0;
  }catch(_){
    parcelCt = 0;
  }

  try{
    standingCt = computeStandingCountsByStop()[stop] || 0;
  }catch(_){
    standingCt = 0;
  }

  try{
    bagSeats = bagSeatsForStop(stop);
  }catch(_){
    bagSeats = [];
  }

  let bay = 0;
  let bayan = 0;
  let yolcu = 0;

  seats.forEach(seatNo => {
    const g = genders[String(seatNo)] || "";
    if(g === "bay") bay++;
    else if(g === "bayan") bayan++;
    else yolcu++;
  });

  // Ayakta yolcuyu "ayakta" diye söyleme; normal yolcu gibi ekle.
  yolcu += Number(standingCt || 0);

  const parts = [];
  if(bay > 0) parts.push(`${bay} bay`);
  if(bayan > 0) parts.push(`${bayan} bayan`);
  if(yolcu > 0) parts.push(`${yolcu} yolcu`);

  let msg = "";

  if(parts.length > 0){
    msg = `${stop} durağında ${parts.join(", ")} inecek.`;
  }else{
    msg = `${stop} durağı için inecek yolcu görünmüyor.`;
  }

  if(parcelCt > 0){
    msg += ` Ayrıca ${parcelCt} emanet teslim var.`;
  }

  const bagMsg = bagVoiceSummaryForStop(stop);
  if(bagMsg){
    msg += ` ${bagMsg}`;
  }

  return msg;
}


function setVoiceBadge(text){
    setText("#voiceStateBadge", text || "Hazır");
  }

  function refreshStopBadges(){
    const sel = $("#alertStop");
    if(!sel) return;

    const seatCounts = computeSeatCountsByStop();
    const standingCounts = computeStandingCountsByStop();
    const parcelCounts = computeParcelCountsByStop();

    [...sel.options].forEach(opt => {
      if(!opt.value){
        opt.textContent = "—";
        return;
      }

      const base = opt.dataset.label || opt.value;
      const stop = findStopByName(base);
      const dot = hasCoord(stop) ? " •" : "";
      const seatTxt = seatCounts[base] ? ` (${seatCounts[base]} koltuk)` : "";
      const standTxt = standingCounts[base] ? ` + Ayakta ${standingCounts[base]}` : "";
      const parcelTxt = parcelCounts[base] ? ` 📦 ${parcelCounts[base]}` : "";

      opt.textContent = base + dot + seatTxt + standTxt + parcelTxt;
    });
  }

  function updateStopSeatBadges(){
    const stop = getSelectedStopName();
    $$(".seat").forEach(el => el.classList.remove("has-stop"));
    if(!stop) return;

    seatsForStop(stop).forEach(n => {
      const el = $("#seat-" + n);
      if(el) el.classList.add("has-stop");
    });
  }

  function setSeatVisual(seatNo){
    const key = String(seatNo);
    const el = $("#seat-" + seatNo);
    if(!el) return;

    el.classList.remove("male","female","isAssigned","has-service");

    const isAssigned = !!assigned[key];
    const gender = genders[key] || "";

    if(isAssigned) el.classList.add("isAssigned");
    if(gender === "bay") el.classList.add("male");
    if(gender === "bayan") el.classList.add("female");
    if(serviceMap[key]) el.classList.add("has-service");

    const label = $("#label-" + seatNo);
    if(label){
      const from = boardsMap[key] || "";
      const to = stopsMap[key] || "";
      label.textContent = isAssigned ? (from ? `${from} → ${to}` : to) : "";
    }

    const svc = el.querySelector(".svc-badge");
    if(svc){
      const note = (serviceNotes[key] || "").trim();
      svc.title = note ? `Servis: ${note}` : "Servis";
    }
  }

  function updateStats(){
    const totalSeats = Object.keys(seatPositions || {}).length;
    const filled = Object.values(assigned || {}).filter(Boolean).length;
    const empty = totalSeats - filled;
    const occ = totalSeats ? Math.round((filled / totalSeats) * 100) : 0;

    setText("#pillTotal", String(filled + standingCount));
    setText("#pillEmpty", String(empty));
    setText("#pillStanding", String(standingCount));
    setText("#pillCash", fmtTL(standingRevenue));
    setText("#pillService", String(totalServiceCount()));
    setText("#pillParcel", String(totalParcelCount()));
    setText("#topOcc", occ + "%");

    const standingCard = $("#standingCard");
    if(standingCard){
      standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse");
    }

    setText("#quickStandingMeta", `${standingCount} kişi · ${fmtTL(standingRevenue)}`);
  }

  function renderQuickStandingList(){
    const box = $("#quickStandingList");
    if(!box) return;
    box.innerHTML = "";

    if(!standingItems.length){
      box.innerHTML = `<div class="muted">Ayakta kayıt yok.</div>`;
      return;
    }

    standingItems.slice(0, 6).forEach(it => {
      const total = (typeof it?.total_amount !== "undefined" && it?.total_amount !== null)
        ? Number(it.total_amount || 0)
        : (Number(it.count || 0) * Number(it.price || 0));

      const d = document.createElement("div");
      d.className = "standing-item";
      d.innerHTML = `
        <div>
          <b>${it.from || "—"} → ${it.to || "—"}</b>
          <small>${it.count} kişi · ${fmtTL(total)}</small>
        </div>
        <span>${it.payment || "nakit"}</span>
      `;
      box.appendChild(d);
    });
  }

function centerRouteStripItem(item, behavior = "smooth"){
  const wrap = $("#routeStrip");
  if(!wrap || !item) return;

  const left = item.offsetLeft - (wrap.clientWidth / 2) + (item.clientWidth / 2);

  wrap.scrollTo({
    left: Math.max(0, left),
    behavior
  });
}

function renderRouteStrip(){
  const wrap = $("#routeStrip");
  if(!wrap) return;

  const list = allStopsList();
  wrap.innerHTML = "";

  if(!list.length){
    wrap.innerHTML = `
      <div class="route-stop active">
        <div class="name">Rota hazırlanıyor</div>
        <div class="meta">Duraklar yüklenecek</div>
      </div>
    `;
    return;
  }

  const selected = getSelectedStopName();
  const live = getDisplayLiveStop();
  const selectedNorm = norm(selected);
  const liveNorm = norm(live);
  let routeFocusItem = null;
  const liveKm = stopDistanceKmByName(live);
  const liveDangerOn = Number.isFinite(liveKm) && liveKm <= 5;
  // if(liveDangerOn){maybeSpeakApproachStop(live, liveKm);}
  const nextWarnStop = liveDangerOn? computeNextStopName(live || selected || "", "nextWithSeats"): "";
  const greenStop = liveDangerOn && nextWarnStop? computeNextStopName(nextWarnStop, "nextWithSeats"): "";

  const nextWarnNorm = norm(nextWarnStop);
  const greenNorm = norm(greenStop);
  const seatCounts = computeSeatCountsByStop();
  const standingCounts = computeStandingCountsByStop();
  const parcelCounts = computeParcelCountsByStop();

  const actualSchedule = buildActualSchedule();
  const planMap = new Map(
    actualSchedule.map(x => [norm(x.stop), x.plan || ""])
  );

  list.forEach(stop => {
    const seatCt = seatCounts[stop] || 0;
    const standingCt = standingCounts[stop] || 0;
    const parcelCt = parcelCounts[stop] || 0;

    const isActive = !!selectedNorm && norm(stop) === selectedNorm;
    const isLive = !!liveNorm && norm(stop) === liveNorm;
    const isDone = speedState.passedStops.has(stop) && !isActive && !isLive;
    const isNextWarn = liveDangerOn && !!nextWarnNorm && norm(stop) === nextWarnNorm;
    const isFlowGreen = liveDangerOn && !!greenNorm && norm(stop) === greenNorm;

    const stopObj = findStopByName(stop);
    const plan = planMap.get(norm(stop)) || "";
    let kmText = "";

    if(currentCoords && stopObj && hasCoord(stopObj)){
      const km = distKm(currentCoords, {
        lat: Number(stopObj.lat),
        lng: Number(stopObj.lng)
      });
      kmText = `${km.toFixed(1)} km`;
    }

    let metaLine1 = "";
    if(isLive) metaLine1 = "Canlı";
    else if(isActive) metaLine1 = "Seçili";
    else if(isDone) metaLine1 = "Geçildi";
    else metaLine1 = "Bekliyor";

    let metaLine2 = "";
    if(seatCt || standingCt || parcelCt){
      metaLine2 = `${seatCt}K ${standingCt}A ${parcelCt}E`;
    }else{
      metaLine2 = isDone ? "İşlem bitti" : "İşlem yok";
    }

    const extraBits = [];
    if(plan) extraBits.push(`Plan ${plan}`);
    if(kmText) extraBits.push(kmText);
    const item = document.createElement("button");
    item.type = "button";
    item.className = `route-stop ${isActive || isLive ? "active" : ""} ${isDone ? "done" : ""} ${liveDangerOn && isLive ? "live-danger" : ""} ${isNextWarn ? "next-warning" : ""} ${isFlowGreen ? "flow-green" : ""}`;
    if(isLive){routeFocusItem = item;}   

    const planText = plan || "—";
    const kmValue = kmText || "—";

    item.innerHTML = `
  <div class="name">${stop}</div>
  <div class="meta">${metaLine1} · ${metaLine2}</div>
  <div class="extra">
    <div class="extra-line">
      <span class="extra-k">Saat</span>
      <span class="extra-v">${planText}</span>
    </div>
    <div class="extra-line">
      <span class="extra-k">Mesafe</span>
      <span class="extra-v">${kmValue}</span>
    </div>
  </div>
   `;

item.addEventListener("click", () => {
  setSelectedStop(stop, { silent:false, voiceReply:true });
});

wrap.appendChild(item);
});

if(routeFocusItem && live){
  const focusKey = norm(live);

  if(lastRouteStripCenteredStop !== focusKey){
    lastRouteStripCenteredStop = focusKey;

    requestAnimationFrame(() => {
      setTimeout(() => {
        centerRouteStripItem(routeFocusItem, "smooth");
      }, 80);
    });
  }
}
}
  function updateCompactHeader(){
    const selected = getSelectedStopName();
    const live = getDisplayLiveStop();
    const next = computeNextStopName(live || selected || "", "nextWithSeats");

    setText("#topLiveStop", live || selected || "—");
    setText("#topSpeed", `${Math.round(Number(speedState.current || 0))} km/h`);
    setText("#selectedStopBadge", selected || "—");
    setText("#miniStop", selected || live || "—");
    setText("#routeLiveStop", live || "—");
    setText("#routeLiveStopCard", live || "—");
    setValue("#coordStopName", selected || "");
    setText("#routeMiniLive", live || "—");
    setText("#routeMiniNext", next || "—");

    const liveState = $("#miniLiveState");
    if(liveState){
      const seatCt = selected ? seatsForStop(selected).length : 0;
      const standingCt = selected ? (computeStandingCountsByStop()[selected] || 0) : 0;
      const parcelCt = selected ? (computeParcelCountsByStop()[selected] || 0) : 0;
      const totalOps = seatCt + standingCt + parcelCt;

      liveState.textContent = selected
        ? (totalOps > 0 ? "İşlem var" : "Sakin")
        : (live ? "Yolda" : "Hazır");
    }

    renderRouteStrip();
  }

  function computeNextStopName(currentName, mode="nextWithSeats"){
    const list = allStopsList();
    if(!list.length) return "";

    const curIdx = indexOfStopByName(currentName);
    let i = curIdx >= 0 ? curIdx + 1 : 0;

    if(mode === "strictNext") return list[i] || "";

    for(; i < list.length; i++){
      const nm = list[i];
      if(!nm) continue;
      if(mode === "nextWithSeats"){
        if(
          hasPassengersFor(nm) ||
          computeStandingCountsByStop()[nm] ||
          computeParcelCountsByStop()[nm] ||
          isTimedStop(nm)
        ){
          return nm;
        }
      }
    }

    return "";
  }

  function setSelectedStop(name, { silent=false, voiceReply=true } = {}){
    const sel = $("#alertStop");
    if(!sel) return false;

    if(!name){
      sel.value = "";
      refreshStopBadges();
      updateStopSeatBadges();
      updateGeoHint();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      return true;
    }

    const canonical = findCanonicalStopName(name);
    if(!canonical) return false;

    const ok = [...sel.options].some(o => norm(o.value) === norm(canonical));
    if(!ok) return false;

    sel.value = canonical;
    refreshStopBadges();
    updateStopSeatBadges();
    updateGeoHint();
    renderAI();
    renderTimeline();
    updateCompactHeader();

    if(!silent && voiceReply){
      speak(stopHumanVoiceSummary(canonical));
    }

    return true;
  }

  function markPassedStopsUntil(stopName){
    const idx = indexOfStopByName(stopName);
    const list = allStopsList();
    if(idx < 0 || !list.length) return;

    for(let i = 0; i <= idx; i++){
      speedState.passedStops.add(list[i]);
    }
    persistVoiceState();
  }

  function setLiveStop(name){
    const canonical = findCanonicalStopName(name);
    if(!canonical) return false;

    speedState.liveStop = canonical;
    markPassedStopsUntil(canonical);
    persistVoiceState();
    updateCompactHeader();
    renderTimeline();
    renderAI();
    return true;
  }

  function advanceToNextStop({ mode="nextWithSeats", silent=false, ignoreToggle=false } = {}){
    const autoOn = $("#autoAdvanceToggle")?.checked;
    if(autoOn === false && !ignoreToggle) return;

    const cur = getSelectedStopName();
    const next = computeNextStopName(cur, mode);

    if(!next){
      toast("Rota bitti ya da ileride işlem yok.");
      setSelectedStop("", { silent:true, voiceReply:false });
      return;
    }

    setSelectedStop(next, { silent, voiceReply: !silent });
  }

  function updateGeoHint(){
    const h = $("#geoHint");
    if(!h) return;

    const stopName = getSelectedStopName();

    if(geoWatchId){
      return;
    }

    if(!stopName){
      h.textContent = "Durak seç.";
      return;
    }

    const s = findStopByName(stopName);
    h.textContent = hasCoord(s) ? "Koordinat hazır." : "Koordinat yok. Aşağıdan ekleyin.";
  }

  function openModal(backdropSel, modalSel){
    show($(backdropSel));
    show($(modalSel));
  }

  function closeModal(backdropSel, modalSel){
    hide($(backdropSel));
    hide($(modalSel));
  }

  function openSeat(seatNo){
    currentSeat = seatNo;
    $$(".seat.selected").forEach(x => x.classList.remove("selected"));

    const seatEl = $("#seat-" + seatNo);
    if(seatEl) seatEl.classList.add("selected");

    setText("#seatTitle", "Koltuk " + seatNo);
    setValue("#pickup", boardsMap[String(seatNo)] || getSelectedStopName() || "");
    setValue("#dropoff", stopsMap[String(seatNo)] || "");

    const pay = document.querySelector('input[name="pay"][value="nakit"]');
    if(pay) pay.checked = true;

    const ticket = document.querySelector('input[name="ticket"][value="biletsiz"]');
    if(ticket) ticket.checked = true;

    setValue("#price", "0.00");

    const prevGender = genders[String(seatNo)] || "";
    const gInput =
      document.querySelector(`input[name="gender"][value="${prevGender}"]`) ||
      document.querySelector('input[name="gender"][value=""]');
    if(gInput) gInput.checked = true;

    if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)];
    setValue("#service_note", serviceNotes[String(seatNo)] || "");
    if($("#pairOk")) $("#pairOk").checked = false;

    openModal("#seatBackdrop", "#seatModal");
  }

  function closeSeat(){
    currentSeat = null;
    closeModal("#seatBackdrop", "#seatModal");
    $$(".seat.selected").forEach(x => x.classList.remove("selected"));
  }

  async function saveSeat(){
    if(!currentSeat) return;

    const from = $("#pickup")?.value || getSelectedStopName() || "";
    const stop = $("#dropoff")?.value || "";
    const ticket = document.querySelector('input[name="ticket"]:checked')?.value || "biletsiz";
    const payment = document.querySelector('input[name="pay"]:checked')?.value || "nakit";
    const amount = parseMoney($("#price")?.value || 0);
    const gender = document.querySelector('input[name="gender"]:checked')?.value || "";
    const pair_ok = $("#pairOk")?.checked ? 1 : 0;
    const service = $("#service")?.checked || false;
    const service_note = $("#service_note")?.value || "";

    try{
      const j = await safeJsonFetch("/api/seat", {
        method:"POST",
        headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
        body:JSON.stringify({
          seat_no: currentSeat,
          from,
          stop,
          ticket_type: ticket,
          payment,
          amount,
          gender,
          pair_ok,
          service,
          service_note
        })
      });

      if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");

      assigned[String(currentSeat)] = true;
      stopsMap[String(currentSeat)] = stop;
      genders[String(currentSeat)] = gender;
      serviceMap[String(currentSeat)] = !!service;
      serviceNotes[String(currentSeat)] = service_note;
      boardsMap[String(currentSeat)] = from;

      persistBoards();
      setSeatVisual(currentSeat);
      closeSeat();
      updateStats();
      refreshStopBadges();
      updateStopSeatBadges();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      toast("Koltuk kaydedildi");
    }catch(e){
      toast(e.message || "Kaydetme hatası");
    }
  }

  function clearSeatUI(seatNo){
    delete assigned[String(seatNo)];
    delete stopsMap[String(seatNo)];
    delete genders[String(seatNo)];
    delete serviceMap[String(seatNo)];
    delete serviceNotes[String(seatNo)];
    delete boardsMap[String(seatNo)];

    persistBoards();
    setSeatVisual(seatNo);

    const el = $("#seat-" + seatNo);
    if(el){
      el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");
      const cnt = el.querySelector(".bag-count");
      const dir = el.querySelector(".bag-dir");
      if(cnt) cnt.textContent = "0";
      if(dir) dir.textContent = "";
    }
  }

  async function offloadSeat(){
    if(!currentSeat) return;

    try{
      const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, {
        method:"DELETE",
        headers:{ "X-CSRF-Token": csrf }
      });

      if(!j.ok) throw new Error(j.msg || "Silme başarısız");

      await clearBagsForSeat(currentSeat);
      clearSeatUI(currentSeat);
      closeSeat();
      updateStats();
      refreshStopBadges();
      updateStopSeatBadges();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      toast("Koltuk boşaltıldı");
    }catch(e){
      toast(e.message || "İniş hatası");
    }
  }

  function clearMultiPicks(){
    for(const el of multiSelected){
      el.classList.remove("multi-picked");
    }
    multiSelected.clear();
  }

  function toggleSeatPick(el){
    if(el.classList.contains("isAssigned")) return;

    if(multiSelected.has(el)){
      multiSelected.delete(el);
      el.classList.remove("multi-picked");
    }else{
      multiSelected.add(el);
      el.classList.add("multi-picked");
    }
  }

  function setMultiMode(on){
    multiMode = !!on;
    const cb = $("#multiPick");
    if(cb) cb.checked = multiMode;

    if(!multiMode){
      clearMultiPicks();
      toast("Çoklu seçim kapalı");
    }else{
      toast("Çoklu seçim açık. Koltukları seç.");
    }
  }

  function openBulk(){
    populateStops().then(() => {
      const selected = getSelectedStopName() || "";
      const live = getDisplayLiveStop();
      const fromDefault = live || selected || serverStops?.[0] || "";
      if(selected) setValue("#bulkTo", selected);
      if(fromDefault) setValue("#bulkFrom", fromDefault);
      if($("#multiPick")) $("#multiPick").checked = !!multiMode;
      openModal("#bulkBackdrop", "#bulkModal");
    });
  }

  function closeBulk(){
    closeModal("#bulkBackdrop", "#bulkModal");
  }

  async function saveBulk(){
    const from = $("#bulkFrom")?.value || speedState.liveStop || getSelectedStopName() || "";
    const to = $("#bulkTo")?.value || "";
    const count = Math.max(1, parseInt($("#bulkCount")?.value || "1", 10));
    const ticketVal = document.querySelector('input[name="bulkTicket"]:checked')?.value || "biletsiz";
    const useService = $("#bulkService")?.checked || false;

    if(!to){
      toast("Nereye seç");
      return;
    }

    const chosen = [...multiSelected].map(el => Number(el.dataset.seat));
    let targets = [];

    if(multiMode){
      if(!chosen.length){
        toast("Önce koltukları seç.");
        return;
      }
      targets = chosen;
    }else{
      const empties = [];
      $$(".seat").forEach(el => {
        const no = el.dataset.seat;
        if(!assigned?.[no]) empties.push(Number(no));
      });

      if(!empties.length){
        toast("Boş koltuk yok");
        return;
      }

      targets = sampleRandom(empties, count);
    }

    try{
      let ok = false;

      try{
        const j = await safeJsonFetch("/api/seats/bulk", {
          method:"POST",
          headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
          body:JSON.stringify({
            seats: targets,
            from,
            stop: to,
            ticket_type: ticketVal,
            service: useService
          })
        });
        ok = !!j.ok;
      }catch(_){}

      if(!ok){
        for(const n of targets){
          await safeJsonFetch("/api/seat", {
            method:"POST",
            headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
            body:JSON.stringify({
              seat_no:n,
              from,
              stop:to,
              ticket_type:ticketVal,
              payment:"nakit",
              amount:0,
              gender:"",
              pair_ok:0,
              service:useService,
              service_note:""
            })
          });
        }
      }

      for(const n of targets){
        assigned[String(n)] = true;
        stopsMap[String(n)] = to;
        boardsMap[String(n)] = from;
        serviceMap[String(n)] = !!useService;
        serviceNotes[String(n)] = "";
        setSeatVisual(n);
      }

      persistBoards();
      clearMultiPicks();
      multiMode = false;
      if($("#multiPick")) $("#multiPick").checked = false;
      closeBulk();
      updateStats();
      refreshStopBadges();
      updateStopSeatBadges();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      toast(`${targets.length} koltuk eklendi`);
    }catch(e){
      toast(e.message || "Toplu giriş hatası");
    }
  }

  function openCash(){
    populateStops().then(() => {
      const selected = getSelectedStopName() || "";
      const live = getDisplayLiveStop();
      const fromDefault = live || selected || serverStops?.[0] || "";
      if(selected) setValue("#cashTo", selected);
      if(fromDefault) setValue("#cashFrom", fromDefault);
      openModal("#cashBackdrop", "#cashModal");
    });
  }

  function closeCash(){
    closeModal("#cashBackdrop", "#cashModal");
  }

  async function saveCash(){
    const cnt = Math.max(1, parseInt($("#cashCount")?.value || "1", 10));
    const price = parseMoney($("#cashPrice")?.value || 0);
    const pay = $("#cashPay")?.value || "nakit";
    const from = $("#cashFrom")?.value || speedState.liveStop || getSelectedStopName() || serverStops?.[0] || "";
    const to = $("#cashTo")?.value || "";
    const note = $("#cashNote")?.value || "";

    if(!to){
      toast("Nereye seç");
      return;
    }

    try{
      const j = await safeJsonFetch("/api/standing", {
        method:"POST",
        headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
        body:JSON.stringify({ count:cnt, price, payment:pay, from, to, note })
      });

      if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıt hatası");

      await loadStandingTotals();
      await loadStandingItems();

      updateStats();
      refreshStopBadges();
      renderAI();
      renderTimeline();
      renderStandingList();
      renderQuickStandingList();
      updateCompactHeader();

      setValue("#cashCount", "1");
      setValue("#cashPrice", "0");
      setValue("#cashNote", "");
      closeCash();
      toast("Ayakta satış eklendi");
    }catch(e){
      toast(e.message || "Tahsilat hatası");
    }
  }

  async function loadStandingTotals(){
    try{
      const j = await safeJsonFetch("/api/standing");
      if(j?.ok){
        standingCount = Number(j.count || 0);
        standingRevenue = Number(j.revenue || 0);
        return;
      }
    }catch(_){}

    try{
      const x = JSON.parse(localStorage.getItem("standingTotals:" + TRIP_KEY) || "null");
      standingCount = Number(x?.count || 0);
      standingRevenue = Number(x?.revenue || 0);
    }catch(_){
      standingCount = 0;
      standingRevenue = 0;
    }
  }

  async function loadStandingItems(){
    try{
      const j = await safeJsonFetch("/api/standing/list");
      if(j?.ok && Array.isArray(j.items)){
        standingItems = j.items.slice();
        return;
      }
    }catch(_){}

    try{
      const x = JSON.parse(localStorage.getItem("standingItems:" + TRIP_KEY) || "[]");
      standingItems = Array.isArray(x) ? x : [];
    }catch(_){
      standingItems = [];
    }
  }

  async function loadParcelItems(){
    try{
      const j = await safeJsonFetch("/api/parcels?status=bekliyor");
      if(j?.ok && Array.isArray(j.items)){
        parcelItems = j.items.slice();
        return;
      }
    }catch(_){}
    parcelItems = [];
  }

  function renderStandingList(){
    const list = $("#standingList");
    const sum = $("#standingSummary");
    const bulk = $("#standingBulkOff");
    if(!list || !sum || !bulk) return;

    list.innerHTML = "";

    if(!standingItems.length){
      sum.textContent = "Kayıt yok";
      bulk.style.display = "none";
      return;
    }

    const totalPeople = standingItems.reduce((acc, it) => acc + Number(it?.count || 0), 0);
    const totalPrice = standingItems.reduce((acc, it) => {
      if(typeof it?.total_amount !== "undefined" && it?.total_amount !== null){
        return acc + Number(it.total_amount || 0);
      }
      return acc + (Number(it?.count || 0) * Number(it?.price || 0));
    }, 0);

    sum.textContent = `${totalPeople} ayakta · ${fmtTL(totalPrice)}`;
    bulk.style.display = "inline-flex";

    standingItems.forEach((it) => {
      const total = (typeof it.total_amount !== "undefined" && it.total_amount !== null)
        ? Number(it.total_amount || 0)
        : (Number(it.count || 0) * Number(it.price || 0));

      const d = document.createElement("div");
      d.className = "standing-item";
      d.innerHTML = `
        <div>
          <b>${it.from || "—"} → ${it.to || "—"}</b>
          <small>${it.count || 0} kişi · ${fmtTL(total)} · ${it.payment || "nakit"}</small>
        </div>
        <button class="btn danger" style="min-height:40px;padding:8px 12px" data-id="${it.id}">İndir</button>
      `;
      list.appendChild(d);
    });

    list.querySelectorAll("button[data-id]").forEach(btn => {
      btn.addEventListener("click", () => removeStandingById(parseInt(btn.dataset.id, 10)));
    });
  }

  function openStandingModal(){
    renderStandingList();
    openModal("#standingBackdrop", "#standingModal");
  }

  function closeStandingModal(){
    closeModal("#standingBackdrop", "#standingModal");
  }

  async function removeStandingById(itemId){
    if(!itemId) return;

    try{
      const j = await safeJsonFetch(`/api/standing?id=${encodeURIComponent(itemId)}`, {
        method:"DELETE",
        headers:{ "X-CSRF-Token": csrf }
      });

      if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıt silinemedi");

      await loadStandingTotals();
      await loadStandingItems();

      updateStats();
      refreshStopBadges();
      renderStandingList();
      renderQuickStandingList();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      toast("Ayakta kayıt indirildi");
    }catch(e){
      toast(e.message || "Silme hatası");
    }
  }

  async function offloadStandingForStop(stopName){
    try{
      const j = await safeJsonFetch("/api/standing?to=" + encodeURIComponent(stopName), {
        method:"DELETE",
        headers:{ "X-CSRF-Token": csrf }
      });

      if(!j?.ok) throw new Error(j?.msg || "Ayakta kayıtlar indirilemedi");

      await loadStandingTotals();
      await loadStandingItems();

      updateStats();
      refreshStopBadges();
      renderQuickStandingList();
      renderStandingList();
      renderAI();
      renderTimeline();
      updateCompactHeader();

      return Number(j.count || 0);
    }catch(e){
      toast(e.message || "Ayakta indirme hatası");
      return 0;
    }
  }

  function startBlink(list){
    if(!Array.isArray(list) || !list.length) return;
    list.forEach(n => {
      const el = $("#seat-" + n);
      if(el) el.classList.add("blink-yellow");
    });
  }

  function stopBlink(list){
    const arr = list || [...$$(".seat.blink-yellow")].map(el => Number(el.dataset.seat));
    arr.forEach(n => {
      const el = $("#seat-" + n);
      if(el) el.classList.remove("blink-yellow");
    });
  }

  function snoozeBlink(ms=5*60*1000){
    stopBlink();
    snoozeUntil = Date.now() + ms;
    toast("Uyarı 5 dk ertelendi");
  }

  function speak(text){
    const msg = String(text || "").trim();
    if(!msg) return;

    const soundToggle = $("#soundToggle");

    // Checkbox varsa ve kapalıysa konuşma.
    // Checkbox bulunamazsa sistemi tamamen susturma.
    if(soundToggle && !soundToggle.checked) return;

    try{
      if("speechSynthesis" in window){
        // Android/Chrome bazen eski sesi kuyrukta kilitliyor; temizleyip başlatıyoruz.
        speechSynthesis.cancel();

        const u = new SpeechSynthesisUtterance(msg);

        const voices = speechSynthesis.getVoices ? speechSynthesis.getVoices() : [];
        const trVoice = voices.find(v => (v.lang || "").toLowerCase().startsWith("tr"));

        if(trVoice) u.voice = trVoice;
        u.lang = trVoice ? trVoice.lang : "tr-TR";
        u.rate = 1;
        u.pitch = 1;
        u.volume = 1;

        setTimeout(() => {
          speechSynthesis.speak(u);
        }, 80);
      }
    }catch(e){
      console.warn("Sesli okuma hatası:", e);
    }

    if(navigator.vibrate) navigator.vibrate([140, 70, 140]);
  }

  function speakFinalStopSequence(name){
    speak(stopHumanVoiceSummary(name));
    setTimeout(() => {
      speak("Sarıkız Turizm ailesini tercih ettiğiniz için teşekkür ederiz. Bir sonraki yolculukta görüşmek üzere.");
    }, 1800);
  }

  function renderApproachPanel(stop, seats){
    lastApproach = { stop, seats:[...seats] };

    const standingMap = computeStandingCountsByStop();
    const parcelMap = computeParcelCountsByStop();

    setText("#approachTitle", stop + " yaklaşıyor");
    setText("#approachInfo", `${seats.length} koltuk · ${standingMap[stop] || 0} ayakta · ${parcelMap[stop] || 0} emanet`);

    const list = $("#approachList");
    if(!list) return;
    list.innerHTML = "";

    if(!seats.length && !(standingMap[stop] || 0) && !(parcelMap[stop] || 0)){
      list.innerHTML = `<div class="approach-row">Bu durakta işlem görünmüyor.</div>`;
    }

    seats.forEach(n => {
      const row = document.createElement("div");
      row.className = "approach-row";
      row.innerHTML = `<b>Koltuk ${n}</b><span>${boardsMap[String(n)] || "—"} → ${stopsMap[String(n)] || "—"}</span>`;
      list.appendChild(row);
    });

    if(standingMap[stop]){
      const row = document.createElement("div");
      row.className = "approach-row";
      row.innerHTML = `<b>Ayakta</b><span>${standingMap[stop]} kişi inecek</span>`;
      list.appendChild(row);
    }

    if(parcelMap[stop]){
      const row = document.createElement("div");
      row.className = "approach-row";
      row.innerHTML = `<b>Emanet</b><span>${parcelMap[stop]} teslim var</span>`;
      list.appendChild(row);
    }

    openModal("#approachBackdrop", "#approachModal");

    if(isFinalStop(stop)) speakFinalStopSequence(stop);
    else{
      speak(stopHumanVoiceSummary(stop));
    }
}
  async function bulkOffload(seatNums){
    if(!Array.isArray(seatNums) || !seatNums.length) return;

    try{
      let ok = false;

      try{
        const j = await safeJsonFetch("/api/seats/offload", {
          method:"POST",
          headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
          body:JSON.stringify({ seats: seatNums })
        });
        ok = !!j.ok;
      }catch(_){}

      if(!ok){
        for(const n of seatNums){
          const j = await safeJsonFetch("/api/seat?seat_no=" + n, {
            method:"DELETE",
            headers:{ "X-CSRF-Token":csrf }
          });
          if(!j.ok) throw new Error(j.msg || ("Koltuk " + n + " boşaltılamadı"));
        }
      }

      for(const n of seatNums){
        await clearBagsForSeat(n);
        clearSeatUI(n);
      }

      stopBlink(seatNums);
      updateStats();
      refreshStopBadges();
      updateStopSeatBadges();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      lastApproach = { stop:null, seats:[] };
      toast(`${seatNums.length} koltuk boşaltıldı`);
    }catch(e){
      toast(e.message || "Toplu boşaltma hatası");
    }
  }

  async function triggerManualApproach(){
    const stop = getSelectedStopName();
    if(!stop){
      toast("Önce durak seç");
      return;
    }

    const seats = seatsForStop(stop);
    if(!seats.length && !(computeStandingCountsByStop()[stop] || 0) && !(computeParcelCountsByStop()[stop] || 0)){
      toast("Bu durakta işlem yok. İleri atlanıyor.");
      advanceToNextStop({ mode:"nextWithSeats" });
      return;
    }

    renderApproachPanel(stop, seats);
    startBlink(seats);
  }

  async function offloadSelectedStop(){
    const stop = getSelectedStopName();
    if(!stop){
      toast("Önce durak seç");
      return;
    }

    const seats = seatsForStop(stop);
    if(!seats.length && !(computeStandingCountsByStop()[stop] || 0)){
      toast("Bu durakta indirilecek yolcu yok");
      return;
    }

    const ok = confirm(`"${stop}" için işlemleri yapayım mı?`);
    if(!ok) return;

    if(seats.length) await bulkOffload(seats);
    const removed = await offloadStandingForStop(stop);
    if(removed > 0) toast(`Ayakta ${removed} kişi indirildi`);

    markPassedStopsUntil(stop);
    setLiveStop(stop);
    refreshStopBadges();
    updateStopSeatBadges();
    advanceToNextStop({ mode:"nextWithSeats", ignoreToggle:true });
  }

  async function toggleGeoWatch(){
    const btn = $("#btnGeoWatch");

    if(geoWatchId){
      navigator.geolocation.clearWatch(geoWatchId);
      geoWatchId = null;
      if(btn) btn.textContent = "KAPALI";
      updateGeoHint();
      toast("Konum izleme kapatıldı");
      return;
    }

    if(!cachedStops) await fetchStops();

    const stopName = getSelectedStopName();
    if(!stopName){
      toast("Önce durak seç");
      return;
    }

    const s = findStopByName(stopName);
    if(!s || !hasCoord(s)){
      toast("Bu durak için koordinat yok");
      return;
    }

    const radiusKm = parseFloat($("#alertRadius")?.value || "3");

    geoWatchId = navigator.geolocation.watchPosition((pos) => {
      const p = { lat:pos.coords.latitude, lng:pos.coords.longitude };
      currentCoords = p;

      const d = distKm(p, { lat:Number(s.lat), lng:Number(s.lng) });
      setText("#geoHint", `Mesafe: ${d.toFixed(2)} km (eşik ${radiusKm} km)`);

      autoDetectLiveStop(p);
      renderTimeline();

      if(d <= radiusKm){
        const now = Date.now();
        if((now - lastAlertAt) > ALERT_COOLDOWN_MS && now >= snoozeUntil){
          lastAlertAt = now;
          const seats = seatsForStop(stopName);
          renderApproachPanel(stopName, seats);
          startBlink(seats);
        }
      }
    }, (err) => {
      toast("Konum hatası: " + (err?.message || ""));
    }, {
      enableHighAccuracy:true,
      timeout:10000,
      maximumAge:2000
    });

    if(btn) btn.textContent = "AÇIK";
  }

  async function saveCoord(){
    try{
      const stop = (getSelectedStopName() || $("#coordStopName")?.value || "").trim();
      if(!stop){
        toast("Önce durak seç");
        return;
      }

      const lat = numTR($("#coordLat")?.value);
      const lng = numTR($("#coordLng")?.value);

      if(!Number.isFinite(lat) || !Number.isFinite(lng)){
        toast("Lat/Lng geçersiz");
        return;
      }

      const j = await safeJsonFetch("/api/coords", {
        method:"POST",
        headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
        body:JSON.stringify({ stop, lat, lng })
      });

      if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");

      await fetchStops();
      await populateStops();
      refreshStopBadges();
      updateGeoHint();
      renderAI();
      renderTimeline();
      updateCompactHeader();

      setValue("#coordLat", "");
      setValue("#coordLng", "");
      toast("Koordinat kaydedildi");
    }catch(e){
      toast(e.message || "Koordinat kaydedilemedi");
    }
  }

  async function fetchBagMeta(seatNo){
    const key = String(seatNo);

    try{
      const u = `/api/bags/meta?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seatNo)}`;
      const j = await safeJsonFetch(u);

      const right = Number(j?.right || 0);
      const leftFront = Number(j?.left_front || 0);
      const leftBack = Number(j?.left_back || 0);
      const total = Number(j?.count || (right + leftFront + leftBack));

      const eyes = [];
      if(right > 0) eyes.push("R");
      if(leftFront > 0) eyes.push("LF");
      if(leftBack > 0) eyes.push("LB");

      const meta = {
        count: total,
        right,
        left_front: leftFront,
        left_back: leftBack,
        eyes
      };

      bagMetaCache[key] = meta;
      return meta;
    }catch(_){
      const fallback = bagMetaCache[key] || { count:0, right:0, left_front:0, left_back:0, eyes:[] };
      return fallback;
    }
  }


function eyesToIcons(eyes){
    if(!eyes || !eyes.length) return "";
    const set = new Set(eyes);
    const parts = [];
    if(set.has("R")) parts.push("➡️");
    if(set.has("LF")) parts.push("⬅️🔺");
    if(set.has("LB")) parts.push("⬅️🔻");
    return parts.join(" ");
  }

  async function refreshBagBadgeForSeat(seatNo){
    const el = $("#seat-" + seatNo);
    if(!el) return;

    const meta = await fetchBagMeta(seatNo);
    const cnt = meta.count;
    const eyes = meta.eyes || [];

    el.classList.toggle("has-bag", cnt > 0);

    const bagCount = el.querySelector(".bag-count");
    const bagDir = el.querySelector(".bag-dir");
    const badge = el.querySelector(".bag-badge");

    if(bagCount) bagCount.textContent = String(cnt || 0);
    if(bagDir) bagDir.textContent = eyesToIcons(eyes) || "";
    if(badge) badge.title = cnt ? `Bagaj: ${cnt} adet` : "Bagaj yok";
  }

  async function refreshBagsAll(){
    const seats = $$(".seat").map(el => Number(el.dataset.seat));
    for(const n of seats){
      await refreshBagBadgeForSeat(n);
    }
  }

  async function clearBagsForSeat(seatNo){
    try{
      const u = `/bags/clear?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seatNo)}`;
      await safeJsonFetch(u, {
        method:"DELETE",
        headers:{ "X-CSRF-Token":csrf }
      });
    }catch(_){}

    const el = $("#seat-" + seatNo);
    if(el){
      el.classList.remove("has-bag");
      const cnt = el.querySelector(".bag-count");
      const dir = el.querySelector(".bag-dir");
      if(cnt) cnt.textContent = "0";
      if(dir) dir.textContent = "";
    }
  }

  function buildEtaModel(){
    const items = buildActualSchedule();

    if(!items.length){
      speedState.etaItems = [];
      setText("#routeNextTimed", "—");
      setText("#stEtaTarget", "—");
      setText("#stEtaHint", "Plan / ETA");
      setText("#delayMain", "—");
      setText("#delaySub", "Saatli durak tanımlı değil");
      return [];
    }

    const now = new Date();
    const liveIdx = indexOfStopByName(speedState.liveStop);
    const selectedIdx = indexOfStopByName(getSelectedStopName());

    let anchor = null;
    if(liveIdx >= 0){
      anchor = [...items].reverse().find(x => x.routeIndex >= 0 && x.routeIndex <= liveIdx) || items[0];
    }else if(selectedIdx >= 0){
      anchor = [...items].reverse().find(x => x.routeIndex >= 0 && x.routeIndex <= selectedIdx) || items[0];
    }else{
      anchor = items[0];
    }

    const globalDelayMin = minutesDiff(now, anchor.planDate);

    const model = items.map(item => {
      const etaDate = new Date(item.planDate.getTime() + globalDelayMin * 60000);
      const delayMin = minutesDiff(etaDate, item.planDate);

      const passed = liveIdx >= 0
        ? (item.routeIndex >= 0 && item.routeIndex < liveIdx)
        : etaDate.getTime() < now.getTime() - (5 * 60000);

      let badgeCls = "good";
      if(passed) badgeCls = "info";
      else if(delayMin > 15) badgeCls = "bad";
      else if(delayMin > 0) badgeCls = "warn";

      const badgeText = passed ? "Geçildi" : fmtSignedMin(delayMin);

      const activeName = getSelectedStopName();
      const active = activeName
        ? norm(activeName) === norm(item.stop)
        : (!passed && item === (
            items.find(x => !(
              liveIdx >= 0
                ? (x.routeIndex >= 0 && x.routeIndex < liveIdx)
                : (new Date(x.planDate.getTime() + globalDelayMin * 60000).getTime() < now.getTime() - 5 * 60000)
            )) || items[items.length - 1]
          ));

      return {
        stop: item.stop,
        plan: fmtHour(item.planDate),
        planDate: item.planDate,
        etaDate,
        delayMin,
        badgeCls,
        badgeText,
        passed,
        active
      };
    });

    speedState.etaItems = model;

    const nextTimed = model.find(x => !x.passed) || model[model.length - 1];
    setText("#routeNextTimed", nextTimed?.stop || "—");
    setText("#stEtaTarget", nextTimed?.stop || "—");
    setText("#stEtaHint", nextTimed ? `Plan ${nextTimed.plan} · ETA ${fmtHour(nextTimed.etaDate)}` : "Plan / ETA");

    const delayEl = $("#delayMain");
    if(nextTimed && delayEl){
      const diff = nextTimed.delayMin;
      delayEl.textContent = fmtSignedMin(diff);
      delayEl.className = "delay-main " + (diff <= 0 ? "good" : diff <= 15 ? "warn" : "bad");
      setText("#delaySub", `${nextTimed.stop} · plan ${nextTimed.plan} · ETA ${fmtHour(nextTimed.etaDate)}`);
    }

    return model;
  }

  function renderTimeline(){
    const list = $("#etaTimeline");
    if(!list) return;

    const items = buildEtaModel();
    list.innerHTML = "";

    if(!items.length){
      list.innerHTML = `
        <div class="eta-row">
          <div>
            <div class="eta-name">Saatli durak yok</div>
            <div class="eta-meta">Bu hatta henüz saat tanımı yapılmamış.</div>
          </div>
        </div>
      `;
      return;
    }

    items.forEach(item => {
      const row = document.createElement("div");
      row.className = `eta-row ${item.active ? "active" : ""} ${item.passed ? "passed" : ""}`;
      row.innerHTML = `
        <div>
          <div class="eta-name">${item.stop}</div>
          <div class="eta-meta">Plan ${item.plan}</div>
        </div>
        <div class="eta-right">
          <div class="eta-main">ETA ${fmtHour(item.etaDate)}</div>
          <div class="eta-badge ${item.badgeCls}">${item.badgeText}</div>
        </div>
      `;
      row.addEventListener("click", () => setSelectedStop(item.stop, { silent:true, voiceReply:false }));
      list.appendChild(row);
    });
  }

  function renderAI(){
    const stop = getSelectedStopName();
    const seatCounts = computeSeatCountsByStop();
    const standingCounts = computeStandingCountsByStop();
    const parcelCounts = computeParcelCountsByStop();

    const selectedSeatCount = stop ? (seatCounts[stop] || 0) : 0;
    const selectedStanding = stop ? (standingCounts[stop] || 0) : 0;
    const selectedParcel = stop ? (parcelCounts[stop] || 0) : 0;

    let unserved = 0;
    Object.keys(assigned || {}).forEach(k => {
      if(assigned[k] && !serviceMap[k]) unserved++;
    });

    let busiestStop = "—";
    let busiestCount = 0;
    Object.entries(seatCounts).forEach(([k,v]) => {
      if(v > busiestCount){
        busiestCount = v;
        busiestStop = k;
      }
    });

    const totalOps = selectedSeatCount + selectedStanding + selectedParcel;
    const live = speedState.liveStop || "—";
    const nextTimed = speedState.etaItems.find(x => !x.passed) || null;

    setText("#aiMain", stop
      ? `${stop} için ${selectedSeatCount} koltuk, ${selectedStanding} ayakta, ${selectedParcel} emanet görünüyor.`
      : `${live} civarındasın. Sistem canlı durak ve rötarı izliyor.`
    );

    let aiSub = "Şu an sistem normal akışta.";
    if(stop && totalOps >= 6) aiSub = "Bu durakta yoğun işlem bekleniyor. Ön hazırlık yap.";
    else if(stop && totalOps > 0) aiSub = "Bu durak orta yoğunlukta görünüyor.";
    else if(stop) aiSub = "Bu durak için kayıtlı işlem görünmüyor.";
    else if(nextTimed) aiSub = `${nextTimed.stop} için plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.`;

    setText("#aiSub", aiSub);

    const nextAction = stop
      ? (totalOps ? `Hazırlık: ${stop}` : "İleri atlanabilir")
      : (nextTimed?.stop || "Durak bekleniyor");

    setText("#aiNextAction", nextAction);
    setText("#aiNextActionMirror", nextAction);
    setText("#aiLiveStop", live);
    setText("#aiDelay", nextTimed ? fmtSignedMin(nextTimed.delayMin) : "—");
    setText("#aiDensity", busiestCount > 0 ? `${busiestStop} (${busiestCount} koltuk)` : "Henüz veri yok");
    setText("#aiService", unserved > 0 ? `${unserved} yolcu servis bekliyor` : "Servis tarafı temiz");
    setText("#aiParcel", selectedParcel > 0 ? `${selectedParcel} teslim var` : (stop ? "Teslim yok" : "Durak seçilmedi"));
  }

  function autoDetectLiveStop(coords){
    if(!coords || !cachedStops?.length) return;

    let best = null;
    for(const stop of cachedStops){
      if(!hasCoord(stop)) continue;
      const km = distKm(coords, { lat:Number(stop.lat), lng:Number(stop.lng) });
      if(!best || km < best.km) best = { stop: stop.name, km };
    }

    if(best && best.km <= 3.5){
      setLiveStop(best.stop);
    }
  }

  function findStopMention(text){
    const ntext = norm(text);
    const list = allStopsList();
    let best = "";

    for(const stop of list){
      const ns = norm(stop);
      if(ns && ntext.includes(ns) && ns.length > best.length){
        best = stop;
      }
    }

    return best;
  }

function extractSeatNumbersFromText(text){
  const nums = String(text || "").match(/\b\d{1,2}\b/g) || [];
  const out = [];
  nums.forEach(n => {
    const x = parseInt(n, 10);
    if(Number.isInteger(x) && x > 0 && x <= 60 && !out.includes(x)){
      out.push(x);
    }
  });
  return out;
}

function detectGenderFromText(text){
  const t = norm(text);

  if(/\b(erkek|bay|adam)\b/.test(t)) return "bay";
  if(/\b(kadin|kadın|bayan|kiz|kız)\b/.test(t)) return "bayan";
  if(/\b(bos yap|boş yap|cinsiyeti kaldir|cinsiyeti kaldır|temizle|sil|sifirla|sıfırla)\b/.test(t)) return "";

  return null;
}

async function applySeatGender(seats, gender){
  const validSeats = (Array.isArray(seats) ? seats : [])
    .map(x => Number(x))
    .filter(x => Number.isInteger(x) && x > 0);

  if(!validSeats.length){
    toast("Koltuk bulunamadı");
    speak("Koltuk bulunamadı.");
    return true;
  }

  const occupiedSeats = validSeats.filter(n => !!assigned[String(n)]);
  const emptySeats = validSeats.filter(n => !assigned[String(n)]);

  if(!occupiedSeats.length){
    toast("Önce koltuğa yolcu ekle");
    speak("Önce koltuğa yolcu eklemelisin.");
    return true;
  }

  const j = await safeJsonFetch("/api/seats/gender", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrf
    },
    body: JSON.stringify({
      seats: occupiedSeats,
      gender: gender
    })
  });

  if(!j.ok) throw new Error(j.msg || "Cinsiyet güncellenemedi");

  occupiedSeats.forEach(n => {
    genders[String(n)] = gender;
    setSeatVisual(n);
  });

  const genderLabel =
    gender === "bay" ? "bay" :
    gender === "bayan" ? "bayan" : "boş";

  let msg = `${occupiedSeats.join(", ")} numara ${genderLabel} yapıldı`;
  if(emptySeats.length){
    msg += `. Boş olduğu için atlanan: ${emptySeats.join(", ")}`;
  }

  toast(msg, 3200);
  speak(msg);
  return true;
}

function parseVoiceCommand(text){
  const t = norm(text);
  const mentionedStop = findStopMention(text);
  const seats = extractSeatNumbersFromText(text);
  const gender = detectGenderFromText(text);

  if(/^(hesap ac|hesap aç)$/.test(t)) return { type:"open_hesap" };
  if(/^(emanet ac|emanet aç|emanetler ac|emanetler aç)$/.test(t)) return { type:"open_emanet" };
  if(/^(sesli yardim|sesli yardım|yardim|yardım)$/.test(t)) return { type:"help" };
  if(/(kac yolcu var|kaç yolcu var|toplam yolcu)/.test(t)) return { type:"ask_total" };
  if(/(ayakta kac|ayakta kaç)/.test(t)) return { type:"ask_standing" };
  if(/(hangi duraktayiz|hangi duraktayız|neredeyiz)/.test(t)) return { type:"ask_live_stop" };
  if(/(rotar kac|rötar kaç|gecikme kac|gecikme kaç)/.test(t)) return { type:"ask_delay" };
  if(/(bir sonraki durak|siradaki saatli|sıradaki saatli)/.test(t)) return { type:"ask_next_timed" };

  if(mentionedStop && /(kaç yolcu var|kac yolcu var|orada kaç yolcu var|orada kac yolcu var|kaç kişi var|kac kisi var)/.test(t)){
    return { type:"ask_stop_count", stop: mentionedStop };
  }

  if(seats.length && gender !== null){
    return { type:"set_gender", seats, gender };
  }

  if((/(siradaki durak|sıradaki durak|durak sec|durak seç)/.test(t)) && mentionedStop){
    return { type:"set_stop", stop: mentionedStop };
  }

  if(mentionedStop && /(durak|sec|seç)/.test(t)){
    return { type:"set_stop", stop: mentionedStop };
  }

  return { type:"unknown", raw:text };
}

  function aiIntentTitle(intent){
    const map = {
      seat_add_single: "Tek koltuk ekleme",
      seat_add_group: "Çoklu koltuk ekleme",
      seat_remove_single: "Tek koltuk boşaltma",
      seat_remove_group: "Çoklu koltuk boşaltma",
      standing_add: "Ayakta ekleme",
      service_mark: "Servis işaretleme",
      query: "Sorgu"
    };
    return map[intent] || intent || "Bilinmeyen işlem";
  }

  async function resolveVoiceWithBackendAI(text){
    const j = await safeJsonFetch("/api/ai/resolve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-Token": csrf
      },
      body: JSON.stringify({ command: text })
    });

    return j?.result || null;
  }

  function extractFirstNumberFromText(text, fallback=1){
    const m = String(text || "").match(/\b\d+\b/);
    if(!m) return fallback;
    const n = parseInt(m[0], 10);
    return Number.isFinite(n) && n > 0 ? n : fallback;
  }

  async function openSingleSeatAddFlow(seatNo){
    await populateStops();
    openSeat(seatNo);

    const selectedStop = getSelectedStopName() || "";
    if(selectedStop && $("#pickup")) $("#pickup").value = selectedStop;

    toast(`Koltuk ${seatNo} için giriş formu açıldı`);
    speak(`Koltuk ${seatNo} için giriş formu açıldı.`);
  }

  async function openBulkSeatAddFlow(seats){
    await populateStops();

    openModal("#bulkBackdrop", "#bulkModal");

    const selectedStop = getSelectedStopName() || "";
    if(selectedStop && $("#bulkTo")) $("#bulkTo").value = selectedStop;

    clearMultiPicks();
    setMultiMode(true);

    seats.forEach(seatNo => {
      const el = $("#seat-" + seatNo);
      if(!el) return;
      if(assigned[String(seatNo)]) return;
      if(!multiSelected.has(el)) toggleSeatPick(el);
    });

    if($("#bulkCount")) $("#bulkCount").value = String(seats.length || 1);

    toast("Toplu giriş formu hazırlandı");
    speak("Toplu giriş formu açıldı.");
  }

  async function openStandingAddFlow(text, resolved){
    await populateStops();

    openModal("#cashBackdrop", "#cashModal");

    const selectedStop = getSelectedStopName() || "";
    if(selectedStop && $("#cashTo")) $("#cashTo").value = selectedStop;

    const inferred =
      (Array.isArray(resolved?.seats) && resolved.seats.length === 1)
        ? Number(resolved.seats[0] || 1)
        : extractFirstNumberFromText(text, 1);

    if($("#cashCount")) $("#cashCount").value = String(inferred > 0 ? inferred : 1);

    toast("Ayakta satış formu açıldı");
    speak("Ayakta satış formu açıldı.");
  }

  async function applyServiceMark(seats){
    if(!Array.isArray(seats) || !seats.length){
      toast("Servis için koltuk bulunamadı");
      speak("Servis için koltuk bulunamadı.");
      return;
    }

    const note = "Sesli komut";

    const j = await safeJsonFetch("/api/seats/service", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-Token": csrf
      },
      body: JSON.stringify({
        seats,
        service: 1,
        service_note: note
      })
    });

    if(!j.ok) throw new Error(j.msg || "Servis işaretleme başarısız");

    seats.forEach(n => {
      serviceMap[String(n)] = true;
      serviceNotes[String(n)] = note;
      setSeatVisual(n);
    });

    updateStats();
    renderAI();
    renderTimeline();
    updateCompactHeader();

    toast(`Servis işlendi: ${seats.join(", ")}`);
    speak(`Servis işlendi. Koltuklar ${seats.join(", ")}`);
  }

  async function executeResolvedAiOnSeats(resolved, rawText){
    if(!resolved) return false;

    const intent = resolved.intent || "";
    const seats = Array.isArray(resolved.seats) ? resolved.seats.map(Number).filter(Number.isFinite) : [];

    if(resolved.status === "suggest"){
      toast(`Düşük güven: ${aiIntentTitle(intent)}`);
      speak(`Komut düşük güvenle algılandı. Tahmin edilen işlem ${aiIntentTitle(intent)}.`);
      return true;
    }

    if(resolved.status !== "matched"){
      return false;
    }

    if(intent === "seat_remove_single" || intent === "seat_remove_group"){
      if(!seats.length){
        toast("Boşaltılacak koltuk bulunamadı");
        speak("Boşaltılacak koltuk bulunamadı.");
        return true;
      }

      await bulkOffload(seats);
      speak(`${seats.join(" ve ")} numaralı koltuk boşaltıldı.`);
      return true;
    }

    if(intent === "service_mark"){
      await applyServiceMark(seats);
      return true;
    }

    if(intent === "seat_add_single"){
      if(!seats.length){
        toast("Koltuk bulunamadı");
        speak("Koltuk bulunamadı.");
        return true;
      }
      await openSingleSeatAddFlow(seats[0]);
      return true;
    }

    if(intent === "seat_add_group"){
      if(!seats.length){
        toast("Koltuk listesi bulunamadı");
        speak("Koltuk listesi bulunamadı.");
        return true;
      }
      await openBulkSeatAddFlow(seats);
      return true;
    }

    if(intent === "standing_add"){
      await openStandingAddFlow(rawText, resolved);
      return true;
    }

    if(intent === "query"){
      return false;
    }

    return false;
  }

async function handleLocalVoiceCommand(text){
  const cmd = parseVoiceCommand(text);

  if(cmd.type === "help"){
    const help = "Temel komutlar: " + VOICE_HELP.join(", ");
    toast(help, 4200);
    speak(help);
    return true;
  }

  if(cmd.type === "open_hesap"){
    speak("Hesap sayfası açılıyor.");
    location.href = URLS.hesap || "/hesap";
    return true;
  }

  if(cmd.type === "open_emanet"){
    speak("Emanet sayfası açılıyor.");
    location.href = URLS.consignments || "/emanetler";
    return true;
  }

  if(cmd.type === "set_gender"){
    await applySeatGender(cmd.seats, cmd.gender);
    return true;
  }

  if(cmd.type === "ask_total"){
    const seated = Object.values(assigned || {}).filter(Boolean).length;
    const total = seated + (standingCount || 0);
    const msg = `Toplam ${total} yolcu var. ${seated} oturan, ${standingCount || 0} ayakta.`;
    toast(msg, 3600);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_standing"){
    const msg = `Ayakta ${standingCount || 0} kişi var. Tahsilat ${fmtTL(standingRevenue || 0)}.`;
    toast(msg, 3600);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_stop_count"){
    const stop = cmd.stop;
    const msg = stopHumanVoiceSummary(stop);

    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_live_stop"){
    const live = speedState.liveStop || getSelectedStopName() || "henüz belli değil";
    const msg = `Şu an ${live} civarındasın.`;
    toast(msg, 3200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_delay"){
    const nextTimed = speedState.etaItems.find(x => !x.passed) || null;
    if(!nextTimed){
      const msg = "Saatli durak bilgisi yok.";
      toast(msg, 3200);
      speak(msg);
      return true;
    }

    const msg = `${nextTimed.stop} için ${fmtSignedMin(nextTimed.delayMin)}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.`;
    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "ask_next_timed"){
    const nextTimed = speedState.etaItems.find(x => !x.passed) || null;
    if(!nextTimed){
      const msg = "Sıradaki saatli durak bulunamadı.";
      toast(msg, 3200);
      speak(msg);
      return true;
    }

    const msg = `Sıradaki saatli nokta ${nextTimed.stop}. Plan ${nextTimed.plan}, tahmini ${fmtHour(nextTimed.etaDate)}.`;
    toast(msg, 4200);
    speak(msg);
    return true;
  }

  if(cmd.type === "set_stop"){
    const ok = setSelectedStop(cmd.stop, { silent:true, voiceReply:false });
    if(!ok){
      toast("Bu durak güzergâhta yok");
      speak("Bu durak bu güzergâhta bulunmuyor.");
      return true;
    }

    const stop = getSelectedStopName();
    const msg = stopHumanVoiceSummary(stop);
    toast(msg, 3600);
    speak(msg);
    return true;
  }

  return false;
}

  async function handleBasicVoiceCommand(text){
    const localHandled = await handleLocalVoiceCommand(text);
    if(localHandled) return;

    try{
      const resolved = await resolveVoiceWithBackendAI(text);
      const handled = await executeResolvedAiOnSeats(resolved, text);

      if(handled) return;

      if(resolved?.intent === "query"){
        const cmd = parseVoiceCommand(text);

        if(cmd.type === "ask_stop_count"){
          const stop = cmd.stop;
          const seat = seatsForStop(stop).length;
          const stand = computeStandingCountsByStop()[stop] || 0;
          const parcel = computeParcelCountsByStop()[stop] || 0;
          const total = seat + stand;
          const msg =
            `${stop} için ${total} yolcu var. ${seat} oturan, ${stand} ayakta.` +
            (parcel ? ` Ayrıca ${parcel} emanet var.` : "");
          toast(msg, 4200);
          speak(msg);
          return;
        }

        if(cmd.type === "ask_total"){
          const seated = Object.values(assigned || {}).filter(Boolean).length;
          const total = seated + (standingCount || 0);
          const msg = `Toplam ${total} yolcu var. ${seated} oturan, ${standingCount || 0} ayakta.`;
          toast(msg, 3600);
          speak(msg);
          return;
        }

        if(cmd.type === "ask_standing"){
          const msg = `Ayakta ${standingCount || 0} kişi var. Tahsilat ${fmtTL(standingRevenue || 0)}.`;
          toast(msg, 3600);
          speak(msg);
          return;
        }
      }

      toast("Komut anlaşılmadı");
      speak("Komutu anlayamadım. Sesli yardım diyebilirsin.");
    }catch(e){
      console.error("AI voice resolve error:", e);
      toast("AI sesli komut hatası");
      speak("AI sesli komut tarafında bir hata oluştu.");
    }
  }

  function startDeckAIVoice(){
    const btn = $("#btnDeckAI");
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;

    if(!SR){
      toast("Bu tarayıcı sesli komutu desteklemiyor");
      setVoiceBadge("Destek yok");
      return;
    }

    const rec = new SR();
    rec.lang = "tr-TR";
    rec.continuous = false;
    rec.interimResults = false;
    rec.maxAlternatives = 1;

    if(btn){
      btn.classList.add("listening");
      btn.innerHTML = "🔴 <span>Dinliyor</span>";
    }
    setVoiceBadge("Dinleniyor");

    rec.onresult = async (e) => {
      const text = e.results?.[0]?.[0]?.transcript?.trim() || "";
      if(!text){
        toast("Ses algılandı ama metin çıkarılamadı");
        setVoiceBadge("Tekrar dene");
        return;
      }
      toast("Algılandı: " + text, 1600);
      setVoiceBadge(text.length > 18 ? text.slice(0, 18) + "…" : text);
      await handleBasicVoiceCommand(text);
    };

    rec.onerror = (e) => {
      toast("Sesli komut hatası: " + (e.error || "bilinmiyor"));
      setVoiceBadge("Hata");
    };

    rec.onend = () => {
      if(btn){
        btn.classList.remove("listening");
        btn.innerHTML = "🎤 <span>Sesli Komut</span>";
      }
      setTimeout(() => setVoiceBadge("Hazır"), 900);
    };

    try{
      rec.start();
    }catch(_){
      if(btn){
        btn.classList.remove("listening");
        btn.innerHTML = "🎤 <span>Sesli Komut</span>";
      }
      setVoiceBadge("Başlatılamadı");
      toast("Mikrofon başlatılamadı");
    }
  }

  function initTabs(){
    $$(".tab-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const tab = btn.dataset.tab;
        $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn));
        $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab));
      });
    });
  }

  function openTab(name){
    const btn = document.querySelector(`.tab-btn[data-tab="${name}"]`);
    if(btn) btn.click();
  }

  (function initClock(){
    const topClock = $("#topClock");
    const main = $("#clockMain");
    const date = $("#clockDate");
    const sub = $("#clockSub");

    if(!topClock || !main || !date || !sub) return;

    const tf = new Intl.DateTimeFormat("tr-TR", { hour:"2-digit", minute:"2-digit", second:"2-digit", hour12:false });
    const sf = new Intl.DateTimeFormat("tr-TR", { hour:"2-digit", minute:"2-digit", hour12:false });
    const df = new Intl.DateTimeFormat("tr-TR", { weekday:"long", day:"2-digit", month:"long", year:"numeric" });

    const tick = () => {
      const n = new Date();
      topClock.textContent = sf.format(n);
      main.textContent = tf.format(n);
      date.textContent = df.format(n);
      sub.textContent = df.format(n);
    };

    tick();
    setInterval(tick, 1000);
  })();

  (function initPrayer(){
    const PR_ORDER = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"];
    const TR_PR = { Fajr:"İmsak", Sunrise:"Güneş", Dhuhr:"Öğle", Asr:"İkindi", Maghrib:"Akşam", Isha:"Yatsı" };
    const METHOD = 13;
    const SCHOOL = 0;
    const FALLBACK = { lat:38.5190, lng:28.5192, place:"Alaşehir" };
    const lineEl = $("#prLine");
    if(!lineEl) return;

    const pad2 = n => String(n).padStart(2, "0");

    function fmtHM(d){
      return `${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
    }

    function toTodayDate(s){
      if(!s) return null;
      if(s.includes("T")) return new Date(s);

      const [h,m] = s.split(":").map(x => parseInt(x, 10));
      const d = new Date();
      d.setHours(h || 0, m || 0, 0, 0);
      return d;
    }

    function humanLeft(ms){
      const sec = Math.max(0, Math.floor(ms / 1000));
      const h = Math.floor(sec / 3600);
      const m = Math.floor((sec % 3600) / 60);
      return (h ? `${h} saat ` : "") + `${m} dk`;
    }

    async function reverseGeocode(lat, lng){
      try{
        const r = await fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`);
        const a = (await r.json()).address || {};
        const town = a.village || a.town || a.hamlet || a.suburb || "";
        const dist = a.county || a.district || "";
        const prov = a.province || a.state || "";
        const right = dist && dist !== town ? dist : prov;
        return [town || right, right && right !== town ? right : ""].filter(Boolean).join(", ");
      }catch(_){
        return "";
      }
    }

    async function fetchTimings(lat, lng){
      const url = `https://api.aladhan.com/v1/timings?latitude=${lat}&longitude=${lng}&method=${METHOD}&school=${SCHOOL}&iso8601=true`;
      const j = await (await fetch(url)).json();
      if(!j?.data?.timings) throw new Error("timings yok");
      return j.data.timings;
    }

    function computePrevNext(timings){
      const now = new Date();
      const list = PR_ORDER.map(k => ({ key:k, at:toTodayDate(timings[k]) })).filter(x => x.at && !isNaN(x.at));
      const future = list.filter(x => x.at > now);

      if(future.length){
        const next = future[0];
        const i = list.indexOf(next);
        const prev = i > 0 ? list[i - 1] : list[list.length - 1];
        return { prev, next };
      }

      const prev = list[list.length - 1];
      const tmr = toTodayDate(timings["Fajr"]);
      tmr.setDate(tmr.getDate() + 1);
      return { prev, next:{ key:"Fajr", at:tmr } };
    }

    function render(place, timings){
      const { prev, next } = computePrevNext(timings);
      const placeTxt = place ? `${place}: ` : "";
      const curName = TR_PR[prev.key] || prev.key;
      const nxtName = TR_PR[next.key] || next.key;
      const curHH = fmtHM(prev.at);
      const nxtHH = fmtHM(next.at);
      const leftMs = next.at - new Date();
      const leftTxt = humanLeft(leftMs);

      lineEl.innerHTML =
        `${placeTxt}<span class="pr-accent">${curName} ${curHH}</span> · Sonraki: <b>${nxtName} ${nxtHH}</b> · ` +
        `<span class="pr-left ${leftMs <= 10 * 60 * 1000 ? "soon" : ""}">Kalan ${leftTxt}</span>`;
    }

    async function boot(lat, lng, placeHint=""){
      try{
        const timings = await fetchTimings(lat, lng);
        const place = (await reverseGeocode(lat, lng)) || placeHint;
        render(place, timings);

        let lastDay = new Date().getDate();
        setInterval(async () => {
          const today = new Date().getDate();
          if(today !== lastDay){
            lastDay = today;
            render(place, await fetchTimings(lat, lng));
          }else{
            render(place, timings);
          }
        }, 1000);
      }catch(_){
        lineEl.textContent = "Vakitler alınamadı";
      }
    }

    if("geolocation" in navigator){
      navigator.geolocation.getCurrentPosition(
        p => boot(p.coords.latitude, p.coords.longitude),
        _ => boot(FALLBACK.lat, FALLBACK.lng, FALLBACK.place),
        { enableHighAccuracy:true, timeout:10000, maximumAge:30000 }
      );
    }else{
      boot(FALLBACK.lat, FALLBACK.lng, FALLBACK.place);
    }
  })();

  (function initSpeed(){
    const spVal = $("#spVal");
    const spLimit = $("#spLimit");
    const speedBox = $("#speedBox");
    const ttsBtn = $("#ttsToggle");
    if(!spVal || !spLimit || !speedBox || !ttsBtn) return;

    const TTS_KEY = "ttsEnabled";
    let ttsEnabled = (localStorage.getItem(TTS_KEY) ?? "1") === "1";

    function syncTts(){
      ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted");
    }

    syncTts();

    ttsBtn.addEventListener("click", () => {
      ttsEnabled = !ttsEnabled;
      localStorage.setItem(TTS_KEY, ttsEnabled ? "1" : "0");
      syncTts();
      if(ttsEnabled) speakOnce("Sesli uyarı açık.");
    });

    let trVoice = null;
    function loadVoices(){
      const voices = speechSynthesis.getVoices();
      trVoice = voices.find(v => (v.lang || "").toLowerCase().startsWith("tr")) || null;
    }

    if("speechSynthesis" in window){
      loadVoices();
      speechSynthesis.onvoiceschanged = loadVoices;
    }

    function speakOnce(text){
      if(!ttsEnabled || !("speechSynthesis" in window)) return;
      const u = new SpeechSynthesisUtterance(text);
      u.lang = trVoice ? trVoice.lang : "tr-TR";
      if(trVoice) u.voice = trVoice;
      u.rate = 1;
      speechSynthesis.speak(u);
    }

    function setState(cls){
      speedBox.classList.remove("limit-ok","limit-warn","limit-bad");
      if(cls) speedBox.classList.add(cls);
    }

    function trHighway(hw){
      const m = {
        motorway:"otoyol",
        trunk:"ana yol",
        primary:"birincil",
        secondary:"ikincil",
        tertiary:"üçüncül",
        residential:"yerleşim",
        service:"servis"
      };
      return m[hw] || (hw || "");
    }

    async function fetchLimit(lat, lng){
      const now = Date.now();
      if(now - speedState.lastLimitFetchTs < 10000 && speedState.lastLimitObj) return speedState.lastLimitObj;

      speedState.lastLimitFetchTs = now;

      try{
        const r = await fetch(`/api/speedlimit?lat=${lat}&lng=${lng}`);
        const j = await r.json();
        if(j?.ok){
          speedState.lastLimitObj = { limit:j.limit, highway:j.highway };
          return speedState.lastLimitObj;
        }
      }catch(_){}

      return null;
    }

    function maybeSpeak(speed, limit){
      const s = Math.round(Number(speed || 0));
      const l = Math.round(Number(limit || 0));
      if(!l) return;

      const now = Date.now();
      const ratio = l > 0 ? (s / l) : 0;

      if(l !== speedState.lastLimitValue){
        speedState.lastLimitValue = l;
        speakOnce(`Yeni hız limiti ${l}.`);
      }

      if(ratio >= 1){
        if(now - speedState.lastWarnOverAt > 15000){
          speakOnce(`Dikkat. Limit ${l}, hız ${s}. Yavaşlayın.`);
          speedState.lastWarnOverAt = now;
        }
      }else if(ratio >= .85){
        if(now - speedState.lastWarnNearAt > 30000){
          speakOnce(`Hız limiti ${l}. Mevcut hız ${s}. Dikkat.`);
          speedState.lastWarnNearAt = now;
        }
      }
    }

    if("geolocation" in navigator){
      speedWatchId = navigator.geolocation.watchPosition(async (pos) => {
        const rawSpeed = pos.coords.speed;
        const kmh = (typeof rawSpeed === "number" && !isNaN(rawSpeed)) ? rawSpeed * 3.6 : 0;

        speedState.current = kmh;
        currentCoords = { lat:pos.coords.latitude, lng:pos.coords.longitude };
        speedState.history.push(kmh);
        if(speedState.history.length > 15) speedState.history.shift();

        spVal.textContent = Math.round(kmh);
        autoDetectLiveStop(currentCoords);
        updateCompactHeader();

        const lim = await fetchLimit(pos.coords.latitude, pos.coords.longitude);
        if(lim?.limit){
          spLimit.textContent = `Limit: ${lim.limit} km/h${lim.highway ? " · " + trHighway(lim.highway) : ""}`;
          if(kmh <= lim.limit) setState("limit-ok");
          else if(kmh <= lim.limit + 10) setState("limit-warn");
          else setState("limit-bad");
          maybeSpeak(kmh, lim.limit);
        }else{
          spLimit.textContent = "Limit: —";
          setState("");
        }

        renderTimeline();
        renderAI();
      }, () => {
        spVal.textContent = "0";
        spLimit.textContent = "GPS kapalı";
        setState("");
      }, {
        enableHighAccuracy:true,
        maximumAge:3000,
        timeout:12000
      });
    }else{
      spLimit.textContent = "GPS yok";
    }
  })();

  document.addEventListener("click", (e) => {
    const bagBadge = e.target.closest(".bag-badge");
    if(bagBadge){
      e.preventDefault();
      e.stopPropagation();
      const seat = bagBadge.closest(".seat")?.dataset.seat;
      if(!seat) return;
      const next = location.pathname;
      const url = `/bags?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seat)}&next=${encodeURIComponent(next)}`;
      location.href = url;
      return;
    }

    const seatEl = e.target.closest(".seat");
    if(seatEl && !multiMode){
      openSeat(Number(seatEl.dataset.seat));
      return;
    }
    if(seatEl && multiMode){
      e.preventDefault();
      e.stopPropagation();
      toggleSeatPick(seatEl);
      return;
    }
  }, true);

  onClick("#btnSeatClose", closeSeat);
  onClick("#seatBackdrop", closeSeat);
  onClick("#btnSeatSave", saveSeat);
  onClick("#btnSeatOffload", offloadSeat);

  onClick("#btnBagAdd", () => {
    const seat = currentSeat;
    if(!seat) return;
    const drop = $("#dropoff")?.value || "";
    const next = window.location.pathname;
    const url = `/bags/capture?trip_code=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seat)}&to_stop=${encodeURIComponent(drop)}&next=${encodeURIComponent(next)}`;
    window.location.href = url;
  });

  onClick("#btnBagView", () => {
    const seat = currentSeat;
    if(!seat) return;
    const next = window.location.pathname;
    const url = `/bags?trip=${encodeURIComponent(BAG_TRIP)}&seat=${encodeURIComponent(seat)}&next=${encodeURIComponent(next)}`;
    window.location.href = url;
  });

  onClick("#fabBulk", openBulk);
  onClick("#fabBulkPane", openBulk);
  onClick("#bulkClose", closeBulk);
  onClick("#bulkBackdrop", closeBulk);
  onClick("#bulkSave", saveBulk);
  onChange("#multiPick", (e) => setMultiMode(e.target.checked));

  onClick("#fabCash", openCash);
  onClick("#fabCashPane", openCash);
  onClick("#cashClose", closeCash);
  onClick("#cashBackdrop", closeCash);
  onClick("#cashSave", saveCash);

  onClick("#standingCard", openStandingModal);
  onClick("#openStandingModalBtn", openStandingModal);
  onClick("#standingClose", closeStandingModal);
  onClick("#standingBackdrop", closeStandingModal);

  onClick("#standingBulkOff", async () => {
    try{
      const j = await safeJsonFetch("/api/standing?all=1", {
        method:"DELETE",
        headers:{ "X-CSRF-Token": csrf }
      });

      if(!j?.ok) throw new Error(j?.msg || "Toplu ayakta silinemedi");

      await loadStandingTotals();
      await loadStandingItems();

      updateStats();
      renderStandingList();
      renderQuickStandingList();
      refreshStopBadges();
      renderAI();
      renderTimeline();
      updateCompactHeader();
      toast("Tüm ayakta kayıtlar temizlendi");
    }catch(e){
      toast(e.message || "Toplu silme hatası");
    }
  });

  onClick("#btnGeoWatch", toggleGeoWatch);
  onClick("#btnTriggerNow", triggerManualApproach);
  onClick("#btnOffloadNow", offloadSelectedStop);
  onClick("#btnOffloadNowPane", offloadSelectedStop);
  onClick("#btnSaveCoord", saveCoord);
  onClick("#btnOpenRouteTab", () => openTab("route"));

  onClick("#approachClose", () => closeModal("#approachBackdrop", "#approachModal"));
  onClick("#approachBackdrop", () => closeModal("#approachBackdrop", "#approachModal"));
  onClick("#approachSnooze", () => {
    closeModal("#approachBackdrop", "#approachModal");
    snoozeBlink();
  });

  onClick("#approachOffload", async () => {
    const stop = lastApproach?.stop;
    if(!stop) return;
    await bulkOffload(lastApproach.seats || []);
    await offloadStandingForStop(stop);
    setLiveStop(stop);
    closeModal("#approachBackdrop", "#approachModal");
    renderAI();
    renderTimeline();
    updateCompactHeader();
  });

  onChange("#alertStop", () => {
    updateGeoHint();
    refreshStopBadges();
    updateStopSeatBadges();
    renderAI();
    renderTimeline();
    updateCompactHeader();

    const a = getSelectedStopName() || "";
    if(a && $("#cashModal")?.style.display === "block") setValue("#cashTo", a);
    if(a && $("#bulkModal")?.style.display === "block") setValue("#bulkTo", a);
  });

  window.addEventListener("keydown", (e) => {
    if(e.key === "Escape"){
      closeSeat();
      closeBulk();
      closeCash();
      closeStandingModal();
      closeModal("#approachBackdrop", "#approachModal");
    }
  });

  onClick("#btnDeckAI", startDeckAIVoice);

  (async function init(){
    try{
      initTabs();
      loadVoiceState();
      setVoiceBadge("Hazır");

      await fetchStops();
      await populateStops();
      await loadRouteScheduleFromApi();
      await loadStandingTotals();
      await loadStandingItems();
      await loadParcelItems();

      for(const seatNo of Object.keys(seatPositions || {})){
        setSeatVisual(seatNo);
      }

      await refreshBagsAll();

      refreshStopBadges();
      updateStopSeatBadges();
      updateStats();
      updateGeoHint();
      renderQuickStandingList();
      renderRouteStrip();

      if(speedState.liveStop){
        updateCompactHeader();
      }

      const next = computeNextStopName(speedState.liveStop || "", "nextWithSeats");
      if(next) setSelectedStop(next, { silent:true, voiceReply:false });
      else if(serverStops?.length) setSelectedStop(serverStops[0], { silent:true, voiceReply:false });

      renderTimeline();
      renderAI();
      updateCompactHeader();
    }catch(e){
      toast(e.message || "Başlangıç yükleme hatası");
    }
  })();
