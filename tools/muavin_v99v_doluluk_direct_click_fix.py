from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99V DOLULUK DIRECT CLICK FIX =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99v-doluluk-direct-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski V99V bloğu varsa temizle
s = re.sub(
    r"\n?/\* V99V_DOLULUK_DIRECT_CLICK_START \*/.*?/\* V99V_DOLULUK_DIRECT_CLICK_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

bridge = r'''

/* V99V_DOLULUK_DIRECT_CLICK_START */
(function(){
  "use strict";

  if(window.__V99V_DOLULUK_DIRECT_CLICK__) return;
  window.__V99V_DOLULUK_DIRECT_CLICK__ = true;

  var LABEL_SEL = ".v99-gauge-label, .v99-stat-label, .v99-info-label, .card-label, .label, .l";

  function norm(v){
    return String(v || "")
      .toLocaleUpperCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function isTopWord(t){
    t = norm(t);
    return t === "HIZ" || t === "DOLULUK" || t === "DURUM";
  }

  function labelTypeFrom(el){
    if(!el) return "";

    if(el.matches && el.matches(LABEL_SEL)){
      var own = norm(el.textContent);
      if(isTopWord(own)) return own;
    }

    var labels = Array.prototype.slice.call(el.querySelectorAll ? el.querySelectorAll(LABEL_SEL) : []);
    var found = [];

    labels.forEach(function(lab){
      var t = norm(lab.textContent);
      if(isTopWord(t) && found.indexOf(t) < 0){
        found.push(t);
      }
    });

    if(found.length === 1) return found[0];
    return "";
  }

  function bestCardForLabel(label){
    var type = labelTypeFrom(label);
    if(!type) return label;

    var best = label;
    var el = label.parentElement;
    var guard = 0;

    while(el && guard < 9){
      guard++;

      if(el === document.body || el === document.documentElement) break;

      var t = labelTypeFrom(el);
      var rect = el.getBoundingClientRect ? el.getBoundingClientRect() : null;

      if(t === type && rect && rect.width >= 45 && rect.height >= 35){
        best = el;
      }

      /*
        Parent içine HIZ + DOLULUK + DURUM beraber girdiyse
        artık ortak satıra çıkmışız demektir, burada dur.
      */
      var allText = norm(el.textContent);
      if(
        allText.indexOf("HIZ") >= 0 &&
        allText.indexOf("DOLULUK") >= 0 &&
        allText.indexOf("DURUM") >= 0
      ){
        break;
      }

      el = el.parentElement;
    }

    return best;
  }

  function rectHas(rect, x, y){
    return rect &&
      x >= rect.left &&
      x <= rect.right &&
      y >= rect.top &&
      y <= rect.bottom;
  }

  function hitTopCardByTarget(target){
    var el = target;

    for(var i = 0; el && i < 8; i++, el = el.parentElement){
      if(el === document.body || el === document.documentElement) break;

      var t = labelTypeFrom(el);
      if(t) return t;
    }

    return "";
  }

  function hitTopCardByGeometry(ev){
    var x = ev.clientX;
    var y = ev.clientY;

    var labels = Array.prototype.slice.call(document.querySelectorAll(LABEL_SEL));

    for(var i = 0; i < labels.length; i++){
      var type = labelTypeFrom(labels[i]);
      if(!isTopWord(type)) continue;

      var card = bestCardForLabel(labels[i]);
      var rect = card && card.getBoundingClientRect ? card.getBoundingClientRect() : null;

      if(rectHas(rect, x, y)){
        return type;
      }
    }

    return "";
  }

  function openDolulukPanel(){
    var api = window.MuavinV99OccupancyPanel;

    if(api && typeof api.open === "function"){
      api.open();
      return true;
    }

    if(api && typeof api.show === "function"){
      api.show();
      return true;
    }

    if(api && typeof api.refresh === "function"){
      api.refresh();
    }

    return false;
  }

  function markDolulukVisual(){
    document.querySelectorAll(".v99v-doluluk-direct").forEach(function(el){
      el.classList.remove("v99v-doluluk-direct");
    });

    document.querySelectorAll(LABEL_SEL).forEach(function(label){
      if(labelTypeFrom(label) === "DOLULUK"){
        var card = bestCardForLabel(label);
        if(card) card.classList.add("v99v-doluluk-direct");
      }
    });
  }

  document.addEventListener("click", function(ev){
    var target = ev.target;

    if(target && target.closest && target.closest(".v99m-panel, .v99m-overlay, .v99m-seat-detail")){
      return;
    }

    var type = hitTopCardByTarget(target) || hitTopCardByGeometry(ev);

    if(type === "DOLULUK"){
      ev.preventDefault();
      ev.stopPropagation();
      ev.stopImmediatePropagation();

      openDolulukPanel();
      return false;
    }

    if(type === "HIZ" || type === "DURUM"){
      ev.stopPropagation();
      ev.stopImmediatePropagation();
      return false;
    }
  }, true);

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", markDolulukVisual);
  }else{
    markDolulukVisual();
  }

  window.addEventListener("load", markDolulukVisual);
  setInterval(markDolulukVisual, 1500);

})();
/* V99V_DOLULUK_DIRECT_CLICK_END */
'''

s = s.rstrip() + bridge + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "V99V_DOLULUK_DIRECT_CLICK_START",
    "hitTopCardByGeometry",
    "openDolulukPanel",
    "type === \"DOLULUK\"",
    "type === \"HIZ\" || type === \"DURUM\"",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99V tamam. Tarayıcıda /continue-trip?v=v99v ile yenile.")
