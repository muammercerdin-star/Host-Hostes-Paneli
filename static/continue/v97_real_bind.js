
/* V97_REAL_BIND_JS_V98 */
(function(){
  const CIRC = 276.46;
  const BOOT = window.CONTINUE_BOOT || {};
  let maxKm = 48;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(sel){
    const el = q(sel);
    return el ? String(el.textContent || "").trim() : "";
  }

  function setText(sel, value){
    const el = q(sel);
    if(el) el.textContent = value;
  }

  function parseKm(raw){
    let s = String(raw || "").trim().toLocaleLowerCase("tr-TR");
    if(!s || s === "—" || s === "-") return NaN;

    s = s.replace(",", ".");

    const n = Number((s.match(/-?\d+(\.\d+)?/) || [""])[0]);
    if(!Number.isFinite(n)) return NaN;

    if(/\bm\b/.test(s) && !/\bkm\b/.test(s)){
      return n / 1000;
    }

    return n;
  }

  function formatRingNumber(km){
    if(!Number.isFinite(km)) return "—";
    if(km <= 0) return "0";
    if(km < 1) return km.toFixed(2);
    if(km < 10) return km.toFixed(1).replace(".0", "");
    return String(Math.round(km));
  }

  function colorRing(km, ring, ringKm){
    if(!ring || !ringKm) return;

    ring.classList.remove("urgent");

    if(Number.isFinite(km) && km <= 5){
      ring.style.stroke = "#e03030";
      ring.style.filter = "drop-shadow(0 0 8px #e03030)";
      ring.classList.add("urgent");
      ringKm.style.color = "#e03030";
      ringKm.style.textShadow = "0 0 18px #e03030";
    }else if(Number.isFinite(km) && km <= 15){
      ring.style.stroke = "#e08820";
      ring.style.filter = "drop-shadow(0 0 8px #e08820)";
      ringKm.style.color = "#e08820";
      ringKm.style.textShadow = "0 0 12px #e08820";
    }else{
      ring.style.stroke = "#3a8bff";
      ring.style.filter = "drop-shadow(0 0 6px #3a8bff)";
      ringKm.style.color = "#3a8bff";
      ringKm.style.textShadow = "0 0 10px #3a8bff";
    }
  }

  function updateRing(){
    const distRaw = text("#liveDistanceValue");
    const km = parseKm(distRaw);
    const ring = q("#ringFill");
    const ringKm = q("#ringKm");

    if(!ring || !ringKm) return;

    if(!Number.isFinite(km)){
      ring.style.strokeDashoffset = CIRC;
      ringKm.textContent = "—";
      return;
    }

    if(km > maxKm){
      maxKm = Math.max(10, Math.ceil(km / 10) * 10);
    }

    const ratio = Math.max(0, Math.min(1, 1 - (km / maxKm)));
    ring.style.strokeDashoffset = CIRC * (1 - ratio);
    ringKm.textContent = formatRingNumber(km);
    colorRing(km, ring, ringKm);
  }

  function updateSpeed(){
    const raw = text("#liveSpeedText");
    const n = Number((raw.match(/\d+/) || ["0"])[0]);
    setText("#v97SpeedVal", Number.isFinite(n) ? String(n) : "0");
  }

  function updateEta(){
    const eta = text("#liveEtaValue");
    if(eta){
      setText("#v97EtaValue", eta);
    }

    const status = text("#liveTopStatusText");
    const sub = q("#v97StatusSub");
    if(sub){
      if(/erken/i.test(status)) sub.textContent = "erken";
      else if(/ge[cç]/i.test(status)) sub.textContent = "gecikme";
      else sub.textContent = "canlı takip";
    }
  }

  function norm(v){
    return String(v || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/ı/g, "i")
      .replace(/İ/g, "i")
      .replace(/\s+/g, " ")
      .trim();
  }

  function updateRouteProgress(){
    const stops = Array.isArray(BOOT.routeStops) ? BOOT.routeStops : [];
    const live = norm(text("#liveCurrentStopName"));

    const pctEl = q("#routePct");
    const bar = q("#routeBar");

    if(!stops.length || !live){
      if(pctEl) pctEl.textContent = "—";
      if(bar) bar.style.width = "0%";
      return;
    }

    let idx = stops.findIndex(s => norm(s) === live);

    if(idx < 0){
      const current = Array.from(document.querySelectorAll(".v97-tl-card.live-card h3"))
        .map(x => norm(x.textContent))
        .find(Boolean);
      if(current){
        idx = stops.findIndex(s => norm(s) === current);
      }
    }

    if(idx < 0){
      if(pctEl) pctEl.textContent = "—";
      return;
    }

    const denom = Math.max(1, stops.length - 1);
    const pct = Math.max(0, Math.min(100, Math.round((idx / denom) * 100)));

    if(pctEl) pctEl.textContent = "%" + pct + " tamamlandı";
    if(bar) bar.style.width = pct + "%";
  }

  function updateClock(){
    const d = new Date();
    const h = String(d.getHours()).padStart(2, "0");
    const m = String(d.getMinutes()).padStart(2, "0");
    setText("#liveClockText", h + ":" + m);
  }

  function sync(){
    updateClock();
    updateSpeed();
    updateEta();
    updateRing();
    updateRouteProgress();
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", sync);
  }else{
    sync();
  }

  setInterval(sync, 700);

  window.addEventListener("continueEtaUpdated", sync);
  window.addEventListener("storage", sync);
})();
