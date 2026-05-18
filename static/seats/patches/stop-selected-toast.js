(function(){
  if(window.__stopSelectedToastPatchLoaded) return;
  window.__stopSelectedToastPatchLoaded = true;

  var timer = null;

  function cleanStopName(v){
    return String(v || "")
      .replace(/\s+/g, " ")
      .replace(/^🎯\s*/g, "")
      .replace(/^Seçili\s+durak\s*:\s*/i, "")
      .trim();
  }

  function ensureToast(){
    var el = document.getElementById("stopSelectedToast");
    if(el) return el;

    el = document.createElement("div");
    el.id = "stopSelectedToast";
    el.innerHTML =
      '<div class="stop-toast-inner">' +
        '<div class="stop-toast-icon">✅</div>' +
        '<div class="stop-toast-text">' +
          '<span class="stop-toast-title" data-stop-toast-title>Durak seçildi</span>' +
          '<span class="stop-toast-sub">Biniş yeri otomatik hazır</span>' +
        '</div>' +
      '</div>';

    document.body.appendChild(el);
    return el;
  }

  function showStopToast(stopName){
    stopName = cleanStopName(stopName);
    if(!stopName) return;

    var el = ensureToast();
    var title = el.querySelector("[data-stop-toast-title]");
    if(title) title.textContent = stopName + " seçildi";

    clearTimeout(timer);

    el.classList.remove("show");
    void el.offsetWidth;
    el.classList.add("show");

    try{
      if(navigator.vibrate) navigator.vibrate(35);
    }catch(e){}

    timer = setTimeout(function(){
      el.classList.remove("show");
    }, 2100);
  }

  window.showStopSelectedToast = showStopToast;

  document.addEventListener("muavin:selected-stop-change", function(e){
    var stopName = e && e.detail ? e.detail.stop : "";
    showStopToast(stopName);
  });
})();
