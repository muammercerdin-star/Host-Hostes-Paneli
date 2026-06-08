from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

CSS_MAIN_FILES = [
    ROOT / "static/continue/continue_trip.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css",
]

CSS_PART_FILES = [
    ROOT / "static/continue/css_parts/73-seat-map-glass-effect-v46.css",
    ROOT / "android_app/app/src/main/python/static/continue/css_parts/73-seat-map-glass-effect-v46.css",
]

CSS = r'''
/* =========================================================
   CONTINUE_SEAT_MAP_GLASS_EFFECT_V46
   V45 koltuk planını kaba tam ekran yerine cam/blur modal efekti yapar.
   Sadece görünüm. API/JS mantığına dokunmaz.
========================================================= */

#continueSeatMapFullscreenV45{
  background:rgba(2,6,23,.62) !important;
  backdrop-filter:blur(18px) saturate(1.25) !important;
  -webkit-backdrop-filter:blur(18px) saturate(1.25) !important;
}

#continueSeatMapFullscreenV45::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    radial-gradient(circle at 18% 12%, rgba(37,99,235,.28), transparent 34%),
    radial-gradient(circle at 84% 10%, rgba(244,63,94,.18), transparent 32%),
    radial-gradient(circle at 50% 100%, rgba(14,165,233,.13), transparent 38%);
}

#continueSeatMapFullscreenV45 .v45-seatmap-page{
  position:absolute !important;
  left:14px !important;
  right:14px !important;
  top:calc(74px + env(safe-area-inset-top)) !important;
  bottom:calc(18px + env(safe-area-inset-bottom)) !important;
  inset:auto 14px calc(18px + env(safe-area-inset-bottom)) 14px !important;

  padding:20px 12px 12px !important;
  overflow:hidden !important;

  border-radius:34px !important;
  border:1px solid rgba(148,163,184,.28) !important;

  background:
    linear-gradient(180deg, rgba(15,23,42,.88), rgba(2,6,23,.88)) padding-box,
    linear-gradient(135deg, rgba(96,165,250,.55), rgba(255,255,255,.10), rgba(244,63,94,.34)) border-box !important;

  box-shadow:
    0 36px 92px rgba(0,0,0,.62),
    0 0 0 1px rgba(255,255,255,.05),
    inset 0 1px 0 rgba(255,255,255,.12) !important;
}

#continueSeatMapFullscreenV45 .v45-seatmap-page::before{
  content:"";
  position:absolute;
  top:10px;
  left:50%;
  width:96px;
  height:7px;
  transform:translateX(-50%);
  border-radius:999px;
  background:rgba(226,232,240,.28);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.18);
}

#continueSeatMapFullscreenV45 .v45-seatmap-page::after{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  border-radius:34px;
  background:
    linear-gradient(180deg, rgba(255,255,255,.07), transparent 22%),
    radial-gradient(circle at 50% 0%, rgba(96,165,250,.13), transparent 34%);
}

#continueSeatMapFullscreenV45 .v45-seatmap-close{
  position:absolute !important;
  top:calc(88px + env(safe-area-inset-top)) !important;
  right:28px !important;

  width:48px !important;
  height:48px !important;
  border-radius:18px !important;

  border:1px solid rgba(255,255,255,.18) !important;
  background:
    radial-gradient(circle at 28% 18%, rgba(255,255,255,.24), transparent 34%),
    rgba(15,23,42,.78) !important;

  color:#fff !important;
  font-size:29px !important;
  font-weight:900 !important;

  box-shadow:
    0 18px 42px rgba(0,0,0,.42),
    inset 0 1px 0 rgba(255,255,255,.14) !important;
}

#continueSeatMapFullscreenV45 .v45-seatmap-board{
  position:relative !important;
  z-index:1 !important;

  height:100% !important;
  min-height:unset !important;
  overflow:auto !important;

  padding:18px 14px 24px !important;
  border-radius:26px !important;

  border:1px solid rgba(148,163,184,.16) !important;
  background:
    radial-gradient(circle at 50% 0%, rgba(37,99,235,.18), transparent 32%),
    linear-gradient(180deg, rgba(15,23,42,.70), rgba(2,6,23,.72)) !important;

  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.07),
    inset 0 0 0 1px rgba(255,255,255,.025) !important;
}

#continueSeatMapFullscreenV45 .v45-seat{
  border-radius:18px !important;
  box-shadow:
    0 12px 26px rgba(0,0,0,.28),
    inset 0 1px 0 rgba(255,255,255,.13) !important;
}

#continueSeatMapFullscreenV45 .v45-seat.is-empty{
  opacity:.42 !important;
  background:
    radial-gradient(circle at 30% 16%, rgba(255,255,255,.08), transparent 36%),
    linear-gradient(180deg, rgba(51,65,85,.34), rgba(15,23,42,.66)) !important;
}

#continueSeatMapFullscreenV45 .v45-seat.is-full{
  background:
    radial-gradient(circle at 28% 14%, rgba(255,255,255,.22), transparent 34%),
    linear-gradient(180deg, rgba(37,99,235,.92), rgba(29,78,216,.82)) !important;
}

#continueSeatMapFullscreenV45 .v45-seat.is-female{
  background:
    radial-gradient(circle at 28% 14%, rgba(255,255,255,.22), transparent 34%),
    linear-gradient(180deg, rgba(219,39,119,.94), rgba(157,23,77,.86)) !important;
}

#continueSeatMapFullscreenV45 .v45-seat.is-due{
  outline:0 !important;
  border-color:rgba(250,204,21,.88) !important;
  box-shadow:
    0 0 0 3px rgba(250,204,21,.62),
    0 0 32px rgba(250,204,21,.34),
    0 12px 26px rgba(0,0,0,.30),
    inset 0 1px 0 rgba(255,255,255,.16) !important;
}

#continueSeatMapFullscreenV45 .v45-seatmap-corridor{
  background:rgba(15,23,42,.30) !important;
  border-color:rgba(148,163,184,.16) !important;
  color:rgba(226,232,240,.24) !important;
}

#continueSeatMapFullscreenV45 .v45-seatmap-loading{
  position:absolute;
  inset:0;
  display:grid;
  place-items:center;
  color:rgba(226,232,240,.88);
  background:rgba(2,6,23,.58);
  backdrop-filter:blur(12px);
  -webkit-backdrop-filter:blur(12px);
}

@media(max-width:420px){
  #continueSeatMapFullscreenV45 .v45-seatmap-page{
    left:10px !important;
    right:10px !important;
    top:calc(70px + env(safe-area-inset-top)) !important;
    bottom:calc(14px + env(safe-area-inset-bottom)) !important;
    border-radius:31px !important;
    padding:18px 10px 10px !important;
  }

  #continueSeatMapFullscreenV45 .v45-seatmap-close{
    top:calc(82px + env(safe-area-inset-top)) !important;
    right:22px !important;
    width:45px !important;
    height:45px !important;
    border-radius:17px !important;
    font-size:28px !important;
  }

  #continueSeatMapFullscreenV45 .v45-seatmap-board{
    padding:16px 12px 22px !important;
    border-radius:24px !important;
  }
}
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-glass-effect-v46-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== SEAT MAP GLASS EFFECT V46 =====")

# 1) CSS part yaz
for p in CSS_PART_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

# 2) Ana CSS'e import ekle
for p in CSS_MAIN_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    lines = []
    for line in s.splitlines():
        if "73-seat-map-glass-effect-v46.css" in line:
            continue
        lines.append(line)

    lines.append('@import url("./css_parts/73-seat-map-glass-effect-v46.css");')

    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("✅ CSS import eklendi:", p.relative_to(ROOT))

# 3) Template cache güncelle
for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(r"continue_trip\.css'\) }}\?v=[^\"']+", "continue_trip.css') }}?v=seat-map-v46", s)
    s = re.sub(r'continue_trip\.css"\) }}\?v=[^"\']+', 'continue_trip.css") }}?v=seat-map-v46', s)

    p.write_text(s, encoding="utf-8")
    print("✅ Template cache V46:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in CSS_MAIN_FILES + CSS_PART_FILES + TPL_FILES:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(
            p.relative_to(ROOT),
            "V46:", txt.count("seat-map-v46") + txt.count("73-seat-map-glass-effect-v46") + txt.count("GLASS_EFFECT_V46")
        )

print()
print("✅ V46 cam efekt yaması tamam.")
