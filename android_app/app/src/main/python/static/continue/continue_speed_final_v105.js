/* V105_SPEED_FINAL_POLISH_START */
(function(){
  "use strict";

  if(window.__MUAVIN_V105_SPEED_FINAL__) return;
  window.__MUAVIN_V105_SPEED_FINAL__ = true;

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function norm(v){
    return String(v || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function findSpeedCard(){
    var cells = qa(".v99-gauges .v99-gauge-cell");
    for(var i = 0; i < cells.length; i++){
      var label = q(".v99-gauge-label", cells[i]);
      if(norm(text(label)) === "HIZ"){
        return cells[i];
      }
    }
    return null;
  }

  function parseSpeed(v){
    var raw = String(v || "")
      .replace(",", ".")
      .replace(/km\/sa|km\/h|kmh|km|sa/gi, " ")
      .trim();

    var m = raw.match(/-?\d+(\.\d+)?/);
    if(!m) return 0;

    var n = Number(m[0]);
    if(!Number.isFinite(n)) n = 0;
    if(n < 0) n = 0;
    if(n > 180) n = 180;
    return n;
  }

  function readSpeed(){
    var visible = q("#v99SpeedVal");
    var hidden = q("#liveSpeedText");

    var n = parseSpeed(text(visible));
    if(!n && hidden){
      n = parseSpeed(text(hidden));
    }

    return n;
  }

  function ensure(card){
    if(!card) return;

    card.classList.add("v105-speed-card");

    if(!q(".v105-speed-track", card)){
      var track = document.createElement("div");
      track.className = "v105-speed-track";
      track.innerHTML = '<div class="v105-speed-fill"></div><div class="v105-speed-dot"></div>';
      card.appendChild(track);
    }
  }

  function paint(){
    var card = findSpeedCard();
    if(!card) return;

    ensure(card);

    var speed = readSpeed();
    var capped = Math.max(0, Math.min(speed, 140));
    var pct = capped / 140;
    var pctText = Math.max(4, pct * 100).toFixed(1) + "%";

    card.style.setProperty("--v105-speed-pct", pctText);

    var fill = q(".v105-speed-fill", card);
    if(fill){
      fill.style.width = pctText;
    }

    card.classList.toggle("v105-speed-low", speed < 50);
    card.classList.toggle("v105-speed-high", speed >= 95);
  }

  function boot(){
    paint();

    try{
      var a = q("#v99SpeedVal");
      if(a && !a.dataset.v105Observed){
        a.dataset.v105Observed = "1";
        new MutationObserver(paint).observe(a, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }

      var b = q("#liveSpeedText");
      if(b && !b.dataset.v105Observed){
        b.dataset.v105Observed = "1";
        new MutationObserver(paint).observe(b, {
          childList:true,
          subtree:true,
          characterData:true
        });
      }
    }catch(_){}
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  }else{
    boot();
  }

  window.addEventListener("load", boot);

  var tries = 80;
  var timer = setInterval(function(){
    boot();
    paint();
    tries--;
    if(tries <= 0) clearInterval(timer);
  }, 500);

  window.MuavinV105SpeedFinal = {
    boot: boot,
    paint: paint
  };
})();
/* V105_SPEED_FINAL_POLISH_END */
