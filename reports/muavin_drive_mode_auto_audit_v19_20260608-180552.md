# Muavin Drive Mode Otomatik Geri Dönme Audit V19

- Tarih: `20260608-180552`
- Bu rapor sadece tespittir. Dosya değiştirmez.

## 1) Drive Mode İzleri

### `templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `auto` | `<link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1">` |
| 28 | `driveMode` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 211 | `watch` | `                  <button class="btn primary" type="button" id="btnGeoWatch">KAPALI</button>` |
| 217 | `auto` | `                <label><input type="checkbox" id="autoAdvanceToggle" checked> Oto ilerle</label>` |
| 375 | `auto` | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 379 | `drive-mode` | `<style id="drive-mode-actions-independent-style">` |
| 381 | `Sürüş` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |
| 389 | `driveMode` | `#driveModeActionsDock{` |
| 410 | `driveMode` | `#driveModeActionsDock .dma-btn{` |
| 435 | `driveMode` | `#driveModeActionsDock .dma-btn.danger{` |
| 440 | `driveMode` | `#driveModeActionsDock .dma-btn:active{` |
| 445 | `driveMode` | `  #driveModeActionsDock{` |
| 453 | `driveMode` | `  #driveModeActionsDock .dma-btn{` |
| 464 | `drive-mode` | `<script id="drive-mode-actions-independent-js">` |
| 466 | `driveMode` | `  function isDriveMode(){` |
| 467 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 470 | `Normal` | `    // Sürüş modunda buton "Normal" oluyor` |
| 471 | `Normal` | `    if(txt.includes("normal")) return true;` |
| 485 | `driveMode` | `    let dock = document.getElementById("driveModeActionsDock");` |
| 489 | `driveMode` | `    dock.id = "driveModeActionsDock";` |
| 559 | `driveMode` | `    const active = isDriveMode();` |
| 567 | `Normal` | `       Normal HTML akışındaki yerinde sabit duracak. */` |
| 583 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 586 | `setTimeout` | `        setTimeout(placeDock, 50);` |
| 587 | `setTimeout` | `        setTimeout(placeDock, 250);` |
| 588 | `setTimeout` | `        setTimeout(placeDock, 700);` |
| 606 | `setTimeout` | `      setTimeout(placeDock, 300);` |
| 610 | `setInterval` | `    const t = setInterval(function(){` |
| 631 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI SABİTLEME` |
| 637 | `auto` | `  inset:auto !important;` |
| 638 | `auto` | `  left:auto !important;` |
| 639 | `auto` | `  right:auto !important;` |
| 640 | `auto` | `  top:auto !important;` |
| 641 | `auto` | `  bottom:auto !important;` |
| 667 | `auto` | `  left:auto !important;` |
| 668 | `auto` | `  right:auto !important;` |
| 669 | `auto` | `  top:auto !important;` |
| 670 | `auto` | `  bottom:auto !important;` |
| 676 | `Sürüş` | `/* Sürüş butonu */` |
| 677 | `driveMode` | `#driveModeToggle{` |
| 796 | `driveMode` | `  #driveModeToggle{` |
| 838 | `force` | `<!-- DRIVE MODE FORCE TOGGLE START -->` |
| 839 | `drive-mode` | `<script id="drive-mode-force-toggle-js">` |
| 841 | `driveMode` | `  if(window.__driveModeForceToggleReady) return;` |
| 842 | `driveMode` | `  window.__driveModeForceToggleReady = true;` |
| 847 | `driveMode` | `    return "driveMode:" + tripKey;` |
| 852 | `localStorage` | `      return localStorage.getItem(driveKey()) === "1";` |
| 860 | `localStorage` | `      localStorage.setItem(driveKey(), on ? "1" : "0");` |
| 863 | `drive-mode` | `    document.body.classList.toggle("drive-mode", !!on);` |
| 864 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 866 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 868 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 869 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 875 | `sync` | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 878 | `driveMode` | `      window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 882 | `sync` | `  function sync(){` |
| 888 | `driveMode` | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 899 | `sync` | `    document.addEventListener("DOMContentLoaded", sync);` |
| 901 | `sync` | `    sync();` |
| 904 | `setTimeout` | `  setTimeout(sync, 300);` |
| 907 | `force` | `<!-- DRIVE MODE FORCE TOGGLE END -->` |
| 912 | `sync` | `  function syncDriveVoiceStats(){` |
| 943 | `watch` | `  function watchNode(id){` |
| 947 | `sync` | `    new MutationObserver(syncDriveVoiceStats).observe(el, {` |
| 956 | `sync` | `    syncDriveVoiceStats();` |
| 957 | `watch` | `    watchNode("voiceSeatFilled");` |
| 958 | `watch` | `    watchNode("voiceSeatEmpty");` |
| 960 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 150);` |
| 961 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 600);` |
| 962 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 1400);` |
| 964 | `driveMode` | `    window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 965 | `sync` | `    window.addEventListener("resize", syncDriveVoiceStats);` |
| 990 | `localStorage` | `      localStorage.setItem("seatUiMode:" + tripKey, "advanced");` |
| 993 | `classList.remove` | `    document.documentElement.classList.remove("seat-simple-mode");` |
| 994 | `classList.remove` | `    document.body.classList.remove("seat-simple-mode");` |
| 1056 | `setTimeout` | `        setTimeout(function(){` |
| 1085 | `setTimeout` | `  setTimeout(boot, 500);` |

### `android_app/app/src/main/python/templates/seats.html`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 12 | `auto` | `<link rel="stylesheet" href="/static/seats/patches/modal-bottom-nav-autohide.css?v=1">` |
| 28 | `driveMode` | `          <button id="driveModeToggle" type="button" aria-label="Sürüş modu">🚘 Sürüş</button>` |
| 211 | `watch` | `                  <button class="btn primary" type="button" id="btnGeoWatch">KAPALI</button>` |
| 217 | `auto` | `                <label><input type="checkbox" id="autoAdvanceToggle" checked> Oto ilerle</label>` |
| 375 | `auto` | `<script src="/static/seats/patches/modal-bottom-nav-autohide.js?v=1"></script>` |
| 379 | `drive-mode` | `<style id="drive-mode-actions-independent-style">` |
| 381 | `Sürüş` | `   SÜRÜŞ MODU ÜST HIZLI MENÜ - BAĞIMSIZ FINAL` |
| 389 | `driveMode` | `#driveModeActionsDock{` |
| 410 | `driveMode` | `#driveModeActionsDock .dma-btn{` |
| 435 | `driveMode` | `#driveModeActionsDock .dma-btn.danger{` |
| 440 | `driveMode` | `#driveModeActionsDock .dma-btn:active{` |
| 445 | `driveMode` | `  #driveModeActionsDock{` |
| 453 | `driveMode` | `  #driveModeActionsDock .dma-btn{` |
| 464 | `drive-mode` | `<script id="drive-mode-actions-independent-js">` |
| 466 | `driveMode` | `  function isDriveMode(){` |
| 467 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 470 | `Normal` | `    // Sürüş modunda buton "Normal" oluyor` |
| 471 | `Normal` | `    if(txt.includes("normal")) return true;` |
| 485 | `driveMode` | `    let dock = document.getElementById("driveModeActionsDock");` |
| 489 | `driveMode` | `    dock.id = "driveModeActionsDock";` |
| 559 | `driveMode` | `    const active = isDriveMode();` |
| 567 | `Normal` | `       Normal HTML akışındaki yerinde sabit duracak. */` |
| 583 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 586 | `setTimeout` | `        setTimeout(placeDock, 50);` |
| 587 | `setTimeout` | `        setTimeout(placeDock, 250);` |
| 588 | `setTimeout` | `        setTimeout(placeDock, 700);` |
| 606 | `setTimeout` | `      setTimeout(placeDock, 300);` |
| 610 | `setInterval` | `    const t = setInterval(function(){` |
| 631 | `Sürüş` | `   SÜRÜŞ / HIZ / RÖTAR SATIRI SABİTLEME` |
| 637 | `auto` | `  inset:auto !important;` |
| 638 | `auto` | `  left:auto !important;` |
| 639 | `auto` | `  right:auto !important;` |
| 640 | `auto` | `  top:auto !important;` |
| 641 | `auto` | `  bottom:auto !important;` |
| 667 | `auto` | `  left:auto !important;` |
| 668 | `auto` | `  right:auto !important;` |
| 669 | `auto` | `  top:auto !important;` |
| 670 | `auto` | `  bottom:auto !important;` |
| 676 | `Sürüş` | `/* Sürüş butonu */` |
| 677 | `driveMode` | `#driveModeToggle{` |
| 796 | `driveMode` | `  #driveModeToggle{` |
| 838 | `force` | `<!-- DRIVE MODE FORCE TOGGLE START -->` |
| 839 | `drive-mode` | `<script id="drive-mode-force-toggle-js">` |
| 841 | `driveMode` | `  if(window.__driveModeForceToggleReady) return;` |
| 842 | `driveMode` | `  window.__driveModeForceToggleReady = true;` |
| 847 | `driveMode` | `    return "driveMode:" + tripKey;` |
| 852 | `localStorage` | `      return localStorage.getItem(driveKey()) === "1";` |
| 860 | `localStorage` | `      localStorage.setItem(driveKey(), on ? "1" : "0");` |
| 863 | `drive-mode` | `    document.body.classList.toggle("drive-mode", !!on);` |
| 864 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 866 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 868 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 869 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 875 | `sync` | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 878 | `driveMode` | `      window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 882 | `sync` | `  function sync(){` |
| 888 | `driveMode` | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 899 | `sync` | `    document.addEventListener("DOMContentLoaded", sync);` |
| 901 | `sync` | `    sync();` |
| 904 | `setTimeout` | `  setTimeout(sync, 300);` |
| 907 | `force` | `<!-- DRIVE MODE FORCE TOGGLE END -->` |
| 912 | `sync` | `  function syncDriveVoiceStats(){` |
| 943 | `watch` | `  function watchNode(id){` |
| 947 | `sync` | `    new MutationObserver(syncDriveVoiceStats).observe(el, {` |
| 956 | `sync` | `    syncDriveVoiceStats();` |
| 957 | `watch` | `    watchNode("voiceSeatFilled");` |
| 958 | `watch` | `    watchNode("voiceSeatEmpty");` |
| 960 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 150);` |
| 961 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 600);` |
| 962 | `setTimeout` | `    setTimeout(syncDriveVoiceStats, 1400);` |
| 964 | `driveMode` | `    window.addEventListener("driveModeChanged", syncDriveVoiceStats);` |
| 965 | `sync` | `    window.addEventListener("resize", syncDriveVoiceStats);` |
| 990 | `localStorage` | `      localStorage.setItem("seatUiMode:" + tripKey, "advanced");` |
| 993 | `classList.remove` | `    document.documentElement.classList.remove("seat-simple-mode");` |
| 994 | `classList.remove` | `    document.body.classList.remove("seat-simple-mode");` |
| 1056 | `setTimeout` | `        setTimeout(function(){` |
| 1085 | `setTimeout` | `  setTimeout(boot, 500);` |

### `static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 31 | `localStorage` | `    if(localStorage.getItem(key) === version) return;` |
| 39 | `localStorage` | `    ].forEach(k => localStorage.removeItem(k));` |
| 41 | `localStorage` | `    localStorage.setItem(key, version);` |
| 141 | `localStorage` | `    const oldTripId = localStorage.getItem(activeTripMemoryKey) \|\| "";` |
| 142 | `localStorage` | `    const oldSchema = localStorage.getItem(memorySchemaKey) \|\| "";` |
| 165 | `localStorage` | `      localStorage.removeItem(prefix + TRIP_KEY);` |
| 168 | `localStorage` | `    localStorage.removeItem("continueTripStop:last");` |
| 170 | `localStorage` | `    Object.keys(localStorage).forEach(k => {` |
| 175 | `localStorage` | `        localStorage.removeItem(k);` |
| 179 | `localStorage` | `    localStorage.setItem(activeTripMemoryKey, currentTripId);` |
| 180 | `localStorage` | `    localStorage.setItem(memorySchemaKey, memorySchemaVersion);` |
| 188 | `localStorage` | `    JSON.parse(localStorage.getItem("boardsMap:" + TRIP_KEY) \|\| "{}")` |
| 198 | `watch` | `  let geoWatchId = null;` |
| 199 | `watch` | `  let speedWatchId = null;` |
| 229 | `setTimeout` | `    toast._timer = setTimeout(() => {` |
| 252 | `Normal` | `      .normalize("NFKD")` |
| 263 | `sync` | `  async function safeJsonFetch(url, opt){` |
| 274 | `localStorage` | `    localStorage.setItem("boardsMap:" + TRIP_KEY, JSON.stringify(boardsMap \|\| {}));` |
| 278 | `localStorage` | `    localStorage.setItem("liveStop:" + TRIP_KEY, speedState.liveStop \|\| "");` |
| 279 | `localStorage` | `    localStorage.setItem("passedStops:" + TRIP_KEY, JSON.stringify([...speedState.passedStops]));` |
| 283 | `localStorage` | `    speedState.liveStop = localStorage.getItem("liveStop:" + TRIP_KEY) \|\| "";` |
| 285 | `localStorage` | `      speedState.passedStops = new Set(JSON.parse(localStorage.getItem("passedStops:" + TRIP_KEY) \|\| "[]"));` |
| 292 | `localStorage` | `    localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({` |
| 299 | `localStorage` | `    localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| []));` |
| 393 | `localStorage` | `        localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 394 | `localStorage` | `        localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 410 | `localStorage` | `        localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 411 | `localStorage` | `        localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 453 | `sync` | `async function loadRouteScheduleFromApi(){` |
| 563 | `sync` | `  async function fetchStops(){` |
| 581 | `sync` | `  async function populateStops(){` |
| 652 | `localStorage` | `      const raw = localStorage.getItem(STOP_FLOW_EVENT_KEY) \|\| "{}";` |
| 662 | `localStorage` | `      localStorage.setItem(STOP_FLOW_EVENT_KEY, JSON.stringify(obj \|\| {}));` |
| 668 | `localStorage` | `      const raw = localStorage.getItem(STOP_FLOW_SUMMARY_KEY) \|\| "{}";` |
| 695 | `localStorage` | `      keys.forEach(k => localStorage.removeItem(k));` |
| 711 | `setTimeout` | `  setTimeout(clearStaleStopFlowIfTripEmpty, 0);` |
| 715 | `localStorage` | `      localStorage.setItem(STOP_FLOW_SUMMARY_KEY, JSON.stringify(stopFlowSummary \|\| {}));` |
| 933 | `classList.remove` | `    $$(".seat").forEach(el => el.classList.remove("has-stop"));` |
| 938 | `classList.add` | `      if(el) el.classList.add("has-stop");` |
| 947 | `classList.remove` | `    el.classList.remove("male","female","isAssigned","has-service");` |
| 952 | `classList.add` | `    if(isAssigned) el.classList.add("isAssigned");` |
| 953 | `classList.add` | `    if(gender === "bay") el.classList.add("male");` |
| 954 | `classList.add` | `    if(gender === "bayan") el.classList.add("female");` |
| 955 | `classList.add` | `    if(serviceMap[key]) el.classList.add("has-service");` |
| 991 | `classList.add` | `      standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse");` |
| 1053 | `requestAnimationFrame` | `  requestAnimationFrame(() => {` |
| 1054 | `setTimeout` | `    setTimeout(() => {` |
| 1063 | `classList.add` | `        target.classList.add("route-focus-flash");` |
| 1064 | `classList.remove` | `        setTimeout(() => target.classList.remove("route-focus-flash"), 1200);` |
| 1209 | `requestAnimationFrame` | `    requestAnimationFrame(() => {` |
| 1210 | `setTimeout` | `      setTimeout(() => {` |
| 1343 | `auto` | `    const autoOn = $("#autoAdvanceToggle")?.checked;` |
| 1344 | `auto` | `    if(autoOn === false && !ignoreToggle) return;` |
| 1364 | `watch` | `    if(geoWatchId){` |
| 1389 | `classList.remove` | `    $$(".seat.selected").forEach(x => x.classList.remove("selected"));` |
| 1392 | `classList.add` | `    if(seatEl) seatEl.classList.add("selected");` |
| 1422 | `classList.remove` | `    $$(".seat.selected").forEach(x => x.classList.remove("selected"));` |
| 1425 | `sync` | `  async function saveSeat(){` |
| 1505 | `classList.remove` | `      el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");` |
| 1513 | `sync` | `  async function offloadSeat(){` |
| 1547 | `classList.remove` | `      el.classList.remove("multi-picked");` |
| 1557 | `classList.remove` | `      el.classList.remove("multi-picked");` |
| 1560 | `classList.add` | `      el.classList.add("multi-picked");` |
| 1593 | `sync` | `  async function saveBulk(){` |
| 1698 | `classList.add` | `      if(el) el.classList.add("blink-yellow");` |
| 1706 | `classList.remove` | `      if(el) el.classList.remove("blink-yellow");` |
| 1769 | `sync` | `  async function bulkOffload(seatNums){` |
| 1825 | `sync` | `  async function triggerManualApproach(){` |
| 1843 | `sync` | `  async function offloadSelectedStop(){` |
| 1880 | `watch` | `  async function toggleGeoWatch(){` |
| 1881 | `watch` | `    const btn = $("#btnGeoWatch");` |
| 1883 | `watch` | `    if(geoWatchId){` |
| 1884 | `watch` | `      navigator.geolocation.clearWatch(geoWatchId);` |
| 1885 | `watch` | `      geoWatchId = null;` |
| 1908 | `watch` | `    geoWatchId = navigator.geolocation.watchPosition((pos) => {` |
| 1915 | `auto` | `      autoDetectLiveStop(p);` |
| 1938 | `sync` | `  async function saveCoord(){` |
| 2215 | `Normal` | `    let aiSub = "Şu an sistem normal akışta.";` |
| 2237 | `force` | `  const LIVE_FORCE_KM = 1.2;       // Çok yakına girerse beklemeden canlı yap` |
| 2292 | `auto` | `        function autoDetectLiveStop(coords){` |
| 2369 | `localStorage` | `            localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 2370 | `localStorage` | `            localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 2427 | `force` | `      const forceNow = Number(best.km) <= LIVE_FORCE_KM;` |
| 2434 | `force` | `      if(!forceNow && nextHits < LIVE_STABLE_HITS){` |
| 2445 | `classList.toggle` | `        $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn));` |
| 2446 | `classList.toggle` | `        $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab));` |
| 2469 | `localStorage` | `        return (localStorage.getItem(TTS_KEY) ?? "1") === "1";` |
| 2477 | `sync` | `    function syncTts(){` |
| 2480 | `classList.add` | `      ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted");` |
| 2483 | `sync` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 2484 | `sync` | `        window.SeatsVoice.syncButtons();` |
| 2488 | `sync` | `    syncTts();` |
| 2496 | `localStorage` | `        localStorage.setItem(TTS_KEY, next ? "1" : "0");` |
| 2500 | `sync` | `      syncTts();` |
| 2504 | `force` | `          window.SeatsSpeak("Sesli uyarı açık.", { force:true });` |
| 2562 | `classList.remove` | `      speedBox.classList.remove("limit-ok","limit-warn","limit-bad");` |
| 2563 | `classList.add` | `      if(cls) speedBox.classList.add(cls);` |
| 2579 | `sync` | `    async function fetchLimit(lat, lng){` |
| 2624 | `watch` | `      speedWatchId = navigator.geolocation.watchPosition(async (pos) => {` |
| 2634 | `auto` | `        autoDetectLiveStop(currentCoords);` |
| 2738 | `sync` | `  onClick("#standingBulkOff", async () => {` |
| 2763 | `watch` | `  onClick("#btnGeoWatch", toggleGeoWatch);` |
| 2777 | `sync` | `  onClick("#approachOffload", async () => {` |
| 2848 | `sync` | `  (async function init(){` |
| 2897 | `sync` | `async function persistLiveRuntimeStateToServer(){` |
| 2951 | `setInterval` | `  window.__liveRuntimeBridgeInterval = setInterval(function(){` |

### `android_app/app/src/main/python/static/seats/seats.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 31 | `localStorage` | `    if(localStorage.getItem(key) === version) return;` |
| 39 | `localStorage` | `    ].forEach(k => localStorage.removeItem(k));` |
| 41 | `localStorage` | `    localStorage.setItem(key, version);` |
| 141 | `localStorage` | `    const oldTripId = localStorage.getItem(activeTripMemoryKey) \|\| "";` |
| 142 | `localStorage` | `    const oldSchema = localStorage.getItem(memorySchemaKey) \|\| "";` |
| 165 | `localStorage` | `      localStorage.removeItem(prefix + TRIP_KEY);` |
| 168 | `localStorage` | `    localStorage.removeItem("continueTripStop:last");` |
| 170 | `localStorage` | `    Object.keys(localStorage).forEach(k => {` |
| 175 | `localStorage` | `        localStorage.removeItem(k);` |
| 179 | `localStorage` | `    localStorage.setItem(activeTripMemoryKey, currentTripId);` |
| 180 | `localStorage` | `    localStorage.setItem(memorySchemaKey, memorySchemaVersion);` |
| 188 | `localStorage` | `    JSON.parse(localStorage.getItem("boardsMap:" + TRIP_KEY) \|\| "{}")` |
| 198 | `watch` | `  let geoWatchId = null;` |
| 199 | `watch` | `  let speedWatchId = null;` |
| 229 | `setTimeout` | `    toast._timer = setTimeout(() => {` |
| 252 | `Normal` | `      .normalize("NFKD")` |
| 263 | `sync` | `  async function safeJsonFetch(url, opt){` |
| 274 | `localStorage` | `    localStorage.setItem("boardsMap:" + TRIP_KEY, JSON.stringify(boardsMap \|\| {}));` |
| 278 | `localStorage` | `    localStorage.setItem("liveStop:" + TRIP_KEY, speedState.liveStop \|\| "");` |
| 279 | `localStorage` | `    localStorage.setItem("passedStops:" + TRIP_KEY, JSON.stringify([...speedState.passedStops]));` |
| 283 | `localStorage` | `    speedState.liveStop = localStorage.getItem("liveStop:" + TRIP_KEY) \|\| "";` |
| 285 | `localStorage` | `      speedState.passedStops = new Set(JSON.parse(localStorage.getItem("passedStops:" + TRIP_KEY) \|\| "[]"));` |
| 292 | `localStorage` | `    localStorage.setItem("standingTotals:" + TRIP_KEY, JSON.stringify({` |
| 299 | `localStorage` | `    localStorage.setItem("standingItems:" + TRIP_KEY, JSON.stringify(standingItems \|\| []));` |
| 393 | `localStorage` | `        localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 394 | `localStorage` | `        localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 410 | `localStorage` | `        localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 411 | `localStorage` | `        localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 453 | `sync` | `async function loadRouteScheduleFromApi(){` |
| 563 | `sync` | `  async function fetchStops(){` |
| 581 | `sync` | `  async function populateStops(){` |
| 652 | `localStorage` | `      const raw = localStorage.getItem(STOP_FLOW_EVENT_KEY) \|\| "{}";` |
| 662 | `localStorage` | `      localStorage.setItem(STOP_FLOW_EVENT_KEY, JSON.stringify(obj \|\| {}));` |
| 668 | `localStorage` | `      const raw = localStorage.getItem(STOP_FLOW_SUMMARY_KEY) \|\| "{}";` |
| 695 | `localStorage` | `      keys.forEach(k => localStorage.removeItem(k));` |
| 711 | `setTimeout` | `  setTimeout(clearStaleStopFlowIfTripEmpty, 0);` |
| 715 | `localStorage` | `      localStorage.setItem(STOP_FLOW_SUMMARY_KEY, JSON.stringify(stopFlowSummary \|\| {}));` |
| 933 | `classList.remove` | `    $$(".seat").forEach(el => el.classList.remove("has-stop"));` |
| 938 | `classList.add` | `      if(el) el.classList.add("has-stop");` |
| 947 | `classList.remove` | `    el.classList.remove("male","female","isAssigned","has-service");` |
| 952 | `classList.add` | `    if(isAssigned) el.classList.add("isAssigned");` |
| 953 | `classList.add` | `    if(gender === "bay") el.classList.add("male");` |
| 954 | `classList.add` | `    if(gender === "bayan") el.classList.add("female");` |
| 955 | `classList.add` | `    if(serviceMap[key]) el.classList.add("has-service");` |
| 991 | `classList.add` | `      standingCount > 0 ? standingCard.classList.add("pulse") : standingCard.classList.remove("pulse");` |
| 1053 | `requestAnimationFrame` | `  requestAnimationFrame(() => {` |
| 1054 | `setTimeout` | `    setTimeout(() => {` |
| 1063 | `classList.add` | `        target.classList.add("route-focus-flash");` |
| 1064 | `classList.remove` | `        setTimeout(() => target.classList.remove("route-focus-flash"), 1200);` |
| 1209 | `requestAnimationFrame` | `    requestAnimationFrame(() => {` |
| 1210 | `setTimeout` | `      setTimeout(() => {` |
| 1343 | `auto` | `    const autoOn = $("#autoAdvanceToggle")?.checked;` |
| 1344 | `auto` | `    if(autoOn === false && !ignoreToggle) return;` |
| 1364 | `watch` | `    if(geoWatchId){` |
| 1389 | `classList.remove` | `    $$(".seat.selected").forEach(x => x.classList.remove("selected"));` |
| 1392 | `classList.add` | `    if(seatEl) seatEl.classList.add("selected");` |
| 1422 | `classList.remove` | `    $$(".seat.selected").forEach(x => x.classList.remove("selected"));` |
| 1425 | `sync` | `  async function saveSeat(){` |
| 1505 | `classList.remove` | `      el.classList.remove("has-stop","multi-picked","blink-yellow","has-bag");` |
| 1513 | `sync` | `  async function offloadSeat(){` |
| 1547 | `classList.remove` | `      el.classList.remove("multi-picked");` |
| 1557 | `classList.remove` | `      el.classList.remove("multi-picked");` |
| 1560 | `classList.add` | `      el.classList.add("multi-picked");` |
| 1593 | `sync` | `  async function saveBulk(){` |
| 1698 | `classList.add` | `      if(el) el.classList.add("blink-yellow");` |
| 1706 | `classList.remove` | `      if(el) el.classList.remove("blink-yellow");` |
| 1769 | `sync` | `  async function bulkOffload(seatNums){` |
| 1825 | `sync` | `  async function triggerManualApproach(){` |
| 1843 | `sync` | `  async function offloadSelectedStop(){` |
| 1880 | `watch` | `  async function toggleGeoWatch(){` |
| 1881 | `watch` | `    const btn = $("#btnGeoWatch");` |
| 1883 | `watch` | `    if(geoWatchId){` |
| 1884 | `watch` | `      navigator.geolocation.clearWatch(geoWatchId);` |
| 1885 | `watch` | `      geoWatchId = null;` |
| 1908 | `watch` | `    geoWatchId = navigator.geolocation.watchPosition((pos) => {` |
| 1915 | `auto` | `      autoDetectLiveStop(p);` |
| 1938 | `sync` | `  async function saveCoord(){` |
| 2215 | `Normal` | `    let aiSub = "Şu an sistem normal akışta.";` |
| 2237 | `force` | `  const LIVE_FORCE_KM = 1.2;       // Çok yakına girerse beklemeden canlı yap` |
| 2292 | `auto` | `        function autoDetectLiveStop(coords){` |
| 2369 | `localStorage` | `            localStorage.removeItem("liveStop:" + TRIP_KEY);` |
| 2370 | `localStorage` | `            localStorage.removeItem("passedStops:" + TRIP_KEY);` |
| 2427 | `force` | `      const forceNow = Number(best.km) <= LIVE_FORCE_KM;` |
| 2434 | `force` | `      if(!forceNow && nextHits < LIVE_STABLE_HITS){` |
| 2445 | `classList.toggle` | `        $$(".tab-btn").forEach(b => b.classList.toggle("active", b === btn));` |
| 2446 | `classList.toggle` | `        $$(".tab-pane").forEach(p => p.classList.toggle("active", p.dataset.pane === tab));` |
| 2469 | `localStorage` | `        return (localStorage.getItem(TTS_KEY) ?? "1") === "1";` |
| 2477 | `sync` | `    function syncTts(){` |
| 2480 | `classList.add` | `      ttsEnabled ? ttsBtn.classList.remove("muted") : ttsBtn.classList.add("muted");` |
| 2483 | `sync` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 2484 | `sync` | `        window.SeatsVoice.syncButtons();` |
| 2488 | `sync` | `    syncTts();` |
| 2496 | `localStorage` | `        localStorage.setItem(TTS_KEY, next ? "1" : "0");` |
| 2500 | `sync` | `      syncTts();` |
| 2504 | `force` | `          window.SeatsSpeak("Sesli uyarı açık.", { force:true });` |
| 2562 | `classList.remove` | `      speedBox.classList.remove("limit-ok","limit-warn","limit-bad");` |
| 2563 | `classList.add` | `      if(cls) speedBox.classList.add(cls);` |
| 2579 | `sync` | `    async function fetchLimit(lat, lng){` |
| 2624 | `watch` | `      speedWatchId = navigator.geolocation.watchPosition(async (pos) => {` |
| 2634 | `auto` | `        autoDetectLiveStop(currentCoords);` |
| 2738 | `sync` | `  onClick("#standingBulkOff", async () => {` |
| 2763 | `watch` | `  onClick("#btnGeoWatch", toggleGeoWatch);` |
| 2777 | `sync` | `  onClick("#approachOffload", async () => {` |
| 2848 | `sync` | `  (async function init(){` |
| 2897 | `sync` | `async function persistLiveRuntimeStateToServer(){` |
| 2951 | `setInterval` | `  window.__liveRuntimeBridgeInterval = setInterval(function(){` |

### `static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 4 | `Sürüş` | `   /seats?drive=1 ile gelirse sürüş modunu açar` |
| 6 | `driveMode` | `(function autoOpenDriveModeFromUrl(){` |
| 15 | `driveMode` | `    const key = "driveMode:" + tripKey;` |
| 17 | `localStorage` | `    localStorage.setItem(key, "1");` |
| 18 | `drive-mode` | `    document.body.classList.add("drive-mode");` |
| 20 | `setTimeout` | `    setTimeout(() => {` |
| 33 | `Sürüş` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |
| 39 | `Sürüş` | `   Sürüş modu + hız kutusu + ses açık/sessiz` |
| 47 | `driveMode` | `  const DRIVE_MODE_KEY = "driveMode:" + tripKey;` |
| 57 | `force` | `        window.SeatsSpeak(msg, { force:true });` |
| 92 | `localStorage` | `    return localStorage.getItem(DRIVE_MODE_KEY) === "1";` |
| 95 | `driveMode` | `  function syncDriveMode(){` |
| 96 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 99 | `drive-mode` | `    document.body.classList.toggle("drive-mode", on);` |
| 100 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", on);` |
| 103 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 104 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 111 | `sync` | `      if(typeof syncDriveEtaChip === "function") syncDriveEtaChip();` |
| 115 | `driveMode` | `      window.dispatchEvent(new CustomEvent("driveModeChanged", {` |
| 121 | `driveMode` | `  function bindDriveMode(){` |
| 122 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 126 | `driveMode` | `      syncDriveMode();` |
| 136 | `localStorage` | `      localStorage.setItem(DRIVE_MODE_KEY, next ? "1" : "0");` |
| 138 | `driveMode` | `      syncDriveMode();` |
| 140 | `driveMode` | `      setTimeout(syncDriveMode, 80);` |
| 141 | `driveMode` | `      setTimeout(syncDriveMode, 250);` |
| 144 | `driveMode` | `    syncDriveMode();` |
| 183 | `localStorage` | `    const saved = localStorage.getItem("ttsEnabled");` |
| 194 | `sync` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 195 | `sync` | `        window.SeatsVoice.syncButtons();` |
| 205 | `classList.toggle` | `    btn.classList.toggle("is-off", !on);` |
| 221 | `localStorage` | `          localStorage.setItem("ttsEnabled", enabled ? "1" : "0");` |
| 225 | `localStorage` | `          localStorage.setItem("ttsEnabled", enabled ? "1" : "0");` |
| 239 | `setTimeout` | `        setTimeout(() => safeSpeak("Sesli robot açık."), 80);` |
| 266 | `driveMode` | `    bindDriveMode();` |
| 276 | `setTimeout` | `  setTimeout(bootDriveControls, 400);` |
| 277 | `setTimeout` | `  setTimeout(bootDriveControls, 1200);` |
| 279 | `setInterval` | `  setInterval(updateDriveSpeedChip, 1000);` |

### `android_app/app/src/main/python/static/seats/drive-controls.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Sürüş` | `   HIZLI KOLTUK → OTOMATİK SÜRÜŞ MODU` |
| 4 | `Sürüş` | `   /seats?drive=1 ile gelirse sürüş modunu açar` |
| 6 | `driveMode` | `(function autoOpenDriveModeFromUrl(){` |
| 15 | `driveMode` | `    const key = "driveMode:" + tripKey;` |
| 17 | `localStorage` | `    localStorage.setItem(key, "1");` |
| 18 | `drive-mode` | `    document.body.classList.add("drive-mode");` |
| 20 | `setTimeout` | `    setTimeout(() => {` |
| 33 | `Sürüş` | `    console.warn("Hızlı koltuk sürüş modu açılamadı:", e);` |
| 39 | `Sürüş` | `   Sürüş modu + hız kutusu + ses açık/sessiz` |
| 47 | `driveMode` | `  const DRIVE_MODE_KEY = "driveMode:" + tripKey;` |
| 57 | `force` | `        window.SeatsSpeak(msg, { force:true });` |
| 92 | `localStorage` | `    return localStorage.getItem(DRIVE_MODE_KEY) === "1";` |
| 95 | `driveMode` | `  function syncDriveMode(){` |
| 96 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 99 | `drive-mode` | `    document.body.classList.toggle("drive-mode", on);` |
| 100 | `drive-mode` | `    document.documentElement.classList.toggle("drive-mode", on);` |
| 103 | `Normal` | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 104 | `Normal` | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 111 | `sync` | `      if(typeof syncDriveEtaChip === "function") syncDriveEtaChip();` |
| 115 | `driveMode` | `      window.dispatchEvent(new CustomEvent("driveModeChanged", {` |
| 121 | `driveMode` | `  function bindDriveMode(){` |
| 122 | `driveMode` | `    const btn = document.getElementById("driveModeToggle");` |
| 126 | `driveMode` | `      syncDriveMode();` |
| 136 | `localStorage` | `      localStorage.setItem(DRIVE_MODE_KEY, next ? "1" : "0");` |
| 138 | `driveMode` | `      syncDriveMode();` |
| 140 | `driveMode` | `      setTimeout(syncDriveMode, 80);` |
| 141 | `driveMode` | `      setTimeout(syncDriveMode, 250);` |
| 144 | `driveMode` | `    syncDriveMode();` |
| 183 | `localStorage` | `    const saved = localStorage.getItem("ttsEnabled");` |
| 194 | `sync` | `      if(window.SeatsVoice && typeof window.SeatsVoice.syncButtons === "function"){` |
| 195 | `sync` | `        window.SeatsVoice.syncButtons();` |
| 205 | `classList.toggle` | `    btn.classList.toggle("is-off", !on);` |
| 221 | `localStorage` | `          localStorage.setItem("ttsEnabled", enabled ? "1" : "0");` |
| 225 | `localStorage` | `          localStorage.setItem("ttsEnabled", enabled ? "1" : "0");` |
| 239 | `setTimeout` | `        setTimeout(() => safeSpeak("Sesli robot açık."), 80);` |
| 266 | `driveMode` | `    bindDriveMode();` |
| 276 | `setTimeout` | `  setTimeout(bootDriveControls, 400);` |
| 277 | `setTimeout` | `  setTimeout(bootDriveControls, 1200);` |
| 279 | `setInterval` | `  setInterval(updateDriveSpeedChip, 1000);` |

### `static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `drive-mode` | `  body.drive-mode .seat .manual-ticket-badge{` |

### `static/seats/patches/manual-ticket-system.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 27 | `localStorage` | `      const raw = localStorage.getItem(sigKey()) \|\| "{}";` |
| 37 | `localStorage` | `      localStorage.setItem(sigKey(), JSON.stringify(obj \|\| {}));` |
| 43 | `localStorage` | `      localStorage.setItem(legacyKey(), "[]");` |
| 103 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge");` |
| 104 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge-sig");` |
| 107 | `classList.add` | `        el.classList.add("has-manual-ticket-badge-sig");` |
| 153 | `classList.add` | `      el.classList.add("has-manual-ticket-badge-sig");` |
| 154 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge");` |
| 161 | `setTimeout` | `    setTimeout(applyBadges, 150);` |
| 162 | `setTimeout` | `    setTimeout(applyBadges, 600);` |
| 163 | `setTimeout` | `    setTimeout(applyBadges, 1200);` |
| 180 | `classList.remove` | `        el.classList.remove("has-manual-ticket-badge");` |
| 181 | `classList.remove` | `        el.classList.remove("has-manual-ticket-badge-sig");` |
| 198 | `setTimeout` | `    timer = setTimeout(applyBadges, 180);` |
| 210 | `setTimeout` | `    setTimeout(schedule, 250);` |
| 211 | `setTimeout` | `    setTimeout(schedule, 900);` |
| 212 | `setTimeout` | `    setTimeout(schedule, 1600);` |
| 225 | `setTimeout` | `  setTimeout(applyBadges, 500);` |
| 226 | `setTimeout` | `  setTimeout(applyBadges, 1400);` |

### `static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `auto` | `    scroll-behavior:auto !important;` |
| 58 | `driveMode` | `  #driveModeActionsDock,` |

### `static/seats/patches/modal-bottom-nav-autohide.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `auto` | `  if(window.__muavinModalBottomNavAutohideV3) return;` |
| 3 | `auto` | `  window.__muavinModalBottomNavAutohideV3 = true;` |
| 100 | `classList.toggle` | `    document.body.classList.toggle("muavin-work-modal-open", open);` |
| 106 | `classList.add` | `        nav.classList.add("muavin-hidden-bottom-nav-by-modal");` |
| 110 | `classList.remove` | `        el.classList.remove("muavin-hidden-bottom-nav-by-modal");` |
| 122 | `requestAnimationFrame` | `    requestAnimationFrame(function(){` |
| 129 | `setTimeout` | `    setTimeout(scheduleApply, 30);` |
| 130 | `setTimeout` | `    setTimeout(scheduleApply, 160);` |
| 131 | `setTimeout` | `    setTimeout(scheduleApply, 420);` |
| 147 | `setInterval` | `  setInterval(applyState, 700);` |

### `static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 15 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |

### `static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 38 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 41 | `drive-mode` | `  body.drive-mode .deck{` |
| 46 | `drive-mode` | `    body.drive-mode .deck{` |

### `static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 42 | `drive-mode` | `  body.drive-mode .deck{` |
| 47 | `drive-mode` | `    body.drive-mode .deck{` |
| 65 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 101 | `auto` | `    right:auto !important;` |
| 102 | `auto` | `    bottom:auto !important;` |
| 109 | `auto` | `    pointer-events:auto !important;` |
| 120 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 133 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 259 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 282 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `drive-mode` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 299 | `drive-mode` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 304 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 309 | `auto` | `    right:auto !important;` |
| 310 | `auto` | `    bottom:auto !important;` |
| 322 | `auto` | `    height:auto !important;` |
| 345 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 362 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 382 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 389 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 400 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 18 | `classList.add` | `    col.classList.add("fab-left-gap-moved");` |
| 52 | `setTimeout` | `    timer = setTimeout(placeFabColumn, 80);` |
| 74 | `setTimeout` | `  setTimeout(placeFabColumn, 150);` |
| 75 | `setTimeout` | `  setTimeout(placeFabColumn, 600);` |
| 76 | `setTimeout` | `  setTimeout(placeFabColumn, 1400);` |
| 89 | `setTimeout` | `      setTimeout(refreshFabPosition, 120);` |
| 90 | `setTimeout` | `      setTimeout(refreshFabPosition, 600);` |
| 93 | `setTimeout` | `    setTimeout(refreshFabPosition, 120);` |
| 94 | `setTimeout` | `    setTimeout(refreshFabPosition, 600);` |
| 97 | `setTimeout` | `  setTimeout(refreshFabPosition, 1200);` |
| 102 | `driveMode` | `  if(window.__fabDriveModeOverrideFixReady) return;` |
| 103 | `driveMode` | `  window.__fabDriveModeOverrideFixReady = true;` |
| 117 | `classList.add` | `    col.classList.add("fab-left-gap-moved");` |
| 149 | `setTimeout` | `    timer = setTimeout(place, 80);` |
| 162 | `driveMode` | `  window.addEventListener("driveModeChanged", schedule);` |
| 164 | `setTimeout` | `  setTimeout(place, 150);` |
| 165 | `setTimeout` | `  setTimeout(place, 600);` |
| 166 | `setTimeout` | `  setTimeout(place, 1400);` |

### `static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 30 | `auto` | `  margin:0 auto !important;` |
| 50 | `auto` | `  margin:0 auto !important;` |
| 57 | `Sürüş` | `/* üst sürüş/eta dock sade modda gizli */` |
| 59 | `driveMode` | `html.seat-simple-mode #driveModeActionsDock{` |
| 184 | `auto` | `  flex:0 0 auto;` |

### `static/seats/patches/seat-simple-ui-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 20 | `localStorage` | `      return localStorage.getItem(key()) \|\| "simple";` |
| 28 | `localStorage` | `      localStorage.setItem(key(), mode);` |
| 34 | `classList.toggle` | `    document.documentElement.classList.toggle("seat-simple-mode", simple);` |
| 35 | `classList.toggle` | `    document.body.classList.toggle("seat-simple-mode", simple);` |
| 75 | `setTimeout` | `    setTimeout(function(){ applyMode(readMode()); }, 250);` |
| 76 | `setTimeout` | `    setTimeout(function(){ applyMode(readMode()); }, 900);` |
| 135 | `setInterval` | `    setInterval(update, 1000);` |
| 198 | `setTimeout` | `  setTimeout(boot, 300);` |
| 199 | `setTimeout` | `  setTimeout(update, 900);` |
| 224 | `sync` | `  function sync(){` |
| 230 | `classList.toggle` | `    document.documentElement.classList.toggle("seat-modal-open", open);` |
| 231 | `classList.toggle` | `    document.body.classList.toggle("seat-modal-open", open);` |
| 235 | `sync` | `    sync();` |
| 237 | `watch` | `    const watchList = [` |
| 245 | `sync` | `    const observer = new MutationObserver(sync);` |
| 247 | `watch` | `    watchList.forEach(sel => {` |
| 260 | `setTimeout` | `      setTimeout(sync, 20);` |
| 261 | `setTimeout` | `      setTimeout(sync, 120);` |
| 262 | `setTimeout` | `      setTimeout(sync, 300);` |
| 265 | `sync` | `    window.addEventListener("resize", sync);` |
| 267 | `setTimeout` | `      setTimeout(sync, 250);` |
| 270 | `setInterval` | `    setInterval(sync, 500);` |

### `static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 28 | `auto` | `    margin:0 auto;` |
| 96 | `auto` | `    overflow:auto;` |
| 164 | `auto` | `    flex:0 0 auto;` |

### `static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 51 | `localStorage` | `    return cleanStopName(localStorage.getItem(memoryKey) \|\| "");` |
| 58 | `localStorage` | `    try{ localStorage.setItem(memoryKey, name); }catch(e){}` |
| 88 | `force` | `  function setPickupToSelected(name, force){` |
| 96 | `force` | `    if(!force && current) return;` |
| 236 | `setTimeout` | `    setTimeout(function(){` |
| 246 | `classList.add` | `    document.documentElement.classList.add("stop-flow-focus-lock");` |
| 247 | `classList.add` | `    document.body.classList.add("stop-flow-focus-lock");` |
| 254 | `classList.remove` | `    document.documentElement.classList.remove("stop-flow-focus-lock");` |
| 255 | `classList.remove` | `    document.body.classList.remove("stop-flow-focus-lock");` |
| 258 | `setTimeout` | `      setTimeout(function(){` |
| 272 | `document.documentElement.classList` | `      if(document.documentElement.classList.contains("seat-simple-mode")) return true;` |
| 273 | `document.body.classList` | `      if(document.body.classList.contains("seat-simple-mode")) return true;` |
| 278 | `localStorage` | `      var v = localStorage.getItem("seatUiMode:" + tripKey);` |
| 329 | `Normal` | `    // Normal moddaki alt Durak butonunu engelleme.` |
| 368 | `setTimeout` | `        setTimeout(function(){` |
| 385 | `setTimeout` | `  setTimeout(installHooks, 300);` |
| 386 | `setTimeout` | `  setTimeout(installHooks, 1000);` |

### `static/seats/patches/stop-selected-toast.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 44 | `classList.remove` | `    el.classList.remove("show");` |
| 46 | `classList.add` | `    el.classList.add("show");` |
| 52 | `setTimeout` | `    timer = setTimeout(function(){` |
| 53 | `classList.remove` | `      el.classList.remove("show");` |

### `static/seats/patches/top-sound-toggle.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `auto` | `    grid-template-columns:1fr auto;` |

### `static/seats/patches/top-sound-toggle.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `localStorage` | `      return (localStorage.getItem(KEY) ?? "1") === "1";` |
| 35 | `localStorage` | `        localStorage.setItem(KEY, on ? "1" : "0");` |
| 38 | `localStorage` | `      try{ localStorage.setItem(KEY, on ? "1" : "0"); }catch(e){}` |
| 49 | `classList.toggle` | `      tts.classList.toggle("muted", !on);` |
| 69 | `sync` | `    syncButton();` |
| 72 | `sync` | `  function syncButton(){` |
| 78 | `classList.toggle` | `    btn.classList.toggle("is-off", !on);` |
| 117 | `force` | `          try{ window.SeatsSpeak("Sesli asistan açık.", {force:true}); }catch(_){}` |
| 124 | `sync` | `    syncButton();` |
| 131 | `setTimeout` | `    timer = setTimeout(ensureButton, 80);` |
| 142 | `sync` | `  window.addEventListener("ttsEnabledChanged", syncButton);` |
| 156 | `setTimeout` | `  setTimeout(ensureButton, 150);` |
| 157 | `setTimeout` | `  setTimeout(ensureButton, 600);` |
| 158 | `setTimeout` | `  setTimeout(ensureButton, 1400);` |

### `static/seats/patches/unified-seat-deck-report-style.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 3 | `Normal` | `   Normal mod + Sürüş modu + Sade mod aynı koltuk planını kullanır.` |
| 18 | `drive-mode` | `body.drive-mode .board-stage,` |
| 22 | `auto` | `  overflow-x:auto !important;` |
| 28 | `drive-mode` | `body.drive-mode .deck-wrap,` |
| 33 | `auto` | `  margin:0 auto !important;` |
| 40 | `drive-mode` | `body.drive-mode .deck,` |
| 52 | `auto` | `  grid-auto-rows:var(--unified-row-h) !important;` |
| 72 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-column:4"],` |
| 73 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-column: 4"],` |
| 78 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 79 | `drive-mode` | `body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `body.drive-mode .cell,` |
| 97 | `drive-mode` | `body.drive-mode .label,` |
| 111 | `drive-mode` | `body.drive-mode .seat,` |
| 140 | `drive-mode` | `body.drive-mode .seat:not(.isAssigned):not(.male):not(.female),` |
| 146 | `drive-mode` | `body.drive-mode .seat.male,` |
| 152 | `drive-mode` | `body.drive-mode .seat.female,` |
| 158 | `drive-mode` | `body.drive-mode .seat.isAssigned:not(.male):not(.female),` |
| 165 | `drive-mode` | `body.drive-mode .seat.selected,` |
| 177 | `drive-mode` | `body.drive-mode .seat.has-stop,` |
| 186 | `drive-mode` | `body.drive-mode .corr,` |
| 221 | `drive-mode` | `body.drive-mode .door,` |
| 250 | `drive-mode` | `body.drive-mode .seat .bag-badge,` |
| 265 | `drive-mode` | `body.drive-mode .seat .svc-badge,` |
| 275 | `drive-mode` | `body.drive-mode .seat .stop-badge,` |
| 283 | `Sürüş` | `/* Sürüş modunda koltuk planı artık ayrı küçülmesin/büyümesin */` |
| 284 | `drive-mode` | `body.drive-mode{` |
| 301 | `drive-mode` | `  body.drive-mode .board-stage,` |
| 307 | `drive-mode` | `  body.drive-mode .deck,` |
| 314 | `drive-mode` | `  body.drive-mode .seat,` |
| 321 | `drive-mode` | `  body.drive-mode .corr,` |
| 328 | `drive-mode` | `  body.drive-mode .door,` |
| 347 | `drive-mode` | `  body.drive-mode .seat,` |
| 355 | `Normal` | `/* Etiketler geri geldi: normal + sürüş + sade mod aynı kompakt etiket düzeni */` |
| 364 | `drive-mode` | `body.drive-mode .cell,` |
| 373 | `drive-mode` | `body.drive-mode .label,` |
| 401 | `drive-mode` | `body.drive-mode .label:empty,` |
| 408 | `Sürüş` | `/* Sürüş modunda da aynı düzen kalsın */` |
| 409 | `drive-mode` | `body.drive-mode{` |
| 427 | `drive-mode` | `  body.drive-mode .label,` |
| 435 | `drive-mode` | `  body.drive-mode .label:empty,` |
| 450 | `drive-mode` | `  body.drive-mode .label,` |
| 460 | `Normal` | `/* Koltuk aralarını biraz açar; normal + sürüş + sade mod aynı kalır */` |
| 470 | `drive-mode` | `body.drive-mode .deck,` |
| 474 | `auto` | `  grid-auto-rows:var(--unified-row-h) !important;` |
| 479 | `drive-mode` | `body.drive-mode .corr,` |
| 497 | `drive-mode` | `  body.drive-mode .deck,` |

### `android_app/app/src/main/python/static/seats/patches/bottom-row-51-54-equal-spacing.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 14 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |

### `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `drive-mode` | `  body.drive-mode .seat .manual-ticket-badge{` |

### `android_app/app/src/main/python/static/seats/patches/manual-ticket-system.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 27 | `localStorage` | `      const raw = localStorage.getItem(sigKey()) \|\| "{}";` |
| 37 | `localStorage` | `      localStorage.setItem(sigKey(), JSON.stringify(obj \|\| {}));` |
| 43 | `localStorage` | `      localStorage.setItem(legacyKey(), "[]");` |
| 103 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge");` |
| 104 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge-sig");` |
| 107 | `classList.add` | `        el.classList.add("has-manual-ticket-badge-sig");` |
| 153 | `classList.add` | `      el.classList.add("has-manual-ticket-badge-sig");` |
| 154 | `classList.remove` | `      el.classList.remove("has-manual-ticket-badge");` |
| 161 | `setTimeout` | `    setTimeout(applyBadges, 150);` |
| 162 | `setTimeout` | `    setTimeout(applyBadges, 600);` |
| 163 | `setTimeout` | `    setTimeout(applyBadges, 1200);` |
| 180 | `classList.remove` | `        el.classList.remove("has-manual-ticket-badge");` |
| 181 | `classList.remove` | `        el.classList.remove("has-manual-ticket-badge-sig");` |
| 198 | `setTimeout` | `    timer = setTimeout(applyBadges, 180);` |
| 210 | `setTimeout` | `    setTimeout(schedule, 250);` |
| 211 | `setTimeout` | `    setTimeout(schedule, 900);` |
| 212 | `setTimeout` | `    setTimeout(schedule, 1600);` |
| 225 | `setTimeout` | `  setTimeout(applyBadges, 500);` |
| 226 | `setTimeout` | `  setTimeout(applyBadges, 1400);` |

### `android_app/app/src/main/python/static/seats/patches/mobile-performance-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `auto` | `    scroll-behavior:auto !important;` |
| 58 | `driveMode` | `  #driveModeActionsDock,` |

### `android_app/app/src/main/python/static/seats/patches/modal-bottom-nav-autohide.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 2 | `auto` | `  if(window.__muavinModalBottomNavAutohideV3) return;` |
| 3 | `auto` | `  window.__muavinModalBottomNavAutohideV3 = true;` |
| 100 | `classList.toggle` | `    document.body.classList.toggle("muavin-work-modal-open", open);` |
| 106 | `classList.add` | `        nav.classList.add("muavin-hidden-bottom-nav-by-modal");` |
| 110 | `classList.remove` | `        el.classList.remove("muavin-hidden-bottom-nav-by-modal");` |
| 122 | `requestAnimationFrame` | `    requestAnimationFrame(function(){` |
| 129 | `setTimeout` | `    setTimeout(scheduleApply, 30);` |
| 130 | `setTimeout` | `    setTimeout(scheduleApply, 160);` |
| 131 | `setTimeout` | `    setTimeout(scheduleApply, 420);` |
| 147 | `setInterval` | `  setInterval(applyState, 700);` |

### `android_app/app/src/main/python/static/seats/patches/only-54-reapply-right-shift.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 15 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 16 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 17 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 18 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |

### `android_app/app/src/main/python/static/seats/patches/right-seat-column-spacing-fix.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 38 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 41 | `drive-mode` | `  body.drive-mode .deck{` |
| 46 | `drive-mode` | `    body.drive-mode .deck{` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 39 | `Sürüş` | `    Sürüş modunda koltuklar biraz daha sıkıştığı için` |
| 42 | `drive-mode` | `  body.drive-mode .deck{` |
| 47 | `drive-mode` | `    body.drive-mode .deck{` |
| 65 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"],` |
| 66 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"]{` |
| 85 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column:4"],` |
| 86 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row:14"][style*="grid-column: 4"],` |
| 87 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column:4"],` |
| 88 | `drive-mode` | `  body.drive-mode .deck .cell[style*="grid-row: 14"][style*="grid-column: 4"]{` |
| 101 | `auto` | `    right:auto !important;` |
| 102 | `auto` | `    bottom:auto !important;` |
| 109 | `auto` | `    pointer-events:auto !important;` |
| 120 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 133 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 259 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 282 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 295 | `drive-mode` | `    static/seats/seats.css içindeki body.drive-mode .fab-column kuralı` |
| 299 | `drive-mode` | `    .fab-left-gap-moved sınıfı varsa, drive-mode kurallarını ezip` |
| 304 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved{` |
| 309 | `auto` | `    right:auto !important;` |
| 310 | `auto` | `    bottom:auto !important;` |
| 322 | `auto` | `    height:auto !important;` |
| 345 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved::before{` |
| 362 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab{` |
| 382 | `drive-mode` | `  body.drive-mode .fab-column.fab-left-gap-moved .fab::after{` |
| 389 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved{` |
| 400 | `drive-mode` | `    body.drive-mode .fab-column.fab-left-gap-moved .fab{` |

### `android_app/app/src/main/python/static/seats/patches/seat-layout-fab-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 18 | `classList.add` | `    col.classList.add("fab-left-gap-moved");` |
| 52 | `setTimeout` | `    timer = setTimeout(placeFabColumn, 80);` |
| 74 | `setTimeout` | `  setTimeout(placeFabColumn, 150);` |
| 75 | `setTimeout` | `  setTimeout(placeFabColumn, 600);` |
| 76 | `setTimeout` | `  setTimeout(placeFabColumn, 1400);` |
| 89 | `setTimeout` | `      setTimeout(refreshFabPosition, 120);` |
| 90 | `setTimeout` | `      setTimeout(refreshFabPosition, 600);` |
| 93 | `setTimeout` | `    setTimeout(refreshFabPosition, 120);` |
| 94 | `setTimeout` | `    setTimeout(refreshFabPosition, 600);` |
| 97 | `setTimeout` | `  setTimeout(refreshFabPosition, 1200);` |
| 102 | `driveMode` | `  if(window.__fabDriveModeOverrideFixReady) return;` |
| 103 | `driveMode` | `  window.__fabDriveModeOverrideFixReady = true;` |
| 117 | `classList.add` | `    col.classList.add("fab-left-gap-moved");` |
| 149 | `setTimeout` | `    timer = setTimeout(place, 80);` |
| 162 | `driveMode` | `  window.addEventListener("driveModeChanged", schedule);` |
| 164 | `setTimeout` | `  setTimeout(place, 150);` |
| 165 | `setTimeout` | `  setTimeout(place, 600);` |
| 166 | `setTimeout` | `  setTimeout(place, 1400);` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 30 | `auto` | `  margin:0 auto !important;` |
| 50 | `auto` | `  margin:0 auto !important;` |
| 57 | `Sürüş` | `/* üst sürüş/eta dock sade modda gizli */` |
| 59 | `driveMode` | `html.seat-simple-mode #driveModeActionsDock{` |
| 184 | `auto` | `  flex:0 0 auto;` |

### `android_app/app/src/main/python/static/seats/patches/seat-simple-ui-pack.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 20 | `localStorage` | `      return localStorage.getItem(key()) \|\| "simple";` |
| 28 | `localStorage` | `      localStorage.setItem(key(), mode);` |
| 34 | `classList.toggle` | `    document.documentElement.classList.toggle("seat-simple-mode", simple);` |
| 35 | `classList.toggle` | `    document.body.classList.toggle("seat-simple-mode", simple);` |
| 75 | `setTimeout` | `    setTimeout(function(){ applyMode(readMode()); }, 250);` |
| 76 | `setTimeout` | `    setTimeout(function(){ applyMode(readMode()); }, 900);` |
| 135 | `setInterval` | `    setInterval(update, 1000);` |
| 198 | `setTimeout` | `  setTimeout(boot, 300);` |
| 199 | `setTimeout` | `  setTimeout(update, 900);` |
| 224 | `sync` | `  function sync(){` |
| 230 | `classList.toggle` | `    document.documentElement.classList.toggle("seat-modal-open", open);` |
| 231 | `classList.toggle` | `    document.body.classList.toggle("seat-modal-open", open);` |
| 235 | `sync` | `    sync();` |
| 237 | `watch` | `    const watchList = [` |
| 245 | `sync` | `    const observer = new MutationObserver(sync);` |
| 247 | `watch` | `    watchList.forEach(sel => {` |
| 260 | `setTimeout` | `      setTimeout(sync, 20);` |
| 261 | `setTimeout` | `      setTimeout(sync, 120);` |
| 262 | `setTimeout` | `      setTimeout(sync, 300);` |
| 265 | `sync` | `    window.addEventListener("resize", sync);` |
| 267 | `setTimeout` | `      setTimeout(sync, 250);` |
| 270 | `setInterval` | `    setInterval(sync, 500);` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 28 | `auto` | `    margin:0 auto;` |
| 96 | `auto` | `    overflow:auto;` |
| 164 | `auto` | `    flex:0 0 auto;` |

### `android_app/app/src/main/python/static/seats/patches/stop-flow-focus-patch.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 51 | `localStorage` | `    return cleanStopName(localStorage.getItem(memoryKey) \|\| "");` |
| 58 | `localStorage` | `    try{ localStorage.setItem(memoryKey, name); }catch(e){}` |
| 88 | `force` | `  function setPickupToSelected(name, force){` |
| 96 | `force` | `    if(!force && current) return;` |
| 236 | `setTimeout` | `    setTimeout(function(){` |
| 246 | `classList.add` | `    document.documentElement.classList.add("stop-flow-focus-lock");` |
| 247 | `classList.add` | `    document.body.classList.add("stop-flow-focus-lock");` |
| 254 | `classList.remove` | `    document.documentElement.classList.remove("stop-flow-focus-lock");` |
| 255 | `classList.remove` | `    document.body.classList.remove("stop-flow-focus-lock");` |
| 258 | `setTimeout` | `      setTimeout(function(){` |
| 272 | `document.documentElement.classList` | `      if(document.documentElement.classList.contains("seat-simple-mode")) return true;` |
| 273 | `document.body.classList` | `      if(document.body.classList.contains("seat-simple-mode")) return true;` |
| 278 | `localStorage` | `      var v = localStorage.getItem("seatUiMode:" + tripKey);` |
| 329 | `Normal` | `    // Normal moddaki alt Durak butonunu engelleme.` |
| 368 | `setTimeout` | `        setTimeout(function(){` |
| 385 | `setTimeout` | `  setTimeout(installHooks, 300);` |
| 386 | `setTimeout` | `  setTimeout(installHooks, 1000);` |

### `android_app/app/src/main/python/static/seats/patches/stop-selected-toast.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 44 | `classList.remove` | `    el.classList.remove("show");` |
| 46 | `classList.add` | `    el.classList.add("show");` |
| 52 | `setTimeout` | `    timer = setTimeout(function(){` |
| 53 | `classList.remove` | `      el.classList.remove("show");` |

### `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.css`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 4 | `auto` | `    grid-template-columns:1fr auto;` |

### `android_app/app/src/main/python/static/seats/patches/top-sound-toggle.js`

| Satır | Anahtar | İçerik |
| ---: | --- | --- |
| 13 | `localStorage` | `      return (localStorage.getItem(KEY) ?? "1") === "1";` |
| 35 | `localStorage` | `        localStorage.setItem(KEY, on ? "1" : "0");` |
| 38 | `localStorage` | `      try{ localStorage.setItem(KEY, on ? "1" : "0"); }catch(e){}` |
| 49 | `classList.toggle` | `      tts.classList.toggle("muted", !on);` |
| 69 | `sync` | `    syncButton();` |
| 72 | `sync` | `  function syncButton(){` |
| 78 | `classList.toggle` | `    btn.classList.toggle("is-off", !on);` |
| 117 | `force` | `          try{ window.SeatsSpeak("Sesli asistan açık.", {force:true}); }catch(_){}` |
| 124 | `sync` | `    syncButton();` |
| 131 | `setTimeout` | `    timer = setTimeout(ensureButton, 80);` |
| 142 | `sync` | `  window.addEventListener("ttsEnabledChanged", syncButton);` |
| 156 | `setTimeout` | `  setTimeout(ensureButton, 150);` |
| 157 | `setTimeout` | `  setTimeout(ensureButton, 600);` |
| 158 | `setTimeout` | `  setTimeout(ensureButton, 1400);` |

## 2) Şüpheli Template Blokları

### `templates/seats.html` satır 830-880

| Satır | İçerik |
| ---: | --- |
| 830 | `  .drive-eta-sub{` |
| 831 | `    font-size:10px !important;` |
| 832 | `  }` |
| 833 | `}` |
| 834 | `</style>` |
| 835 | `` |
| 836 | `{% include "seats_parts/offload_confirm.html" %}` |
| 837 | `` |
| 838 | `<!-- DRIVE MODE FORCE TOGGLE START -->` |
| 839 | `<script id="drive-mode-force-toggle-js">` |
| 840 | `(function(){` |
| 841 | `  if(window.__driveModeForceToggleReady) return;` |
| 842 | `  window.__driveModeForceToggleReady = true;` |
| 843 | `` |
| 844 | `  function driveKey(){` |
| 845 | `    const boot = window.SEATS_BOOT \|\| {};` |
| 846 | `    const tripKey = boot.tripKey \|\| window.TRIP_KEY \|\| window.BAG_TRIP \|\| "default";` |
| 847 | `    return "driveMode:" + tripKey;` |
| 848 | `  }` |
| 849 | `` |
| 850 | `  function isDriveOn(){` |
| 851 | `    try{` |
| 852 | `      return localStorage.getItem(driveKey()) === "1";` |
| 853 | `    }catch(e){` |
| 854 | `      return false;` |
| 855 | `    }` |
| 856 | `  }` |
| 857 | `` |
| 858 | `  function setDrive(on){` |
| 859 | `    try{` |
| 860 | `      localStorage.setItem(driveKey(), on ? "1" : "0");` |
| 861 | `    }catch(e){}` |
| 862 | `` |
| 863 | `    document.body.classList.toggle("drive-mode", !!on);` |
| 864 | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 865 | `` |
| 866 | `    const btn = document.getElementById("driveModeToggle");` |
| 867 | `    if(btn){` |
| 868 | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 869 | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 870 | `      btn.setAttribute("aria-pressed", on ? "true" : "false");` |
| 871 | `    }` |
| 872 | `` |
| 873 | `    try{ if(typeof renderRouteStrip === "function") renderRouteStrip(); }catch(e){}` |
| 874 | `    try{ if(typeof updateCompactHeader === "function") updateCompactHeader(); }catch(e){}` |
| 875 | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 876 | `` |
| 877 | `    try{` |
| 878 | `      window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 879 | `    }catch(e){}` |
| 880 | `  }` |

### `templates/seats.html` satır 880-930

| Satır | İçerik |
| ---: | --- |
| 880 | `  }` |
| 881 | `` |
| 882 | `  function sync(){` |
| 883 | `    setDrive(isDriveOn());` |
| 884 | `  }` |
| 885 | `` |
| 886 | `  // En üstten yakala: diğer click listener'lar aç-kapa karışıklığı yapmasın.` |
| 887 | `  document.addEventListener("click", function(e){` |
| 888 | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 889 | `    if(!btn) return;` |
| 890 | `` |
| 891 | `    e.preventDefault();` |
| 892 | `    e.stopPropagation();` |
| 893 | `    e.stopImmediatePropagation();` |
| 894 | `` |
| 895 | `    setDrive(!isDriveOn());` |
| 896 | `  }, true);` |
| 897 | `` |
| 898 | `  if(document.readyState === "loading"){` |
| 899 | `    document.addEventListener("DOMContentLoaded", sync);` |
| 900 | `  }else{` |
| 901 | `    sync();` |
| 902 | `  }` |
| 903 | `` |
| 904 | `  setTimeout(sync, 300);` |
| 905 | `})();` |
| 906 | `</script>` |
| 907 | `<!-- DRIVE MODE FORCE TOGGLE END -->` |
| 908 | `` |
| 909 | `<!-- DRIVE VOICE MIRROR SCRIPT START -->` |
| 910 | `<script id="drive-voice-mirror-script">` |
| 911 | `(function(){` |
| 912 | `  function syncDriveVoiceStats(){` |
| 913 | `    const oldFilled = document.getElementById("voiceSeatFilled");` |
| 914 | `    const oldEmpty  = document.getElementById("voiceSeatEmpty");` |
| 915 | `    const newFilled = document.getElementById("driveVoiceFilled");` |
| 916 | `    const newEmpty  = document.getElementById("driveVoiceEmpty");` |
| 917 | `` |
| 918 | `    if(oldFilled && newFilled){` |
| 919 | `      newFilled.textContent = (oldFilled.textContent \|\| "0").trim();` |
| 920 | `    }` |
| 921 | `    if(oldEmpty && newEmpty){` |
| 922 | `      newEmpty.textContent = (oldEmpty.textContent \|\| "0").trim();` |
| 923 | `    }` |
| 924 | `  }` |
| 925 | `` |
| 926 | `  function bindDriveVoiceButton(){` |
| 927 | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 928 | `    const realBtn = document.getElementById("btnDeckAI");` |
| 929 | `` |
| 930 | `    if(!fakeBtn \|\| fakeBtn.dataset.bound === "1") return;` |

### `android_app/app/src/main/python/templates/seats.html` satır 829-879

| Satır | İçerik |
| ---: | --- |
| 829 | `  .drive-speed-sub,` |
| 830 | `  .drive-eta-sub{` |
| 831 | `    font-size:10px !important;` |
| 832 | `  }` |
| 833 | `}` |
| 834 | `</style>` |
| 835 | `` |
| 836 | `{% include "seats_parts/offload_confirm.html" %}` |
| 837 | `` |
| 838 | `<!-- DRIVE MODE FORCE TOGGLE START -->` |
| 839 | `<script id="drive-mode-force-toggle-js">` |
| 840 | `(function(){` |
| 841 | `  if(window.__driveModeForceToggleReady) return;` |
| 842 | `  window.__driveModeForceToggleReady = true;` |
| 843 | `` |
| 844 | `  function driveKey(){` |
| 845 | `    const boot = window.SEATS_BOOT \|\| {};` |
| 846 | `    const tripKey = boot.tripKey \|\| window.TRIP_KEY \|\| window.BAG_TRIP \|\| "default";` |
| 847 | `    return "driveMode:" + tripKey;` |
| 848 | `  }` |
| 849 | `` |
| 850 | `  function isDriveOn(){` |
| 851 | `    try{` |
| 852 | `      return localStorage.getItem(driveKey()) === "1";` |
| 853 | `    }catch(e){` |
| 854 | `      return false;` |
| 855 | `    }` |
| 856 | `  }` |
| 857 | `` |
| 858 | `  function setDrive(on){` |
| 859 | `    try{` |
| 860 | `      localStorage.setItem(driveKey(), on ? "1" : "0");` |
| 861 | `    }catch(e){}` |
| 862 | `` |
| 863 | `    document.body.classList.toggle("drive-mode", !!on);` |
| 864 | `    document.documentElement.classList.toggle("drive-mode", !!on);` |
| 865 | `` |
| 866 | `    const btn = document.getElementById("driveModeToggle");` |
| 867 | `    if(btn){` |
| 868 | `      btn.innerHTML = on ? "↩ Normal" : "🚘 Sürüş";` |
| 869 | `      btn.title = on ? "Normal moda geç" : "Sürüş moduna geç";` |
| 870 | `      btn.setAttribute("aria-pressed", on ? "true" : "false");` |
| 871 | `    }` |
| 872 | `` |
| 873 | `    try{ if(typeof renderRouteStrip === "function") renderRouteStrip(); }catch(e){}` |
| 874 | `    try{ if(typeof updateCompactHeader === "function") updateCompactHeader(); }catch(e){}` |
| 875 | `    try{ if(typeof syncDriveEtaChip === "function") syncDriveEtaChip(); }catch(e){}` |
| 876 | `` |
| 877 | `    try{` |
| 878 | `      window.dispatchEvent(new CustomEvent("driveModeChanged", { detail:{ on:!!on } }));` |
| 879 | `    }catch(e){}` |

### `android_app/app/src/main/python/templates/seats.html` satır 879-929

| Satır | İçerik |
| ---: | --- |
| 879 | `    }catch(e){}` |
| 880 | `  }` |
| 881 | `` |
| 882 | `  function sync(){` |
| 883 | `    setDrive(isDriveOn());` |
| 884 | `  }` |
| 885 | `` |
| 886 | `  // En üstten yakala: diğer click listener'lar aç-kapa karışıklığı yapmasın.` |
| 887 | `  document.addEventListener("click", function(e){` |
| 888 | `    const btn = e.target.closest && e.target.closest("#driveModeToggle");` |
| 889 | `    if(!btn) return;` |
| 890 | `` |
| 891 | `    e.preventDefault();` |
| 892 | `    e.stopPropagation();` |
| 893 | `    e.stopImmediatePropagation();` |
| 894 | `` |
| 895 | `    setDrive(!isDriveOn());` |
| 896 | `  }, true);` |
| 897 | `` |
| 898 | `  if(document.readyState === "loading"){` |
| 899 | `    document.addEventListener("DOMContentLoaded", sync);` |
| 900 | `  }else{` |
| 901 | `    sync();` |
| 902 | `  }` |
| 903 | `` |
| 904 | `  setTimeout(sync, 300);` |
| 905 | `})();` |
| 906 | `</script>` |
| 907 | `<!-- DRIVE MODE FORCE TOGGLE END -->` |
| 908 | `` |
| 909 | `<!-- DRIVE VOICE MIRROR SCRIPT START -->` |
| 910 | `<script id="drive-voice-mirror-script">` |
| 911 | `(function(){` |
| 912 | `  function syncDriveVoiceStats(){` |
| 913 | `    const oldFilled = document.getElementById("voiceSeatFilled");` |
| 914 | `    const oldEmpty  = document.getElementById("voiceSeatEmpty");` |
| 915 | `    const newFilled = document.getElementById("driveVoiceFilled");` |
| 916 | `    const newEmpty  = document.getElementById("driveVoiceEmpty");` |
| 917 | `` |
| 918 | `    if(oldFilled && newFilled){` |
| 919 | `      newFilled.textContent = (oldFilled.textContent \|\| "0").trim();` |
| 920 | `    }` |
| 921 | `    if(oldEmpty && newEmpty){` |
| 922 | `      newEmpty.textContent = (oldEmpty.textContent \|\| "0").trim();` |
| 923 | `    }` |
| 924 | `  }` |
| 925 | `` |
| 926 | `  function bindDriveVoiceButton(){` |
| 927 | `    const fakeBtn = document.getElementById("btnDeckAIDrive");` |
| 928 | `    const realBtn = document.getElementById("btnDeckAI");` |
| 929 | `` |

## 3) İlk Teknik Yorum

- Eğer `setInterval` veya `setTimeout` içinde `drive-mode` tekrar ekleniyorsa, normal moda geçtikten sonra ekran tekrar sürüş moduna döner.
- Eğer `localStorage` içinde eski değer sürüş modu olarak kalıyorsa, sen normal yapsan bile senkron script onu geri basabilir.
- Temiz çözüm: Drive mode için tek kaynak bırakmak. Normal butonuna basılınca hem class hem localStorage aynı anda `false` yapılmalı; otomatik script normal tercihini ezmemeli.