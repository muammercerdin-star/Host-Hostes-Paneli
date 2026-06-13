/* CONTINUE_END_TRIP_MODAL_V106_START */
(function(){
  "use strict";

  if(window.__CONTINUE_END_TRIP_MODAL_V106__) return;
  window.__CONTINUE_END_TRIP_MODAL_V106__ = true;

  function ready(fn){
    if(document.readyState === "loading"){
      document.addEventListener("DOMContentLoaded", fn);
    }else{
      fn();
    }
  }

  function tripKey(){
    try{
      return String(
        window.CONTINUE_BOOT && window.CONTINUE_BOOT.tripKey
          ? window.CONTINUE_BOOT.tripKey
          : ""
      );
    }catch(_){
      return "";
    }
  }

  function clearTripLocalMemory(){
    try{
      var key = tripKey();
      if(!key) return;

      var exactKeys = [
        "liveStop:" + key,
        "passedStops:" + key,
        "boardsMap:" + key,
        "standingTotals:" + key,
        "standingItems:" + key,
        "continueTripStop:" + key,
        "continueTripStop:last",
        "stopFlowSummary:" + key,
        "stopFlowLiveEvents:" + key
      ];

      exactKeys.forEach(function(k){
        localStorage.removeItem(k);
      });

      Object.keys(localStorage).forEach(function(k){
        if(
          k.indexOf(key) !== -1 &&
          (
            k.indexOf("liveStop:") === 0 ||
            k.indexOf("passedStops:") === 0 ||
            k.indexOf("boardsMap:") === 0 ||
            k.indexOf("standingTotals:") === 0 ||
            k.indexOf("standingItems:") === 0 ||
            k.indexOf("continueTripStop:") === 0 ||
            k.indexOf("stopFlowSummary:") === 0 ||
            k.indexOf("stopFlowLiveEvents:") === 0
          )
        ){
          localStorage.removeItem(k);
        }
      });
    }catch(_){}
  }

  ready(function(){
    var form = document.getElementById("endTripForm");
    var overlay = document.getElementById("endTripOverlay");
    var cancel = document.getElementById("endTripCancel");
    var ok = document.getElementById("endTripOk");

    if(!form || !overlay || !cancel || !ok) return;

    if(form.dataset.v106EndTripBound === "1") return;
    form.dataset.v106EndTripBound = "1";

    var confirmed = false;

    function openModal(){
      overlay.classList.add("show");
      overlay.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
    }

    function closeModal(){
      overlay.classList.remove("show");
      overlay.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
    }

    form.addEventListener("submit", function(e){
      if(confirmed) return;
      e.preventDefault();
      openModal();
    });

    cancel.addEventListener("click", closeModal);

    overlay.addEventListener("click", function(e){
      if(e.target === overlay) closeModal();
    });

    document.addEventListener("keydown", function(e){
      if(e.key === "Escape" && overlay.classList.contains("show")){
        closeModal();
      }
    });

    ok.addEventListener("click", function(){
      confirmed = true;
      clearTripLocalMemory();
      closeModal();
      form.submit();
    });

    window.ContinueEndTripModalV106 = {
      open: openModal,
      close: closeModal,
      clearTripLocalMemory: clearTripLocalMemory
    };
  });
})();
/* CONTINUE_END_TRIP_MODAL_V106_END */
