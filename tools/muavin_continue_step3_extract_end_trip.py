from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

WEB_JS = ROOT / "static/continue/continue_end_trip_modal_v106.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_end_trip_modal_v106.js"

print("===== STEP-3 END-TRIP INLINE SCRIPT AYIRMA =====")
print("ROOT:", ROOT)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def backup(p):
    if p.exists():
        bak = p.with_name(p.name + f".bak-step3-endtrip-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

for p in [WEB_TPL, AND_TPL, WEB_JS, AND_JS]:
    backup(p)

if not WEB_TPL.exists():
    raise SystemExit("❌ template yok")

WEB_JS.parent.mkdir(parents=True, exist_ok=True)

js = r'''
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
'''.strip() + "\n"

WEB_JS.write_text(js, encoding="utf-8")
print("✅ web JS oluşturuldu:", WEB_JS)

tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
old_tpl = tpl

# 1) Eski V106 çağrısı varsa kaldır
tpl = re.sub(
    r'\n?\s*<script[^>]+continue_end_trip_modal_v106\.js[^>]*></script>\s*',
    "\n",
    tpl
)

# 2) endTripForm kullanan inline scripti kaldır
# Bu özellikle <script> ... const form = document.getElementById("endTripForm") ... </script> bloğunu hedefler.
tpl, n_remove = re.subn(
    r'\n?<script>\s*\(function\(\)\{\s*const form = document\.getElementById\("endTripForm"\);.*?\}\)\(\);\s*</script>\s*',
    "\n",
    tpl,
    count=1,
    flags=re.S
)

if n_remove != 1:
    print("⚠️ Inline end-trip script otomatik bulunamadı, alternatif arama deneniyor...")
    tpl, n_remove2 = re.subn(
        r'\n?<script>.*?endTripForm.*?clearTripLocalMemory.*?</script>\s*',
        "\n",
        tpl,
        count=1,
        flags=re.S
    )
    n_remove = n_remove2

# 3) Yeni scripti CONTINUE_BOOT sonrasına, ana JS dosyalarından önce ekle
script_tag = """<script src="{{ url_for('static', filename='continue/continue_end_trip_modal_v106.js') }}?v=v106-{{ trip['id'] }}"></script>"""

anchor = '<script src="{{ url_for(\'static\', filename=\'continue/continue_trip_core.js\') }}?v=live-stop-lock-v82"></script>'
if anchor in tpl:
    tpl = tpl.replace(anchor, script_tag + "\n" + anchor)
elif "</body>" in tpl:
    tpl = tpl.replace("</body>", script_tag + "\n</body>")
else:
    tpl = tpl.rstrip() + "\n" + script_tag + "\n"

WEB_TPL.write_text(tpl, encoding="utf-8")

print("✅ inline end-trip script kaldırma sayısı:", n_remove)
print("✅ template güncellendi:", WEB_TPL)

# Android sync
if AND_TPL.parent.exists():
    shutil.copy2(WEB_TPL, AND_TPL)
    print("✅ android template senkron")

if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ android JS senkron")

print()
print("===== NODE SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ V106 JS syntax OK")
    else:
        print("❌ V106 JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KONTROL =====")
now = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
js_now = WEB_JS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("V106 script template'e eklendi", "continue_end_trip_modal_v106.js" in now),
    ("Eski inline endTripForm scripti kalktı", 'const form = document.getElementById("endTripForm");' not in now),
    ("CONTINUE_BOOT kaldı", "window.CONTINUE_BOOT" in now),
    ("V106 JS marker var", "CONTINUE_END_TRIP_MODAL_V106_START" in js_now),
    ("V106 JS tripKey CONTINUE_BOOT kullanıyor", "window.CONTINUE_BOOT" in js_now),
    ("Web/Android template aynı", WEB_TPL.exists() and AND_TPL.exists() and sha(WEB_TPL) == sha(AND_TPL)),
    ("Web/Android V106 JS aynı", WEB_JS.exists() and AND_JS.exists() and sha(WEB_JS) == sha(AND_JS)),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== TEMPLATE SCRIPT SATIRLARI =====")
for i, line in enumerate(now.splitlines(), 1):
    if "<script" in line:
        print(f"{i}: {line}")

print()
print("===== SATIR SAYISI =====")
print("template lines:", len(now.splitlines()))
print("v106 js lines:", len(js_now.splitlines()))
print("template sha:", sha(WEB_TPL))
print("android template sha:", sha(AND_TPL))

print()
print("✅ Step-3 tamam.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=step3-endtrip-v106")
