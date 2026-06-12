from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99K MESAFE ZIPLAMA FIX =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99k-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")
changes = []

# Daha önce eklendiyse temizle
s = re.sub(
    r"\n?/\* V99K_DISTANCE_NO_FLICKER_GUARD_START \*/.*?/\* V99K_DISTANCE_NO_FLICKER_GUARD_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

start_marker = "/* V99F_REAL_ROUTE_KM_START */"
end_marker = "/* V99F_REAL_ROUTE_KM_END */"

start = s.find(start_marker)
end = s.find(end_marker)

if start == -1 or end == -1 or end <= start:
    print("⚠️ V99F bloğu bulunamadı. Sadece koruma bloğu eklenecek.")
else:
    end = end + len(end_marker)
    before = s[:start]
    block = s[start:end]
    after = s[end:]

    old_block = block

    # V99F bloğu artık MESAFE yazmayacak. Sadece saat/varış tarafı çalışabilir.
    block = re.sub(
        r'(\s*)distanceVal\.textContent\s*=\s*"—"\s*;',
        r'\1/* V99K: MESAFE yazma; GPS motoru yazacak. */',
        block
    )

    block = re.sub(
        r'(\s*)distanceVal\.textContent\s*=\s*runtimeKm\s*!==\s*null\s*\?\s*formatKm\(runtimeKm\)\s*:\s*"0 km"\s*;',
        r'\1/* V99K: CANLI MESAFE yazma; GPS motoru yazacak. */',
        block
    )

    block = re.sub(
        r'(\s*)distanceVal\.textContent\s*=\s*formatKm\(dist\)\s*;',
        r'\1/* V99K: GELECEK DURAK MESAFE yazma; GPS motoru yazacak. */',
        block
    )

    block = re.sub(
        r'(\s*)distanceVal\.textContent\s*=\s*String\s*\(\s*targetIdx\s*-\s*currentIdx\s*\)\s*\+\s*" durak"\s*;',
        r'\1/* V99K: durak sayısı yazma; GPS motoru yazacak. */',
        block
    )

    if block != old_block:
        changes.append("V99F içindeki mesafe yazmaları pasifleştirildi")
    else:
        print("⚠️ V99F içinde değiştirilecek mesafe yazma satırı bulunamadı")

    s = before + block + after

# Ek koruma: başka script '-' basarsa, son gerçek km değerini geri koy.
guard = r'''

/* V99K_DISTANCE_NO_FLICKER_GUARD_START */
(function(){
  "use strict";

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function isRealKm(t){
    return /\d/.test(t || "") && /(km|m)$/i.test(String(t || "").trim());
  }

  function isBlankDistance(t){
    t = String(t || "").trim();
    return !t || t === "—" || t === "-" || /durak|sonra|sırada|sirada/i.test(t);
  }

  function findDistanceVal(card){
    if(!card) return null;

    var metrics = card.querySelectorAll(".v99-tl-metric");
    for(var i = 0; i < metrics.length; i++){
      var lbl = metrics[i].querySelector(".v99-tl-m-lbl");
      var val = metrics[i].querySelector(".v99-tl-m-val");
      if(!lbl || !val) continue;

      var lt = text(lbl).toLocaleLowerCase("tr-TR");
      if(lt.indexOf("mesafe") >= 0){
        return val;
      }
    }

    return null;
  }

  function protectDistances(){
    document.querySelectorAll(".v99-tl-card").forEach(function(card){
      var val = findDistanceVal(card);
      if(!val) return;

      var now = text(val);
      var last = val.getAttribute("data-v99-last-real-km") || "";

      if(isRealKm(now)){
        val.setAttribute("data-v99-last-real-km", now);
        return;
      }

      if(last && isBlankDistance(now)){
        val.textContent = last;
      }
    });
  }

  protectDistances();

  var obs = new MutationObserver(function(){
    protectDistances();
  });

  try{
    obs.observe(document.body, {
      childList: true,
      subtree: true,
      characterData: true
    });
  }catch(_){}

  setInterval(protectDistances, 300);
  document.addEventListener("continueEtaUpdated", protectDistances);
  window.addEventListener("load", protectDistances);
})();
/* V99K_DISTANCE_NO_FLICKER_GUARD_END */
'''

s = s.rstrip() + guard + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== DEĞİŞİKLİKLER =====")
for c in changes:
    print("✅", c)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "V99K_DISTANCE_NO_FLICKER_GUARD_START",
    "V99K: MESAFE yazma",
    "V99J_DIRECT_GPS_DISTANCE_START",
    "MuavinV99DirectGpsDistance",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99K tamam. Tarayıcıda /continue-trip?v=v99k ile yenile.")
