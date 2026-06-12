from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99Q SADECE DOLULUK TIKLAYINCA PANEL AÇILSIN =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99q-only-occupancy-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")

# Eski V99Q bloğunu temizle
s = re.sub(
    r"\n?/\* V99Q_ONLY_OCCUPANCY_CLICK_START \*/.*?/\* V99Q_ONLY_OCCUPANCY_CLICK_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

patch = r'''

/* V99Q_ONLY_OCCUPANCY_CLICK_START */
(function(){
  "use strict";

  function txt(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function insidePanel(target){
    return !!(
      target &&
      target.closest &&
      target.closest(".v99-seat-panel, .v99-seat-sheet, .v99-seat-modal, .v99-occupancy-panel, .v99-panel, .v99-doluluk-panel")
    );
  }

  function climbForTopCard(target){
    var el = target;
    for(var i = 0; el && i < 7; i++, el = el.parentElement){
      var t = norm(txt(el));

      // Üstteki küçük bilgi kartları: SAAT / HIZ / DOLULUK / DURUM
      if(
        t.indexOf("doluluk") >= 0 ||
        t.indexOf("hiz") >= 0 ||
        t.indexOf("hız") >= 0 ||
        t.indexOf("durum") >= 0 ||
        t.indexOf("saat") >= 0
      ){
        return el;
      }
    }
    return null;
  }

  function isDolulukCard(card){
    if(!card) return false;
    return norm(txt(card)).indexOf("doluluk") >= 0;
  }

  function isHeaderClock(target){
    if(!target || !target.closest) return false;

    if(target.closest("#liveClockText")) return true;
    if(target.closest(".v99-clock")) return true;
    if(target.closest(".v97-clock")) return true;

    var t = norm(txt(target));
    if(/^\d{1,2}:\d{2}$/.test(t) || /^\d{1,2}:\d{2}:\d{2}$/.test(t)){
      return true;
    }

    return false;
  }

  document.addEventListener("click", function(e){
    var target = e.target;
    if(!target) return;

    // Panelin içindeki tıklamalara karışma
    if(insidePanel(target)) return;

    // Header saatine basınca panel açılmasın
    if(isHeaderClock(target)){
      e.stopImmediatePropagation();
      return;
    }

    var card = climbForTopCard(target);

    if(!card) return;

    // Sadece DOLULUK kartı serbest
    if(isDolulukCard(card)) return;

    // SAAT / HIZ / DURUM kartlarında doluluk paneli açılmasın
    e.stopImmediatePropagation();
  }, true);

  window.MuavinV99OnlyOccupancyClick = true;
})();
/* V99Q_ONLY_OCCUPANCY_CLICK_END */
'''

s = s.rstrip() + patch + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")
for key in [
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
    "MuavinV99OnlyOccupancyClick",
    "isDolulukCard",
    "isHeaderClock",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99Q tamam. /continue-trip?v=v99q ile yenile.")
