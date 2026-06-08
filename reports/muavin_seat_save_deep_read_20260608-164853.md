# Muavin Asistanı Koltuk Kaydetme Derin Okuma V7

- Tarih: `20260608-164853`
- Bu rapor sadece okuma/tespittir. Dosya değiştirmez.

## WEB modals.html
- Yol: `templates/seats_parts/modals.html`
- Satır: `196`

### Kritik kelime satırları
| Satır | İçerik |
| --- | --- |
| 1 | <div class="modal-backdrop" id="seatBackdrop"></div> |
| 2 | <div class="modal glass" id="seatModal"> |
| 3 |   <h3 id="seatTitle">Koltuk</h3> |
| 18 |       <div class="muted" style="margin-bottom:8px">Bilet Türü</div> |
| 27 |       <div class="muted" style="margin-bottom:8px">Cinsiyet</div> |
| 41 |       <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button> |
| 42 |       <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button> |
| 48 |         <input type="number" id="price" value="0.00" step="0.01"> |
| 52 |         <input type="text" id="service_note" placeholder="Not / konum / açıklama"> |
| 57 |       <div class="muted" style="margin-bottom:8px">Ödeme</div> |
| 70 |     <button class="btn green" type="button" id="btnSeatSave">Kaydet</button> |
| 71 |     <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button> |
| 72 |     <button class="btn ghost" type="button" id="btnSeatClose">Kapat</button> |
| 100 |         <div class="radio-row" style="padding-top:8px"> |
| 116 |     <button class="btn ghost" type="button" id="bulkClose">Kapat</button> |
| 117 |     <button class="btn primary" type="button" id="bulkSave">Kaydet</button> |
| 165 |     <button class="btn ghost" type="button" id="cashClose">Kapat</button> |
| 166 |     <button class="btn primary" type="button" id="cashSave">Ekle</button> |
| 177 |     <button class="btn danger" type="button" id="approachOffload">Toplu İndir</button> |
| 178 |     <button class="btn ghost" type="button" id="approachSnooze">Ertele (5 dk)</button> |
| 179 |     <button class="btn ghost" type="button" id="approachClose">Kapat</button> |
| 187 |   <div class="standing-list" id="standingList" style="margin-top:12px;"></div> |
| 190 |     <button class="btn danger" type="button" id="standingBulkOff" style="display:none">Toplu İndir</button> |
| 191 |     <button class="btn ghost" type="button" id="standingClose">Kapat</button> |
| 195 | <div id="toast"></div> |

### WEB modals.html satır 1-120
```html
0001: <div class="modal-backdrop" id="seatBackdrop"></div>
0002: <div class="modal glass" id="seatModal">
0003:   <h3 id="seatTitle">Koltuk</h3>
0004: 
0005:   <div class="field-grid">
0006:     <div class="field-row">
0007:       <label class="field">
0008:         <span>Biniş Yeri</span>
0009:         <select id="pickup"><option value="">—</option></select>
0010:       </label>
0011:       <label class="field">
0012:         <span>İniş Yeri</span>
0013:         <select id="dropoff"><option value="">—</option></select>
0014:       </label>
0015:     </div>
0016: 
0017:     <div>
0018:       <div class="muted" style="margin-bottom:8px">Bilet Türü</div>
0019:       <div class="radio-row">
0020:         <label><input type="radio" name="ticket" value="biletli"> Biletli</label>
0021:         <label><input type="radio" name="ticket" value="biletsiz" checked> Biletsiz</label>
0022:         <label><input type="radio" name="ticket" value="ucretsiz"> Ücretsiz</label>
0023:       </div>
0024:     </div>
0025: 
0026:     <div>
0027:       <div class="muted" style="margin-bottom:8px">Cinsiyet</div>
0028:       <div class="radio-row">
0029:         <label><input type="radio" name="gender" value="bay"> Bay</label>
0030:         <label><input type="radio" name="gender" value="bayan"> Bayan</label>
0031:         <label><input type="radio" name="gender" value=""> Boş</label>
0032:       </div>
0033:     </div>
0034: 
0035:     <div class="check-row">
0036:       <label><input type="checkbox" id="pairOk"> Yan yana istisna</label>
0037:       <label><input type="checkbox" id="service"> Servis kullanacak</label>
0038:     </div>
0039: 
0040:     <div class="action-grid">
0041:       <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button>
0042:       <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button>
0043:     </div>
0044: 
0045:     <div class="field-row">
0046:       <label class="field">
0047:         <span>Tutar (₺)</span>
0048:         <input type="number" id="price" value="0.00" step="0.01">
0049:       </label>
0050:       <label class="field">
0051:         <span>Servis Notu</span>
0052:         <input type="text" id="service_note" placeholder="Not / konum / açıklama">
0053:       </label>
0054:     </div>
0055: 
0056:     <div>
0057:       <div class="muted" style="margin-bottom:8px">Ödeme</div>
0058:       <div class="radio-row">
0059:         <label><input type="radio" name="pay" value="nakit" checked> Nakit</label>
0060:         <label><input type="radio" name="pay" value="iban"> IBAN</label>
0061:         <label><input type="radio" name="pay" value="online"> Online</label>
0062:         <label><input type="radio" name="pay" value="pos"> POS</label>
0063:         <label><input type="radio" name="pay" value="ucretsiz"> Ücretsiz</label>
0064:       </div>
0065:     </div>
0066: 
0067:   </div>
0068: 
0069:   <div class="modal-actions">
0070:     <button class="btn green" type="button" id="btnSeatSave">Kaydet</button>
0071:     <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button>
0072:     <button class="btn ghost" type="button" id="btnSeatClose">Kapat</button>
0073:   </div>
0074: </div>
0075: 
0076: <div class="modal-backdrop" id="bulkBackdrop"></div>
0077: <div class="sheet-modal glass" id="bulkModal">
0078:   <h3>Toplu Giriş</h3>
0079: 
0080:   <div class="field-grid">
0081:     <div class="field-row">
0082:       <label class="field">
0083:         <span>Nereden</span>
0084:         <select id="bulkFrom"><option value="">—</option></select>
0085:       </label>
0086:       <label class="field">
0087:         <span>Nereye</span>
0088:         <select id="bulkTo"><option value="">—</option></select>
0089:       </label>
0090:     </div>
0091: 
0092:     <div class="field-row">
0093:       <label class="field">
0094:         <span>Adet</span>
0095:         <input type="number" id="bulkCount" min="1" value="1">
0096:       </label>
0097: 
0098:       <div class="field">
0099:         <span>Bilet</span>
0100:         <div class="radio-row" style="padding-top:8px">
0101:           <label><input type="radio" name="bulkTicket" value="biletsiz" checked> Biletsiz</label>
0102:           <label><input type="radio" name="bulkTicket" value="biletli"> Biletli</label>
0103:         </div>
0104:       </div>
0105:     </div>
0106: 
0107:     <div class="check-row">
0108:       <label><input type="checkbox" id="multiPick"> Çoklu seçim</label>
0109:       <label><input type="checkbox" id="bulkService"> Servis</label>
0110:     </div>
0111: 
0112:     <div class="muted">Çoklu seçim açıksa koltukları elle seçersin. Kapalıysa sistem boş koltuklardan yerleştirir.</div>
0113:   </div>
0114: 
0115:   <div class="modal-actions">
0116:     <button class="btn ghost" type="button" id="bulkClose">Kapat</button>
0117:     <button class="btn primary" type="button" id="bulkSave">Kaydet</button>
0118:   </div>
0119: </div>
0120:
```

## WEB seats.js
- Yol: `static/seats/seats.js`
- Satır: `2960`

### Kritik kelime satırları
| Satır | İçerik |
| --- | --- |
| 12 | const stopsMap = BOOT.stopsMap \|\| {}; |
| 17 | const serverStops = BOOT.serverStops \|\| []; |
| 24 | (function hardCleanOldStopFlowOnce(){ |
| 28 |     const key = "hardCleanStopFlowOnce:" + TRIP_KEY; |
| 31 |     if(localStorage.getItem(key) === version) return; |
| 34 |       "stopFlowSummary:" + TRIP_KEY, |
| 35 |       "passedStops:" + TRIP_KEY, |
| 36 |       "liveStop:" + TRIP_KEY, |
| 37 |       "continueTripStop:" + TRIP_KEY, |
| 38 |       "continueTripStop:last" |
| 39 |     ].forEach(k => localStorage.removeItem(k)); |
| 41 |     localStorage.setItem(key, version); |
| 52 |       { stop: "Denizli otogar", time: "20:00" }, |
| 53 |       { stop: "Alaşehir Otogar", time: "23:10" }, |
| 54 |       { stop: "Salihli Garaj", time: "23:50" }, |
| 55 |       { stop: "Turgutlu Garaj", time: "00:25" }, |
| 56 |       { stop: "Manisa Otogar", time: "01:05" }, |
| 57 |       { stop: "Balıkesir", time: "03:10" }, |
| 58 |       { stop: "Bursa Otogar", time: "04:30" }, |
| 59 |       { stop: "Harem", time: "07:30" }, |
| 60 |       { stop: "Esenler Otogar", time: "08:00" } |
| 63 |       { stop: "Esenler Otogar", time: "20:00" }, |
| 64 |       { stop: "Harem", time: "20:35" }, |
| 65 |       { stop: "Bursa Otogar", time: "23:15" }, |
| 66 |       { stop: "Balıkesir", time: "00:35" }, |
| 67 |       { stop: "Manisa Otogar", time: "02:40" }, |
| 68 |       { stop: "Turgutlu Garaj", time: "03:15" }, |
| 69 |       { stop: "Salihli Garaj", time: "03:55" }, |
| 70 |       { stop: "Alaşehir Otogar", time: "04:40" }, |
| 71 |       { stop: "Denizli otogar", time: "07:20" } |
| 74 |       { stop: "Denizli otogar", time: "20:00" }, |
| 75 |       { stop: "Alaşehir Otogar", time: "22:10" }, |
| 76 |       { stop: "Salihli Garaj", time: "22:50" }, |
| 77 |       { stop: "Turgutlu Garaj", time: "23:25" }, |
| 78 |       { stop: "Manisa Otogar", time: "00:00" }, |
| 79 |       { stop: "İzmir Otogar", time: "01:10" } |
| 82 |       { stop: "İzmir Otogar", time: "20:00" }, |
| 83 |       { stop: "Manisa Otogar", time: "21:00" }, |
| 84 |       { stop: "Turgutlu Garaj", time: "21:35" }, |
| 85 |       { stop: "Salihli Garaj", time: "22:10" }, |
| 86 |       { stop: "Alaşehir Otogar", time: "22:50" }, |
| 87 |       { stop: "Denizli otogar", time: "01:00" } |
| 90 |   const $ = (s) => document.querySelector(s); |
| 91 |   const $$ = (s) => Array.from(document.querySelectorAll(s)); |
| 95 |     if(el) el.addEventListener("click", fn); |
| 100 |     if(el) el.addEventListener("change", fn); |
| 139 |     const memorySchemaVersion = "v2-stop-flow-clean-20260512"; |
| 141 |     const oldTripId = localStorage.getItem(activeTripMemoryKey) \|\| ""; |
| 142 |     const oldSchema = localStorage.getItem(memorySchemaKey) \|\| ""; |
| 155 |       "liveStop:", |
| 156 |       "passedStops:", |
| 160 |       "continueTripStop:", |
| 161 |       "stopFlowSummary:" |
| 165 |       localStorage.removeItem(prefix + TRIP_KEY); |
| 168 |     localStorage.removeItem("continueTripStop:last"); |
| 170 |     Object.keys(localStorage).forEach(k => { |
| 175 |         localStorage.removeItem(k); |
| 179 |     localStorage.setItem(activeTripMemoryKey, currentTripId); |
| 180 |     localStorage.setItem(memorySchemaKey, memorySchemaVersion); |
| 188 |     JSON.parse(localStorage.getItem("boardsMap:" + TRIP_KEY) \|\| "{}") |
| 191 |   let cachedStops = null; |
| 192 |   let currentSeat = null; |
| 202 |   let lastApproach = { stop:null, seats:[] }; |
| 204 |   let lastApproachVoiceStop = ""; |
| 205 |   let lastRouteStripCenteredStop = ""; |
| 212 |     history: [], |
| 218 |     liveStop: "", |
| 219 |     passedStops: new Set(), |
| 223 |   function toast(msg, ms=2400){ |
| 224 |     const t = $("#toast"); |
| 228 |     clearTimeout(toast._timer); |
| 229 |     toast._timer = setTimeout(() => { |
| 235 |     return "₺" + Number(v \|\| 0).toFixed(2); |
| 251 |       .toString() |
| 255 |       .toLowerCase(); |
| 273 |   function persistBoards(){ |
| 274 |     localStorage.setItem("boardsMap:" + TRIP_KEY, JSON.stringify(boardsMap \|\| {})); |
| 277 |   function persistVoiceState(){ |
| 278 |     localStorage.setItem("liveStop:" + TRIP_KEY, speedState.liveStop \|\| ""); |
| 279 |     localStorage.setItem("passedStops:" + TRIP_KEY, JSON.stringify([...speedState.passedStops])); |
| 283 |     speedState.liveStop = localStorage.getItem("liveStop:" + TRIP_KEY) \|\| ""; |
| 285 |       speedState.passedStops = new Set(JSON.parse(localStorage.getItem("passedStops:" + TRIP_KEY) \|\| "[]")); |
| 287 |       speedState.passedStops = new Set(); |
| 291 |   function persistStandingTotals(){ |
| 292 |     localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({ |
| 298 |   function persistStandingItems(){ |
| 299 |     localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| [])); |
| 311 |   function allStopsList(){ |
| 312 |     if(Array.isArray(cachedStops) && cachedStops.length) return cachedStops.map(x => x.name); |
| 313 |     return Array.isArray(serverStops) ? serverStops.slice() : []; |
| 316 |   function indexOfStopByName(name){ |
| 317 |     const list = allStopsList(); |
| 322 |   function findStopByName(name){ |
| 324 |     const list = Array.isArray(cachedStops) |
| 325 |       ? cachedStops |
| 326 |       : (Array.isArray(serverStops) ? serverStops.map(s => ({ name:s, lat:null, lng:null })) : []); |
| 330 |   function findCanonicalStopName(name){ |
| 331 |     const s = findStopByName(name); |
| 335 |   function hasCoord(stop){ |
| 336 |     if(!stop) return false; |
| 337 |     const lat = parseFloat(stop.lat); |
| 338 |     const lng = parseFloat(stop.lng); |
| 344 |     const toRad = d => d * Math.PI / 180; |
| 345 |     const dLat = toRad(b.lat - a.lat); |
| 346 |     const dLng = toRad(b.lng - a.lng); |
| 347 |     const la1 = toRad(a.lat); |
| 348 |     const la2 = toRad(b.lat); |
| 353 | function nearestStopByGps(maxKm = 15){ |
| 354 |   if(!currentCoords \|\| !Array.isArray(cachedStops)) return ""; |
| 358 |   for(const s of cachedStops){ |
| 382 | function getDisplayLiveStop(){ |
| 383 |   const live = speedState.liveStop \|\| ""; |
| 388 |     if(typeof hasLiveStopOperation === "function" && !hasLiveStopOperation(live)){ |
| 389 |       speedState.liveStop = ""; |
| 390 |       speedState.passedStops = new Set(); |
| 393 |         localStorage.removeItem("liveStop:" + TRIP_KEY); |
| 394 |         localStorage.removeItem("passedStops:" + TRIP_KEY); |
| 403 |     const km = stopDistanceKmByName(live); |
| 406 |       speedState.liveStop = ""; |
| 407 |       speedState.passedStops = new Set(); |
| 410 |         localStorage.removeItem("liveStop:" + TRIP_KEY); |
| 411 |         localStorage.removeItem("passedStops:" + TRIP_KEY); |
| 421 | function stopDistanceKmByName(name){ |
| 424 |   const stopObj = findStopByName(name); |
| 425 |   if(!stopObj \|\| !hasCoord(stopObj)) return NaN; |
| 428 |     lat: Number(stopObj.lat), |
| 429 |     lng: Number(stopObj.lng) |
| 434 |   const datePart = TRIP_DATE \|\| new Date().toISOString().slice(0,10); |
| 438 |   const firstTimedStop = Array.isArray(routeSchedule) |
| 442 |   const rawTime = firstTimedStop?.time \|\| TRIP_DEPARTURE_TIME \|\| "00:00"; |
| 466 |         stop: x.stop_name, |
| 508 |         stop:item.stop, |
| 520 |       stop: x.stop, |
| 524 |       routeIndex: indexOfStopByName(x.stop) |
| 534 |     return d.toLocaleTimeString("tr-TR", { hour:"2-digit", minute:"2-digit" }); |
| 545 |   function getSelectedStopName(){ |
| 546 |     return ($("#alertStop")?.value \|\| "").trim(); |
| 549 |   function isTimedStop(name){ |
| 550 |     return getRouteSchedule().some(x => norm(x.stop) === norm(name)); |
| 553 |   function hasPassengersFor(stopName){ |
| 554 |     return seatsForStop(stopName).length > 0; |
| 557 |   function isFinalStop(name){ |
| 558 |     const list = allStopsList(); |
| 559 |     const idx = indexOfStopByName(name); |
| 563 |   async function fetchStops(){ |
| 564 |     const j = await safeJsonFetch("/api/stops"); |
| 567 |     let stops = (j.stops \|\| []).map(name => ({ name, lat:null, lng:null })); |
| 572 |         const coordMap = new Map((c.items \|\| []).map(i => [i.stop, { lat:i.lat, lng:i.lng }])); |
| 573 |         stops = stops.map(s => coordMap.has(s.name) ? { ...s, ...coordMap.get(s.name) } : s); |
| 577 |     cachedStops = stops; |
| 578 |     return stops; |
| 581 |   async function populateStops(){ |
| 582 |     if(!cachedStops) await fetchStops(); |
| 584 |     const ids = ["alertStop","pickup","dropoff","bulkFrom","bulkTo","cashFrom","cashTo"]; |
| 597 |       for(const s of cachedStops){ |
| 600 |         o.dataset.label = s.name; |
| 611 |   function computeSeatCountsByStop(){ |
| 613 |     Object.values(stopsMap \|\| {}).forEach(stop => { |
| 614 |       if(stop) out[stop] = (out[stop] \|\| 0) + 1; |
| 619 |   function computeStandingCountsByStop(){ |
| 622 |       const raw = (it?.to \|\| "").trim(); |
| 624 |       const key = (findStopByName(raw)?.name \|\| raw).trim(); |
| 632 |   function computeParcelCountsByStop(){ |
| 635 |       const raw = (it?.to \|\| "").trim(); |
| 637 |       const key = (findStopByName(raw)?.name \|\| raw).trim(); |
| 646 |   const STOP_FLOW_SUMMARY_KEY = "stopFlowSummary:" + TRIP_KEY; |
| 647 |   const STOP_FLOW_EVENT_KEY = "stopFlowLiveEvents:" + TRIP_KEY; |
| 648 |   let stopFlowSummary = {}; |
| 650 |   function readStopFlowLiveEvents(){ |
| 652 |       const raw = localStorage.getItem(STOP_FLOW_EVENT_KEY) \|\| "{}"; |
| 660 |   function writeStopFlowLiveEvents(obj){ |
| 662 |       localStorage.setItem(STOP_FLOW_EVENT_KEY, JSON.stringify(obj \|\| {})); |
| 666 |   function loadStopFlowSummary(){ |
| 668 |       const raw = localStorage.getItem(STOP_FLOW_SUMMARY_KEY) \|\| "{}"; |
| 670 |       stopFlowSummary = obj && typeof obj === "object" ? obj : {}; |
| 672 |       stopFlowSummary = {}; |
| 677 |   function clearStaleStopFlowIfTripEmpty(){ |
| 685 |         "stopFlowSummary:" + TRIP_KEY, |
| 686 |         "liveStop:" + TRIP_KEY, |
| 687 |         "passedStops:" + TRIP_KEY, |
| 691 |         "continueTripStop:" + TRIP_KEY, |
| 692 |         "continueTripStop:last" |
| 695 |       keys.forEach(k => localStorage.removeItem(k)); |
| 697 |       stopFlowSummary = {}; |
| 700 |         speedState.liveStop = ""; |
| 701 |         speedState.passedStops = new Set(); |
| 704 |       if(typeof renderTimeline === "function") renderTimeline(); |
| 706 |       if(typeof renderAI === "function") renderAI(); |
| 711 |   setTimeout(clearStaleStopFlowIfTripEmpty, 0); |
| 713 |   function persistStopFlowSummary(){ |
| 715 |       localStorage.setItem(STOP_FLOW_SUMMARY_KEY, JSON.stringify(stopFlowSummary \|\| {})); |
| 719 |   function stopSummaryKey(stopName){ |
| 720 |     return (findCanonicalStopName(stopName) \|\| String(stopName \|\| "")).trim(); |
| 723 |   function boardCountForStop(stopName){ |
| 724 |     const key = norm(stopName); |
| 727 |     let total = 0; |
| 729 |     Object.keys(assigned \|\| {}).forEach(seatNo => { |
| 730 |       if(!assigned[seatNo]) return; |
| 731 |       if(norm(boardsMap[String(seatNo)] \|\| "") === key){ |
| 732 |         total += 1; |

### WEB seats.js satır 70-125
```js
0070:       { stop: "Alaşehir Otogar", time: "04:40" },
0071:       { stop: "Denizli otogar", time: "07:20" }
0072:     ],
0073:     "Denizli – İzmir": [
0074:       { stop: "Denizli otogar", time: "20:00" },
0075:       { stop: "Alaşehir Otogar", time: "22:10" },
0076:       { stop: "Salihli Garaj", time: "22:50" },
0077:       { stop: "Turgutlu Garaj", time: "23:25" },
0078:       { stop: "Manisa Otogar", time: "00:00" },
0079:       { stop: "İzmir Otogar", time: "01:10" }
0080:     ],
0081:     "İzmir – Denizli": [
0082:       { stop: "İzmir Otogar", time: "20:00" },
0083:       { stop: "Manisa Otogar", time: "21:00" },
0084:       { stop: "Turgutlu Garaj", time: "21:35" },
0085:       { stop: "Salihli Garaj", time: "22:10" },
0086:       { stop: "Alaşehir Otogar", time: "22:50" },
0087:       { stop: "Denizli otogar", time: "01:00" }
0088:     ]
0089:   };
0090:   const $ = (s) => document.querySelector(s);
0091:   const $$ = (s) => Array.from(document.querySelectorAll(s));
0092: 
0093:   function onClick(sel, fn){
0094:     const el = $(sel);
0095:     if(el) el.addEventListener("click", fn);
0096:   }
0097: 
0098:   function onChange(sel, fn){
0099:     const el = $(sel);
0100:     if(el) el.addEventListener("change", fn);
0101:   }
0102: 
0103:   function setText(sel, val){
0104:     const el = $(sel);
0105:     if(el) el.textContent = val;
0106:   }
0107: 
0108:   function setValue(sel, val){
0109:     const el = $(sel);
0110:     if(el) el.value = val;
0111:   }
0112: 
0113:   function show(el){
0114:     if(el) el.style.display = "block";
0115:   }
0116: 
0117:   function hide(el){
0118:     if(el) el.style.display = "none";
0119:   }
0120: 
0121:   
0122: /* =========================================================
0123:    TRIP MEMORY GUARD
0124:    Aynı rota/plaka ile yeni sefer açılınca eski canlı durak,
0125:    geçildi bilgisi ve durak akışı özeti taşınmasın.
```

### WEB seats.js satır 1160-1210
```js
1160:     const item = document.createElement("button");
1161:     item.type = "button";
1162:     item.dataset.stop = stop;
1163:     item.className = `route-stop ${isActive || isLive ? "active" : ""} ${isDone ? "done has-flow-summary" : ""} ${liveDangerOn && isLive ? "live-danger" : ""} ${isNextWarn ? "next-warning" : ""} ${isFlowGreen ? "flow-green" : ""}`;
1164:     if(isLive){routeFocusItem = item;}   
1165: 
1166:     const etaItem = etaMap.get(norm(stop));
1167:     const planText = plan || "—";
1168:     const etaText = etaItem && plan ? fmtHour(etaItem.etaDate) : "";
1169:     const delayText = etaItem && plan ? etaItem.badgeText : "";
1170:     const kmValue = kmText || (etaItem && Number.isFinite(etaItem.km) ? `${etaItem.km.toFixed(1)} km` : "—");
1171: 
1172:     const timeText = etaText ? `${planText} → ${etaText}` : planText;
1173:     const statusText = delayText ? `${kmValue} · ${delayText}` : kmValue;
1174: 
1175:     item.innerHTML = `
1176:   <div class="name">${stop}</div>
1177:   <div class="meta ${isDone ? "done-summary" : ""}">${metaLine1} · ${metaLine2}</div>
1178:   <div class="extra">
1179:     <div class="extra-line">
1180:       <span class="extra-k">Plan/ETA</span>
1181:       <span class="extra-v">${timeText}</span>
1182:     </div>
1183:     <div class="extra-line">
1184:       <span class="extra-k">Durum</span>
1185:       <span class="extra-v">${statusText}</span>
1186:     </div>
1187:   </div>
1188:    `;
1189: 
1190: item.addEventListener("click", () => {
1191:   setSelectedStop(stop, { silent:false, voiceReply:true });
1192: 
1193:   // APK/WebView için ek garanti: durak kartı tıklamasında doğrudan TTS tetikle
1194:   try{
1195:     const msg = stopHumanVoiceSummary(stop);
1196:     if(typeof speakOnce === "function") speakOnce(msg);
1197:   }catch(_){}
1198: });
1199: 
1200: wrap.appendChild(item);
1201: });
1202: 
1203: if(routeFocusItem && live){
1204:   const focusKey = norm(live);
1205: 
1206:   if(lastRouteStripCenteredStop !== focusKey){
1207:     lastRouteStripCenteredStop = focusKey;
1208: 
1209:     requestAnimationFrame(() => {
1210:       setTimeout(() => {
```

### WEB seats.js satır 1360-1475
```js
1360:     if(!h) return;
1361: 
1362:     const stopName = getSelectedStopName();
1363: 
1364:     if(geoWatchId){
1365:       return;
1366:     }
1367: 
1368:     if(!stopName){
1369:       h.textContent = "Durak seç.";
1370:       return;
1371:     }
1372: 
1373:     const s = findStopByName(stopName);
1374:     h.textContent = hasCoord(s) ? "Koordinat hazır." : "Koordinat yok. Aşağıdan ekleyin.";
1375:   }
1376: 
1377:   function openModal(backdropSel, modalSel){
1378:     show($(backdropSel));
1379:     show($(modalSel));
1380:   }
1381: 
1382:   function closeModal(backdropSel, modalSel){
1383:     hide($(backdropSel));
1384:     hide($(modalSel));
1385:   }
1386: 
1387:   function openSeat(seatNo){
1388:     currentSeat = seatNo;
1389:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1390: 
1391:     const seatEl = $("#seat-" + seatNo);
1392:     if(seatEl) seatEl.classList.add("selected");
1393: 
1394:     setText("#seatTitle", "Koltuk " + seatNo);
1395:     setValue("#pickup", boardsMap[String(seatNo)] || getSelectedStopName() || "");
1396:     setValue("#dropoff", stopsMap[String(seatNo)] || "");
1397: 
1398:     const pay = document.querySelector('input[name="pay"][value="nakit"]');
1399:     if(pay) pay.checked = true;
1400: 
1401:     const ticket = document.querySelector('input[name="ticket"][value="biletsiz"]');
1402:     if(ticket) ticket.checked = true;
1403: 
1404:     setValue("#price", "0.00");
1405: 
1406:     const prevGender = genders[String(seatNo)] || "";
1407:     const gInput =
1408:       document.querySelector(`input[name="gender"][value="${prevGender}"]`) ||
1409:       document.querySelector('input[name="gender"][value=""]');
1410:     if(gInput) gInput.checked = true;
1411: 
1412:     if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)];
1413:     setValue("#service_note", serviceNotes[String(seatNo)] || "");
1414:     if($("#pairOk")) $("#pairOk").checked = false;
1415: 
1416:     openModal("#seatBackdrop", "#seatModal");
1417:   }
1418: 
1419:   function closeSeat(){
1420:     currentSeat = null;
1421:     closeModal("#seatBackdrop", "#seatModal");
1422:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1423:   }
1424: 
1425:   async function saveSeat(){
1426:     if(!currentSeat) return;
1427: 
1428:     const wasAlreadyAssigned = !!assigned[String(currentSeat)];
1429: 
1430:     const from = $("#pickup")?.value || getSelectedStopName() || "";
1431:     const stop = $("#dropoff")?.value || "";
1432:     const ticket = document.querySelector('input[name="ticket"]:checked')?.value || "biletsiz";
1433:     const payment = document.querySelector('input[name="pay"]:checked')?.value || "nakit";
1434:     const amount = parseMoney($("#price")?.value || 0);
1435:     const gender = document.querySelector('input[name="gender"]:checked')?.value || "";
1436:     const pair_ok = $("#pairOk")?.checked ? 1 : 0;
1437:     const service = $("#service")?.checked || false;
1438:     const service_note = $("#service_note")?.value || "";
1439: 
1440:     try{
1441:       const j = await safeJsonFetch("/api/seat", {
1442:         method:"POST",
1443:         headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1444:         body:JSON.stringify({
1445:           seat_no: currentSeat,
1446:           from,
1447:           stop,
1448:           ticket_type: ticket,
1449:           payment,
1450:           amount,
1451:           gender,
1452:           pair_ok,
1453:           service,
1454:           service_note
1455:         })
1456:       });
1457: 
1458:       if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");
1459: 
1460:       assigned[String(currentSeat)] = true;
1461:       stopsMap[String(currentSeat)] = stop;
1462:       genders[String(currentSeat)] = gender;
1463:       serviceMap[String(currentSeat)] = !!service;
1464:       serviceNotes[String(currentSeat)] = service_note;
1465:       boardsMap[String(currentSeat)] = from;
1466: 
1467:       if(!wasAlreadyAssigned && from){
1468:         recordStopFlowEvent(from, { board: 1 });
1469:       }
1470: 
1471:       persistBoards();
1472:       setSeatVisual(currentSeat);
1473:       closeSeat();
1474:       updateStats();
1475:       refreshStopBadges();
```

### WEB seats.js satır 1475-1545
```js
1475:       refreshStopBadges();
1476:       updateStopSeatBadges();
1477:       renderAI();
1478:       renderTimeline();
1479:       updateCompactHeader();
1480:       toast("Koltuk kaydedildi");
1481:     }catch(e){
1482:       toast(e.message || "Kaydetme hatası");
1483:     }
1484:   }
1485: 
1486:   function clearSeatUI(seatNo){
1487:     try{
1488:       if(typeof window.clearBiletsizSeatBadges === "function"){
1489:         window.clearBiletsizSeatBadges([seatNo]);
1490:       }
1491:     }catch(_){}
1492: 
1493:     delete assigned[String(seatNo)];
1494:     delete stopsMap[String(seatNo)];
1495:     delete genders[String(seatNo)];
1496:     delete serviceMap[String(seatNo)];
1497:     delete serviceNotes[String(seatNo)];
1498:     delete boardsMap[String(seatNo)];
1499: 
1500:     persistBoards();
1501:     setSeatVisual(seatNo);
1502: 
1503:     const el = $("#seat-" + seatNo);
1504:     if(el){
1505:       el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");
1506:       const cnt = el.querySelector(".bag-count");
1507:       const dir = el.querySelector(".bag-dir");
1508:       if(cnt) cnt.textContent = "0";
1509:       if(dir) dir.textContent = "";
1510:     }
1511:   }
1512: 
1513:   async function offloadSeat(){
1514:     if(!currentSeat) return;
1515: 
1516:     const offStop = stopsMap[String(currentSeat)] || getSelectedStopName() || "";
1517: 
1518:     try{
1519:       const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, {
1520:         method:"DELETE",
1521:         headers:{ "X-CSRF-Token": csrf }
1522:       });
1523: 
1524:       if(!j.ok) throw new Error(j.msg || "Silme başarısız");
1525: 
1526:       if(offStop){
1527:         recordStopFlowEvent(offStop, { offload: 1 });
1528:       }
1529: 
1530:       await clearBagsForSeat(currentSeat);
1531:       clearSeatUI(currentSeat);
1532:       closeSeat();
1533:       updateStats();
1534:       refreshStopBadges();
1535:       updateStopSeatBadges();
1536:       renderAI();
1537:       renderTimeline();
1538:       updateCompactHeader();
1539:       toast("Koltuk boşaltıldı");
1540:     }catch(e){
1541:       toast(e.message || "İniş hatası");
1542:     }
1543:   }
1544: 
1545:   function clearMultiPicks(){
```

### WEB seats.js satır 1545-1615
```js
1545:   function clearMultiPicks(){
1546:     for(const el of multiSelected){
1547:       el.classList.remove("multi-picked");
1548:     }
1549:     multiSelected.clear();
1550:   }
1551: 
1552:   function toggleSeatPick(el){
1553:     if(el.classList.contains("isAssigned")) return;
1554: 
1555:     if(multiSelected.has(el)){
1556:       multiSelected.delete(el);
1557:       el.classList.remove("multi-picked");
1558:     }else{
1559:       multiSelected.add(el);
1560:       el.classList.add("multi-picked");
1561:     }
1562:   }
1563: 
1564:   function setMultiMode(on){
1565:     multiMode = !!on;
1566:     const cb = $("#multiPick");
1567:     if(cb) cb.checked = multiMode;
1568: 
1569:     if(!multiMode){
1570:       clearMultiPicks();
1571:       toast("Çoklu seçim kapalı");
1572:     }else{
1573:       toast("Çoklu seçim açık. Koltukları seç.");
1574:     }
1575:   }
1576: 
1577:   function openBulk(){
1578:     populateStops().then(() => {
1579:       const selected = getSelectedStopName() || "";
1580:       const live = getDisplayLiveStop();
1581:       const fromDefault = live || selected || serverStops?.[0] || "";
1582:       if(selected) setValue("#bulkTo", selected);
1583:       if(fromDefault) setValue("#bulkFrom", fromDefault);
1584:       if($("#multiPick")) $("#multiPick").checked = !!multiMode;
1585:       openModal("#bulkBackdrop", "#bulkModal");
1586:     });
1587:   }
1588: 
1589:   function closeBulk(){
1590:     closeModal("#bulkBackdrop", "#bulkModal");
1591:   }
1592: 
1593:   async function saveBulk(){
1594:     const from = $("#bulkFrom")?.value || speedState.liveStop || getSelectedStopName() || "";
1595:     const to = $("#bulkTo")?.value || "";
1596:     const count = Math.max(1, parseInt($("#bulkCount")?.value || "1", 10));
1597:     const ticketVal = document.querySelector('input[name="bulkTicket"]:checked')?.value || "biletsiz";
1598:     const useService = $("#bulkService")?.checked || false;
1599: 
1600:     if(!to){
1601:       toast("Nereye seç");
1602:       return;
1603:     }
1604: 
1605:     const chosen = [...multiSelected].map(el => Number(el.dataset.seat));
1606:     let targets = [];
1607: 
1608:     if(multiMode){
1609:       if(!chosen.length){
1610:         toast("Önce koltukları seç.");
1611:         return;
1612:       }
1613:       targets = chosen;
1614:     }else{
1615:       const empties = [];
```

### WEB seats.js satır 2400-2510
```js
2400: 
2401:       const now = Date.now();
2402: 
2403:       if(currentLive && norm(currentLive) === norm(best.stop)){
2404:         liveDetectCandidate = {
2405:           name: best.stop,
2406:           hits: LIVE_STABLE_HITS,
2407:           lastAt: now
2408:         };
2409:         return;
2410:       }
2411: 
2412:       const sameCandidate =
2413:         liveDetectCandidate &&
2414:         norm(liveDetectCandidate.name || "") === norm(best.stop) &&
2415:         now - Number(liveDetectCandidate.lastAt || 0) < 15000;
2416: 
2417:       const nextHits = sameCandidate
2418:         ? Number(liveDetectCandidate.hits || 0) + 1
2419:         : 1;
2420: 
2421:       liveDetectCandidate = {
2422:         name: best.stop,
2423:         hits: nextHits,
2424:         lastAt: now
2425:       };
2426: 
2427:       const forceNow = Number(best.km) <= LIVE_FORCE_KM;
2428: 
2429:       /*
2430:         GPS tek sefer saparsa durak değiştirmesin.
2431:         Aynı aday 2 kez görülürse canlı yap.
2432:         Çok yakına girdiyse beklemeden canlı yap.
2433:       */
2434:       if(!forceNow && nextHits < LIVE_STABLE_HITS){
2435:         return;
2436:       }
2437: 
2438:       setLiveStop(best.stop);
2439:     }
2440: 
2441:   function initTabs(){
2442:     $$(".tab-btn").forEach(btn => {
2443:       btn.addEventListener("click", () => {
2444:         const tab = btn.dataset.tab;
2445:         $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn));
2446:         $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab));
2447:       });
2448:     });
2449:   }
2450: 
2451:   function openTab(name){
2452:     const btn = document.querySelector(`.tab-btn[data-tab="${name}"]`);
2453:     if(btn) btn.click();
2454:   }
2455: 
2456: 
2457: 
2458:   (function initSpeed(){
2459:     const spVal = $("#spVal");
2460:     const spLimit = $("#spLimit");
2461:     const speedBox = $("#speedBox");
2462:     const ttsBtn = $("#ttsToggle");
2463:     if(!spVal || !spLimit || !speedBox || !ttsBtn) return;
2464: 
2465:     const TTS_KEY = "ttsEnabled";
2466: 
2467:     function readTtsEnabled(){
2468:       try{
2469:         return (localStorage.getItem(TTS_KEY) ?? "1") === "1";
2470:       }catch(_){
2471:         return true;
2472:       }
2473:     }
2474: 
2475:     let ttsEnabled = readTtsEnabled();
2476: 
2477:     function syncTts(){
2478:       ttsEnabled = readTtsEnabled();
2479: 
2480:       ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted");
2481:       ttsBtn.title = ttsEnabled ? "Sesli uyarı açık" : "Sesli uyarı kapalı";
2482: 
2483:       if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){
2484:         window.SeatsVoice.syncButtons();
2485:       }
2486:     }
2487: 
2488:     syncTts();
2489: 
2490:     ttsBtn.addEventListener("click", () => {
2491:       const next = !readTtsEnabled();
2492: 
2493:       if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){
2494:         window.SeatsVoice.setEnabled(next);
2495:       }else{
2496:         localStorage.setItem(TTS_KEY, next ? "1" : "0");
2497:       }
2498: 
2499:       ttsEnabled = next;
2500:       syncTts();
2501: 
2502:       if(next){
2503:         if(window.SeatsSpeak){
2504:           window.SeatsSpeak("Sesli uyarı açık.", { force:true });
2505:         }else{
2506:           speakOnce("Sesli uyarı açık.");
2507:         }
2508:       }else{
2509:         if(window.SeatsStopVoice){
2510:           window.SeatsStopVoice();
```

### WEB seats.js satır 2790-2850
```js
2790:     renderAI();
2791:     renderTimeline();
2792:     updateCompactHeader();
2793:   });
2794: 
2795:   onChange("#alertStop", () => {
2796:     updateGeoHint();
2797:     refreshStopBadges();
2798:     updateStopSeatBadges();
2799:     renderAI();
2800:     renderTimeline();
2801:     updateCompactHeader();
2802: 
2803:     const a = getSelectedStopName() || "";
2804:     if(a && $("#cashModal")?.style.display === "block") setValue("#cashTo", a);
2805:     if(a && $("#bulkModal")?.style.display === "block") setValue("#bulkTo", a);
2806:   });
2807: 
2808:   window.addEventListener("keydown", (e) => {
2809:     if(e.key === "Escape"){
2810:       closeSeat();
2811:       closeBulk();
2812:       closeCash();
2813:       closeStandingModal();
2814:       closeModal("#approachBackdrop", "#approachModal");
2815:     }
2816:   });
2817: 
2818: 
2819:   const livePill = $("#routeMiniLive")?.closest(".route-pill");
2820:   if(livePill){
2821:     livePill.addEventListener("click", () => {
2822:       const live = getDisplayLiveStop();
2823:       if(!live){
2824:         toast("Canlı durak henüz yok");
2825:         return;
2826:       }
2827:       focusRouteStripStop(live, { select:true, voice:true });
2828:     });
2829:   }
2830: 
2831:   const nextPill = $("#routeMiniNext")?.closest(".route-pill");
2832:   if(nextPill){
2833:     nextPill.addEventListener("click", () => {
2834:       const live = getDisplayLiveStop();
2835:       const selected = getSelectedStopName();
2836:       const next = computeNextStopName(live || selected || "", "nextWithSeats") || selected;
2837:       if(!next){
2838:         toast("Sıradaki durak bulunamadı");
2839:         return;
2840:       }
2841:       focusRouteStripStop(next, { select:true, voice:true });
2842:     });
2843:   }
2844: 
2845: 
2846:   onClick("#btnDeckAI", startDeckAIVoice);
2847: 
2848:   (async function init(){
2849:     try{
2850:       initTabs();
```

### Fonksiyon gövdeleri
### WEB seats.js :: openModal
```js
1377:   function openModal(backdropSel, modalSel){
1378:     show($(backdropSel));
1379:     show($(modalSel));
1380:   }
```

### WEB seats.js :: closeModal
```js
1382:   function closeModal(backdropSel, modalSel){
1383:     hide($(backdropSel));
1384:     hide($(modalSel));
1385:   }
```

### WEB seats.js :: openSeat
```js
1387:   function openSeat(seatNo){
1388:     currentSeat = seatNo;
1389:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1390: 
1391:     const seatEl = $("#seat-" + seatNo);
1392:     if(seatEl) seatEl.classList.add("selected");
1393: 
1394:     setText("#seatTitle", "Koltuk " + seatNo);
1395:     setValue("#pickup", boardsMap[String(seatNo)] || getSelectedStopName() || "");
1396:     setValue("#dropoff", stopsMap[String(seatNo)] || "");
1397: 
1398:     const pay = document.querySelector('input[name="pay"][value="nakit"]');
1399:     if(pay) pay.checked = true;
1400: 
1401:     const ticket = document.querySelector('input[name="ticket"][value="biletsiz"]');
1402:     if(ticket) ticket.checked = true;
1403: 
1404:     setValue("#price", "0.00");
1405: 
1406:     const prevGender = genders[String(seatNo)] || "";
1407:     const gInput =
1408:       document.querySelector(`input[name="gender"][value="${prevGender}"]`) ||
1409:       document.querySelector('input[name="gender"][value=""]');
1410:     if(gInput) gInput.checked = true;
1411: 
1412:     if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)];
1413:     setValue("#service_note", serviceNotes[String(seatNo)] || "");
1414:     if($("#pairOk")) $("#pairOk").checked = false;
1415: 
1416:     openModal("#seatBackdrop", "#seatModal");
1417:   }
```

### WEB seats.js :: closeSeat
```js
1419:   function closeSeat(){
1420:     currentSeat = null;
1421:     closeModal("#seatBackdrop", "#seatModal");
1422:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1423:   }
```

### WEB seats.js :: saveSeat
```js
1425:   async function saveSeat(){
1426:     if(!currentSeat) return;
1427: 
1428:     const wasAlreadyAssigned = !!assigned[String(currentSeat)];
1429: 
1430:     const from = $("#pickup")?.value || getSelectedStopName() || "";
1431:     const stop = $("#dropoff")?.value || "";
1432:     const ticket = document.querySelector('input[name="ticket"]:checked')?.value || "biletsiz";
1433:     const payment = document.querySelector('input[name="pay"]:checked')?.value || "nakit";
1434:     const amount = parseMoney($("#price")?.value || 0);
1435:     const gender = document.querySelector('input[name="gender"]:checked')?.value || "";
1436:     const pair_ok = $("#pairOk")?.checked ? 1 : 0;
1437:     const service = $("#service")?.checked || false;
1438:     const service_note = $("#service_note")?.value || "";
1439: 
1440:     try{
1441:       const j = await safeJsonFetch("/api/seat", {
1442:         method:"POST",
1443:         headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1444:         body:JSON.stringify({
1445:           seat_no: currentSeat,
1446:           from,
1447:           stop,
1448:           ticket_type: ticket,
1449:           payment,
1450:           amount,
1451:           gender,
1452:           pair_ok,
1453:           service,
1454:           service_note
1455:         })
1456:       });
1457: 
1458:       if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");
1459: 
1460:       assigned[String(currentSeat)] = true;
1461:       stopsMap[String(currentSeat)] = stop;
1462:       genders[String(currentSeat)] = gender;
1463:       serviceMap[String(currentSeat)] = !!service;
1464:       serviceNotes[String(currentSeat)] = service_note;
1465:       boardsMap[String(currentSeat)] = from;
1466: 
1467:       if(!wasAlreadyAssigned && from){
1468:         recordStopFlowEvent(from, { board: 1 });
1469:       }
1470: 
1471:       persistBoards();
1472:       setSeatVisual(currentSeat);
1473:       closeSeat();
1474:       updateStats();
1475:       refreshStopBadges();
1476:       updateStopSeatBadges();
1477:       renderAI();
1478:       renderTimeline();
1479:       updateCompactHeader();
1480:       toast("Koltuk kaydedildi");
1481:     }catch(e){
1482:       toast(e.message || "Kaydetme hatası");
1483:     }
1484:   }
```

### WEB seats.js :: clearSeatUI
```js
1486:   function clearSeatUI(seatNo){
1487:     try{
1488:       if(typeof window.clearBiletsizSeatBadges === "function"){
1489:         window.clearBiletsizSeatBadges([seatNo]);
1490:       }
1491:     }catch(_){}
1492: 
1493:     delete assigned[String(seatNo)];
1494:     delete stopsMap[String(seatNo)];
1495:     delete genders[String(seatNo)];
1496:     delete serviceMap[String(seatNo)];
1497:     delete serviceNotes[String(seatNo)];
1498:     delete boardsMap[String(seatNo)];
1499: 
1500:     persistBoards();
1501:     setSeatVisual(seatNo);
1502: 
1503:     const el = $("#seat-" + seatNo);
1504:     if(el){
1505:       el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");
1506:       const cnt = el.querySelector(".bag-count");
1507:       const dir = el.querySelector(".bag-dir");
1508:       if(cnt) cnt.textContent = "0";
1509:       if(dir) dir.textContent = "";
1510:     }
1511:   }
```

### WEB seats.js :: offloadSeat
```js
1513:   async function offloadSeat(){
1514:     if(!currentSeat) return;
1515: 
1516:     const offStop = stopsMap[String(currentSeat)] || getSelectedStopName() || "";
1517: 
1518:     try{
1519:       const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, {
1520:         method:"DELETE",
1521:         headers:{ "X-CSRF-Token": csrf }
1522:       });
1523: 
1524:       if(!j.ok) throw new Error(j.msg || "Silme başarısız");
1525: 
1526:       if(offStop){
1527:         recordStopFlowEvent(offStop, { offload: 1 });
1528:       }
1529: 
1530:       await clearBagsForSeat(currentSeat);
1531:       clearSeatUI(currentSeat);
1532:       closeSeat();
1533:       updateStats();
1534:       refreshStopBadges();
1535:       updateStopSeatBadges();
1536:       renderAI();
1537:       renderTimeline();
1538:       updateCompactHeader();
1539:       toast("Koltuk boşaltıldı");
1540:     }catch(e){
1541:       toast(e.message || "İniş hatası");
1542:     }
1543:   }
```

### WEB seats.js :: toggleSeatPick
```js
1552:   function toggleSeatPick(el){
1553:     if(el.classList.contains("isAssigned")) return;
1554: 
1555:     if(multiSelected.has(el)){
1556:       multiSelected.delete(el);
1557:       el.classList.remove("multi-picked");
1558:     }else{
1559:       multiSelected.add(el);
1560:       el.classList.add("multi-picked");
1561:     }
1562:   }
```

### WEB seats.js :: saveBulk
```js
1593:   async function saveBulk(){
1594:     const from = $("#bulkFrom")?.value || speedState.liveStop || getSelectedStopName() || "";
1595:     const to = $("#bulkTo")?.value || "";
1596:     const count = Math.max(1, parseInt($("#bulkCount")?.value || "1", 10));
1597:     const ticketVal = document.querySelector('input[name="bulkTicket"]:checked')?.value || "biletsiz";
1598:     const useService = $("#bulkService")?.checked || false;
1599: 
1600:     if(!to){
1601:       toast("Nereye seç");
1602:       return;
1603:     }
1604: 
1605:     const chosen = [...multiSelected].map(el => Number(el.dataset.seat));
1606:     let targets = [];
1607: 
1608:     if(multiMode){
1609:       if(!chosen.length){
1610:         toast("Önce koltukları seç.");
1611:         return;
1612:       }
1613:       targets = chosen;
1614:     }else{
1615:       const empties = [];
1616:       $$(".seat").forEach(el => {
1617:         const no = el.dataset.seat;
1618:         if(!assigned?.[no]) empties.push(Number(no));
1619:       });
1620: 
1621:       if(!empties.length){
1622:         toast("Boş koltuk yok");
1623:         return;
1624:       }
1625: 
1626:       targets = sampleRandom(empties, count);
1627:     }
1628: 
1629:     try{
1630:       let ok = false;
1631: 
1632:       try{
1633:         const j = await safeJsonFetch("/api/seats/bulk", {
1634:           method:"POST",
1635:           headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1636:           body:JSON.stringify({
1637:             seats: targets,
1638:             from,
1639:             stop: to,
1640:             ticket_type: ticketVal,
1641:             service: useService
1642:           })
1643:         });
1644:         ok = !!j.ok;
1645:       }catch(_){}
1646: 
1647:       if(!ok){
1648:         for(const n of targets){
1649:           await safeJsonFetch("/api/seat", {
1650:             method:"POST",
1651:             headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1652:             body:JSON.stringify({
1653:               seat_no:n,
1654:               from,
1655:               stop:to,
1656:               ticket_type:ticketVal,
1657:               payment:"nakit",
1658:               amount:0,
1659:               gender:"",
1660:               pair_ok:0,
1661:               service:useService,
1662:               service_note:""
1663:             })
1664:           });
1665:         }
1666:       }
1667: 
1668:       for(const n of targets){
1669:         assigned[String(n)] = true;
1670:         stopsMap[String(n)] = to;
1671:         boardsMap[String(n)] = from;
1672:         serviceMap[String(n)] = !!useService;
1673:         serviceNotes[String(n)] = "";
1674:         setSeatVisual(n);
1675:       }
1676: 
1677:       persistBoards();
1678:       clearMultiPicks();
1679:       multiMode = false;
1680:       if($("#multiPick")) $("#multiPick").checked = false;
1681:       closeBulk();
1682:       updateStats();
1683:       refreshStopBadges();
1684:       updateStopSeatBadges();
1685:       renderAI();
1686:       renderTimeline();
1687:       updateCompactHeader();
1688:       toast(`${targets.length} koltuk eklendi`);
1689:     }catch(e){
1690:       toast(e.message || "Toplu giriş hatası");
1691:     }
1692:   }
```

### WEB seats.js :: updateStats
```js
0971:   function updateStats(){
0972:     const totalSeats = Object.keys(seatPositions || {}).length;
0973:     const filled = Object.values(assigned || {}).filter(Boolean).length;
0974:     const empty = totalSeats - filled;
0975:     const occ = totalSeats ? Math.round((filled / totalSeats) * 100) : 0;
0976: 
0977:     setText("#pillTotal", String(filled + standingCount));
0978:     setText("#pillEmpty", String(empty));
0979:     setText("#voiceSeatFilled", String(filled));
0980:     setText("#voiceSeatEmpty", String(empty));
0981:     setText("#driveVoiceFilled", String(filled));
0982:     setText("#driveVoiceEmpty", String(empty));
0983:     setText("#pillStanding", String(standingCount));
0984:     setText("#pillCash", fmtTL(standingRevenue));
0985:     setText("#pillService", String(totalServiceCount()));
0986:     setText("#pillParcel", String(totalParcelCount()));
0987:     setText("#topOcc", occ + "%");
0988: 
0989:     const standingCard = $("#standingCard");
0990:     if(standingCard){
0991:       standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse");
0992:     }
0993: 
0994:     setText("#quickStandingMeta", `${standingCount} kişi · ${fmtTL(standingRevenue)}`);
0995:   }
```

### WEB seats.js :: setSeatVisual
```js
0942:   function setSeatVisual(seatNo){
0943:     const key = String(seatNo);
0944:     const el = $("#seat-" + seatNo);
0945:     if(!el) return;
0946: 
0947:     el.classList.remove("male","female","isAssigned","has-service");
0948: 
0949:     const isAssigned = !!assigned[key];
0950:     const gender = genders[key] || "";
0951: 
0952:     if(isAssigned) el.classList.add("isAssigned");
0953:     if(gender === "bay") el.classList.add("male");
0954:     if(gender === "bayan") el.classList.add("female");
0955:     if(serviceMap[key]) el.classList.add("has-service");
0956: 
0957:     const label = $("#label-" + seatNo);
0958:     if(label){
0959:         const from = boardsMap[key] || "";
0960:         const to = stopsMap[key] || "";
0961:         label.textContent = isAssigned ? (from ? `${from} → ${to}` : to) : "";
0962:       }
0963: 
0964:     const svc = el.querySelector(".svc-badge");
0965:     if(svc){
0966:       const note = (serviceNotes[key] || "").trim();
0967:       svc.title = note ? `Servis: ${note}` : "Servis";
0968:     }
0969:   }
```

### Kayıt akışı özet satırları
| Satır | İçerik |
| --- | --- |
| 192 | let currentSeat = null; |
| 553 | function hasPassengersFor(stopName){ |
| 942 | function setSeatVisual(seatNo){ |
| 971 | function updateStats(){ |
| 1261 | hasPassengersFor(nm) \|\| |
| 1387 | function openSeat(seatNo){ |
| 1388 | currentSeat = seatNo; |
| 1420 | currentSeat = null; |
| 1425 | async function saveSeat(){ |
| 1426 | if(!currentSeat) return; |
| 1428 | const wasAlreadyAssigned = !!assigned[String(currentSeat)]; |
| 1445 | seat_no: currentSeat, |
| 1460 | assigned[String(currentSeat)] = true; |
| 1461 | stopsMap[String(currentSeat)] = stop; |
| 1462 | genders[String(currentSeat)] = gender; |
| 1463 | serviceMap[String(currentSeat)] = !!service; |
| 1464 | serviceNotes[String(currentSeat)] = service_note; |
| 1465 | boardsMap[String(currentSeat)] = from; |
| 1472 | setSeatVisual(currentSeat); |
| 1474 | updateStats(); |
| 1501 | setSeatVisual(seatNo); |
| 1514 | if(!currentSeat) return; |
| 1516 | const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| ""; |
| 1519 | const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, { |
| 1530 | await clearBagsForSeat(currentSeat); |
| 1531 | clearSeatUI(currentSeat); |
| 1533 | updateStats(); |
| 1674 | setSeatVisual(n); |
| 1682 | updateStats(); |
| 1812 | updateStats(); |
| 2188 | const selectedSeatCount = stop ? (seatCounts[stop] \|\| 0) : 0; |
| 2206 | const totalOps = selectedSeatCount + selectedStanding + selectedParcel; |
| 2211 | ? `${stop} için ${selectedSeatCount} koltuk, ${selectedStanding} ayakta, ${selectedParcel} emanet görünüyor.` |
| 2687 | openSeat(Number(seatEl.dataset.seat)); |
| 2700 | onClick("#btnSeatSave", saveSeat); |
| 2704 | const seat = currentSeat; |
| 2713 | const seat = currentSeat; |
| 2750 | updateStats(); |
| 2863 | setSeatVisual(seatNo); |
| 2870 | updateStats(); |

## ANDROID modals.html
- Yol: `android_app/app/src/main/python/templates/seats_parts/modals.html`
- Satır: `196`

### Kritik kelime satırları
| Satır | İçerik |
| --- | --- |
| 1 | <div class="modal-backdrop" id="seatBackdrop"></div> |
| 2 | <div class="modal glass" id="seatModal"> |
| 3 |   <h3 id="seatTitle">Koltuk</h3> |
| 18 |       <div class="muted" style="margin-bottom:8px">Bilet Türü</div> |
| 27 |       <div class="muted" style="margin-bottom:8px">Cinsiyet</div> |
| 41 |       <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button> |
| 42 |       <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button> |
| 48 |         <input type="number" id="price" value="0.00" step="0.01"> |
| 52 |         <input type="text" id="service_note" placeholder="Not / konum / açıklama"> |
| 57 |       <div class="muted" style="margin-bottom:8px">Ödeme</div> |
| 70 |     <button class="btn green" type="button" id="btnSeatSave">Kaydet</button> |
| 71 |     <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button> |
| 72 |     <button class="btn ghost" type="button" id="btnSeatClose">Kapat</button> |
| 100 |         <div class="radio-row" style="padding-top:8px"> |
| 116 |     <button class="btn ghost" type="button" id="bulkClose">Kapat</button> |
| 117 |     <button class="btn primary" type="button" id="bulkSave">Kaydet</button> |
| 165 |     <button class="btn ghost" type="button" id="cashClose">Kapat</button> |
| 166 |     <button class="btn primary" type="button" id="cashSave">Ekle</button> |
| 177 |     <button class="btn danger" type="button" id="approachOffload">Toplu İndir</button> |
| 178 |     <button class="btn ghost" type="button" id="approachSnooze">Ertele (5 dk)</button> |
| 179 |     <button class="btn ghost" type="button" id="approachClose">Kapat</button> |
| 187 |   <div class="standing-list" id="standingList" style="margin-top:12px;"></div> |
| 190 |     <button class="btn danger" type="button" id="standingBulkOff" style="display:none">Toplu İndir</button> |
| 191 |     <button class="btn ghost" type="button" id="standingClose">Kapat</button> |
| 195 | <div id="toast"></div> |

### ANDROID modals.html satır 1-120
```html
0001: <div class="modal-backdrop" id="seatBackdrop"></div>
0002: <div class="modal glass" id="seatModal">
0003:   <h3 id="seatTitle">Koltuk</h3>
0004: 
0005:   <div class="field-grid">
0006:     <div class="field-row">
0007:       <label class="field">
0008:         <span>Biniş Yeri</span>
0009:         <select id="pickup"><option value="">—</option></select>
0010:       </label>
0011:       <label class="field">
0012:         <span>İniş Yeri</span>
0013:         <select id="dropoff"><option value="">—</option></select>
0014:       </label>
0015:     </div>
0016: 
0017:     <div>
0018:       <div class="muted" style="margin-bottom:8px">Bilet Türü</div>
0019:       <div class="radio-row">
0020:         <label><input type="radio" name="ticket" value="biletli"> Biletli</label>
0021:         <label><input type="radio" name="ticket" value="biletsiz" checked> Biletsiz</label>
0022:         <label><input type="radio" name="ticket" value="ucretsiz"> Ücretsiz</label>
0023:       </div>
0024:     </div>
0025: 
0026:     <div>
0027:       <div class="muted" style="margin-bottom:8px">Cinsiyet</div>
0028:       <div class="radio-row">
0029:         <label><input type="radio" name="gender" value="bay"> Bay</label>
0030:         <label><input type="radio" name="gender" value="bayan"> Bayan</label>
0031:         <label><input type="radio" name="gender" value=""> Boş</label>
0032:       </div>
0033:     </div>
0034: 
0035:     <div class="check-row">
0036:       <label><input type="checkbox" id="pairOk"> Yan yana istisna</label>
0037:       <label><input type="checkbox" id="service"> Servis kullanacak</label>
0038:     </div>
0039: 
0040:     <div class="action-grid">
0041:       <button class="btn primary" type="button" id="btnBagAdd">🧳 Bagaj Ekle</button>
0042:       <button class="btn dark" type="button" id="btnBagView">📸 Bagaj Gör</button>
0043:     </div>
0044: 
0045:     <div class="field-row">
0046:       <label class="field">
0047:         <span>Tutar (₺)</span>
0048:         <input type="number" id="price" value="0.00" step="0.01">
0049:       </label>
0050:       <label class="field">
0051:         <span>Servis Notu</span>
0052:         <input type="text" id="service_note" placeholder="Not / konum / açıklama">
0053:       </label>
0054:     </div>
0055: 
0056:     <div>
0057:       <div class="muted" style="margin-bottom:8px">Ödeme</div>
0058:       <div class="radio-row">
0059:         <label><input type="radio" name="pay" value="nakit" checked> Nakit</label>
0060:         <label><input type="radio" name="pay" value="iban"> IBAN</label>
0061:         <label><input type="radio" name="pay" value="online"> Online</label>
0062:         <label><input type="radio" name="pay" value="pos"> POS</label>
0063:         <label><input type="radio" name="pay" value="ucretsiz"> Ücretsiz</label>
0064:       </div>
0065:     </div>
0066: 
0067:   </div>
0068: 
0069:   <div class="modal-actions">
0070:     <button class="btn green" type="button" id="btnSeatSave">Kaydet</button>
0071:     <button class="btn danger" type="button" id="btnSeatOffload">İniş (Boşalt)</button>
0072:     <button class="btn ghost" type="button" id="btnSeatClose">Kapat</button>
0073:   </div>
0074: </div>
0075: 
0076: <div class="modal-backdrop" id="bulkBackdrop"></div>
0077: <div class="sheet-modal glass" id="bulkModal">
0078:   <h3>Toplu Giriş</h3>
0079: 
0080:   <div class="field-grid">
0081:     <div class="field-row">
0082:       <label class="field">
0083:         <span>Nereden</span>
0084:         <select id="bulkFrom"><option value="">—</option></select>
0085:       </label>
0086:       <label class="field">
0087:         <span>Nereye</span>
0088:         <select id="bulkTo"><option value="">—</option></select>
0089:       </label>
0090:     </div>
0091: 
0092:     <div class="field-row">
0093:       <label class="field">
0094:         <span>Adet</span>
0095:         <input type="number" id="bulkCount" min="1" value="1">
0096:       </label>
0097: 
0098:       <div class="field">
0099:         <span>Bilet</span>
0100:         <div class="radio-row" style="padding-top:8px">
0101:           <label><input type="radio" name="bulkTicket" value="biletsiz" checked> Biletsiz</label>
0102:           <label><input type="radio" name="bulkTicket" value="biletli"> Biletli</label>
0103:         </div>
0104:       </div>
0105:     </div>
0106: 
0107:     <div class="check-row">
0108:       <label><input type="checkbox" id="multiPick"> Çoklu seçim</label>
0109:       <label><input type="checkbox" id="bulkService"> Servis</label>
0110:     </div>
0111: 
0112:     <div class="muted">Çoklu seçim açıksa koltukları elle seçersin. Kapalıysa sistem boş koltuklardan yerleştirir.</div>
0113:   </div>
0114: 
0115:   <div class="modal-actions">
0116:     <button class="btn ghost" type="button" id="bulkClose">Kapat</button>
0117:     <button class="btn primary" type="button" id="bulkSave">Kaydet</button>
0118:   </div>
0119: </div>
0120:
```

## ANDROID seats.js
- Yol: `android_app/app/src/main/python/static/seats/seats.js`
- Satır: `2960`

### Kritik kelime satırları
| Satır | İçerik |
| --- | --- |
| 12 | const stopsMap = BOOT.stopsMap \|\| {}; |
| 17 | const serverStops = BOOT.serverStops \|\| []; |
| 24 | (function hardCleanOldStopFlowOnce(){ |
| 28 |     const key = "hardCleanStopFlowOnce:" + TRIP_KEY; |
| 31 |     if(localStorage.getItem(key) === version) return; |
| 34 |       "stopFlowSummary:" + TRIP_KEY, |
| 35 |       "passedStops:" + TRIP_KEY, |
| 36 |       "liveStop:" + TRIP_KEY, |
| 37 |       "continueTripStop:" + TRIP_KEY, |
| 38 |       "continueTripStop:last" |
| 39 |     ].forEach(k => localStorage.removeItem(k)); |
| 41 |     localStorage.setItem(key, version); |
| 52 |       { stop: "Denizli otogar", time: "20:00" }, |
| 53 |       { stop: "Alaşehir Otogar", time: "23:10" }, |
| 54 |       { stop: "Salihli Garaj", time: "23:50" }, |
| 55 |       { stop: "Turgutlu Garaj", time: "00:25" }, |
| 56 |       { stop: "Manisa Otogar", time: "01:05" }, |
| 57 |       { stop: "Balıkesir", time: "03:10" }, |
| 58 |       { stop: "Bursa Otogar", time: "04:30" }, |
| 59 |       { stop: "Harem", time: "07:30" }, |
| 60 |       { stop: "Esenler Otogar", time: "08:00" } |
| 63 |       { stop: "Esenler Otogar", time: "20:00" }, |
| 64 |       { stop: "Harem", time: "20:35" }, |
| 65 |       { stop: "Bursa Otogar", time: "23:15" }, |
| 66 |       { stop: "Balıkesir", time: "00:35" }, |
| 67 |       { stop: "Manisa Otogar", time: "02:40" }, |
| 68 |       { stop: "Turgutlu Garaj", time: "03:15" }, |
| 69 |       { stop: "Salihli Garaj", time: "03:55" }, |
| 70 |       { stop: "Alaşehir Otogar", time: "04:40" }, |
| 71 |       { stop: "Denizli otogar", time: "07:20" } |
| 74 |       { stop: "Denizli otogar", time: "20:00" }, |
| 75 |       { stop: "Alaşehir Otogar", time: "22:10" }, |
| 76 |       { stop: "Salihli Garaj", time: "22:50" }, |
| 77 |       { stop: "Turgutlu Garaj", time: "23:25" }, |
| 78 |       { stop: "Manisa Otogar", time: "00:00" }, |
| 79 |       { stop: "İzmir Otogar", time: "01:10" } |
| 82 |       { stop: "İzmir Otogar", time: "20:00" }, |
| 83 |       { stop: "Manisa Otogar", time: "21:00" }, |
| 84 |       { stop: "Turgutlu Garaj", time: "21:35" }, |
| 85 |       { stop: "Salihli Garaj", time: "22:10" }, |
| 86 |       { stop: "Alaşehir Otogar", time: "22:50" }, |
| 87 |       { stop: "Denizli otogar", time: "01:00" } |
| 90 |   const $ = (s) => document.querySelector(s); |
| 91 |   const $$ = (s) => Array.from(document.querySelectorAll(s)); |
| 95 |     if(el) el.addEventListener("click", fn); |
| 100 |     if(el) el.addEventListener("change", fn); |
| 139 |     const memorySchemaVersion = "v2-stop-flow-clean-20260512"; |
| 141 |     const oldTripId = localStorage.getItem(activeTripMemoryKey) \|\| ""; |
| 142 |     const oldSchema = localStorage.getItem(memorySchemaKey) \|\| ""; |
| 155 |       "liveStop:", |
| 156 |       "passedStops:", |
| 160 |       "continueTripStop:", |
| 161 |       "stopFlowSummary:" |
| 165 |       localStorage.removeItem(prefix + TRIP_KEY); |
| 168 |     localStorage.removeItem("continueTripStop:last"); |
| 170 |     Object.keys(localStorage).forEach(k => { |
| 175 |         localStorage.removeItem(k); |
| 179 |     localStorage.setItem(activeTripMemoryKey, currentTripId); |
| 180 |     localStorage.setItem(memorySchemaKey, memorySchemaVersion); |
| 188 |     JSON.parse(localStorage.getItem("boardsMap:" + TRIP_KEY) \|\| "{}") |
| 191 |   let cachedStops = null; |
| 192 |   let currentSeat = null; |
| 202 |   let lastApproach = { stop:null, seats:[] }; |
| 204 |   let lastApproachVoiceStop = ""; |
| 205 |   let lastRouteStripCenteredStop = ""; |
| 212 |     history: [], |
| 218 |     liveStop: "", |
| 219 |     passedStops: new Set(), |
| 223 |   function toast(msg, ms=2400){ |
| 224 |     const t = $("#toast"); |
| 228 |     clearTimeout(toast._timer); |
| 229 |     toast._timer = setTimeout(() => { |
| 235 |     return "₺" + Number(v \|\| 0).toFixed(2); |
| 251 |       .toString() |
| 255 |       .toLowerCase(); |
| 273 |   function persistBoards(){ |
| 274 |     localStorage.setItem("boardsMap:" + TRIP_KEY, JSON.stringify(boardsMap \|\| {})); |
| 277 |   function persistVoiceState(){ |
| 278 |     localStorage.setItem("liveStop:" + TRIP_KEY, speedState.liveStop \|\| ""); |
| 279 |     localStorage.setItem("passedStops:" + TRIP_KEY, JSON.stringify([...speedState.passedStops])); |
| 283 |     speedState.liveStop = localStorage.getItem("liveStop:" + TRIP_KEY) \|\| ""; |
| 285 |       speedState.passedStops = new Set(JSON.parse(localStorage.getItem("passedStops:" + TRIP_KEY) \|\| "[]")); |
| 287 |       speedState.passedStops = new Set(); |
| 291 |   function persistStandingTotals(){ |
| 292 |     localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({ |
| 298 |   function persistStandingItems(){ |
| 299 |     localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| [])); |
| 311 |   function allStopsList(){ |
| 312 |     if(Array.isArray(cachedStops) && cachedStops.length) return cachedStops.map(x => x.name); |
| 313 |     return Array.isArray(serverStops) ? serverStops.slice() : []; |
| 316 |   function indexOfStopByName(name){ |
| 317 |     const list = allStopsList(); |
| 322 |   function findStopByName(name){ |
| 324 |     const list = Array.isArray(cachedStops) |
| 325 |       ? cachedStops |
| 326 |       : (Array.isArray(serverStops) ? serverStops.map(s => ({ name:s, lat:null, lng:null })) : []); |
| 330 |   function findCanonicalStopName(name){ |
| 331 |     const s = findStopByName(name); |
| 335 |   function hasCoord(stop){ |
| 336 |     if(!stop) return false; |
| 337 |     const lat = parseFloat(stop.lat); |
| 338 |     const lng = parseFloat(stop.lng); |
| 344 |     const toRad = d => d * Math.PI / 180; |
| 345 |     const dLat = toRad(b.lat - a.lat); |
| 346 |     const dLng = toRad(b.lng - a.lng); |
| 347 |     const la1 = toRad(a.lat); |
| 348 |     const la2 = toRad(b.lat); |
| 353 | function nearestStopByGps(maxKm = 15){ |
| 354 |   if(!currentCoords \|\| !Array.isArray(cachedStops)) return ""; |
| 358 |   for(const s of cachedStops){ |
| 382 | function getDisplayLiveStop(){ |
| 383 |   const live = speedState.liveStop \|\| ""; |
| 388 |     if(typeof hasLiveStopOperation === "function" && !hasLiveStopOperation(live)){ |
| 389 |       speedState.liveStop = ""; |
| 390 |       speedState.passedStops = new Set(); |
| 393 |         localStorage.removeItem("liveStop:" + TRIP_KEY); |
| 394 |         localStorage.removeItem("passedStops:" + TRIP_KEY); |
| 403 |     const km = stopDistanceKmByName(live); |
| 406 |       speedState.liveStop = ""; |
| 407 |       speedState.passedStops = new Set(); |
| 410 |         localStorage.removeItem("liveStop:" + TRIP_KEY); |
| 411 |         localStorage.removeItem("passedStops:" + TRIP_KEY); |
| 421 | function stopDistanceKmByName(name){ |
| 424 |   const stopObj = findStopByName(name); |
| 425 |   if(!stopObj \|\| !hasCoord(stopObj)) return NaN; |
| 428 |     lat: Number(stopObj.lat), |
| 429 |     lng: Number(stopObj.lng) |
| 434 |   const datePart = TRIP_DATE \|\| new Date().toISOString().slice(0,10); |
| 438 |   const firstTimedStop = Array.isArray(routeSchedule) |
| 442 |   const rawTime = firstTimedStop?.time \|\| TRIP_DEPARTURE_TIME \|\| "00:00"; |
| 466 |         stop: x.stop_name, |
| 508 |         stop:item.stop, |
| 520 |       stop: x.stop, |
| 524 |       routeIndex: indexOfStopByName(x.stop) |
| 534 |     return d.toLocaleTimeString("tr-TR", { hour:"2-digit", minute:"2-digit" }); |
| 545 |   function getSelectedStopName(){ |
| 546 |     return ($("#alertStop")?.value \|\| "").trim(); |
| 549 |   function isTimedStop(name){ |
| 550 |     return getRouteSchedule().some(x => norm(x.stop) === norm(name)); |
| 553 |   function hasPassengersFor(stopName){ |
| 554 |     return seatsForStop(stopName).length > 0; |
| 557 |   function isFinalStop(name){ |
| 558 |     const list = allStopsList(); |
| 559 |     const idx = indexOfStopByName(name); |
| 563 |   async function fetchStops(){ |
| 564 |     const j = await safeJsonFetch("/api/stops"); |
| 567 |     let stops = (j.stops \|\| []).map(name => ({ name, lat:null, lng:null })); |
| 572 |         const coordMap = new Map((c.items \|\| []).map(i => [i.stop, { lat:i.lat, lng:i.lng }])); |
| 573 |         stops = stops.map(s => coordMap.has(s.name) ? { ...s, ...coordMap.get(s.name) } : s); |
| 577 |     cachedStops = stops; |
| 578 |     return stops; |
| 581 |   async function populateStops(){ |
| 582 |     if(!cachedStops) await fetchStops(); |
| 584 |     const ids = ["alertStop","pickup","dropoff","bulkFrom","bulkTo","cashFrom","cashTo"]; |
| 597 |       for(const s of cachedStops){ |
| 600 |         o.dataset.label = s.name; |
| 611 |   function computeSeatCountsByStop(){ |
| 613 |     Object.values(stopsMap \|\| {}).forEach(stop => { |
| 614 |       if(stop) out[stop] = (out[stop] \|\| 0) + 1; |
| 619 |   function computeStandingCountsByStop(){ |
| 622 |       const raw = (it?.to \|\| "").trim(); |
| 624 |       const key = (findStopByName(raw)?.name \|\| raw).trim(); |
| 632 |   function computeParcelCountsByStop(){ |
| 635 |       const raw = (it?.to \|\| "").trim(); |
| 637 |       const key = (findStopByName(raw)?.name \|\| raw).trim(); |
| 646 |   const STOP_FLOW_SUMMARY_KEY = "stopFlowSummary:" + TRIP_KEY; |
| 647 |   const STOP_FLOW_EVENT_KEY = "stopFlowLiveEvents:" + TRIP_KEY; |
| 648 |   let stopFlowSummary = {}; |
| 650 |   function readStopFlowLiveEvents(){ |
| 652 |       const raw = localStorage.getItem(STOP_FLOW_EVENT_KEY) \|\| "{}"; |
| 660 |   function writeStopFlowLiveEvents(obj){ |
| 662 |       localStorage.setItem(STOP_FLOW_EVENT_KEY, JSON.stringify(obj \|\| {})); |
| 666 |   function loadStopFlowSummary(){ |
| 668 |       const raw = localStorage.getItem(STOP_FLOW_SUMMARY_KEY) \|\| "{}"; |
| 670 |       stopFlowSummary = obj && typeof obj === "object" ? obj : {}; |
| 672 |       stopFlowSummary = {}; |
| 677 |   function clearStaleStopFlowIfTripEmpty(){ |
| 685 |         "stopFlowSummary:" + TRIP_KEY, |
| 686 |         "liveStop:" + TRIP_KEY, |
| 687 |         "passedStops:" + TRIP_KEY, |
| 691 |         "continueTripStop:" + TRIP_KEY, |
| 692 |         "continueTripStop:last" |
| 695 |       keys.forEach(k => localStorage.removeItem(k)); |
| 697 |       stopFlowSummary = {}; |
| 700 |         speedState.liveStop = ""; |
| 701 |         speedState.passedStops = new Set(); |
| 704 |       if(typeof renderTimeline === "function") renderTimeline(); |
| 706 |       if(typeof renderAI === "function") renderAI(); |
| 711 |   setTimeout(clearStaleStopFlowIfTripEmpty, 0); |
| 713 |   function persistStopFlowSummary(){ |
| 715 |       localStorage.setItem(STOP_FLOW_SUMMARY_KEY, JSON.stringify(stopFlowSummary \|\| {})); |
| 719 |   function stopSummaryKey(stopName){ |
| 720 |     return (findCanonicalStopName(stopName) \|\| String(stopName \|\| "")).trim(); |
| 723 |   function boardCountForStop(stopName){ |
| 724 |     const key = norm(stopName); |
| 727 |     let total = 0; |
| 729 |     Object.keys(assigned \|\| {}).forEach(seatNo => { |
| 730 |       if(!assigned[seatNo]) return; |
| 731 |       if(norm(boardsMap[String(seatNo)] \|\| "") === key){ |
| 732 |         total += 1; |

### ANDROID seats.js satır 70-125
```js
0070:       { stop: "Alaşehir Otogar", time: "04:40" },
0071:       { stop: "Denizli otogar", time: "07:20" }
0072:     ],
0073:     "Denizli – İzmir": [
0074:       { stop: "Denizli otogar", time: "20:00" },
0075:       { stop: "Alaşehir Otogar", time: "22:10" },
0076:       { stop: "Salihli Garaj", time: "22:50" },
0077:       { stop: "Turgutlu Garaj", time: "23:25" },
0078:       { stop: "Manisa Otogar", time: "00:00" },
0079:       { stop: "İzmir Otogar", time: "01:10" }
0080:     ],
0081:     "İzmir – Denizli": [
0082:       { stop: "İzmir Otogar", time: "20:00" },
0083:       { stop: "Manisa Otogar", time: "21:00" },
0084:       { stop: "Turgutlu Garaj", time: "21:35" },
0085:       { stop: "Salihli Garaj", time: "22:10" },
0086:       { stop: "Alaşehir Otogar", time: "22:50" },
0087:       { stop: "Denizli otogar", time: "01:00" }
0088:     ]
0089:   };
0090:   const $ = (s) => document.querySelector(s);
0091:   const $$ = (s) => Array.from(document.querySelectorAll(s));
0092: 
0093:   function onClick(sel, fn){
0094:     const el = $(sel);
0095:     if(el) el.addEventListener("click", fn);
0096:   }
0097: 
0098:   function onChange(sel, fn){
0099:     const el = $(sel);
0100:     if(el) el.addEventListener("change", fn);
0101:   }
0102: 
0103:   function setText(sel, val){
0104:     const el = $(sel);
0105:     if(el) el.textContent = val;
0106:   }
0107: 
0108:   function setValue(sel, val){
0109:     const el = $(sel);
0110:     if(el) el.value = val;
0111:   }
0112: 
0113:   function show(el){
0114:     if(el) el.style.display = "block";
0115:   }
0116: 
0117:   function hide(el){
0118:     if(el) el.style.display = "none";
0119:   }
0120: 
0121:   
0122: /* =========================================================
0123:    TRIP MEMORY GUARD
0124:    Aynı rota/plaka ile yeni sefer açılınca eski canlı durak,
0125:    geçildi bilgisi ve durak akışı özeti taşınmasın.
```

### ANDROID seats.js satır 1160-1210
```js
1160:     const item = document.createElement("button");
1161:     item.type = "button";
1162:     item.dataset.stop = stop;
1163:     item.className = `route-stop ${isActive || isLive ? "active" : ""} ${isDone ? "done has-flow-summary" : ""} ${liveDangerOn && isLive ? "live-danger" : ""} ${isNextWarn ? "next-warning" : ""} ${isFlowGreen ? "flow-green" : ""}`;
1164:     if(isLive){routeFocusItem = item;}   
1165: 
1166:     const etaItem = etaMap.get(norm(stop));
1167:     const planText = plan || "—";
1168:     const etaText = etaItem && plan ? fmtHour(etaItem.etaDate) : "";
1169:     const delayText = etaItem && plan ? etaItem.badgeText : "";
1170:     const kmValue = kmText || (etaItem && Number.isFinite(etaItem.km) ? `${etaItem.km.toFixed(1)} km` : "—");
1171: 
1172:     const timeText = etaText ? `${planText} → ${etaText}` : planText;
1173:     const statusText = delayText ? `${kmValue} · ${delayText}` : kmValue;
1174: 
1175:     item.innerHTML = `
1176:   <div class="name">${stop}</div>
1177:   <div class="meta ${isDone ? "done-summary" : ""}">${metaLine1} · ${metaLine2}</div>
1178:   <div class="extra">
1179:     <div class="extra-line">
1180:       <span class="extra-k">Plan/ETA</span>
1181:       <span class="extra-v">${timeText}</span>
1182:     </div>
1183:     <div class="extra-line">
1184:       <span class="extra-k">Durum</span>
1185:       <span class="extra-v">${statusText}</span>
1186:     </div>
1187:   </div>
1188:    `;
1189: 
1190: item.addEventListener("click", () => {
1191:   setSelectedStop(stop, { silent:false, voiceReply:true });
1192: 
1193:   // APK/WebView için ek garanti: durak kartı tıklamasında doğrudan TTS tetikle
1194:   try{
1195:     const msg = stopHumanVoiceSummary(stop);
1196:     if(typeof speakOnce === "function") speakOnce(msg);
1197:   }catch(_){}
1198: });
1199: 
1200: wrap.appendChild(item);
1201: });
1202: 
1203: if(routeFocusItem && live){
1204:   const focusKey = norm(live);
1205: 
1206:   if(lastRouteStripCenteredStop !== focusKey){
1207:     lastRouteStripCenteredStop = focusKey;
1208: 
1209:     requestAnimationFrame(() => {
1210:       setTimeout(() => {
```

### ANDROID seats.js satır 1360-1475
```js
1360:     if(!h) return;
1361: 
1362:     const stopName = getSelectedStopName();
1363: 
1364:     if(geoWatchId){
1365:       return;
1366:     }
1367: 
1368:     if(!stopName){
1369:       h.textContent = "Durak seç.";
1370:       return;
1371:     }
1372: 
1373:     const s = findStopByName(stopName);
1374:     h.textContent = hasCoord(s) ? "Koordinat hazır." : "Koordinat yok. Aşağıdan ekleyin.";
1375:   }
1376: 
1377:   function openModal(backdropSel, modalSel){
1378:     show($(backdropSel));
1379:     show($(modalSel));
1380:   }
1381: 
1382:   function closeModal(backdropSel, modalSel){
1383:     hide($(backdropSel));
1384:     hide($(modalSel));
1385:   }
1386: 
1387:   function openSeat(seatNo){
1388:     currentSeat = seatNo;
1389:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1390: 
1391:     const seatEl = $("#seat-" + seatNo);
1392:     if(seatEl) seatEl.classList.add("selected");
1393: 
1394:     setText("#seatTitle", "Koltuk " + seatNo);
1395:     setValue("#pickup", boardsMap[String(seatNo)] || getSelectedStopName() || "");
1396:     setValue("#dropoff", stopsMap[String(seatNo)] || "");
1397: 
1398:     const pay = document.querySelector('input[name="pay"][value="nakit"]');
1399:     if(pay) pay.checked = true;
1400: 
1401:     const ticket = document.querySelector('input[name="ticket"][value="biletsiz"]');
1402:     if(ticket) ticket.checked = true;
1403: 
1404:     setValue("#price", "0.00");
1405: 
1406:     const prevGender = genders[String(seatNo)] || "";
1407:     const gInput =
1408:       document.querySelector(`input[name="gender"][value="${prevGender}"]`) ||
1409:       document.querySelector('input[name="gender"][value=""]');
1410:     if(gInput) gInput.checked = true;
1411: 
1412:     if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)];
1413:     setValue("#service_note", serviceNotes[String(seatNo)] || "");
1414:     if($("#pairOk")) $("#pairOk").checked = false;
1415: 
1416:     openModal("#seatBackdrop", "#seatModal");
1417:   }
1418: 
1419:   function closeSeat(){
1420:     currentSeat = null;
1421:     closeModal("#seatBackdrop", "#seatModal");
1422:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1423:   }
1424: 
1425:   async function saveSeat(){
1426:     if(!currentSeat) return;
1427: 
1428:     const wasAlreadyAssigned = !!assigned[String(currentSeat)];
1429: 
1430:     const from = $("#pickup")?.value || getSelectedStopName() || "";
1431:     const stop = $("#dropoff")?.value || "";
1432:     const ticket = document.querySelector('input[name="ticket"]:checked')?.value || "biletsiz";
1433:     const payment = document.querySelector('input[name="pay"]:checked')?.value || "nakit";
1434:     const amount = parseMoney($("#price")?.value || 0);
1435:     const gender = document.querySelector('input[name="gender"]:checked')?.value || "";
1436:     const pair_ok = $("#pairOk")?.checked ? 1 : 0;
1437:     const service = $("#service")?.checked || false;
1438:     const service_note = $("#service_note")?.value || "";
1439: 
1440:     try{
1441:       const j = await safeJsonFetch("/api/seat", {
1442:         method:"POST",
1443:         headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1444:         body:JSON.stringify({
1445:           seat_no: currentSeat,
1446:           from,
1447:           stop,
1448:           ticket_type: ticket,
1449:           payment,
1450:           amount,
1451:           gender,
1452:           pair_ok,
1453:           service,
1454:           service_note
1455:         })
1456:       });
1457: 
1458:       if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");
1459: 
1460:       assigned[String(currentSeat)] = true;
1461:       stopsMap[String(currentSeat)] = stop;
1462:       genders[String(currentSeat)] = gender;
1463:       serviceMap[String(currentSeat)] = !!service;
1464:       serviceNotes[String(currentSeat)] = service_note;
1465:       boardsMap[String(currentSeat)] = from;
1466: 
1467:       if(!wasAlreadyAssigned && from){
1468:         recordStopFlowEvent(from, { board: 1 });
1469:       }
1470: 
1471:       persistBoards();
1472:       setSeatVisual(currentSeat);
1473:       closeSeat();
1474:       updateStats();
1475:       refreshStopBadges();
```

### ANDROID seats.js satır 1475-1545
```js
1475:       refreshStopBadges();
1476:       updateStopSeatBadges();
1477:       renderAI();
1478:       renderTimeline();
1479:       updateCompactHeader();
1480:       toast("Koltuk kaydedildi");
1481:     }catch(e){
1482:       toast(e.message || "Kaydetme hatası");
1483:     }
1484:   }
1485: 
1486:   function clearSeatUI(seatNo){
1487:     try{
1488:       if(typeof window.clearBiletsizSeatBadges === "function"){
1489:         window.clearBiletsizSeatBadges([seatNo]);
1490:       }
1491:     }catch(_){}
1492: 
1493:     delete assigned[String(seatNo)];
1494:     delete stopsMap[String(seatNo)];
1495:     delete genders[String(seatNo)];
1496:     delete serviceMap[String(seatNo)];
1497:     delete serviceNotes[String(seatNo)];
1498:     delete boardsMap[String(seatNo)];
1499: 
1500:     persistBoards();
1501:     setSeatVisual(seatNo);
1502: 
1503:     const el = $("#seat-" + seatNo);
1504:     if(el){
1505:       el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");
1506:       const cnt = el.querySelector(".bag-count");
1507:       const dir = el.querySelector(".bag-dir");
1508:       if(cnt) cnt.textContent = "0";
1509:       if(dir) dir.textContent = "";
1510:     }
1511:   }
1512: 
1513:   async function offloadSeat(){
1514:     if(!currentSeat) return;
1515: 
1516:     const offStop = stopsMap[String(currentSeat)] || getSelectedStopName() || "";
1517: 
1518:     try{
1519:       const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, {
1520:         method:"DELETE",
1521:         headers:{ "X-CSRF-Token": csrf }
1522:       });
1523: 
1524:       if(!j.ok) throw new Error(j.msg || "Silme başarısız");
1525: 
1526:       if(offStop){
1527:         recordStopFlowEvent(offStop, { offload: 1 });
1528:       }
1529: 
1530:       await clearBagsForSeat(currentSeat);
1531:       clearSeatUI(currentSeat);
1532:       closeSeat();
1533:       updateStats();
1534:       refreshStopBadges();
1535:       updateStopSeatBadges();
1536:       renderAI();
1537:       renderTimeline();
1538:       updateCompactHeader();
1539:       toast("Koltuk boşaltıldı");
1540:     }catch(e){
1541:       toast(e.message || "İniş hatası");
1542:     }
1543:   }
1544: 
1545:   function clearMultiPicks(){
```

### ANDROID seats.js satır 1545-1615
```js
1545:   function clearMultiPicks(){
1546:     for(const el of multiSelected){
1547:       el.classList.remove("multi-picked");
1548:     }
1549:     multiSelected.clear();
1550:   }
1551: 
1552:   function toggleSeatPick(el){
1553:     if(el.classList.contains("isAssigned")) return;
1554: 
1555:     if(multiSelected.has(el)){
1556:       multiSelected.delete(el);
1557:       el.classList.remove("multi-picked");
1558:     }else{
1559:       multiSelected.add(el);
1560:       el.classList.add("multi-picked");
1561:     }
1562:   }
1563: 
1564:   function setMultiMode(on){
1565:     multiMode = !!on;
1566:     const cb = $("#multiPick");
1567:     if(cb) cb.checked = multiMode;
1568: 
1569:     if(!multiMode){
1570:       clearMultiPicks();
1571:       toast("Çoklu seçim kapalı");
1572:     }else{
1573:       toast("Çoklu seçim açık. Koltukları seç.");
1574:     }
1575:   }
1576: 
1577:   function openBulk(){
1578:     populateStops().then(() => {
1579:       const selected = getSelectedStopName() || "";
1580:       const live = getDisplayLiveStop();
1581:       const fromDefault = live || selected || serverStops?.[0] || "";
1582:       if(selected) setValue("#bulkTo", selected);
1583:       if(fromDefault) setValue("#bulkFrom", fromDefault);
1584:       if($("#multiPick")) $("#multiPick").checked = !!multiMode;
1585:       openModal("#bulkBackdrop", "#bulkModal");
1586:     });
1587:   }
1588: 
1589:   function closeBulk(){
1590:     closeModal("#bulkBackdrop", "#bulkModal");
1591:   }
1592: 
1593:   async function saveBulk(){
1594:     const from = $("#bulkFrom")?.value || speedState.liveStop || getSelectedStopName() || "";
1595:     const to = $("#bulkTo")?.value || "";
1596:     const count = Math.max(1, parseInt($("#bulkCount")?.value || "1", 10));
1597:     const ticketVal = document.querySelector('input[name="bulkTicket"]:checked')?.value || "biletsiz";
1598:     const useService = $("#bulkService")?.checked || false;
1599: 
1600:     if(!to){
1601:       toast("Nereye seç");
1602:       return;
1603:     }
1604: 
1605:     const chosen = [...multiSelected].map(el => Number(el.dataset.seat));
1606:     let targets = [];
1607: 
1608:     if(multiMode){
1609:       if(!chosen.length){
1610:         toast("Önce koltukları seç.");
1611:         return;
1612:       }
1613:       targets = chosen;
1614:     }else{
1615:       const empties = [];
```

### ANDROID seats.js satır 2400-2510
```js
2400: 
2401:       const now = Date.now();
2402: 
2403:       if(currentLive && norm(currentLive) === norm(best.stop)){
2404:         liveDetectCandidate = {
2405:           name: best.stop,
2406:           hits: LIVE_STABLE_HITS,
2407:           lastAt: now
2408:         };
2409:         return;
2410:       }
2411: 
2412:       const sameCandidate =
2413:         liveDetectCandidate &&
2414:         norm(liveDetectCandidate.name || "") === norm(best.stop) &&
2415:         now - Number(liveDetectCandidate.lastAt || 0) < 15000;
2416: 
2417:       const nextHits = sameCandidate
2418:         ? Number(liveDetectCandidate.hits || 0) + 1
2419:         : 1;
2420: 
2421:       liveDetectCandidate = {
2422:         name: best.stop,
2423:         hits: nextHits,
2424:         lastAt: now
2425:       };
2426: 
2427:       const forceNow = Number(best.km) <= LIVE_FORCE_KM;
2428: 
2429:       /*
2430:         GPS tek sefer saparsa durak değiştirmesin.
2431:         Aynı aday 2 kez görülürse canlı yap.
2432:         Çok yakına girdiyse beklemeden canlı yap.
2433:       */
2434:       if(!forceNow && nextHits < LIVE_STABLE_HITS){
2435:         return;
2436:       }
2437: 
2438:       setLiveStop(best.stop);
2439:     }
2440: 
2441:   function initTabs(){
2442:     $$(".tab-btn").forEach(btn => {
2443:       btn.addEventListener("click", () => {
2444:         const tab = btn.dataset.tab;
2445:         $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn));
2446:         $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab));
2447:       });
2448:     });
2449:   }
2450: 
2451:   function openTab(name){
2452:     const btn = document.querySelector(`.tab-btn[data-tab="${name}"]`);
2453:     if(btn) btn.click();
2454:   }
2455: 
2456: 
2457: 
2458:   (function initSpeed(){
2459:     const spVal = $("#spVal");
2460:     const spLimit = $("#spLimit");
2461:     const speedBox = $("#speedBox");
2462:     const ttsBtn = $("#ttsToggle");
2463:     if(!spVal || !spLimit || !speedBox || !ttsBtn) return;
2464: 
2465:     const TTS_KEY = "ttsEnabled";
2466: 
2467:     function readTtsEnabled(){
2468:       try{
2469:         return (localStorage.getItem(TTS_KEY) ?? "1") === "1";
2470:       }catch(_){
2471:         return true;
2472:       }
2473:     }
2474: 
2475:     let ttsEnabled = readTtsEnabled();
2476: 
2477:     function syncTts(){
2478:       ttsEnabled = readTtsEnabled();
2479: 
2480:       ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted");
2481:       ttsBtn.title = ttsEnabled ? "Sesli uyarı açık" : "Sesli uyarı kapalı";
2482: 
2483:       if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){
2484:         window.SeatsVoice.syncButtons();
2485:       }
2486:     }
2487: 
2488:     syncTts();
2489: 
2490:     ttsBtn.addEventListener("click", () => {
2491:       const next = !readTtsEnabled();
2492: 
2493:       if(window.SeatsVoice && typeof window.SeatsVoice.setEnabled === "function"){
2494:         window.SeatsVoice.setEnabled(next);
2495:       }else{
2496:         localStorage.setItem(TTS_KEY, next ? "1" : "0");
2497:       }
2498: 
2499:       ttsEnabled = next;
2500:       syncTts();
2501: 
2502:       if(next){
2503:         if(window.SeatsSpeak){
2504:           window.SeatsSpeak("Sesli uyarı açık.", { force:true });
2505:         }else{
2506:           speakOnce("Sesli uyarı açık.");
2507:         }
2508:       }else{
2509:         if(window.SeatsStopVoice){
2510:           window.SeatsStopVoice();
```

### ANDROID seats.js satır 2790-2850
```js
2790:     renderAI();
2791:     renderTimeline();
2792:     updateCompactHeader();
2793:   });
2794: 
2795:   onChange("#alertStop", () => {
2796:     updateGeoHint();
2797:     refreshStopBadges();
2798:     updateStopSeatBadges();
2799:     renderAI();
2800:     renderTimeline();
2801:     updateCompactHeader();
2802: 
2803:     const a = getSelectedStopName() || "";
2804:     if(a && $("#cashModal")?.style.display === "block") setValue("#cashTo", a);
2805:     if(a && $("#bulkModal")?.style.display === "block") setValue("#bulkTo", a);
2806:   });
2807: 
2808:   window.addEventListener("keydown", (e) => {
2809:     if(e.key === "Escape"){
2810:       closeSeat();
2811:       closeBulk();
2812:       closeCash();
2813:       closeStandingModal();
2814:       closeModal("#approachBackdrop", "#approachModal");
2815:     }
2816:   });
2817: 
2818: 
2819:   const livePill = $("#routeMiniLive")?.closest(".route-pill");
2820:   if(livePill){
2821:     livePill.addEventListener("click", () => {
2822:       const live = getDisplayLiveStop();
2823:       if(!live){
2824:         toast("Canlı durak henüz yok");
2825:         return;
2826:       }
2827:       focusRouteStripStop(live, { select:true, voice:true });
2828:     });
2829:   }
2830: 
2831:   const nextPill = $("#routeMiniNext")?.closest(".route-pill");
2832:   if(nextPill){
2833:     nextPill.addEventListener("click", () => {
2834:       const live = getDisplayLiveStop();
2835:       const selected = getSelectedStopName();
2836:       const next = computeNextStopName(live || selected || "", "nextWithSeats") || selected;
2837:       if(!next){
2838:         toast("Sıradaki durak bulunamadı");
2839:         return;
2840:       }
2841:       focusRouteStripStop(next, { select:true, voice:true });
2842:     });
2843:   }
2844: 
2845: 
2846:   onClick("#btnDeckAI", startDeckAIVoice);
2847: 
2848:   (async function init(){
2849:     try{
2850:       initTabs();
```

### Fonksiyon gövdeleri
### ANDROID seats.js :: openModal
```js
1377:   function openModal(backdropSel, modalSel){
1378:     show($(backdropSel));
1379:     show($(modalSel));
1380:   }
```

### ANDROID seats.js :: closeModal
```js
1382:   function closeModal(backdropSel, modalSel){
1383:     hide($(backdropSel));
1384:     hide($(modalSel));
1385:   }
```

### ANDROID seats.js :: openSeat
```js
1387:   function openSeat(seatNo){
1388:     currentSeat = seatNo;
1389:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1390: 
1391:     const seatEl = $("#seat-" + seatNo);
1392:     if(seatEl) seatEl.classList.add("selected");
1393: 
1394:     setText("#seatTitle", "Koltuk " + seatNo);
1395:     setValue("#pickup", boardsMap[String(seatNo)] || getSelectedStopName() || "");
1396:     setValue("#dropoff", stopsMap[String(seatNo)] || "");
1397: 
1398:     const pay = document.querySelector('input[name="pay"][value="nakit"]');
1399:     if(pay) pay.checked = true;
1400: 
1401:     const ticket = document.querySelector('input[name="ticket"][value="biletsiz"]');
1402:     if(ticket) ticket.checked = true;
1403: 
1404:     setValue("#price", "0.00");
1405: 
1406:     const prevGender = genders[String(seatNo)] || "";
1407:     const gInput =
1408:       document.querySelector(`input[name="gender"][value="${prevGender}"]`) ||
1409:       document.querySelector('input[name="gender"][value=""]');
1410:     if(gInput) gInput.checked = true;
1411: 
1412:     if($("#service")) $("#service").checked = !!serviceMap[String(seatNo)];
1413:     setValue("#service_note", serviceNotes[String(seatNo)] || "");
1414:     if($("#pairOk")) $("#pairOk").checked = false;
1415: 
1416:     openModal("#seatBackdrop", "#seatModal");
1417:   }
```

### ANDROID seats.js :: closeSeat
```js
1419:   function closeSeat(){
1420:     currentSeat = null;
1421:     closeModal("#seatBackdrop", "#seatModal");
1422:     $$(".seat.selected").forEach(x => x.classList.remove("selected"));
1423:   }
```

### ANDROID seats.js :: saveSeat
```js
1425:   async function saveSeat(){
1426:     if(!currentSeat) return;
1427: 
1428:     const wasAlreadyAssigned = !!assigned[String(currentSeat)];
1429: 
1430:     const from = $("#pickup")?.value || getSelectedStopName() || "";
1431:     const stop = $("#dropoff")?.value || "";
1432:     const ticket = document.querySelector('input[name="ticket"]:checked')?.value || "biletsiz";
1433:     const payment = document.querySelector('input[name="pay"]:checked')?.value || "nakit";
1434:     const amount = parseMoney($("#price")?.value || 0);
1435:     const gender = document.querySelector('input[name="gender"]:checked')?.value || "";
1436:     const pair_ok = $("#pairOk")?.checked ? 1 : 0;
1437:     const service = $("#service")?.checked || false;
1438:     const service_note = $("#service_note")?.value || "";
1439: 
1440:     try{
1441:       const j = await safeJsonFetch("/api/seat", {
1442:         method:"POST",
1443:         headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1444:         body:JSON.stringify({
1445:           seat_no: currentSeat,
1446:           from,
1447:           stop,
1448:           ticket_type: ticket,
1449:           payment,
1450:           amount,
1451:           gender,
1452:           pair_ok,
1453:           service,
1454:           service_note
1455:         })
1456:       });
1457: 
1458:       if(!j.ok) throw new Error(j.msg || "Kayıt başarısız");
1459: 
1460:       assigned[String(currentSeat)] = true;
1461:       stopsMap[String(currentSeat)] = stop;
1462:       genders[String(currentSeat)] = gender;
1463:       serviceMap[String(currentSeat)] = !!service;
1464:       serviceNotes[String(currentSeat)] = service_note;
1465:       boardsMap[String(currentSeat)] = from;
1466: 
1467:       if(!wasAlreadyAssigned && from){
1468:         recordStopFlowEvent(from, { board: 1 });
1469:       }
1470: 
1471:       persistBoards();
1472:       setSeatVisual(currentSeat);
1473:       closeSeat();
1474:       updateStats();
1475:       refreshStopBadges();
1476:       updateStopSeatBadges();
1477:       renderAI();
1478:       renderTimeline();
1479:       updateCompactHeader();
1480:       toast("Koltuk kaydedildi");
1481:     }catch(e){
1482:       toast(e.message || "Kaydetme hatası");
1483:     }
1484:   }
```

### ANDROID seats.js :: clearSeatUI
```js
1486:   function clearSeatUI(seatNo){
1487:     try{
1488:       if(typeof window.clearBiletsizSeatBadges === "function"){
1489:         window.clearBiletsizSeatBadges([seatNo]);
1490:       }
1491:     }catch(_){}
1492: 
1493:     delete assigned[String(seatNo)];
1494:     delete stopsMap[String(seatNo)];
1495:     delete genders[String(seatNo)];
1496:     delete serviceMap[String(seatNo)];
1497:     delete serviceNotes[String(seatNo)];
1498:     delete boardsMap[String(seatNo)];
1499: 
1500:     persistBoards();
1501:     setSeatVisual(seatNo);
1502: 
1503:     const el = $("#seat-" + seatNo);
1504:     if(el){
1505:       el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");
1506:       const cnt = el.querySelector(".bag-count");
1507:       const dir = el.querySelector(".bag-dir");
1508:       if(cnt) cnt.textContent = "0";
1509:       if(dir) dir.textContent = "";
1510:     }
1511:   }
```

### ANDROID seats.js :: offloadSeat
```js
1513:   async function offloadSeat(){
1514:     if(!currentSeat) return;
1515: 
1516:     const offStop = stopsMap[String(currentSeat)] || getSelectedStopName() || "";
1517: 
1518:     try{
1519:       const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, {
1520:         method:"DELETE",
1521:         headers:{ "X-CSRF-Token": csrf }
1522:       });
1523: 
1524:       if(!j.ok) throw new Error(j.msg || "Silme başarısız");
1525: 
1526:       if(offStop){
1527:         recordStopFlowEvent(offStop, { offload: 1 });
1528:       }
1529: 
1530:       await clearBagsForSeat(currentSeat);
1531:       clearSeatUI(currentSeat);
1532:       closeSeat();
1533:       updateStats();
1534:       refreshStopBadges();
1535:       updateStopSeatBadges();
1536:       renderAI();
1537:       renderTimeline();
1538:       updateCompactHeader();
1539:       toast("Koltuk boşaltıldı");
1540:     }catch(e){
1541:       toast(e.message || "İniş hatası");
1542:     }
1543:   }
```

### ANDROID seats.js :: toggleSeatPick
```js
1552:   function toggleSeatPick(el){
1553:     if(el.classList.contains("isAssigned")) return;
1554: 
1555:     if(multiSelected.has(el)){
1556:       multiSelected.delete(el);
1557:       el.classList.remove("multi-picked");
1558:     }else{
1559:       multiSelected.add(el);
1560:       el.classList.add("multi-picked");
1561:     }
1562:   }
```

### ANDROID seats.js :: saveBulk
```js
1593:   async function saveBulk(){
1594:     const from = $("#bulkFrom")?.value || speedState.liveStop || getSelectedStopName() || "";
1595:     const to = $("#bulkTo")?.value || "";
1596:     const count = Math.max(1, parseInt($("#bulkCount")?.value || "1", 10));
1597:     const ticketVal = document.querySelector('input[name="bulkTicket"]:checked')?.value || "biletsiz";
1598:     const useService = $("#bulkService")?.checked || false;
1599: 
1600:     if(!to){
1601:       toast("Nereye seç");
1602:       return;
1603:     }
1604: 
1605:     const chosen = [...multiSelected].map(el => Number(el.dataset.seat));
1606:     let targets = [];
1607: 
1608:     if(multiMode){
1609:       if(!chosen.length){
1610:         toast("Önce koltukları seç.");
1611:         return;
1612:       }
1613:       targets = chosen;
1614:     }else{
1615:       const empties = [];
1616:       $$(".seat").forEach(el => {
1617:         const no = el.dataset.seat;
1618:         if(!assigned?.[no]) empties.push(Number(no));
1619:       });
1620: 
1621:       if(!empties.length){
1622:         toast("Boş koltuk yok");
1623:         return;
1624:       }
1625: 
1626:       targets = sampleRandom(empties, count);
1627:     }
1628: 
1629:     try{
1630:       let ok = false;
1631: 
1632:       try{
1633:         const j = await safeJsonFetch("/api/seats/bulk", {
1634:           method:"POST",
1635:           headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1636:           body:JSON.stringify({
1637:             seats: targets,
1638:             from,
1639:             stop: to,
1640:             ticket_type: ticketVal,
1641:             service: useService
1642:           })
1643:         });
1644:         ok = !!j.ok;
1645:       }catch(_){}
1646: 
1647:       if(!ok){
1648:         for(const n of targets){
1649:           await safeJsonFetch("/api/seat", {
1650:             method:"POST",
1651:             headers:{ "Content-Type":"application/json", "X-CSRF-Token":csrf },
1652:             body:JSON.stringify({
1653:               seat_no:n,
1654:               from,
1655:               stop:to,
1656:               ticket_type:ticketVal,
1657:               payment:"nakit",
1658:               amount:0,
1659:               gender:"",
1660:               pair_ok:0,
1661:               service:useService,
1662:               service_note:""
1663:             })
1664:           });
1665:         }
1666:       }
1667: 
1668:       for(const n of targets){
1669:         assigned[String(n)] = true;
1670:         stopsMap[String(n)] = to;
1671:         boardsMap[String(n)] = from;
1672:         serviceMap[String(n)] = !!useService;
1673:         serviceNotes[String(n)] = "";
1674:         setSeatVisual(n);
1675:       }
1676: 
1677:       persistBoards();
1678:       clearMultiPicks();
1679:       multiMode = false;
1680:       if($("#multiPick")) $("#multiPick").checked = false;
1681:       closeBulk();
1682:       updateStats();
1683:       refreshStopBadges();
1684:       updateStopSeatBadges();
1685:       renderAI();
1686:       renderTimeline();
1687:       updateCompactHeader();
1688:       toast(`${targets.length} koltuk eklendi`);
1689:     }catch(e){
1690:       toast(e.message || "Toplu giriş hatası");
1691:     }
1692:   }
```

### ANDROID seats.js :: updateStats
```js
0971:   function updateStats(){
0972:     const totalSeats = Object.keys(seatPositions || {}).length;
0973:     const filled = Object.values(assigned || {}).filter(Boolean).length;
0974:     const empty = totalSeats - filled;
0975:     const occ = totalSeats ? Math.round((filled / totalSeats) * 100) : 0;
0976: 
0977:     setText("#pillTotal", String(filled + standingCount));
0978:     setText("#pillEmpty", String(empty));
0979:     setText("#voiceSeatFilled", String(filled));
0980:     setText("#voiceSeatEmpty", String(empty));
0981:     setText("#driveVoiceFilled", String(filled));
0982:     setText("#driveVoiceEmpty", String(empty));
0983:     setText("#pillStanding", String(standingCount));
0984:     setText("#pillCash", fmtTL(standingRevenue));
0985:     setText("#pillService", String(totalServiceCount()));
0986:     setText("#pillParcel", String(totalParcelCount()));
0987:     setText("#topOcc", occ + "%");
0988: 
0989:     const standingCard = $("#standingCard");
0990:     if(standingCard){
0991:       standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse");
0992:     }
0993: 
0994:     setText("#quickStandingMeta", `${standingCount} kişi · ${fmtTL(standingRevenue)}`);
0995:   }
```

### ANDROID seats.js :: setSeatVisual
```js
0942:   function setSeatVisual(seatNo){
0943:     const key = String(seatNo);
0944:     const el = $("#seat-" + seatNo);
0945:     if(!el) return;
0946: 
0947:     el.classList.remove("male","female","isAssigned","has-service");
0948: 
0949:     const isAssigned = !!assigned[key];
0950:     const gender = genders[key] || "";
0951: 
0952:     if(isAssigned) el.classList.add("isAssigned");
0953:     if(gender === "bay") el.classList.add("male");
0954:     if(gender === "bayan") el.classList.add("female");
0955:     if(serviceMap[key]) el.classList.add("has-service");
0956: 
0957:     const label = $("#label-" + seatNo);
0958:     if(label){
0959:         const from = boardsMap[key] || "";
0960:         const to = stopsMap[key] || "";
0961:         label.textContent = isAssigned ? (from ? `${from} → ${to}` : to) : "";
0962:       }
0963: 
0964:     const svc = el.querySelector(".svc-badge");
0965:     if(svc){
0966:       const note = (serviceNotes[key] || "").trim();
0967:       svc.title = note ? `Servis: ${note}` : "Servis";
0968:     }
0969:   }
```

### Kayıt akışı özet satırları
| Satır | İçerik |
| --- | --- |
| 192 | let currentSeat = null; |
| 553 | function hasPassengersFor(stopName){ |
| 942 | function setSeatVisual(seatNo){ |
| 971 | function updateStats(){ |
| 1261 | hasPassengersFor(nm) \|\| |
| 1387 | function openSeat(seatNo){ |
| 1388 | currentSeat = seatNo; |
| 1420 | currentSeat = null; |
| 1425 | async function saveSeat(){ |
| 1426 | if(!currentSeat) return; |
| 1428 | const wasAlreadyAssigned = !!assigned[String(currentSeat)]; |
| 1445 | seat_no: currentSeat, |
| 1460 | assigned[String(currentSeat)] = true; |
| 1461 | stopsMap[String(currentSeat)] = stop; |
| 1462 | genders[String(currentSeat)] = gender; |
| 1463 | serviceMap[String(currentSeat)] = !!service; |
| 1464 | serviceNotes[String(currentSeat)] = service_note; |
| 1465 | boardsMap[String(currentSeat)] = from; |
| 1472 | setSeatVisual(currentSeat); |
| 1474 | updateStats(); |
| 1501 | setSeatVisual(seatNo); |
| 1514 | if(!currentSeat) return; |
| 1516 | const offStop = stopsMap[String(currentSeat)] \|\| getSelectedStopName() \|\| ""; |
| 1519 | const j = await safeJsonFetch("/api/seat?seat_no=" + currentSeat, { |
| 1530 | await clearBagsForSeat(currentSeat); |
| 1531 | clearSeatUI(currentSeat); |
| 1533 | updateStats(); |
| 1674 | setSeatVisual(n); |
| 1682 | updateStats(); |
| 1812 | updateStats(); |
| 2188 | const selectedSeatCount = stop ? (seatCounts[stop] \|\| 0) : 0; |
| 2206 | const totalOps = selectedSeatCount + selectedStanding + selectedParcel; |
| 2211 | ? `${stop} için ${selectedSeatCount} koltuk, ${selectedStanding} ayakta, ${selectedParcel} emanet görünüyor.` |
| 2687 | openSeat(Number(seatEl.dataset.seat)); |
| 2700 | onClick("#btnSeatSave", saveSeat); |
| 2704 | const seat = currentSeat; |
| 2713 | const seat = currentSeat; |
| 2750 | updateStats(); |
| 2863 | setSeatVisual(seatNo); |
| 2870 | updateStats(); |

## İlk Okuma Soruları

Bu raporda özellikle şunlara bakacağız:

1. `btnSeatSave` hangi satırda hangi fonksiyona bağlı?
2. `openSeat` seçili koltuğu hangi değişkende tutuyor?
3. `saveSeat` ilk satırlarında “koltuk yoksa çık” gibi erken return var mı?
4. Kaydet butonu tıklanınca buton disabled oluyor mu?
5. Kayıt yaptıktan sonra `closeSeat`, `render`, `updateStats`, `setSeatVisual` sırası doğru mu?
6. `manual-ticket-system.js` koltuk görseline ayrıca müdahale edip state’i geciktiriyor mu?
