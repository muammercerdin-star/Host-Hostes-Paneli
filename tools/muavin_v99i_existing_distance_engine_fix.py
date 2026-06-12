from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99I ESKI MESAFE MOTORUNA BAGLA =====")

if not WEB_JS.exists():
    raise SystemExit("❌ JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99i-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")
old = s
changes = []

# Önce varsa eski V99I bridge bloğunu temizle
s = re.sub(
    r"\n?/\* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_START \*/.*?/\* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

# 1) En kritik hata: V99 JS eski core class'ını sökmesin
if 'distanceVal.classList.remove("stop-distance-value");' in s:
    s = s.replace(
        'distanceVal.classList.remove("stop-distance-value");',
        'distanceVal.classList.add("stop-distance-value");'
    )
    changes.append("distanceVal artık stop-distance-value classını sökmüyor")

# 2) Mesafe hücresine data-stop-name garanti et
needle = 'distanceVal.classList.add("v99-timeline-distance-value");'
if needle in s and "V99I_DATA_STOP_BIND" not in s:
    s = s.replace(
        needle,
        needle + '\n      /* V99I_DATA_STOP_BIND */\n      distanceVal.classList.add("stop-distance-value");\n      if(stopName) distanceVal.setAttribute("data-stop-name", stopName);'
    )
    changes.append("timeline mesafe hücresine data-stop-name garantisi eklendi")

# 3) Geçilen duraklarda mesafeyi V99 boşaltmasın
pat_passed = re.compile(
    r'if\s*\(\s*idx\s*<\s*currentIdx\s*\)\s*\{\s*'
    r'distanceVal\.textContent\s*=\s*"—";\s*'
    r'return;\s*'
    r'\}',
    re.S
)

s2, n = pat_passed.subn(
    '''if(idx < currentIdx){
        /* V99I: geçilen durakta MESAFE alanını boşaltma.
           Eski core motor .stop-distance-value[data-stop-name] üzerinden gerçek km'yi yazacak. */
        return;
      }''',
    s,
    count=1
)

if n:
    s = s2
    changes.append("passed kartlarda mesafe boşaltma iptal edildi")
else:
    print("⚠️ passed mesafe boşaltma bloğu birebir bulunamadı")

# 4) '2 durak', '3 durak' fallback yazmasın
pat_durak = re.compile(
    r'distanceVal\.textContent\s*=\s*String\s*\(\s*targetIdx\s*-\s*currentIdx\s*\)\s*\+\s*" durak";'
)

s2, n = pat_durak.subn(
    'distanceVal.textContent = "—";',
    s
)

if n:
    s = s2
    changes.append("'N durak' mesafe fallback yazısı kaldırıldı")
else:
    print("⚠️ 'N durak' fallback satırı bulunamadı")

# 5) Güvenlik bridge: V99 kartlarındaki MESAFE alanını eski core motoruna bağlı tut
bridge = r'''

/* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_START */
(function(){
  "use strict";

  function text(el){
    return el ? String(el.textContent || "").trim() : "";
  }

  function findDistanceVal(card){
    if(!card) return null;

    var metrics = card.querySelectorAll(".v99-tl-metric");
    for(var i=0; i<metrics.length; i++){
      var lbl = metrics[i].querySelector(".v99-tl-m-lbl");
      var val = metrics[i].querySelector(".v99-tl-m-val");
      var lt = text(lbl).toLocaleLowerCase("tr-TR");

      if(val && (lt.indexOf("mesafe") >= 0)){
        return val;
      }
    }

    return null;
  }

  function bindDistanceCells(){
    var cards = document.querySelectorAll(".v99-tl-card");
    cards.forEach(function(card){
      var nameEl = card.querySelector(".v99-tl-stop-name");
      var val = findDistanceVal(card);
      var stopName = text(nameEl);

      if(!val || !stopName) return;

      val.classList.add("stop-distance-value");
      val.setAttribute("data-stop-name", stopName);

      var t = text(val);
      if(/durak|sonra|sırada|sirada/i.test(t)){
        val.textContent = "—";
      }
    });
  }

  bindDistanceCells();

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", bindDistanceCells);
  }

  window.addEventListener("load", bindDistanceCells);
  document.addEventListener("continueEtaUpdated", bindDistanceCells);

  var left = 30;
  var timer = setInterval(function(){
    bindDistanceCells();
    left--;
    if(left <= 0) clearInterval(timer);
  }, 700);
})();
/* V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_END */
'''

s = s.rstrip() + bridge + "\n"

WEB_JS.write_text(s, encoding="utf-8")
print("✅ web JS yazıldı:", WEB_JS)

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron:", AND_JS)

print()
print("===== DEGISIKLIKLER =====")
for c in changes:
    print("✅", c)

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    'distanceVal.classList.remove("stop-distance-value")',
    'String(targetIdx - currentIdx) + " durak"',
    'V99I_EXISTING_DISTANCE_ENGINE_BRIDGE_START',
    'V99I_DATA_STOP_BIND',
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99I tamam. Tarayıcıda /continue-trip?v=v99i ile yenile.")
