from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/continue/continue_trip_v99_clean.css"
WEB_JS  = ROOT / "static/continue/continue_trip_v99_clean.js"

AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"
AND_JS  = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99C FINAL POLISH =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99c-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok")

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(r"/\* V99C_FINAL_POLISH_START \*/.*?/\* V99C_FINAL_POLISH_END \*/", "", css, flags=re.S)

css += r'''

/* V99C_FINAL_POLISH_START */

/* Alttaki büyük boşluğu temizle */
.v99-live-body{
  padding-bottom:88px !important;
}

.v99-main{
  padding-bottom:0 !important;
}

.v99-live-body .v99-end-wrap,
.v99-live-body .v99-end-wrap.danger-zone{
  margin:0 !important;
  min-height:0 !important;
  height:auto !important;
  padding:20px 20px 104px !important;
}

.v99-live-body .danger-zone::before,
.v99-live-body .danger-zone::after{
  display:none !important;
  content:none !important;
}

.v99-live-body .bottom-home{
  display:none !important;
}

/* Dock eski oval/pill CSS'lerinden tamamen ayrıldı */
.v99-live-body .v99-dock.dock{
  position:fixed !important;
  left:0 !important;
  right:0 !important;
  bottom:0 !important;
  width:100vw !important;
  max-width:none !important;
  height:82px !important;
  min-height:82px !important;
  margin:0 !important;
  padding:7px 0 max(env(safe-area-inset-bottom), 7px) !important;
  border-radius:0 !important;
  background:var(--v99-panel) !important;
  border-top:1px solid var(--v99-border) !important;
  border-left:0 !important;
  border-right:0 !important;
  border-bottom:0 !important;
  box-shadow:0 -10px 28px rgba(0,0,0,.38) !important;
  transform:none !important;
  overflow:hidden !important;
}

.v99-live-body .v99-dock.dock::before,
.v99-live-body .v99-dock.dock::after,
.v99-live-body .v99-dock-btn::before,
.v99-live-body .v99-dock-btn::after,
.v99-live-body .dock-item::before,
.v99-live-body .dock-item::after{
  display:none !important;
  content:none !important;
  opacity:0 !important;
}

.v99-live-body .v99-dock-btn,
.v99-live-body .v99-dock-btn.dock-item{
  height:100% !important;
  min-height:0 !important;
  margin:0 !important;
  padding:6px 0 !important;
  border:0 !important;
  border-radius:0 !important;
  background:transparent !important;
  box-shadow:none !important;
  transform:none !important;
}

/* Timeline içindeki uzun gerçek veri kırılmadan daha düzgün dursun */
.v99-tl-metrics{
  grid-template-columns:1.15fr 1.15fr .75fr .8fr !important;
  gap:7px !important;
}

.v99-tl-m-val{
  font-size:12.8px !important;
  letter-spacing:.2px !important;
}

.v99-tl-m-lbl{
  font-size:7.8px !important;
}

/* Ana kartta görsel ölçüleri sabit kalsın */
.v99-prox-card{
  margin-bottom:0 !important;
}

.v99-ring-wrap,
.v99-ring-svg{
  width:110px !important;
  height:110px !important;
}

.v99-pm-cell{
  min-height:82px !important;
}

/* V99C_FINAL_POLISH_END */
'''

WEB_CSS.write_text(css, encoding="utf-8")
print("✅ CSS final polish yazıldı")

if WEB_JS.exists():
    js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
    js = re.sub(r"/\* V99C_CLOCK_LOCK_START \*/.*?/\* V99C_CLOCK_LOCK_END \*/", "", js, flags=re.S)

    js += r'''

/* V99C_CLOCK_LOCK_START */
(function(){
  "use strict";

  function lockClock(){
    var el = document.getElementById("liveClockText");
    if(!el) return;

    var now = new Date();
    var h = String(now.getHours()).padStart(2, "0");
    var m = String(now.getMinutes()).padStart(2, "0");
    el.textContent = h + ":" + m;
  }

  lockClock();
  setInterval(lockClock, 300);
})();
/* V99C_CLOCK_LOCK_END */
'''
    WEB_JS.write_text(js, encoding="utf-8")
    print("✅ JS saat kilidi yazıldı")

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ Android CSS senkron")

if AND_JS.parent.exists() and WEB_JS.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS senkron")

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS]:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.name, "V99C:", "VAR" if "V99C_" in txt else "YOK")

print()
print("✅ V99C final polish tamam")
