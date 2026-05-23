/* =========================================================
   continue_flow_refresh.js
   Canlı durak değişince kart sırasını sayfa yenilemeden günceller.
   Alt kartlarda kalan mesafeyi GPS + durak koordinatına göre km gösterir.
========================================================= */

(function(){
  const BOOT = window.CONTINUE_BOOT || {};
  const routeStops = Array.isArray(BOOT.routeStops) ? BOOT.routeStops : [];
  const routeCoords = Array.isArray(BOOT.routeCoords) ? BOOT.routeCoords : [];

  const POLL_MS = 1500;
  const DETAIL_REFRESH_MS = 2500;

  let lastFlowSig = "";
  let lastDetailAt = 0;
  let detailSeq = 0;
  let detailBusy = false;

  let currentCoords = null;
  let geoWatchId = null;
  let lastGeoRefreshAt = 0;

  function text(v){
    return String(v == null ? "" : v);
  }

  function norm(v){
    return text(v)
      .trim()
      .toLocaleLowerCase("tr-TR")
      .replace(/[–—_\/\\.,()[\]]/g, " ")
      .replace(/\s+/g, " ");
  }

  function distKm(a, b){
    const R = 6371;
    const toRad = d => d * Math.PI / 180;
    const dLat = toRad(Number(b.lat) - Number(a.lat));
    const dLng = toRad(Number(b.lng) - Number(a.lng));
    const la1 = toRad(Number(a.lat));
    const la2 = toRad(Number(b.lat));
    const h =
      Math.sin(dLat / 2) ** 2 +
      Math.cos(la1) * Math.cos(la2) * Math.sin(dLng / 2) ** 2;

    return 2 * R * Math.asin(Math.sqrt(h));
  }

  function coordForStop(stopName){
    const key = norm(stopName);
    if(!key) return null;

    const item = routeCoords.find(x => norm(x.stop || x.name) === key);
    if(!item) return null;

    const lat = Number(item.lat);
    const lng = Number(item.lng);

    if(!Number.isFinite(lat) || !Number.isFinite(lng)) return null;

    return { lat, lng };
  }

  function stopDistanceLabel(stopName){
    if(!currentCoords) return "";

    const target = coordForStop(stopName);
    if(!target) return "";

    const km = distKm(currentCoords, target);

    if(!Number.isFinite(km)) return "";

    if(km < 1){
      return Math.round(km * 1000) + " m";
    }

    return km.toFixed(2) + " km";
  }

  function startGeoWatch(){
    if(geoWatchId) return;
    if(!("geolocation" in navigator)) return;

    try{
      geoWatchId = navigator.geolocation.watchPosition(function(pos){
        currentCoords = {
          lat: pos.coords.latitude,
          lng: pos.coords.longitude
        };

        const now = Date.now();

        if(now - lastGeoRefreshAt > 900){
          lastGeoRefreshAt = now;
          refreshFlow();
        }
      }, function(){}, {
        enableHighAccuracy: true,
        maximumAge: 3000,
        timeout: 12000
      });
    }catch(_){}
  }

  function routeIndex(name){
    const n = norm(name);
    if(!n) return -1;
    return routeStops.findIndex(x => norm(x) === n);
  }

  function currentStopName(){
    const el = document.getElementById("liveCurrentStopName");
    return el ? text(el.textContent).trim() : "";
  }

  function statusByOffset(offset){
    if(offset === 0){
      return { kind:"live", status:"Canlı", eta:"Şimdi", fallbackDistance:"—" };
    }

    if(offset === 1){
      return { kind:"next", status:"Sıradaki", eta:"Sırada", fallbackDistance:"—" };
    }

    return {
      kind:"upcoming",
      status:"Bekliyor",
      eta: offset + " durak sonra",
      fallbackDistance:"—"
    };
  }

  function makeFlow(currentIndex){
    return routeStops
      .slice(currentIndex, currentIndex + 4)
      .map((name, i) => ({
        name,
        index: currentIndex + i,
        offset: i,
        ...statusByOffset(i)
      }));
  }

  function regularCards(){
    return Array.from(document.querySelectorAll(".timeline .journey-card .card.regular"));
  }

  function setText(el, value){
    if(el) el.textContent = text(value);
  }

  function setFutureCardBase(card, item){
    const article = card.closest(".journey-card");
    const node = article ? article.querySelector(".node") : null;

    if(!item){
      if(article) article.style.display = "none";
      return;
    }

    if(article) article.style.display = "";

    const previousStopName = card.dataset.flowStopName || "";
    const nameChanged = norm(previousStopName) !== norm(item.name || "");
    card.dataset.flowStopName = item.name || "";

    if(node){
      node.className = "node " + item.kind;
    }

    card.classList.remove("next-card", "upcoming-card", "passed-card", "live-card");

    if(item.kind === "next"){
      card.classList.add("next-card");
    }else if(item.kind === "upcoming"){
      card.classList.add("upcoming-card");
    }

    const title = card.querySelector(".card-title");
    const pill = card.querySelector(".status-pill");
    const metricValues = card.querySelectorAll(".metric b");

    setText(title, item.name || "—");

    if(pill){
      pill.className = "status-pill " + item.kind;
      pill.textContent = item.status || "Bekliyor";
    }

    if(metricValues[0]){
      metricValues[0].textContent = item.eta || "—";
    }

    if(metricValues[1]){
      const kmLabel = stopDistanceLabel(item.name);
      metricValues[1].textContent = kmLabel || item.fallbackDistance || "—";
      metricValues[1].classList.add("stop-distance-value");
      metricValues[1].dataset.stopName = item.name || "";
      metricValues[1].dataset.distanceMode = kmLabel ? "km" : "waiting";
    }

    /*
      Önemli:
      Aynı durakta her 1.5 saniyede bir gerçek sayıları silme.
      Sadece kart başka durağa döndüyse geçici bekleme işareti koy.
    */
    if(nameChanged && metricValues[2]){
      metricValues[2].textContent = "…";
    }

    if(nameChanged && metricValues[3]){
      metricValues[3].textContent = "…";
    }
  }

  function countsFromDetail(data){
    data = data || {};

    const passengers = Array.isArray(data.passengers) ? data.passengers : [];
    const consignments = Array.isArray(data.consignments) ? data.consignments : [];

    /*
      Bagaj hesabında ana kaynak yolcu/koltuk bagajıdır.
      data.bag_total bazı eski hesaplarda emanetle birleşebildiği için
      önce passengers içinden gerçek koltuk bagajını topluyoruz.
    */
    let seatBagTotal = passengers.reduce((sum, p) => {
      const explicit = Number(p.bag_count || 0);
      const byLocation =
        Number(p.bag_right || 0) +
        Number(p.bag_left_front || 0) +
        Number(p.bag_left_back || 0);

      return sum + Math.max(explicit, byLocation, 0);
    }, 0);

    let bagTotal = seatBagTotal;

    // Eğer passenger listesi gelmemişse mecburen endpoint toplamına düş.
    if((!passengers.length || bagTotal <= 0) && Number(data.seat_bag_count || 0) > 0){
      bagTotal = Number(data.seat_bag_count || 0);
    }else if(!passengers.length && Number(data.bag_total || 0) > 0){
      bagTotal = Number(data.bag_total || 0);
    }

    let offCount = Number(data.off_count || 0);

    if(!Number.isFinite(offCount) || offCount <= 0){
      offCount = passengers.length;
    }

    return {
      offCount: Math.max(0, offCount),
      bagTotal: Math.max(0, bagTotal),
      emanetCount: Math.max(0, consignments.length)
    };
  }

  async function fetchStopDetail(stopName){
    if(!stopName) return null;

    const res = await fetch(`/api/live-stop-detail?stop=${encodeURIComponent(stopName)}&_=${Date.now()}`, {
      method:"GET",
      credentials:"same-origin",
      cache:"no-store",
      headers:{ "Accept":"application/json" }
    });

    const data = await res.json();

    if(!data || !data.ok){
      return null;
    }

    return data;
  }

  function applyCurrentDetail(data){
    const c = countsFromDetail(data);

    const offEl = document.getElementById("liveOffloadCount");

    if(offEl){
      offEl.textContent = c.offCount + " yolcu";
    }

    if(window.ContinueBagEmanet && typeof window.ContinueBagEmanet.apply === "function"){
      window.ContinueBagEmanet.apply({
        seat_bag_count: c.bagTotal,
        emanet_count: c.emanetCount
      });
    }else{
      const bagEl = document.getElementById("liveBagajCount");
      if(bagEl) bagEl.textContent = String(c.bagTotal);
    }

    document.dispatchEvent(new CustomEvent("continueLiveFlowUpdated", {
      detail:{
        current:{
          name: data.stop || currentStopName(),
          off_count: c.offCount,
          seat_bag_count: c.bagTotal,
          bagaj_count: c.bagTotal,
          emanet_count: c.emanetCount,
          consignment_count: c.emanetCount
        }
      }
    }));
  }

  function applyFutureDetail(card, data){
    if(!card || !data) return;

    const c = countsFromDetail(data);
    const metricValues = card.querySelectorAll(".metric b");

    if(metricValues[2]){
      metricValues[2].textContent = String(c.offCount);
    }

    if(metricValues[3]){
      if(c.bagTotal > 0){
        metricValues[3].textContent = String(c.bagTotal);
      }else if(c.emanetCount > 0){
        metricValues[3].textContent = "+" + c.emanetCount + " emanet";
      }else{
        metricValues[3].textContent = "yok";
      }
    }
  }

  async function refreshDetails(flow){
    const now = Date.now();
    const sig = flow.map(x => x.name).join("|");

    if(detailBusy) return;
    if(sig === lastFlowSig && now - lastDetailAt < DETAIL_REFRESH_MS) return;

    detailBusy = true;
    lastFlowSig = sig;
    lastDetailAt = now;

    const seq = ++detailSeq;

    try{
      const details = await Promise.all(
        flow.map(x => fetchStopDetail(x.name).catch(() => null))
      );

      if(seq !== detailSeq) return;

      if(details[0]){
        applyCurrentDetail(details[0]);
      }

      const cards = regularCards();

      for(let i = 1; i < details.length; i++){
        applyFutureDetail(cards[i - 1], details[i]);
      }

    }catch(err){
      console.warn("continue flow detail refresh error", err);
    }finally{
      detailBusy = false;
    }
  }

  function refreshFlow(){
    if(!routeStops.length) return;

    const current = currentStopName();
    let idx = routeIndex(current);

    if(idx < 0){
      return;
    }

    const flow = makeFlow(idx);
    const future = flow.slice(1);
    const cards = regularCards();

    cards.forEach((card, i) => {
      setFutureCardBase(card, future[i]);
    });

    refreshDetails(flow);
  }

  window.ContinueFlowRefresh = {
    refresh: refreshFlow
  };

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", function(){
      startGeoWatch();
      refreshFlow();
    });
  }else{
    startGeoWatch();
    refreshFlow();
  }

  setInterval(refreshFlow, POLL_MS);

  document.addEventListener("visibilitychange", function(){
    if(!document.hidden){
      startGeoWatch();
      refreshFlow();
    }
  });

  window.addEventListener("continueEtaUpdated", function(){
    refreshFlow();
  });
})();
