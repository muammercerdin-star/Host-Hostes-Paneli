from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_v76.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css",
]

PATCH = r'''

/* CONTINUE_V76_VISUAL_TUNE_V77 */

/* Sağdaki eski refresh butonu DURUM alanına biniyordu. V76 prototip görünümünde kapalı. */
.continue-refresh-v49-btn{
  display:none !important;
}

/* Durum alanı kesilmesin */
.gauge-cell:nth-child(3) .gauge-val,
#liveTopStatusText{
  font-size:18px !important;
  line-height:1.05 !important;
  white-space:normal !important;
  overflow:visible !important;
  text-overflow:clip !important;
  max-width:100% !important;
  word-break:keep-all !important;
}

.gauge-cell:nth-child(3) .gauge-unit{
  font-size:10px !important;
  margin-top:2px !important;
}

/* Hızda üstte zaten km/sa yazıyor, alt tekrarını gizle */
.gauge-cell:first-child .gauge-unit{
  visibility:hidden !important;
}

/* Üst rota bar biraz daha nefes alsın */
.route-bar{
  padding-right:14px !important;
}

.route-name{
  max-width:calc(100vw - 185px) !important;
}

/* Canlı kart ekran genişliğine daha iyi otursun */
.prox-section{
  padding-top:16px !important;
}

.prox-card{
  box-shadow:0 14px 34px rgba(0,0,0,.28) !important;
}

.prox-stop-name{
  font-size:28px !important;
}

.prox-eta-val{
  font-size:19px !important;
}

/* Alttaki dock içerik üstüne fazla binmesin */
.timeline-section{
  padding-bottom:10px !important;
}

@media(max-width:420px){
  .hdr-clock{
    font-size:20px !important;
  }

  .route-name{
    max-width:calc(100vw - 170px) !important;
  }

  .gauge-val{
    font-size:18px !important;
  }

  .gauge-cell:nth-child(3) .gauge-val,
  #liveTopStatusText{
    font-size:16px !important;
  }

  .prox-stop-name{
    font-size:27px !important;
  }
}
'''

print("===== CONTINUE V76 VISUAL TUNE V77 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-v77-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_V76_VISUAL_TUNE_V77" in s:
        print("ℹ️ V77 zaten var:", p.relative_to(ROOT))
        continue

    s = s.rstrip() + "\n" + PATCH + "\n"
    p.write_text(s, encoding="utf-8")
    print("✅ V77 görsel rötuş eklendi:", p.relative_to(ROOT))

print()
print("✅ V77 tamam.")
