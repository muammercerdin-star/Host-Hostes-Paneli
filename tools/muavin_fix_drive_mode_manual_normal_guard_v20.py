from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

MARKER = "DRIVE_MODE_MANUAL_NORMAL_GUARD_V20"

GUARD = r'''
<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_START -->
<script id="drive-mode-manual-normal-guard-v20">
(function(){
  if(window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__) return;
  window.__DRIVE_MODE_MANUAL_NORMAL_GUARD_V20__ = true;

  const MANUAL_KEY = "driveModeManualNormalGuard:v20";
  let lastUserSwitchOnAt = 0;
  let lastUserSwitchOffAt = 0;

  function btn(){
    return document.getElementById("driveModeToggle");
  }

  function isDriveOn(){
    const b = btn();
    const txt = (b ? b.textContent : "").toLowerCase();
    return document.body.classList.contains("drive-mode") ||
           document.documentElement.classList.contains("drive-mode") ||
           txt.includes("normal");
  }

  function driveKeys(){
    const out = [];
    try{
      for(let i = 0; i < localStorage.length; i++){
        const k = localStorage.key(i);
        if(k && k.indexOf("driveMode:") === 0) out.push(k);
      }
    }catch(_){}
    return out;
  }

  function setAllDriveStorage(v){
    try{
      driveKeys().forEach(k => localStorage.setItem(k, v));
    }catch(_){}
  }

  function hasManualOff(){
    try{
      return localStorage.getItem(MANUAL_KEY) === "1";
    }catch(_){
      return false;
    }
  }

  function markManualOff(){
    try{
      localStorage.setItem(MANUAL_KEY, "1");
      setAllDriveStorage("0");
    }catch(_){}
  }

  function clearManualOff(){
    try{
      localStorage.removeItem(MANUAL_KEY);
    }catch(_){}
  }

  function forceNormal(){
    document.body.classList.remove("drive-mode");
    document.documentElement.classList.remove("drive-mode");

    const b = btn();
    if(b){
      b.innerHTML = "🚘 Sürüş";
      b.title = "Sürüş moduna geç";
    }

    setAllDriveStorage("0");

    try{
      window.dispatchEvent(new CustomEvent("driveModeChanged", {
        detail:{ on:false, source:"manual-normal-guard-v20" }
      }));
    }catch(_){}
  }

  function rememberIntent(e){
    const hit = e.target && e.target.closest && e.target.closest("#driveModeToggle");
    if(!hit) return;

    if(isDriveOn()){
      lastUserSwitchOffAt = Date.now();

      setTimeout(function(){
        if(!isDriveOn()) markManualOff();
      }, 80);

      setTimeout(function(){
        if(!isDriveOn()) markManualOff();
      }, 350);
    }else{
      lastUserSwitchOnAt = Date.now();
      clearManualOff();
    }
  }

  document.addEventListener("pointerdown", rememberIntent, true);
  document.addEventListener("touchstart", rememberIntent, true);
  document.addEventListener("mousedown", rememberIntent, true);

  function tick(){
    const now = Date.now();
    const on = isDriveOn();

    if(!on){
      if(hasManualOff() || now - lastUserSwitchOffAt < 20000){
        markManualOff();
      }
      return;
    }

    if(hasManualOff()){
      if(now - lastUserSwitchOnAt < 2500){
        clearManualOff();
        return;
      }

      forceNormal();
    }
  }

  setInterval(tick, 700);
  setTimeout(tick, 300);
  setTimeout(tick, 1500);
  setTimeout(tick, 5000);
})();
</script>
<!-- DRIVE_MODE_MANUAL_NORMAL_GUARD_V20_END -->
'''

ANCHOR = "<!-- DRIVE MODE FORCE TOGGLE END -->"

def backup(p: Path):
    b = p.with_name(p.name + f".bak-drive-manual-normal-v20-{STAMP}")
    shutil.copy2(p, b)
    return b

print("===== DRIVE MODE MANUEL NORMAL KORUMA V20 =====")

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if MARKER in s:
        print("ℹ️ V20 zaten var:", p.relative_to(ROOT))
        continue

    b = backup(p)

    if ANCHOR in s:
        s = s.replace(ANCHOR, ANCHOR + "\n" + GUARD, 1)
    else:
        s = s.replace("</body>", GUARD + "\n</body>", 1)

    p.write_text(s, encoding="utf-8")

    print("✅ Eklendi:", p.relative_to(ROOT))
    print("   Yedek:", b.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), MARKER + ":", txt.count(MARKER))

print()
print("✅ V20 tamam.")
