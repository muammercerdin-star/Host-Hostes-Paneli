from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS_FILES = [
    ROOT / "static/seats/patches/stop-badge-visible-v57.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/stop-badge-visible-v57.css",
]

CSS = r'''
/* STOP_BADGE_VISIBLE_V57 */
/* V56 performans yaması contain:paint ile dış rozetleri kırpıyordu.
   Koltuk performansını koruyup zil rozetini görünür yapar. */

.cell,
.deck,
.deck-wrap{
  overflow:visible !important;
}

.seat{
  overflow:visible !important;
}

/* Sadece inecek/zil olan koltuklarda paint clipping'i kaldır */
.seat.has-stop{
  contain:layout !important;
  overflow:visible !important;
  z-index:5 !important;
}

.seat.has-stop .stop-badge{
  display:flex !important;
  z-index:80 !important;
  left:-5px !important;
  bottom:-5px !important;
  min-width:24px !important;
  min-height:24px !important;
  padding:3px 6px !important;
  box-shadow:
    0 8px 18px rgba(0,0,0,.28),
    0 0 0 2px rgba(255,255,255,.18) !important;
}
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-stop-badge-v57-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== STOP BADGE VISIBLE V57 =====")

for p in CSS_FILES:
    p.parent.mkdir(parents=True, exist_ok=True)
    backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    line = '<link rel="stylesheet" href="/static/seats/patches/stop-badge-visible-v57.css?v=1">'

    if "stop-badge-visible-v57.css" not in s:
        if "</head>" in s:
            s = s.replace("</head>", line + "\n</head>", 1)
        else:
            s = line + "\n" + s
        print("✅ Link eklendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))

    p.write_text(s, encoding="utf-8")

print()
print("✅ V57 hazır. Commit/push yok. Önce tarayıcıda test et.")
