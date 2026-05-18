(function(){
  if(window.__manualTicketSystemCleanReady) return;
  window.__manualTicketSystemCleanReady = true;

  function tripKey(){
    try{
      return String(
        window.BAG_TRIP ||
        (window.SEATS_BOOT && window.SEATS_BOOT.tripKey) ||
        "default"
      );
    }catch(_){
      return "default";
    }
  }

  function sigKey(){
    return "manualTicketBadgeSigs:" + tripKey();
  }

  function legacyKey(){
    return "manualTicketBadges:" + tripKey();
  }

  function loadMap(){
    try{
      const raw = localStorage.getItem(sigKey()) || "{}";
      const obj = JSON.parse(raw);
      return obj && typeof obj === "object" && !Array.isArray(obj) ? obj : {};
    }catch(_){
      return {};
    }
  }

  function saveMap(obj){
    try{
      localStorage.setItem(sigKey(), JSON.stringify(obj || {}));
    }catch(_){}
  }

  function clearLegacy(){
    try{
      localStorage.setItem(legacyKey(), "[]");
    }catch(_){}
  }

  function seatEl(no){
    return document.getElementById("seat-" + no);
  }

  function ensureBadge(el){
    if(!el) return;

    let b = el.querySelector(".manual-ticket-badge");
    if(!b){
      b = document.createElement("span");
      b.className = "manual-ticket-badge";
      b.textContent = "🎫";
      b.title = "Biletsiz yolcu";
      el.appendChild(b);
    }
  }

  function seatAssigned(no){
    const el = seatEl(no);
    if(!el) return false;

    return (
      el.classList.contains("isAssigned") ||
      el.classList.contains("male") ||
      el.classList.contains("female")
    );
  }

  function seatSignature(no){
    const label = document.getElementById("label-" + no);
    const text = label ? String(label.textContent || "").replace(/\s+/g, " ").trim() : "";

    if(text) return text;

    if(seatAssigned(no)){
      return "__assigned__";
    }

    return "";
  }

  function applyBadges(){
    clearLegacy();

    const map = loadMap();
    let changed = false;

    document.querySelectorAll(".seat[id^='seat-']").forEach(function(el){
      const no = String(el.dataset.seat || (el.id || "").replace(/^seat-/, "") || "").trim();
      if(!no) return;

      ensureBadge(el);

      const savedSig = map[no] || "";
      const curSig = seatSignature(no);

      el.classList.remove("has-manual-ticket-badge");
      el.classList.remove("has-manual-ticket-badge-sig");

      if(savedSig && seatAssigned(no) && curSig && savedSig === curSig){
        el.classList.add("has-manual-ticket-badge-sig");
        return;
      }

      /*
        Koltuk dolu ama imza değişmişse yeni yolcu gelmiştir.
        Eski 🎫 işareti silinir.
      */
      if(savedSig && seatAssigned(no) && curSig && savedSig !== curSig){
        delete map[no];
        changed = true;
      }
    });

    if(changed){
      saveMap(map);
    }
  }

  window.markBiletsizSeatBadges = function(seats){
    const list = (Array.isArray(seats) ? seats : [seats])
      .map(x => Number(x))
      .filter(x => Number.isInteger(x) && x > 0);

    const map = loadMap();
    const done = [];
    const failed = [];

    list.forEach(function(no){
      const el = seatEl(no);

      if(!el || !seatAssigned(no)){
        failed.push(no);
        return;
      }

      ensureBadge(el);

      const sig = seatSignature(no);

      if(!sig){
        failed.push(no);
        return;
      }

      map[String(no)] = sig;
      el.classList.add("has-manual-ticket-badge-sig");
      el.classList.remove("has-manual-ticket-badge");
      done.push(no);
    });

    saveMap(map);
    clearLegacy();

    setTimeout(applyBadges, 150);
    setTimeout(applyBadges, 600);
    setTimeout(applyBadges, 1200);

    return { done, failed };
  };

  window.clearBiletsizSeatBadges = function(seats){
    const list = (Array.isArray(seats) ? seats : [seats])
      .map(x => Number(x))
      .filter(x => Number.isInteger(x) && x > 0);

    const map = loadMap();

    list.forEach(function(no){
      delete map[String(no)];

      const el = seatEl(no);
      if(el){
        el.classList.remove("has-manual-ticket-badge");
        el.classList.remove("has-manual-ticket-badge-sig");
      }
    });

    saveMap(map);
    clearLegacy();
    applyBadges();

    return true;
  };

  window.refreshManualTicketBadges = applyBadges;

  let timer = null;

  function schedule(){
    clearTimeout(timer);
    timer = setTimeout(applyBadges, 180);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", schedule);
  }else{
    schedule();
  }

  window.addEventListener("load", schedule);

  document.addEventListener("click", function(){
    setTimeout(schedule, 250);
    setTimeout(schedule, 900);
    setTimeout(schedule, 1600);
  }, true);

  document.addEventListener("change", schedule, true);

  const obs = new MutationObserver(schedule);
  obs.observe(document.documentElement, {
    childList:true,
    subtree:true,
    attributes:true,
    attributeFilter:["class"]
  });

  setTimeout(applyBadges, 500);
  setTimeout(applyBadges, 1400);
})();
