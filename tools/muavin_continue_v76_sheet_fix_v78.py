from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_FILES = [
    ROOT / "static/continue/continue_v76.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

PATCH = r'''

/* CONTINUE_V76_SHEET_FIX_V78 */

/* Detay paneli dock altında kalmasın, gerçek bottom-sheet gibi açılsın */
.live-sheet-overlay,
#liveStopSheetOverlay{
  position:fixed !important;
  inset:0 !important;
  background:rgba(0,0,0,.62) !important;
  opacity:0 !important;
  pointer-events:none !important;
  z-index:800 !important;
  transition:opacity .2s ease !important;
}

.live-sheet-overlay.show,
.live-sheet-overlay.active,
.live-sheet-overlay.is-open,
#liveStopSheetOverlay.show,
#liveStopSheetOverlay.active,
#liveStopSheetOverlay.is-open,
#liveStopSheetOverlay[aria-hidden="false"]{
  opacity:1 !important;
  pointer-events:auto !important;
}

.live-stop-sheet,
#liveStopSheet{
  position:fixed !important;
  left:12px !important;
  right:12px !important;
  bottom:calc(76px + env(safe-area-inset-bottom, 0px)) !important;
  max-height:68vh !important;
  overflow:auto !important;
  background:#12151a !important;
  border:1px solid #1f2530 !important;
  border-radius:22px !important;
  padding:18px !important;
  z-index:900 !important;
  box-shadow:0 -18px 50px rgba(0,0,0,.65), 0 0 0 1px rgba(255,255,255,.03) inset !important;
  transform:translateY(calc(100% + 120px)) !important;
  opacity:0 !important;
  pointer-events:none !important;
  transition:transform .25s ease, opacity .2s ease !important;
}

.live-stop-sheet.show,
.live-stop-sheet.active,
.live-stop-sheet.is-open,
.live-stop-sheet.open,
#liveStopSheet.show,
#liveStopSheet.active,
#liveStopSheet.is-open,
#liveStopSheet.open,
#liveStopSheet[aria-hidden="false"]{
  transform:translateY(0) !important;
  opacity:1 !important;
  pointer-events:auto !important;
}

.sheet-grip{
  width:46px !important;
  height:5px !important;
  border-radius:999px !important;
  background:#2b3340 !important;
  margin:0 auto 14px !important;
}

.sheet-head{
  display:flex !important;
  align-items:flex-start !important;
  justify-content:space-between !important;
  gap:12px !important;
}

.sheet-title{
  font-size:28px !important;
  line-height:1.05 !important;
  color:#fff !important;
}

.sheet-sub{
  color:#8a95a8 !important;
}

.sheet-close{
  flex:0 0 auto !important;
  width:44px !important;
  height:44px !important;
  border-radius:50% !important;
  background:#181c23 !important;
  border:1px solid #1f2530 !important;
  color:#d8dde8 !important;
  font-size:30px !important;
  display:grid !important;
  place-items:center !important;
}

.sheet-body{
  padding-bottom:10px !important;
}

/* Sheet açıkken alttaki dock sheet üstüne çıkmasın */
body:has(#liveStopSheet[aria-hidden="false"]) .dock{
  z-index:700 !important;
}

@supports not selector(:has(*)){
  .dock{
    z-index:100 !important;
  }
}

@media(max-width:420px){
  .live-stop-sheet,
  #liveStopSheet{
    left:10px !important;
    right:10px !important;
    bottom:calc(74px + env(safe-area-inset-bottom, 0px)) !important;
    max-height:70vh !important;
    padding:16px !important;
  }

  .sheet-title{
    font-size:25px !important;
  }
}
'''

print("===== CONTINUE V76 SHEET FIX V78 =====")

for p in CSS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sheet-v78-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_V76_SHEET_FIX_V78" in s:
        print("ℹ️ V78 zaten var:", p.relative_to(ROOT))
        continue

    s = s.rstrip() + "\n" + PATCH + "\n"
    p.write_text(s, encoding="utf-8")
    print("✅ Sheet/modal düzeltmesi eklendi:", p.relative_to(ROOT))

print()
print("===== CACHE KIR =====")
for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sheet-v78-cache-{STAMP}")
    shutil.copy2(p, b)

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue/continue_v76\.css'\) }}\?v=[^\"']+",
        "continue/continue_v76.css') }}?v=prototype-layout-v78",
        s
    )
    p.write_text(s, encoding="utf-8")
    print("✅ Cache:", p.relative_to(ROOT))

print()
print("✅ V78 tamam.")
