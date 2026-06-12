from pathlib import Path
from datetime import datetime
import shutil
import re
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/continue/continue_speed_overlay_v102.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/continue/continue_speed_overlay_v102.css"

print("===== V102B HIZ OVERLAY SON İNCE AYAR =====")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

if not WEB_CSS.exists():
    raise SystemExit("❌ V102 CSS yok")

for p in [WEB_CSS, AND_CSS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v102b-speed-final-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_CSS.read_text(encoding="utf-8", errors="ignore")

s = re.sub(
    r"\n?/\* V102B_SPEED_OVERLAY_FINAL_TUNE_START \*/.*?/\* V102B_SPEED_OVERLAY_FINAL_TUNE_END \*/\n?",
    "\n",
    s,
    flags=re.S
)

tune = r'''
/* V102B_SPEED_OVERLAY_FINAL_TUNE_START */

/* Kutuyu kesinlikle büyütme */
.v102-speed-card{
  min-height:89px !important;
  max-height:89px !important;
  padding-top:13px !important;
  padding-bottom:12px !important;
}

/* Ana dijital yazı her şeyin üstünde ve net */
.v102-speed-card .v99-gauge-label{
  z-index:20 !important;
}

.v102-speed-card .v99-gauge-val{
  z-index:22 !important;
  font-size:23px !important;
  line-height:1 !important;
  color:#f1a340 !important;
  text-shadow:
    0 0 10px rgba(241,163,64,.38),
    0 2px 6px rgba(0,0,0,.85) !important;
}

.v102-speed-card .v99-gauge-unit{
  z-index:22 !important;
  position:relative !important;
  margin-top:2px !important;
  opacity:.62 !important;
  color:rgba(232,238,248,.60) !important;
  text-shadow:0 2px 5px rgba(0,0,0,.90) !important;
}

/* Overlay tamamen dekor olsun */
.v102-speed-overlay{
  z-index:1 !important;
  opacity:.42 !important;
}

/* Alt hız barı daha sade */
.v102-speed-bar{
  left:22px !important;
  right:22px !important;
  bottom:9px !important;
  height:2px !important;
  opacity:.35 !important;
}

/* Analog yayı daha yukarı değil, arka plan gibi ortada dursun */
.v102-speed-arc{
  top:36px !important;
  width:68px !important;
  height:29px !important;
  border-width:2px !important;
  opacity:0 !important;
  filter:none !important;
}

/* İbre artık yazıyı kesmeyecek kadar kısa ve sönük */
.v102-speed-needle{
  top:48px !important;
  height:18px !important;
  width:2px !important;
  opacity:0 !important;
  box-shadow:none !important;
}

/* Orta nokta daha geride */
.v102-speed-dot{
  top:61px !important;
  width:6px !important;
  height:6px !important;
  opacity:0 !important;
  box-shadow:0 0 8px rgba(255,224,165,.22) !important;
}

/* Analog açıkken bile gösterge hayalet gibi kalsın */
.v102-speed-card.v102-speed-analog-on .v102-speed-arc{
  opacity:.34 !important;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-needle{
  opacity:.32 !important;
}

.v102-speed-card.v102-speed-analog-on .v102-speed-dot{
  opacity:.36 !important;
}

/* Açık modda yeşil parlamayı azalt */
.v102-speed-card.v102-speed-analog-on{
  background:
    radial-gradient(circle at 50% 72%, rgba(224,136,32,.055), transparent 45%),
    var(--v99-panel) !important;
}

/* Düşük hız yeşili daha koyu, gözü yormasın */
.v102-speed-card.v102-low .v102-speed-arc{
  border-color:rgba(29,184,122,.28) !important;
  box-shadow:0 0 8px rgba(29,184,122,.08) !important;
}

.v102-speed-card.v102-low .v102-speed-needle{
  background:linear-gradient(180deg,rgba(184,255,224,.55),rgba(29,184,122,.50)) !important;
}

/* Yüksek hız kırmızısı da kontrollü */
.v102-speed-card.v102-high .v102-speed-arc{
  border-color:rgba(224,48,48,.34) !important;
  box-shadow:0 0 8px rgba(224,48,48,.10) !important;
}

.v102-speed-card.v102-high .v102-speed-needle{
  background:linear-gradient(180deg,rgba(255,205,205,.58),rgba(224,48,48,.52)) !important;
}

/* V102B_SPEED_OVERLAY_FINAL_TUNE_END */
'''.strip() + "\n"

WEB_CSS.write_text(s.rstrip() + "\n\n" + tune, encoding="utf-8")
print("✅ web CSS yazıldı")

if AND_CSS.parent.exists():
    shutil.copy2(WEB_CSS, AND_CSS)
    print("✅ android CSS senkron")

print()
print("===== KONTROL =====")
now = WEB_CSS.read_text(encoding="utf-8", errors="ignore")
print(("✅ " if "V102B_SPEED_OVERLAY_FINAL_TUNE_START" in now else "❌ ") + "V102B marker")
print("web sha:", sha(WEB_CSS))
print("and sha:", sha(AND_CSS))

print()
print("✅ V102B son ince ayar tamam.")
print("Yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v102b-speed-final")
