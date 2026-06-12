from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99R SADECE DOLULUK TIKLAMA KİLİDİ =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99r-doluluk-gate-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski denemeleri temizle
for rgx in [
    r"\n?/\* V99Q_ONLY_OCCUPANCY_CLICK_START \*/.*?/\* V99Q_ONLY_OCCUPANCY_CLICK_END \*/\n?",
    r"\n?/\* V99R_ONLY_DOLULUK_CLICK_GATE_START \*/.*?/\* V99R_ONLY_DOLULUK_CLICK_GATE_END \*/\n?",
]:
    s = re.sub(rgx, "\n", s, flags=re.S)

gate = r'''

/* V99R_ONLY_DOLULUK_CLICK_GATE_START */
(function(){
  "use strict";

  function norm(x){
    return String(x || "")
      .replace(/İ/g, "i")
      .replace(/I/g, "ı")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function text(el){
    if(!el) return "";
    return norm(el.innerText || el.textContent || "");
  }

  function isElement(x){
    return x && x.nodeType === 1;
  }

  function isSafeControl(target){
    if(!isElement(target)) return false;

    /*
      Yenile, kapat, alt menü, link, form, koltuk gibi gerçek kontrolleri bozma.
      Sadece üst bilgi kartlarındaki yanlış panel açılmasını kesiyoruz.
    */
    return !!target.closest(
      "a[href],button,input,select,textarea," +
      ".v99-dock,.v99-seat,.v99-seat-cell,.v99-bus-seat," +
      ".v99-sheet-close,.v99-close,.v99-refresh,.v99-refresh-btn," +
      "#v99OccRefresh,#v99OccClose"
    );
  }

  function smallRole(target){
    var el = target;

    for(var i = 0; i < 12 && el && el !== document.body; i++, el = el.parentElement){
      var t = text(el);
      if(!t) continue;

      /*
        Çok büyük container tüm satırı içerir:
        HIZ + DOLULUK + DURUM beraber olabilir.
        Onu rol sayma.
      */
      if(t.length > 190) continue;

      var hasDoluluk =
        t.indexOf("doluluk") >= 0 ||
        (/\d+\s*\/\s*\d+/.test(t) && (t.indexOf("bay") >= 0 || t.indexOf("bayan") >= 0));

      var hasBlocked =
        t.indexOf("saat") >= 0 ||
        t.indexOf("hız") >= 0 ||
        t.indexOf("hiz") >= 0 ||
        t.indexOf("km/sa") >= 0 ||
        t.indexOf("durum") >= 0 ||
        t.indexOf("tahmini durum") >= 0 ||
        t.indexOf("erken") >= 0 ||
        t.indexOf("geç") >= 0 ||
        t.indexOf("gec") >= 0;

      if(hasDoluluk && !hasBlocked) return "allow";
      if(hasBlocked && !hasDoluluk) return "block";
    }

    return "";
  }

  function isClockArea(target){
    if(!isElement(target)) return false;

    if(target.closest("#liveClockText,#v99Clock,.v99-clock,.v99-hdr-clock,.v99-time,.v99-top-time")){
      return true;
    }

    var el = target;
    for(var i = 0; i < 8 && el && el !== document.body; i++, el = el.parentElement){
      var t = text(el);
      if(t && t.length <= 40 && /^\d{1,2}\s*:\s*\d{2}(\s*:\s*\d{2})?$/.test(t)){
        return true;
      }
    }

    return false;
  }

  function isTopStatArea(target){
    if(!isElement(target)) return false;

    return !!target.closest(
      ".v99-stats,.v99-stat-grid,.v99-kpi-grid,.v99-top-stats," +
      ".v99-metrics,.v99-dashboard,.v99-info-grid,.v99-summary-grid"
    );
  }

  function shouldBlock(target){
    if(!isElement(target)) return false;

    /*
      Önce doluluk kartını özellikle serbest bırak.
      Doluluk panelini sadece burası açsın.
    */
    var role = smallRole(target);
    if(role === "allow") return false;

    /*
      Hız / Saat / Durum kartları panel açmasın.
    */
    if(role === "block") return true;

    /*
      Üst saat yazısı panel açmasın.
    */
    if(isClockArea(target)) return true;

    /*
      Üst istatistik alanında boş yere basınca da panel açılmasın.
      Ama gerçek buton/link ise dokunma.
    */
    if(isTopStatArea(target) && !isSafeControl(target)){
      return true;
    }

    return false;
  }

  function gateEvent(ev){
    var target = ev.target;
    if(!shouldBlock(target)) return;

    ev.preventDefault();
    ev.stopPropagation();
    ev.stopImmediatePropagation();
    return false;
  }

  /*
    Capture fazında yakalıyoruz.
    Böylece eski kodun alttaki click listener'ına ulaşmadan kesiliyor.
  */
  ["click", "mousedown", "pointerdown", "touchstart"].forEach(function(type){
    document.addEventListener(type, gateEvent, true);
  });

  window.MuavinV99OnlyDolulukClickGate = true;
})();
/* V99R_ONLY_DOLULUK_CLICK_GATE_END */
'''

s = s.rstrip() + gate + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")
for key in [
    "V99R_ONLY_DOLULUK_CLICK_GATE_START",
    "MuavinV99OnlyDolulukClickGate",
    "smallRole",
    "isClockArea",
    "isTopStatArea",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99R tamam. /continue-trip?v=v99r-doluluk-gate ile yenile.")
