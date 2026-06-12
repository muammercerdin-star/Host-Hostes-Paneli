from pathlib import Path
from datetime import datetime
import shutil
import re
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/continue/continue_speed_overlay_v102.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.css"

print("===== V102A HIZ OVERLAY İNCE AYAR =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

if not WEB_CSS.exists():
    raise SystemExit("❌ V102 CSS bulunamadı: " + str(WEB_CSS))

for p in [WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v102a-speed-tune-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

# Eski V102A tuning varsa temizle
s = re.sub(
    r"\n?/\* V102A_SPEED_OVERLAY_TUNE_START \*/.*?/\* V102A_SPEED_OVERLAY_TUNE_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

tune = r'''

/* V102A_SPEED_OVERLAY_TUNE_START */

/* Hız kutusu artık büyümesin, dijital yazı her zaman önde kalsın */
.v102-speed-card{
  min-height:89px !important;
  padding-top:14px !important;
  padding-bottom:14px !important;
}

/* Dijital hız okunaklı kalsın */
.v102-speed-card .v99-gauge-label{
  z-index:8 !important;
}

.v102-speed-card .v99-gauge-val{
  z-index:9 !important;
  font-size:22px !important;
  text-shadow:
    0 0 8px rgba(224,136,32,.42),
    0 2px 4px rgba(0,0,0,.65) !important;
}

.v102-speed-card .v99-gauge-unit{
  z-index:9 !important;
  opacity:.78 !important;
  text-shadow:0 2px 4px rgba(0,0,0,.70) !important;
}

/* Overlay daha arka planda ve daha sakin */
.v102-speed-overlay{
  opacity:.58 !important;
}

/* Alt bar çok belli olmasın */
.v102-speed-bar{
  left:18px !important;
  right:18px !important;
  bottom:8px !important;
  height:2px !important;
  opacity:.55 !important;
}

/* Analog yay daha küçük ve yazının arkasında */
.v102-speed-arc{
  top:34px !important;
  width:72px !important;
  height:31px !important;
  border-width:2px !important;
  opacity:0 !important;
}

/* İbre yazının üstünü kesmesin */
.v102-speed-needle{
  top:43px !important;
  height:23px !important;
  width:2px !important;
  opacity:0 !important;
  filter:none !important;
}

/* Orta nokta daha küçük */
.v102-speed-dot{
  top:61px !important;
  width:7px !important;
  height:7px !important;
  opacity:0 !important;
}

/* Analog açıkken bile sakin görünüm */
.v102-speed-card.v102-speed-analog-on .v102-speed-arc{
  opacity:.52 !important;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-needle{
  opacity:.56 !important;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-dot{
  opacity:.62 !important;
}

/* HIZ kutusu açıkken fazla yeşil patlamasın */
.v102-speed-card.v102-speed-analog-on{
  background:
    radial-gradient(circle at 50% 70%, rgba(224,136,32,.08), transparent 48%),
    var(--v99-panel) !important;
}

/* Düşük hızda yeşil daha loş olsun */
.v102-speed-card.v102-low .v102-speed-arc{
  border-color:rgba(29,184,122,.42) !important;
  box-shadow:0 0 10px rgba(29,184,122,.11) !important;
}

.v102-speed-card.v102-low .v102-speed-needle{
  background:linear-gradient(180deg,rgba(190,255,226,.82),rgba(29,184,122,.72)) !important;
  box-shadow:0 0 8px rgba(29,184,122,.22) !important;
}

/* Yüksek hızda kırmızı uyarı daha dengeli */
.v102-speed-card.v102-high .v102-speed-arc{
  border-color:rgba(224,48,48,.50) !important;
  box-shadow:0 0 10px rgba(224,48,48,.16) !important;
}

.v102-speed-card.v102-high .v102-speed-needle{
  background:linear-gradient(180deg,rgba(255,208,208,.85),rgba(224,48,48,.78)) !important;
  box-shadow:0 0 8px rgba(224,48,48,.28) !important;
}

/* V102A_SPEED_OVERLAY_TUNE_END */
'''.strip() + "\n"

WEB_CSS.write_text(s.rstrip() + "\n\n" + tune, encoding="utf-8")
print("✅ web CSS ince ayar yazıldı")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron")

print()
print("===== KONTROL =====")
now = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
print(("✅ " if "V102A_SPEED_OVERLAY_TUNE_START" in now else "❌ ") + "V102A marker")
print("web sha:", sha(WEB_CSS))
print("and sha:", sha(AND_CSS))

print()
print("✅ V102A ince ayar tamam.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v102a-speed-tune")
