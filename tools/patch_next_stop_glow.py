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
      0 0 0 1px rgba(250,204,21,.18) inset,
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
  border-color:rgba(250,204,21,.34) !important;
  background:
    radial-gradient(circle at 12% 14%, rgba(250,204,21,.13), transparent 32%),
    radial-gradient(circle at 92% 0%, rgba(245,158,11,.10), transparent 28%),
    linear-gradient(180deg, rgba(255,215,64,.035), rgba(255,255,255,.02)),
    rgba(10,16,30,.88) !important;
  animation:nextStopGlowPulse 2.5s ease-in-out infinite !important;
}

.card.regular.next-card::after{
  content:"";
  position:absolute;
  left:0;
  top:18px;
  bottom:18px;
  width:4px;
  border-radius:999px;
  background:linear-gradient(180deg, rgba(250,204,21,.98), rgba(245,158,11,.48));
  box-shadow:
    0 0 10px rgba(250,204,21,.68),
    0 0 20px rgba(250,204,21,.28);
}

.card.regular.next-card .status-pill.next{
  box-shadow:
    0 0 0 1px rgba(250,204,21,.20) inset,
    0 0 18px rgba(250,204,21,.15) !important;
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

    shutil.copy2(p, str(p) + f".bak_next_stop_glow_{TS}")

    s = p.read_text(encoding="utf-8", errors="ignore")
    original = s

    # Eski yama varsa temizle
    s = re.sub(
        r'\n?<style id="next-stop-glow-style">.*?</style>\s*',
        '\n',
        s,
        flags=re.S
    )

    # Style ekle
    anchor = '<script id="live-clock-script">'
    if anchor in s:
        s = s.replace(anchor, style_block + "\n\n" + anchor, 1)
    else:
        s += "\n" + style_block + "\n"

    # Sadece sıradaki durak kartına class ver
    s = s.replace(
        '<div class="card regular">',
        '<div class="card regular {% if stop.kind == "next" %}next-card{% endif %}">'
    )

    # Tekrar çalıştırılmışsa çift class olmasın
    s = s.replace(
        'next-card{% endif %} {% if stop.kind == "next" %}next-card{% endif %}',
        'next-card{% endif %}'
    )

    if s != original:
        p.write_text(s, encoding="utf-8")
        print(f"✅ patched: {p}")
    else:
        print(f"ℹ️ değişiklik yok: {p}")
