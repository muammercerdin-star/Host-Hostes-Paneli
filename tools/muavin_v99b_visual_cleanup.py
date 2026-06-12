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

print("===== V99B GORSEL TEMIZLIK =====")

for p in [WEB_CSS, WEB_JS, AND_CSS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99b-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not WEB_CSS.exists():
    raise SystemExit("❌ CSS yok: " + str(WEB_CSS))

css = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(r"/\* V99B_VISUAL_CLEANUP_START \*/.*?/\* V99B_VISUAL_CLEANUP_END \*/", "", css, flags=re.S)

css += r'''

/* V99B_VISUAL_CLEANUP_START */

/* Sayfa altı dock altında kalmasın */
.v99-live-body{
  padding-bottom:128px !important;
}

.v99-main{
  padding-bottom:118px !important;
}

/* Eski dock CSS çakışmasını sıfırla: tasarımdaki gibi düz alt bar */
.v99-dock{
  left:0 !important;
  right:0 !important;
  bottom:0 !important;
  width:100% !important;
  max-width:none !important;
  border-radius:0 !important;
  box-shadow:none !important;
  transform:none !important;
  margin:0 !important;
  background:var(--v99-panel) !important;
  border-top:1px solid var(--v99-border) !important;
  border-left:0 !important;
  border-right:0 !important;
  border-bottom:0 !important;
}

/* Eski refresh/yukarıdaki yuvarlak buton tasarımı bozuyor, gizle */
.v99-live-body [class*="refresh" i],
.v99-live-body [id*="refresh" i],
.v99-live-body button[title*="Yenile"],
.v99-live-body button[aria-label*="Yenile"],
.v99-live-body a[title*="Yenile"],
.v99-live-body a[aria-label*="Yenile"]{
  display:none !important;
  opacity:0 !important;
  pointer-events:none !important;
}

/* İnecek / bagaj kartı sıkışmasın */
.v99-pm-cell{
  padding:10px 12px !important;
  gap:9px !important;
  overflow:hidden !important;
  min-height:86px !important;
}

.v99-pm-data{
  min-width:0 !important;
  flex:1 !important;
}

.v99-pm-val{
  font-size:18px !important;
  letter-spacing:0 !important;
  white-space:nowrap !important;
  overflow:hidden !important;
  text-overflow:ellipsis !important;
  line-height:1.05 !important;
}

.v99-pm-lbl{
  font-size:9px !important;
  letter-spacing:1px !important;
  line-height:1.15 !important;
  white-space:nowrap !important;
}

/* Timeline metrikleri kart içine düzgün otursun */
.v99-tl-metrics{
  display:grid !important;
  grid-template-columns:repeat(4,minmax(0,1fr)) !important;
  gap:8px !important;
  width:100% !important;
}

.v99-tl-metric{
  min-width:0 !important;
}

.v99-tl-m-val{
  font-size:13.5px !important;
  white-space:nowrap !important;
  overflow:hidden !important;
  text-overflow:ellipsis !important;
  line-height:1.15 !important;
}

.v99-tl-m-lbl{
  font-size:8px !important;
  letter-spacing:1px !important;
}

.v99-tl-card{
  padding:12px !important;
}

.v99-tl-stop-name{
  font-size:15px !important;
}

/* küçük ekranlarda kart oranını koru */
@media (max-width:380px){
  .v99-pm-cell{
    padding:9px 10px !important;
    gap:7px !important;
  }

  .v99-pm-icon{
    font-size:18px !important;
  }

  .v99-pm-val{
    font-size:16px !important;
  }

  .v99-pm-lbl{
    font-size:8px !important;
  }

  .v99-tl-metrics{
    gap:6px !important;
  }

  .v99-tl-m-val{
    font-size:12.5px !important;
  }
}

/* V99B_VISUAL_CLEANUP_END */
'''

WEB_CSS.write_text(css, encoding="utf-8")
print("✅ CSS temizlendi:", WEB_CSS)

if WEB_JS.exists():
    js = WEB_JS.read_text(encoding="utf-8", errors="ignore")
    js = re.sub(r"/\* V99B_COUNT_CLEANUP_START \*/.*?/\* V99B_COUNT_CLEANUP_END \*/", "", js, flags=re.S)

    js += r'''

/* V99B_COUNT_CLEANUP_START */
(function(){
  "use strict";

  function onlyCount(id){
    var el = document.getElementById(id);
    if(!el) return;

    var t = String(el.textContent || "").trim();
    if(!t) return;

    var m = t.match(/\d+/);
    if(m){
      el.textContent = m[0];
      return;
    }

    if(/yok|none|boş/i.test(t)){
      el.textContent = "0";
    }
  }

  function cleanCounts(){
    onlyCount("liveOffloadCount");
    onlyCount("liveBagajCount");
  }

  cleanCounts();
  setInterval(cleanCounts, 500);
  document.addEventListener("continueEtaUpdated", cleanCounts);
})();
 /* V99B_COUNT_CLEANUP_END */
'''
    WEB_JS.write_text(js, encoding="utf-8")
    print("✅ JS sayı temizliği eklendi:", WEB_JS)

if AND_CSS.parent.exists():
    AND_CSS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ Android CSS senkron:", AND_CSS)

if AND_JS.parent.exists() and WEB_JS.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS senkron:", AND_JS)

print()
print("===== KONTROL =====")
for p in [WEB_CSS, WEB_JS]:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.name, "V99B:", "VAR" if "V99B_" in txt else "YOK")

print()
print("✅ V99B görsel temizlik tamam")
