from pathlib import Path
import re
import shutil
import os

TS = os.environ.get("TS") or "manual"

targets = [
    Path("templates/continue_trip.html"),
    Path("android_app/app/src/main/python/templates/continue_trip.html"),
]

style_block = r'''
<style id="next-stop-glow-style">
@keyframes nextStopGlowPulse{
  0%{
    box-shadow:
      0 0 0 1px rgba(250,204,21,.10) inset,
      0 0 0 rgba(250,204,21,0),
      0 16px 36px rgba(0,0,0,.28);
  }
  50%{
    box-shadow:
      0 0 0 1px rgba(250,204,21,.22) inset,
      0 0 24px rgba(250,204,21,.18),
      0 18px 38px rgba(0,0,0,.30);
  }
  100%{
    box-shadow:
      0 0 0 1px rgba(250,204,21,.10) inset,
      0 0 0 rgba(250,204,21,0),
      0 16px 36px rgba(0,0,0,.28);
  }
}

.card.regular.next-card{
  position:relative !important;
  overflow:hidden !important;
  isolation:isolate !important;
  border:1px solid rgba(250,204,21,.26) !important;
  border-radius:28px !important;
  background:
    radial-gradient(circle at 12% 14%, rgba(250,204,21,.13), transparent 32%),
    radial-gradient(circle at 92% 0%, rgba(245,158,11,.10), transparent 28%),
    linear-gradient(180deg, rgba(255,215,64,.035), rgba(255,255,255,.02)),
    rgba(10,16,30,.88) !important;
  animation:nextStopGlowPulse 2.5s ease-in-out infinite !important;
}

/* Kartın tamamını canlı durak gibi çevreleyen sarı hat */
.card.regular.next-card::before{
  content:"";
  position:absolute;
  inset:0;
  border-radius:28px;
  pointer-events:none;
  border:1px solid rgba(250,204,21,.22);
  box-shadow:
    inset 0 0 0 1px rgba(255,220,90,.05),
    0 0 0 1px rgba(250,204,21,.06),
    0 0 18px rgba(250,204,21,.10);
  z-index:0;
}

/* Soldaki sarı canlı çizgi kalsın */
.card.regular.next-card::after{
  content:"";
  position:absolute;
  left:0;
  top:18px;
  bottom:18px;
  width:6px;
  border-radius:999px;
  background:linear-gradient(180deg, rgba(250,204,21,.98), rgba(245,158,11,.52));
  box-shadow:
    0 0 10px rgba(250,204,21,.72),
    0 0 22px rgba(250,204,21,.30);
  z-index:1;
}

.card.regular.next-card > *{
  position:relative;
  z-index:2;
}

.card.regular.next-card .status-pill.next{
  border-color:rgba(250,204,21,.34) !important;
  box-shadow:
    0 0 0 1px rgba(250,204,21,.22) inset,
    0 0 18px rgba(250,204,21,.16) !important;
}

.card.regular.next-card .metric{
  border-color:rgba(250,204,21,.12) !important;
}
</style>
'''

for p in targets:
    if not p.exists():
        print(f"YOK: {p}")
        continue

    shutil.copy2(p, str(p) + f".bak_next_stop_border_{TS}")

    s = p.read_text(encoding="utf-8", errors="ignore")
    original = s

    s = re.sub(
        r'\n?<style id="next-stop-glow-style">.*?</style>\s*',
        '\n',
        s,
        flags=re.S
    )

    anchor = '<script id="live-clock-script">'
    if anchor in s:
        s = s.replace(anchor, style_block + "\n\n" + anchor, 1)
    else:
        s += "\n" + style_block + "\n"

    if s != original:
        p.write_text(s, encoding="utf-8")
        print(f"✅ updated: {p}")
    else:
        print(f"ℹ️ değişiklik yok: {p}")
