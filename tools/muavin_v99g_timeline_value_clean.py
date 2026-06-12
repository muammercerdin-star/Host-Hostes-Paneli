from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

print("===== V99G TIMELINE VALUE CLEAN =====")

for p in [JS, AND_JS, TPL, AND_TPL]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99g-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not JS.exists():
    raise SystemExit("❌ JS yok")

js = JS.read_text(encoding="utf-8", errors="ignore")
js = re.sub(r"/\* V99G_TIMELINE_VALUE_CLEAN_START \*/.*?/\* V99G_TIMELINE_VALUE_CLEAN_END \*/", "", js, flags=re.S)

js += r'''

/* V99G_TIMELINE_VALUE_CLEAN_START */
(function(){
  "use strict";

  function qa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function q(sel, root){
    return (root || document).querySelector(sel);
  }

  function norm(s){
    return String(s || "")
      .toLocaleLowerCase("tr-TR")
      .replace(/\s+/g, " ")
      .trim();
  }

  function isBadArrivalText(t){
    t = norm(t);

    return (
      !t ||
      t === "geçildi" ||
      t === "simdi" ||
      t === "şimdi" ||
      t === "sırada" ||
      t === "sirada" ||
      t.indexOf("durak sonra") >= 0
    );
  }

  function cleanTimelineArrivalValues(){
    qa(".v99-tl-card").forEach(function(card){
      qa(".v99-tl-metric", card).forEach(function(metric){
        var val = q(".v99-tl-m-val", metric);
        var lbl = q(".v99-tl-m-lbl", metric);

        if(!val || !lbl) return;

        if(norm(lbl.textContent).indexOf("varış") < 0 && norm(lbl.textContent).indexOf("varis") < 0){
          return;
        }

        if(isBadArrivalText(val.textContent)){
          val.textContent = "—";
        }
      });
    });
  }

  cleanTimelineArrivalValues();
  setInterval(cleanTimelineArrivalValues, 400);
  document.addEventListener("continueEtaUpdated", cleanTimelineArrivalValues);
})();
/* V99G_TIMELINE_VALUE_CLEAN_END */
'''

JS.write_text(js, encoding="utf-8")
print("✅ JS varış değeri temizliği eklendi")

if TPL.exists():
    t = TPL.read_text(encoding="utf-8", errors="ignore")
    before = t

    t = re.sub(
        r"continue_trip_v99_clean\.js'\) \}\}\?v=[^\"']+",
        "continue_trip_v99_clean.js') }}?v=v99g-{{ trip['id'] }}",
        t
    )

    if t != before:
        TPL.write_text(t, encoding="utf-8")
        print("✅ template JS cache v99g yapıldı")
    else:
        print("⚠️ template cache değişmedi")

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(JS, AND_JS)
    print("✅ Android JS senkron")

if AND_TPL.parent.exists() and TPL.exists():
    AND_TPL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TPL, AND_TPL)
    print("✅ Android template senkron")

print()
print("===== KONTROL =====")
txt = JS.read_text(encoding="utf-8", errors="ignore")
print("V99G marker:", "VAR" if "V99G_TIMELINE_VALUE_CLEAN_START" in txt else "YOK")

if TPL.exists():
    tt = TPL.read_text(encoding="utf-8", errors="ignore")
    print("template v99g:", "VAR" if "v99g-" in tt else "YOK")

print()
print("✅ V99G tamam")
