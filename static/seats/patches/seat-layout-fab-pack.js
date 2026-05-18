/* ===== FAB_LEFT_GAP_MOVE ===== */
(function(){
  if(window.__fabLeftGapMoveLoaded) return;
  window.__fabLeftGapMoveLoaded = true;

  function q(sel){
    return document.querySelector(sel);
  }

  function placeFabColumn(){
    var col = q(".fab-column");
    var wrap = q(".deck-wrap");
    var seat43 = q("#seat-43");
    var seat51 = q("#seat-51");

    if(!col || !wrap || !seat43 || !seat51) return;

    col.classList.add("fab-left-gap-moved");

    // Ölçülerin oturması için önce sınıfı verip sonra ölçü alıyoruz.
    var wrapRect = wrap.getBoundingClientRect();
    var r43 = seat43.getBoundingClientRect();
    var r51 = seat51.getBoundingClientRect();
    var cRect = col.getBoundingClientRect();

    var colW = cRect.width || 46;
    var colH = cRect.height || 152;

    var centerX43 = r43.left + (r43.width / 2);
    var centerX51 = r51.left + (r51.width / 2);
    var centerX = (centerX43 + centerX51) / 2;

    var gapTop = r43.bottom + 12;
    var gapBottom = r51.top - 12;
    var centerY = (gapTop + gapBottom) / 2;

    var left = centerX - wrapRect.left - (colW / 2);
    var top = centerY - wrapRect.top - (colH / 2);

    // Güvenli sınırlar
    if(top < 0) top = 0;
    if(left < 0) left = 0;

    col.style.left = Math.round(left) + "px";
    col.style.top = Math.round(top) + "px";
  }

  var timer = null;

  function schedule(){
    clearTimeout(timer);
    timer = setTimeout(placeFabColumn, 80);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", schedule);
  }else{
    schedule();
  }

  window.addEventListener("load", schedule);
  window.addEventListener("resize", schedule);
  window.addEventListener("orientationchange", schedule);
  window.addEventListener("scroll", schedule, true);

  var obs = new MutationObserver(schedule);
  obs.observe(document.documentElement, {
    childList:true,
    subtree:true,
    attributes:true,
    attributeFilter:["class","style"]
  });

  setTimeout(placeFabColumn, 150);
  setTimeout(placeFabColumn, 600);
  setTimeout(placeFabColumn, 1400);
})();

/* ===== FAB_COMPACT_FIT ===== */
(function(){
  function refreshFabPosition(){
    try{
      window.dispatchEvent(new Event("resize"));
    }catch(_){}
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", function(){
      setTimeout(refreshFabPosition, 120);
      setTimeout(refreshFabPosition, 600);
    });
  }else{
    setTimeout(refreshFabPosition, 120);
    setTimeout(refreshFabPosition, 600);
  }

  setTimeout(refreshFabPosition, 1200);
})();

/* ===== FAB_DRIVE_MODE_OVERRIDE_FIX ===== */
(function(){
  if(window.__fabDriveModeOverrideFixReady) return;
  window.__fabDriveModeOverrideFixReady = true;

  function q(sel){
    return document.querySelector(sel);
  }

  function place(){
    var col = q(".fab-column");
    var wrap = q(".deck-wrap");
    var seat43 = q("#seat-43");
    var seat51 = q("#seat-51");

    if(!col || !wrap || !seat43 || !seat51) return;

    col.classList.add("fab-left-gap-moved");

    var wrapRect = wrap.getBoundingClientRect();
    var r43 = seat43.getBoundingClientRect();
    var r51 = seat51.getBoundingClientRect();
    var cRect = col.getBoundingClientRect();

    var colW = cRect.width || 64;
    var colH = cRect.height || 150;

    var centerX43 = r43.left + (r43.width / 2);
    var centerX51 = r51.left + (r51.width / 2);
    var centerX = (centerX43 + centerX51) / 2;

    var gapTop = r43.bottom + 12;
    var gapBottom = r51.top - 12;
    var centerY = (gapTop + gapBottom) / 2;

    var left = centerX - wrapRect.left - (colW / 2);
    var top = centerY - wrapRect.top - (colH / 2);

    if(top < 0) top = 0;
    if(left < 0) left = 0;

    col.style.setProperty("--fab-left-gap-left", Math.round(left) + "px");
    col.style.setProperty("--fab-left-gap-top", Math.round(top) + "px");
  }

  var timer = null;

  function schedule(){
    clearTimeout(timer);
    timer = setTimeout(place, 80);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", schedule);
  }else{
    schedule();
  }

  window.addEventListener("load", schedule);
  window.addEventListener("resize", schedule);
  window.addEventListener("orientationchange", schedule);
  window.addEventListener("scroll", schedule, true);
  window.addEventListener("driveModeChanged", schedule);

  setTimeout(place, 150);
  setTimeout(place, 600);
  setTimeout(place, 1400);
})();
