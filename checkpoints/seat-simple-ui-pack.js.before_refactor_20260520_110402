/* ===== seat-simple-open-mode-script ===== */
(function(){
  if(window.__seatSimpleOpenModeReady) return;
  window.__seatSimpleOpenModeReady = true;

  function getTripKey(){
    try{
      return (window.SEATS_BOOT && window.SEATS_BOOT.tripKey) || window.BAG_TRIP || "default";
    }catch(_){
      return "default";
    }
  }

  function key(){
    return "seatUiMode:" + getTripKey();
  }

  function readMode(){
    try{
      return localStorage.getItem(key()) || "simple";
    }catch(_){
      return "simple";
    }
  }

  function writeMode(mode){
    try{
      localStorage.setItem(key(), mode);
    }catch(_){}
  }

  function applyMode(mode){
    const simple = mode !== "advanced";
    document.documentElement.classList.toggle("seat-simple-mode", simple);
    document.body.classList.toggle("seat-simple-mode", simple);

    const btn = document.getElementById("seatSimpleModeToggle");
    if(btn){
      btn.innerHTML = simple
        ? "⚙️ Gelişmiş ekranı aç"
        : "💺 Sade koltuk moduna dön";
      btn.setAttribute("aria-pressed", simple ? "true" : "false");
    }

    try{
      if(typeof renderRouteStrip === "function") renderRouteStrip();
      if(typeof updateCompactHeader === "function") updateCompactHeader();
    }catch(_){}
  }

  function ensureButton(){
    if(document.getElementById("seatSimpleModeToggle")) return;

    const host = document.querySelector(".board-inner") || document.querySelector(".seats-shell");
    if(!host) return;

    const btn = document.createElement("button");
    btn.id = "seatSimpleModeToggle";
    btn.type = "button";
    btn.className = "seat-simple-toggle";
    btn.addEventListener("click", function(){
      const current = readMode();
      const next = current === "advanced" ? "simple" : "advanced";
      writeMode(next);
      applyMode(next);
    });

    host.insertBefore(btn, host.firstChild);
  }

  function boot(){
    ensureButton();
    applyMode(readMode());

    setTimeout(function(){ applyMode(readMode()); }, 250);
    setTimeout(function(){ applyMode(readMode()); }, 900);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();

/* ===== seat-simple-summary-polish-script ===== */
(function(){
  if(window.__seatSimpleSummaryPolishReady) return;
  window.__seatSimpleSummaryPolishReady = true;

  function q(sel){
    return document.querySelector(sel);
  }

  function boot(){
    const board = q(".board-inner");
    if(!board) return;

    let box = q("#seatSimpleSummary");
    if(!box){
      box = document.createElement("div");
      box.id = "seatSimpleSummary";
      box.className = "seat-simple-summary";
      box.innerHTML = `
        <div class="seat-simple-summary-top">
          <div class="seat-simple-route" id="seatSimpleRoute">—</div>
          <div class="seat-simple-status"><span>●</span><span>Sade Mod</span></div>
        </div>

        <div class="seat-simple-summary-grid">
          <div class="seat-simple-mini">
            <small>Durak</small>
            <b id="seatSimpleStop">—</b>
          </div>
          <div class="seat-simple-mini">
            <small>Doluluk</small>
            <b class="ok" id="seatSimpleOcc">0/0</b>
          </div>
          <div class="seat-simple-mini">
            <small>Hız</small>
            <b class="speed" id="seatSimpleSpeed">0 km/h</b>
          </div>
        </div>
      `;

      const toggle = q("#seatSimpleModeToggle");
      if(toggle && toggle.parentNode === board){
        toggle.insertAdjacentElement("afterend", box);
      }else{
        board.insertBefore(box, board.firstChild);
      }
    }

    update();
    setInterval(update, 1000);
  }

  function readText(sel){
    const el = q(sel);
    return (el && el.textContent ? el.textContent.trim() : "");
  }

  function update(){
    const bootData = window.SEATS_BOOT || {};

    const route = bootData.routeName || "—";
    const routeEl = q("#seatSimpleRoute");
    if(routeEl) routeEl.textContent = route;

    let stop = readText("#selectedStopBadge") || "—";
    if(!stop || stop === "-") stop = "—";

    const stopEl = q("#seatSimpleStop");
    if(stopEl) stopEl.textContent = stop;

    let filled = readText("#voiceSeatFilled") || readText("#driveVoiceFilled") || "";
    let empty  = readText("#voiceSeatEmpty")  || readText("#driveVoiceEmpty")  || "";

    if(!filled){
      try{
        filled = String(Object.values(bootData.assigned || {}).filter(Boolean).length);
      }catch(_){
        filled = "0";
      }
    }

    if(!empty){
      try{
        const total = Object.keys(bootData.seatPositions || {}).length;
        empty = String(Math.max(total - Number(filled || 0), 0));
      }catch(_){
        empty = "0";
      }
    }

    const total = Number(filled || 0) + Number(empty || 0);
    const occEl = q("#seatSimpleOcc");
    if(occEl) occEl.textContent = `${filled}/${total || 0}`;

    let speed = "";
    const spVal = q("#spVal");
    if(spVal && spVal.textContent.trim()){
      speed = `${spVal.textContent.trim()} km/h`;
    }else{
      speed = readText("#topSpeed") || "0 km/h";
    }

    const speedEl = q("#seatSimpleSpeed");
    if(speedEl) speedEl.textContent = speed || "0 km/h";
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }

  setTimeout(boot, 300);
  setTimeout(update, 900);
})();

/* ===== seat-hide-bottom-menu-on-modal-script ===== */
(function(){
  if(window.__seatHideBottomMenuOnModalReady) return;
  window.__seatHideBottomMenuOnModalReady = true;

  function q(sel){
    return document.querySelector(sel);
  }

  function isVisible(el){
    if(!el) return false;

    const cs = window.getComputedStyle(el);

    if(cs.display === "none") return false;
    if(cs.visibility === "hidden") return false;
    if(cs.opacity === "0") return false;

    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  function sync(){
    const seatModal = q("#seatModal");
    const seatBackdrop = q("#seatBackdrop");

    const open = isVisible(seatModal) || isVisible(seatBackdrop);

    document.documentElement.classList.toggle("seat-modal-open", open);
    document.body.classList.toggle("seat-modal-open", open);
  }

  function boot(){
    sync();

    const watchList = [
      "#seatModal",
      "#seatBackdrop",
      "#btnSeatClose",
      "#btnSeatSave",
      "#btnSeatOffload"
    ];

    const observer = new MutationObserver(sync);

    watchList.forEach(sel => {
      const el = q(sel);
      if(!el) return;

      try{
        observer.observe(el, {
          attributes:true,
          attributeFilter:["style","class","hidden"]
        });
      }catch(_){}
    });

    document.addEventListener("click", function(){
      setTimeout(sync, 20);
      setTimeout(sync, 120);
      setTimeout(sync, 300);
    }, true);

    window.addEventListener("resize", sync);
    window.addEventListener("orientationchange", function(){
      setTimeout(sync, 250);
    });

    setInterval(sync, 500);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }
})();
