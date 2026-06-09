
/* CONTINUE_RING_V75 */
(function(){
  if(window.CONTINUE_RING_V75_READY) return;
  window.CONTINUE_RING_V75_READY = true;

  const CIRC = 276.46;
  let maxKm = 50;

  function q(sel){
    return document.querySelector(sel);
  }

  function parseKm(v){
    const s = String(v || "").replace(",", ".").trim();
    const m = s.match(/-?\d+(?:\.\d+)?/);
    if(!m) return NaN;
    return Number(m[0]);
  }

  function fmtKm(n){
    if(!Number.isFinite(n)) return "—";
    if(n >= 10) return String(Math.round(n));
    return String(Math.round(n * 10) / 10).replace(".0", "");
  }

  function ensureRing(){
    const card = document.getElementById("liveCurrentCard");
    const head = card ? card.querySelector(".card-head") : null;
    if(!card || !head) return null;

    let wrap = document.getElementById("continueRingV75");
    if(wrap) return wrap;

    wrap = document.createElement("div");
    wrap.id = "continueRingV75";
    wrap.className = "v75-ring-wrap";
    wrap.innerHTML = `
      <svg class="v75-ring-svg" viewBox="0 0 110 110" aria-hidden="true">
        <circle class="v75-ring-track" cx="55" cy="55" r="44"></circle>
        <circle class="v75-ring-fill" id="continueRingFillV75" cx="55" cy="55" r="44"
          stroke-dasharray="${CIRC}" stroke-dashoffset="${CIRC}"></circle>
      </svg>
      <div class="v75-ring-center">
        <div class="v75-ring-km" id="continueRingKmV75">—</div>
        <div class="v75-ring-label">KM</div>
      </div>
    `;

    head.insertBefore(wrap, head.firstChild);
    return wrap;
  }

  function updateRing(){
    const wrap = ensureRing();
    const dist = document.getElementById("liveDistanceValue");
    const fill = document.getElementById("continueRingFillV75");
    const kmEl = document.getElementById("continueRingKmV75");

    if(!wrap || !dist || !fill || !kmEl) return;

    const km = parseKm(dist.textContent);
    if(!Number.isFinite(km)){
      kmEl.textContent = "—";
      fill.style.strokeDashoffset = CIRC;
      wrap.dataset.zone = "far";
      return;
    }

    maxKm = Math.max(maxKm, Math.ceil(km / 10) * 10, 10);

    const ratio = Math.max(0, Math.min(1, 1 - (km / maxKm)));
    const offset = CIRC * (1 - ratio);

    fill.style.strokeDashoffset = String(offset);
    kmEl.textContent = fmtKm(km);

    if(km <= 5){
      wrap.dataset.zone = "close";
    }else if(km <= 15){
      wrap.dataset.zone = "mid";
    }else{
      wrap.dataset.zone = "far";
    }
  }

  function boot(){
    ensureRing();
    updateRing();

    const dist = document.getElementById("liveDistanceValue");
    if(dist && window.MutationObserver){
      const obs = new MutationObserver(updateRing);
      obs.observe(dist, {childList:true, characterData:true, subtree:true});
    }

    setInterval(updateRing, 1000);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
