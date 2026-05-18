(function(){
  if(window.__stopFlowFocusPatchLoaded) return;
  window.__stopFlowFocusPatchLoaded = true;

  var overlayId = "stopFlowFocusOverlay";
  var memoryKey = "muavin:selectedStop:" + String(window.TRIP_KEY || window.BAG_TRIP || location.pathname);

  function qs(s, root){ return (root || document).querySelector(s); }
  function qsa(s, root){ return Array.prototype.slice.call((root || document).querySelectorAll(s)); }

  function cleanStopName(v){
    v = String(v || "").replace(/\s+/g, " ").trim();
    v = v.replace(/^🎯\s*/g, "");
    v = v.replace(/^Seçili\s+durak\s*:\s*/i, "");
    v = v.replace(/^Sıradaki\s*:\s*/i, "");
    if(!v || v === "-" || v === "—" || v.toLowerCase() === "seçiniz") return "";
    return v;
  }

  function sameStop(a, b){
    return cleanStopName(a).toLocaleLowerCase("tr-TR") === cleanStopName(b).toLocaleLowerCase("tr-TR");
  }

  function ensureOption(select, value){
    if(!select || !value) return;
    var found = false;
    qsa("option", select).forEach(function(o){
      if(sameStop(o.value || o.textContent, value)) found = true;
    });
    if(!found){
      var opt = document.createElement("option");
      opt.value = value;
      opt.textContent = value;
      select.appendChild(opt);
    }
  }

  function getCurrentStop(){
    var fromWindow = cleanStopName(window.__muavinSelectedStop || "");
    if(fromWindow) return fromWindow;

    var alertStop = qs("#alertStop");
    if(alertStop && cleanStopName(alertStop.value)) return cleanStopName(alertStop.value);

    var simpleStop = qs("#seatSimpleStop");
    if(simpleStop && cleanStopName(simpleStop.textContent)) return cleanStopName(simpleStop.textContent);

    var badge = qs("#selectedStopBadge");
    if(badge && cleanStopName(badge.textContent)) return cleanStopName(badge.textContent);

    return cleanStopName(localStorage.getItem(memoryKey) || "");
  }

  function rememberStop(name){
    name = cleanStopName(name);
    if(!name) return;
    window.__muavinSelectedStop = name;
    try{ localStorage.setItem(memoryKey, name); }catch(e){}
  }

  function collectStops(){
    var arr = [];
    var seen = Object.create(null);

    function add(v){
      v = cleanStopName(v);
      if(!v) return;
      var k = v.toLocaleLowerCase("tr-TR");
      if(seen[k]) return;
      seen[k] = true;
      arr.push(v);
    }

    if(Array.isArray(window.STOPS)) window.STOPS.forEach(add);
    if(window.SEATS_BOOT && Array.isArray(window.SEATS_BOOT.stops)) window.SEATS_BOOT.stops.forEach(add);

    qsa("#alertStop option, #pickup option, #dropoff option").forEach(function(o){
      add(o.value || o.textContent);
    });

    qsa(".route-stop, [data-stop-name], [data-stop]").forEach(function(el){
      add(el.getAttribute("data-stop-name") || el.getAttribute("data-stop") || (el.querySelector(".stop-name, .name, strong") || el).textContent);
    });

    return arr;
  }

  function setPickupToSelected(name, force){
    name = cleanStopName(name);
    if(!name) return;

    var pickup = qs("#pickup");
    if(!pickup) return;

    var current = cleanStopName(pickup.value || "");
    if(!force && current) return;

    ensureOption(pickup, name);
    pickup.value = name;
    pickup.dispatchEvent(new Event("change", {bubbles:true}));
  }

  function paintSelectedTexts(name){
    name = cleanStopName(name);
    if(!name) return;

    ["#seatSimpleStop", "#topLiveStop"].forEach(function(sel){
      var el = qs(sel);
      if(el) el.textContent = name;
    });

    var badge = qs("#selectedStopBadge");
    if(badge){
      if((badge.textContent || "").toLocaleLowerCase("tr-TR").includes("seçili durak")){
        badge.textContent = "🎯 Seçili durak: " + name;
      }else{
        badge.textContent = name;
      }
    }
  }

  function applySelectedStop(name){
    name = cleanStopName(name);
    if(!name) return;

    rememberStop(name);

    var alertStop = qs("#alertStop");
    if(alertStop){
      ensureOption(alertStop, name);
      alertStop.value = name;
      alertStop.dispatchEvent(new Event("change", {bubbles:true}));
    }

    if(typeof window.setSelectedStop === "function" && !window.__stopFocusCallingSetSelected){
      try{
        window.__stopFocusCallingSetSelected = true;
        window.setSelectedStop(name, true);
      }catch(e){
        console.warn("setSelectedStop çağrısı geçildi:", e);
      }finally{
        window.__stopFocusCallingSetSelected = false;
      }
    }

    setPickupToSelected(name, true);
    paintSelectedTexts(name);

    document.dispatchEvent(new CustomEvent("muavin:selected-stop-change", {detail:{stop:name}}));
  }

  function buildOverlay(){
    var old = qs("#" + overlayId);
    if(old) return old;

    var ov = document.createElement("div");
    ov.id = overlayId;
    ov.hidden = true;
    ov.innerHTML =
      '<div class="stop-focus-panel" role="dialog" aria-modal="true" aria-label="Durak Akışı">' +
        '<div class="stop-focus-head">' +
          '<div class="stop-focus-topline">' +
            '<button type="button" class="stop-focus-back" data-stop-focus-close>← Koltuk Planı</button>' +
            '<div class="stop-focus-badge">Sadece Durak Akışı</div>' +
          '</div>' +
          '<h2 class="stop-focus-title">Durak Akışı</h2>' +
          '<p class="stop-focus-sub">Seçili durak: <b data-current-stop>—</b></p>' +
        '</div>' +
        '<div class="stop-focus-list" data-stop-focus-list></div>' +
      '</div>';

    document.body.appendChild(ov);

    ov.addEventListener("click", function(e){
      var closeBtn = e.target.closest("[data-stop-focus-close]");
      if(closeBtn){
        e.preventDefault();
        closeStopFocus(true);
        return;
      }

      var card = e.target.closest("[data-stop-choice]");
      if(card){
        e.preventDefault();
        var name = card.getAttribute("data-stop-choice") || "";
        applySelectedStop(name);
        closeStopFocus(true);
      }
    });

    return ov;
  }

  function renderOverlay(){
    var ov = buildOverlay();
    var list = qs("[data-stop-focus-list]", ov);
    var current = getCurrentStop();
    var stops = collectStops();

    qs("[data-current-stop]", ov).textContent = current || "—";
    list.innerHTML = "";

    stops.forEach(function(stop, idx){
      var card = document.createElement("button");
      card.type = "button";
      card.className = "stop-focus-card" + (sameStop(stop, current) ? " is-active" : "");
      card.setAttribute("data-stop-choice", stop);

      var pin = document.createElement("span");
      pin.className = "stop-focus-pin";
      pin.textContent = "📍";

      var main = document.createElement("span");
      main.className = "stop-focus-main";

      var name = document.createElement("span");
      name.className = "stop-focus-name";
      name.textContent = stop;

      var meta = document.createElement("span");
      meta.className = "stop-focus-meta";
      meta.textContent = sameStop(stop, current) ? "Şu an seçili durak" : "Dokun, seç ve koltuk planına dön";

      var select = document.createElement("span");
      select.className = "stop-focus-select";
      select.textContent = sameStop(stop, current) ? "Seçili" : "Seç";

      main.appendChild(name);
      main.appendChild(meta);
      card.appendChild(pin);
      card.appendChild(main);
      card.appendChild(select);
      list.appendChild(card);
    });

    setTimeout(function(){
      var active = qs(".stop-focus-card.is-active", ov);
      if(active) active.scrollIntoView({block:"center"});
    }, 60);
  }

  function openStopFocus(){
    renderOverlay();
    var ov = buildOverlay();
    ov.hidden = false;
    document.documentElement.classList.add("stop-flow-focus-lock");
    document.body.classList.add("stop-flow-focus-lock");
  }

  function closeStopFocus(goSeatPlan){
    var ov = qs("#" + overlayId);
    if(ov) ov.hidden = true;

    document.documentElement.classList.remove("stop-flow-focus-lock");
    document.body.classList.remove("stop-flow-focus-lock");

    if(goSeatPlan){
      setTimeout(function(){
        var target = qs("#deck") || qs(".deck") || qs(".board-card") || qs(".seats-shell");
        if(target) target.scrollIntoView({behavior:"smooth", block:"start"});
      }, 40);
    }
  }

  window.openStopFlowFocus = openStopFocus;
  window.closeStopFlowFocus = closeStopFocus;

  function isBottomDurakButton(el){
    var btn = el.closest("button, a, [role='button'], .tab-btn, .nav-item, .dock-item, .bottom-nav-item");
    if(!btn || btn.closest("#" + overlayId)) return null;

    var text = (btn.innerText || btn.textContent || btn.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim();
    var low = text.toLocaleLowerCase("tr-TR");

    if(!low.includes("durak")) return null;
    if(low.includes("seçili durak")) return null;

    var rect = btn.getBoundingClientRect();
    var classHint = String(btn.className || "").toLocaleLowerCase("tr-TR");
    var parentHint = btn.closest(".bottom-nav, .bottom-bar, .dock, .mobile-nav, [class*='bottom'], [class*='dock']");
    var isBottom = !!parentHint || rect.top > window.innerHeight * 0.58;

    return isBottom ? btn : null;
  }

  document.addEventListener("click", function(e){
    var btn = isBottomDurakButton(e.target);
    if(!btn) return;

    e.preventDefault();
    e.stopPropagation();
    e.stopImmediatePropagation();
    openStopFocus();
  }, true);

  function hookSetSelectedStop(){
    if(typeof window.setSelectedStop !== "function") return;
    if(window.setSelectedStop.__stopFlowFocusHooked) return;

    var old = window.setSelectedStop;
    var wrapped = function(name){
      var ret = old.apply(this, arguments);
      name = cleanStopName(name);
      if(name){
        rememberStop(name);
        setPickupToSelected(name, true);
        paintSelectedTexts(name);
      }
      return ret;
    };
    wrapped.__stopFlowFocusHooked = true;
    window.setSelectedStop = wrapped;
  }

  function hookSeatOpeners(){
    ["openSeat", "openFormWithSeat"].forEach(function(fn){
      if(typeof window[fn] !== "function") return;
      if(window[fn].__stopFlowFocusHooked) return;

      var old = window[fn];
      var wrapped = function(){
        var ret = old.apply(this, arguments);
        setTimeout(function(){
          setPickupToSelected(getCurrentStop(), false);
        }, 80);
        return ret;
      };
      wrapped.__stopFlowFocusHooked = true;
      window[fn] = wrapped;
    });
  }

  function installHooks(){
    hookSetSelectedStop();
    hookSeatOpeners();
  }

  installHooks();
  document.addEventListener("DOMContentLoaded", installHooks);
  setTimeout(installHooks, 300);
  setTimeout(installHooks, 1000);
})();
