
/* CONTINUE_PROTOTYPE_LAYOUT_V76_JS */
(function(){
  if(window.CONTINUE_V76_READY) return;
  window.CONTINUE_V76_READY = true;

  const CIRC = 276.46;
  const BOOT = window.CONTINUE_BOOT || {};
  let maxKm = 50;

  function q(sel){
    return document.querySelector(sel);
  }

  function text(v){
    return String(v == null ? "" : v).trim();
  }

  function norm(v){
    return text(v).toLocaleLowerCase("tr-TR").replace(/\s+/g, " ");
  }

  function parseKm(v){
    const s = text(v).replace(",", ".");
    const m = s.match(/-?\d+(?:\.\d+)?/);
    if(!m) return NaN;
    return Number(m[0]);
  }

  function fmtKm(n){
    if(!Number.isFinite(n)) return "—";
    if(n >= 10) return String(Math.round(n));
    return String(Math.round(n * 10) / 10).replace(".0", "");
  }

  function updateClockFallback(){
    const el = document.getElementById("liveClockText");
    if(!el) return;
    if(text(el.textContent) && text(el.textContent) !== "--:--") return;

    const now = new Date();
    const h = String(now.getHours()).padStart(2,"0");
    const m = String(now.getMinutes()).padStart(2,"0");
    el.textContent = h + ":" + m;
  }

  function updateRing(){
    const dist = document.getElementById("liveDistanceValue");
    const ring = document.getElementById("ringFill");
    const ringKm = document.getElementById("ringKm");
    const wrap = document.getElementById("ringWrap");

    if(!dist || !ring || !ringKm || !wrap) return;

    const km = parseKm(dist.textContent);

    if(!Number.isFinite(km)){
      ring.style.strokeDashoffset = CIRC;
      ringKm.textContent = "—";
      wrap.dataset.zone = "far";
      return;
    }

    maxKm = Math.max(maxKm, Math.ceil(km / 10) * 10, 10);

    const ratio = Math.max(0, Math.min(1, 1 - km / maxKm));
    ring.style.strokeDashoffset = String(CIRC * (1 - ratio));
    ringKm.textContent = fmtKm(km);

    if(km <= 5){
      wrap.dataset.zone = "close";
    }else if(km <= 15){
      wrap.dataset.zone = "mid";
    }else{
      wrap.dataset.zone = "far";
    }
  }

  function updateRouteProgress(){
    const stops = Array.isArray(BOOT.routeStops) ? BOOT.routeStops : [];
    const cur = text(document.getElementById("liveCurrentStopName")?.textContent);
    const bar = document.getElementById("routeBar");
    const pct = document.getElementById("distPct");
    const start = document.getElementById("routeStartLabel");
    const end = document.getElementById("routeEndLabel");

    if(start && stops.length) start.textContent = stops[0];
    if(end && stops.length) end.textContent = stops[stops.length - 1];

    if(!bar || !pct || !stops.length || !cur) return;

    const idx = stops.findIndex(s => norm(s) === norm(cur));
    if(idx < 0 || stops.length < 2) return;

    const p = Math.max(0, Math.min(100, Math.round((idx / (stops.length - 1)) * 100)));
    bar.style.width = p + "%";
    pct.textContent = "%" + p + " tamamlandı";
  }

  function syncTopStatus(){
    const top = document.getElementById("liveTopStatusText");
    const eta = document.getElementById("liveEtaValue");
    if(!top || !eta) return;

    const v = text(eta.textContent);
    if(!v || v === "-" || v === "—") return;

    if(/geç/i.test(v)){
      top.textContent = v;
      top.classList.remove("green");
      top.classList.add("red");
    }else if(/erken/i.test(v)){
      top.textContent = v;
      top.classList.remove("red");
      top.classList.add("green");
    }
  }

  function boot(){
    updateClockFallback();
    updateRing();
    updateRouteProgress();
    syncTopStatus();

    const targets = [
      document.getElementById("liveDistanceValue"),
      document.getElementById("liveCurrentStopName"),
      document.getElementById("liveEtaValue")
    ].filter(Boolean);

    if(window.MutationObserver){
      const obs = new MutationObserver(function(){
        updateRing();
        updateRouteProgress();
        syncTopStatus();
      });
      targets.forEach(el => obs.observe(el, {childList:true, characterData:true, subtree:true}));
    }

    setInterval(function(){
      updateClockFallback();
      updateRing();
      updateRouteProgress();
      syncTopStatus();
    }, 1000);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
