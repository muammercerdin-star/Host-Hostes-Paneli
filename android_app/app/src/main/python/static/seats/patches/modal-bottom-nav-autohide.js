(function(){
  if(window.__muavinModalBottomNavAutohideV3) return;
  window.__muavinModalBottomNavAutohideV3 = true;

  var lastBottomNav = null;
  var bottomWords = ["durak", "hesap", "emanet", "harita", "anons"];

  function textOf(el){
    return String((el && (el.innerText || el.textContent)) || "")
      .replace(/\s+/g, " ")
      .trim()
      .toLocaleLowerCase("tr-TR");
  }

  function isVisible(el){
    if(!el) return false;
    var cs = getComputedStyle(el);
    if(cs.display === "none" || cs.visibility === "hidden") return false;

    var r = el.getBoundingClientRect();
    return r.width > 20 && r.height > 20 && r.bottom > 0 && r.top < window.innerHeight;
  }

  function isWorkModalText(t){
    var isBulk =
      (t.includes("toplu giriş") || t.includes("toplu giris")) &&
      t.includes("nereden") &&
      t.includes("nereye") &&
      t.includes("adet") &&
      t.includes("bilet");

    var isQuickCash =
      (t.includes("hızlı tahsilat") || t.includes("hizli tahsilat")) &&
      t.includes("adet") &&
      t.includes("tutar") &&
      t.includes("nereden") &&
      t.includes("nereye") &&
      (t.includes("ödeme") || t.includes("odeme"));

    return isBulk || isQuickCash;
  }

  function workModalIsOpen(){
    var nodes = Array.prototype.slice.call(document.querySelectorAll(
      "[role='dialog'], .modal, .modal-content, .sheet, .sheet-panel, .drawer, " +
      "[class*='modal'], [class*='sheet'], [class*='drawer'], [class*='panel'], form, section, div"
    ));

    return nodes.some(function(el){
      if(!isVisible(el)) return false;

      var r = el.getBoundingClientRect();

      // Modal geniş ve yüksek bir panel olmalı
      if(r.width < window.innerWidth * 0.62) return false;
      if(r.height < 250) return false;

      return isWorkModalText(textOf(el));
    });
  }

  function findBottomNav(){
    var nodes = Array.prototype.slice.call(document.querySelectorAll(
      "nav, footer, .bottom-nav, .bottom-bar, .dock, .tabbar, .mobile-nav, " +
      "[class*='bottom'], [class*='dock'], [class*='nav'], div"
    ));

    var best = null;
    var bestScore = -1;

    nodes.forEach(function(el){
      if(!isVisible(el)) return;

      var r = el.getBoundingClientRect();
      var t = textOf(el);

      var count = 0;
      bottomWords.forEach(function(w){
        if(t.includes(w)) count++;
      });

      if(count < 4) return;
      if(r.top < window.innerHeight * 0.55) return;
      if(r.width < window.innerWidth * 0.60) return;
      if(r.height < 45 || r.height > 180) return;

      var score = count * 1000 + r.top;
      if(score > bestScore){
        bestScore = score;
        best = el;
      }
    });

    return best;
  }

  function applyState(){
    var open = workModalIsOpen();

    document.body.classList.toggle("muavin-work-modal-open", open);

    if(open){
      var nav = findBottomNav() || lastBottomNav;
      if(nav){
        lastBottomNav = nav;
        nav.classList.add("muavin-hidden-bottom-nav-by-modal");
      }
    }else{
      document.querySelectorAll(".muavin-hidden-bottom-nav-by-modal").forEach(function(el){
        el.classList.remove("muavin-hidden-bottom-nav-by-modal");
      });
      lastBottomNav = null;
    }
  }

  var scheduled = false;

  function scheduleApply(){
    if(scheduled) return;
    scheduled = true;

    requestAnimationFrame(function(){
      scheduled = false;
      applyState();
    });
  }

  document.addEventListener("click", function(){
    setTimeout(scheduleApply, 30);
    setTimeout(scheduleApply, 160);
    setTimeout(scheduleApply, 420);
  }, true);

  document.addEventListener("input", scheduleApply, true);
  document.addEventListener("change", scheduleApply, true);
  window.addEventListener("resize", scheduleApply);
  window.addEventListener("scroll", scheduleApply, true);

  var obs = new MutationObserver(scheduleApply);
  obs.observe(document.documentElement, {
    childList:true,
    subtree:true,
    attributes:true,
    attributeFilter:["class", "style", "hidden", "aria-hidden"]
  });

  setInterval(applyState, 700);
  scheduleApply();
})();
