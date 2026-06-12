from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_WEB = ROOT / "static/continue/css_parts/50-live-v2-top-glow.css"
CSS_ANDROID = ROOT / "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css"

MAIN_CSS_WEB = ROOT / "static/continue/continue_trip.css"
MAIN_CSS_ANDROID = ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css"

TPL_WEB = ROOT / "templates/continue_trip.html"
TPL_ANDROID = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

FILES = [CSS_WEB, CSS_ANDROID, MAIN_CSS_WEB, MAIN_CSS_ANDROID, TPL_WEB, TPL_ANDROID]

MARK = "LIVE_STOP_PROGRESS_RUNNER_FIX_V96B"

print("===== V96B CANLI DURAK ÇAPRAZ IŞIK DÜZELTME =====")
print("ROOT:", ROOT)

missing = [p for p in FILES if not p.exists()]
if missing:
    print("❌ Eksik dosyalar:")
    for p in missing:
        print(" -", p.relative_to(ROOT))
    raise SystemExit(1)

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def write(p, s):
    p.write_text(s, encoding="utf-8")

def backup(p):
    b = p.with_name(p.name + f".bak-v96b-runner-fix-{STAMP}")
    shutil.copy2(p, b)
    return b

def patch_file(p, fn):
    old = read(p)
    new = fn(old)
    if new != old:
        b = backup(p)
        write(p, new)
        print("✅ Değişti:", p.relative_to(ROOT))
        print("   backup:", b.relative_to(ROOT))
    else:
        print("ℹ️ Değişmedi:", p.relative_to(ROOT))

CSS_FIX = r'''

/* LIVE_STOP_PROGRESS_RUNNER_FIX_V96B
   Android Chrome'da conic runner maskesi içeri çapraz çizgi basıyordu.
   Eski runner'ı kenarda gezen küçük neon noktaya çevirir.
*/
#liveCurrentCard.card.live.live-stop-progress-ready-v96{
  overflow:hidden !important;
}

/* Eski büyük conic runner artık halka gibi maske kullanmaz */
#liveCurrentCard.card.live .live-stop-progress-runner-v96{
  inset:auto !important;
  width:13px !important;
  height:13px !important;
  padding:0 !important;
  border-radius:999px !important;

  background:
    radial-gradient(circle,
      rgba(255,255,255,.98) 0%,
      var(--liveStopProgressGlow) 38%,
      rgba(255,45,85,.42) 62%,
      transparent 72%
    ) !important;

  -webkit-mask:none !important;
  mask:none !important;
  -webkit-mask-composite:source-over !important;
  mask-composite:add !important;

  left:20px !important;
  top:-6px !important;
  right:auto !important;
  bottom:auto !important;

  opacity:.98 !important;
  z-index:5 !important;
  transform:none !important;

  filter:
    drop-shadow(0 0 8px rgba(255,255,255,.75))
    drop-shadow(0 0 16px var(--liveStopProgressGlow)) !important;

  animation:liveStopRunnerEdgeV96B var(--liveStopRunnerSpeed, 1.75s) linear infinite !important;
}

/* İçeri çizgi atan eski conic görüntüyü tamamen bastır */
#liveCurrentCard.card.live .live-stop-progress-runner-v96::before,
#liveCurrentCard.card.live .live-stop-progress-runner-v96::after{
  content:none !important;
}

/* Kenar üstünde saat yönünde gezen küçük ışık */
@keyframes liveStopRunnerEdgeV96B{
  0%{
    left:22px;
    top:-6px;
  }
  24%{
    left:calc(100% - 34px);
    top:-6px;
  }
  25%{
    left:calc(100% - 7px);
    top:22px;
  }
  49%{
    left:calc(100% - 7px);
    top:calc(100% - 34px);
  }
  50%{
    left:calc(100% - 34px);
    top:calc(100% - 7px);
  }
  74%{
    left:22px;
    top:calc(100% - 7px);
  }
  75%{
    left:-6px;
    top:calc(100% - 34px);
  }
  99%{
    left:-6px;
    top:22px;
  }
  100%{
    left:22px;
    top:-6px;
  }
}

/* Progress border biraz daha sakin kalsın */
#liveCurrentCard.card.live .live-stop-progress-border-v96{
  z-index:2 !important;
  opacity:.92 !important;
}

#liveCurrentCard.card.live.live-stop-progress-ready-v96 > :not(.live-stop-progress-border-v96):not(.live-stop-progress-runner-v96){
  position:relative !important;
  z-index:4 !important;
}
'''

def patch_css(s):
    if MARK in s:
        return s
    return s.rstrip() + "\n" + CSS_FIX + "\n"

def patch_main_css(s):
    s = re.sub(
        r'@import\s+url\("\./css_parts/50-live-v2-top-glow\.css(?:\?v=[^"]*)?"\)\s*;',
        '@import url("./css_parts/50-live-v2-top-glow.css?v=live-stop-progress-v96b");',
        s
    )
    return s

def patch_template(s):
    s = re.sub(
        r"(filename='continue/continue_trip\.css'\)\s*\}\})\?v=[^\"']+",
        r"\1?v=live-stop-progress-v96b",
        s
    )
    return s

for p in [CSS_WEB, CSS_ANDROID]:
    patch_file(p, patch_css)

for p in [MAIN_CSS_WEB, MAIN_CSS_ANDROID]:
    patch_file(p, patch_main_css)

for p in [TPL_WEB, TPL_ANDROID]:
    patch_file(p, patch_template)

print()
print("===== KONTROL =====")
for p in [CSS_WEB, CSS_ANDROID]:
    print(("OK " if MARK in read(p) else "NO "), p.relative_to(ROOT))

print()
print("✅ V96B tamam. Çapraz iç ışık kalkacak, kenarda küçük neon nokta gezecek.")
