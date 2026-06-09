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

/* CONTINUE_V76_SHEET_BEAUTY_V79 */

/* Açılır detay panelini eski premium hissine yaklaştır */
#liveStopSheet,
.live-stop-sheet{
  backdrop-filter:blur(18px) saturate(1.1) !important;
  background:
    radial-gradient(circle at 18% 0%, rgba(224,48,48,.16), transparent 34%),
    radial-gradient(circle at 100% 20%, rgba(58,139,255,.10), transparent 30%),
    #11151b !important;
}

#liveStopSheet::before,
.live-stop-sheet::before{
  content:"" !important;
  position:absolute !important;
  inset:0 !important;
  pointer-events:none !important;
  background:repeating-linear-gradient(
    0deg,
    transparent,
    transparent 4px,
    rgba(255,255,255,.018) 4px,
    rgba(255,255,255,.018) 5px
  ) !important;
  border-radius:22px !important;
}

#liveStopSheet .sheet-head,
#liveStopSheet .sheet-body,
.live-stop-sheet .sheet-head,
.live-stop-sheet .sheet-body{
  position:relative !important;
  z-index:2 !important;
}

.sheet-kicker{
  font-family:ui-monospace,Menlo,monospace !important;
  color:#8a95a8 !important;
  letter-spacing:4px !important;
  text-transform:uppercase !important;
}

.sheet-title{
  text-shadow:0 0 18px rgba(255,255,255,.10) !important;
}

.sheet-sub{
  font-size:17px !important;
  color:#a6afc2 !important;
}

.sheet-close{
  box-shadow:0 8px 22px rgba(0,0,0,.35), inset 0 0 0 1px rgba(255,255,255,.03) !important;
}

/* İçerik düz yazı gibi görünmesin */
.sheet-body{
  margin-top:18px !important;
  font-size:18px !important;
  line-height:1.35 !important;
  color:#d8dde8 !important;
}

/* İçeride gelen düz div/p satırlarını kart hissine yaklaştır */
.sheet-body > div:not(.sheet-empty),
.sheet-body > p,
.sheet-body > section,
.sheet-body > article{
  background:rgba(24,28,35,.72) !important;
  border:1px solid rgba(138,149,168,.16) !important;
  border-radius:16px !important;
  padding:12px 14px !important;
  margin:10px 0 !important;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.02) !important;
}

/* Yolcu satırlarında boşluk ve okunurluk */
.sheet-body strong,
.sheet-body b{
  color:#fff !important;
  font-weight:900 !important;
}

.sheet-body small{
  color:#8a95a8 !important;
  letter-spacing:1.5px !important;
}

/* Düz HTML butonları premium butona çevir */
.sheet-body button,
#liveStopSheet button:not(.sheet-close),
.live-stop-sheet button:not(.sheet-close){
  appearance:none !important;
  border:1px solid rgba(224,136,32,.35) !important;
  background:linear-gradient(180deg, rgba(44,31,8,.95), rgba(24,28,35,.95)) !important;
  color:#f3c278 !important;
  border-radius:12px !important;
  padding:8px 12px !important;
  margin:6px 6px 4px 0 !important;
  font-family:ui-monospace,Menlo,monospace !important;
  font-size:14px !important;
  font-weight:900 !important;
  letter-spacing:.8px !important;
  box-shadow:0 8px 18px rgba(0,0,0,.25), inset 0 0 0 1px rgba(255,255,255,.025) !important;
}

/* İNDİR butonu kırmızı, daha net */
.sheet-body button:last-child,
#liveStopSheet button:last-child{
  border-color:rgba(224,48,48,.40) !important;
  background:linear-gradient(180deg, rgba(58,16,16,.95), rgba(24,28,35,.95)) !important;
  color:#ff7575 !important;
}

/* Boş durum kutusu daha güzel */
.sheet-empty{
  background:rgba(24,28,35,.72) !important;
  border:1px dashed rgba(138,149,168,.25) !important;
  border-radius:18px !important;
  color:#8a95a8 !important;
  font-size:20px !important;
  line-height:1.35 !important;
  padding:34px 20px !important;
}

/* Bagaj yok / emanet yok satırları daha premium dursun */
.sheet-body:has(.sheet-empty){
  text-align:center !important;
}

@media(max-width:420px){
  .sheet-body{
    font-size:17px !important;
  }

  .sheet-body button,
  #liveStopSheet button:not(.sheet-close),
  .live-stop-sheet button:not(.sheet-close){
    font-size:13px !important;
    padding:8px 10px !important;
  }

  .sheet-empty{
    font-size:18px !important;
  }
}
'''

print("===== CONTINUE V76 SHEET BEAUTY V79 =====")

for p in CSS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sheet-beauty-v79-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "CONTINUE_V76_SHEET_BEAUTY_V79" in s:
        print("ℹ️ V79 zaten var:", p.relative_to(ROOT))
        continue

    s = s.rstrip() + "\n" + PATCH + "\n"
    p.write_text(s, encoding="utf-8")
    print("✅ Modal süsleme eklendi:", p.relative_to(ROOT))

print()
print("===== CACHE KIR =====")
for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sheet-beauty-v79-cache-{STAMP}")
    shutil.copy2(p, b)

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue/continue_v76\.css'\) }}\?v=[^\"']+",
        "continue/continue_v76.css') }}?v=prototype-layout-v79",
        s
    )
    p.write_text(s, encoding="utf-8")
    print("✅ Cache:", p.relative_to(ROOT))

print()
print("✅ V79 tamam.")
