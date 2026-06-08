from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_REL = "static/seats/patches/ios-drive-panel-v23.css"
CSS_ANDROID_REL = "android_app/app/src/main/python/static/seats/patches/ios-drive-panel-v23.css"

CSS_TARGETS = [
    ROOT / CSS_REL,
    ROOT / CSS_ANDROID_REL,
]

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS = r'''
/* =========================================================
   IOS_DRIVE_PANEL_DESIGN_V23
   Sadece tasarım yaması.
   JS, kayıt, sürüş modu mantığı ve veri akışına dokunmaz.
========================================================= */

:root{
  --ios23-bg-1:#071426;
  --ios23-bg-2:#0b1d33;
  --ios23-glass:rgba(18,38,64,.58);
  --ios23-glass-2:rgba(255,255,255,.075);
  --ios23-line:rgba(185,213,255,.16);
  --ios23-line-2:rgba(255,255,255,.10);
  --ios23-text:#f4f8ff;
  --ios23-muted:rgba(226,235,255,.70);
  --ios23-blue:#3b82f6;
  --ios23-blue-2:#60a5fa;
  --ios23-green:#7ee787;
  --ios23-red:#ff6b6b;
  --ios23-shadow:0 18px 44px rgba(0,0,0,.34);
}

/* Ana kart: daha sakin cam yüzey */
.board-card.glass{
  background:
    radial-gradient(circle at 20% 0%, rgba(59,130,246,.18), transparent 36%),
    radial-gradient(circle at 95% 15%, rgba(96,165,250,.09), transparent 32%),
    linear-gradient(180deg, rgba(13,32,55,.82), rgba(6,16,30,.92)) !important;
  border:1px solid rgba(173,205,255,.14) !important;
  box-shadow:0 24px 70px rgba(0,0,0,.36) !important;
  border-radius:28px !important;
}

.board-inner{
  background:
    linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.012)) !important;
  border-radius:26px !important;
}

/* Üst sürüş dock: 2 satırlı iOS kontrol alanı hissi */
#driveInlineDock{
  display:grid !important;
  grid-template-columns:1fr 1fr !important;
  gap:10px !important;
  width:100% !important;
  margin:0 0 14px 0 !important;
  padding:0 !important;
  overflow:visible !important;
}

/* Sürüş/normal butonu */
#driveModeToggle{
  grid-column:1 / 2 !important;
  height:54px !important;
  min-height:54px !important;
  border-radius:21px !important;
  padding:0 14px !important;

  background:
    linear-gradient(180deg, rgba(73,142,255,.95), rgba(37,99,235,.95)) !important;
  border:1px solid rgba(191,219,254,.30) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.24),
    0 14px 30px rgba(37,99,235,.26) !important;

  color:#fff !important;
  font-size:15px !important;
  font-weight:950 !important;
  letter-spacing:.01em !important;
}

/* Hız ve rötar cam kapsülleri */
#driveSpeedChip,
#driveEtaChip,
.drive-speed-chip,
.drive-eta-chip{
  min-height:54px !important;
  height:54px !important;
  border-radius:21px !important;
  padding:9px 13px !important;

  background:
    linear-gradient(180deg, rgba(255,255,255,.095), rgba(255,255,255,.045)) !important;
  border:1px solid var(--ios23-line) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.13),
    0 14px 30px rgba(0,0,0,.20) !important;

  backdrop-filter:blur(18px) saturate(1.25) !important;
  -webkit-backdrop-filter:blur(18px) saturate(1.25) !important;
}

/* Sıralama: Normal + hız + rötar */
#driveSpeedChip{
  grid-column:2 / 3 !important;
}

#driveEtaChip{
  grid-column:1 / 3 !important;
}

.drive-speed-top,
.drive-eta-top{
  font-weight:900 !important;
  color:var(--ios23-text) !important;
}

.drive-speed-top b,
.drive-eta-top b{
  font-size:20px !important;
  font-weight:1000 !important;
}

.drive-speed-sub,
.drive-eta-sub{
  color:var(--ios23-muted) !important;
  font-size:11.5px !important;
  font-weight:800 !important;
}

/* Başlık alanını sadeleştir */
.board-head{
  display:block !important;
  margin-top:2px !important;
  padding:0 !important;
}

.board-title{
  display:block !important;
}

.board-kicker,
.board-title h2,
.board-title > small{
  display:none !important;
}

/* Seçili durak: tek temiz kapsül */
.selected-stop-chip{
  width:100% !important;
  min-height:52px !important;
  margin:2px 0 14px 0 !important;
  padding:0 16px !important;

  display:flex !important;
  align-items:center !important;
  justify-content:flex-start !important;
  gap:8px !important;

  border-radius:22px !important;
  background:
    linear-gradient(180deg, rgba(255,255,255,.085), rgba(255,255,255,.040)) !important;
  border:1px solid var(--ios23-line) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.12),
    0 12px 28px rgba(0,0,0,.18) !important;

  color:rgba(235,242,255,.78) !important;
  font-size:15px !important;
  font-weight:800 !important;
}

.selected-stop-chip b{
  color:#fff !important;
  font-weight:1000 !important;
}

/* Sağ alan artık ayrı kart gibi değil, akışın içinde */
.board-head-right{
  width:100% !important;
  display:block !important;
}

/* Eski voice row yerine daha düzenli görünüm */
.voice-row{
  display:grid !important;
  grid-template-columns:1fr 112px !important;
  gap:10px !important;
  align-items:stretch !important;
  margin:0 0 12px 0 !important;
}

.voice-command-btn{
  height:70px !important;
  min-height:70px !important;
  border-radius:25px !important;

  display:flex !important;
  align-items:center !important;
  justify-content:center !important;
  gap:13px !important;

  background:
    linear-gradient(135deg, rgba(99,102,241,.98), rgba(59,130,246,.98)) !important;
  border:1px solid rgba(191,219,254,.30) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.25),
    0 18px 36px rgba(59,130,246,.28) !important;

  color:#fff !important;
  font-size:21px !important;
  font-weight:1000 !important;
  letter-spacing:.01em !important;
}

.voice-command-btn span{
  font-size:21px !important;
  font-weight:1000 !important;
}

.voice-seat-mini{
  height:70px !important;
  min-height:70px !important;
  border-radius:25px !important;

  display:flex !important;
  flex-direction:column !important;
  align-items:center !important;
  justify-content:center !important;
  gap:4px !important;

  background:
    linear-gradient(180deg, rgba(255,255,255,.095), rgba(255,255,255,.045)) !important;
  border:1px solid var(--ios23-line) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.12),
    0 14px 30px rgba(0,0,0,.20) !important;

  color:rgba(235,242,255,.76) !important;
}

.voice-seat-mini span{
  font-size:12px !important;
  font-weight:850 !important;
}

.voice-seat-mini b{
  font-size:25px !important;
  font-weight:1000 !important;
  color:var(--ios23-blue-2) !important;
}

/* Hazır badge kalabalık yapıyorsa gizle */
.voice-state{
  display:none !important;
}

/* Sürüş modundaki ikinci voice satır da aynı dili kullansın */
.drive-voice-row{
  display:grid !important;
  grid-template-columns:1fr 112px !important;
  gap:10px !important;
  align-items:stretch !important;
  margin:0 0 12px 0 !important;
}

.drive-voice-btn{
  min-height:70px !important;
  border-radius:25px !important;
  background:
    linear-gradient(135deg, rgba(99,102,241,.98), rgba(59,130,246,.98)) !important;
  border:1px solid rgba(191,219,254,.30) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.25),
    0 18px 36px rgba(59,130,246,.28) !important;
  color:#fff !important;
  font-size:21px !important;
  font-weight:1000 !important;
}

.drive-voice-seat{
  min-height:70px !important;
  border-radius:25px !important;
  background:
    linear-gradient(180deg, rgba(255,255,255,.095), rgba(255,255,255,.045)) !important;
  border:1px solid var(--ios23-line) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.12),
    0 14px 30px rgba(0,0,0,.20) !important;
}

.drive-voice-seat-values b:first-child{
  color:var(--ios23-blue-2) !important;
}

.drive-voice-seat-values b:last-child{
  color:var(--ios23-green) !important;
}

/* Üstteki legend: cam kapsül */
.legend{
  position:sticky !important;
  bottom:8px !important;
  z-index:40 !important;

  width:100% !important;
  margin:12px 0 10px 0 !important;
  padding:10px 12px !important;

  display:flex !important;
  align-items:center !important;
  justify-content:space-between !important;
  gap:8px !important;
  flex-wrap:nowrap !important;

  border-radius:22px !important;
  background:
    linear-gradient(180deg, rgba(15,31,52,.82), rgba(8,18,34,.88)) !important;
  border:1px solid rgba(185,213,255,.16) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.10),
    0 18px 42px rgba(0,0,0,.30) !important;

  backdrop-filter:blur(18px) saturate(1.25) !important;
  -webkit-backdrop-filter:blur(18px) saturate(1.25) !important;
}

.legend .mini-chip,
.mini-chip{
  min-width:auto !important;
  padding:0 !important;
  background:transparent !important;
  border:0 !important;
  box-shadow:none !important;

  color:rgba(241,247,255,.90) !important;
  font-size:12.5px !important;
  font-weight:900 !important;
  white-space:nowrap !important;
}

/* Durak Akışı kartı */
.route-strip-shell,
.route-flow-shell,
#routeStrip{
  border-radius:26px !important;
  background:
    radial-gradient(circle at 15% 0%, rgba(96,165,250,.13), transparent 36%),
    linear-gradient(180deg, rgba(255,255,255,.070), rgba(255,255,255,.030)) !important;
  border:1px solid var(--ios23-line) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.11),
    0 18px 42px rgba(0,0,0,.24) !important;
  backdrop-filter:blur(16px) saturate(1.18) !important;
  -webkit-backdrop-filter:blur(16px) saturate(1.18) !important;
}

.route-strip-title,
.route-flow-title{
  color:#fff !important;
  font-size:20px !important;
  font-weight:1000 !important;
  letter-spacing:.01em !important;
}

/* Durak kartları */
.route-stop,
.route-stop-card,
.stop-card{
  border-radius:22px !important;
  background:
    linear-gradient(180deg, rgba(255,255,255,.078), rgba(255,255,255,.032)) !important;
  border:1px solid rgba(185,213,255,.14) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.10),
    0 12px 28px rgba(0,0,0,.18) !important;
}

/* Alt panel tabs biraz daha iOS kapsül */
.panel-card.glass{
  border-radius:28px !important;
  background:
    linear-gradient(180deg, rgba(15,31,52,.82), rgba(8,18,34,.92)) !important;
  border:1px solid rgba(185,213,255,.14) !important;
  box-shadow:0 -10px 42px rgba(0,0,0,.24) !important;
}

.panel-tabs{
  background:rgba(255,255,255,.045) !important;
  border:1px solid rgba(185,213,255,.12) !important;
  border-radius:22px !important;
  padding:6px !important;
  gap:6px !important;
}

.tab-btn{
  border-radius:17px !important;
  font-weight:900 !important;
}

.tab-btn.active{
  background:
    linear-gradient(180deg, rgba(59,130,246,.95), rgba(37,99,235,.95)) !important;
  color:#fff !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.20),
    0 10px 22px rgba(37,99,235,.25) !important;
}

/* Sadece görsel: küçük ekran dengeleme */
@media(max-width:430px){
  .board-card.glass{
    border-radius:24px !important;
  }

  #driveInlineDock{
    gap:8px !important;
  }

  #driveModeToggle,
  #driveSpeedChip,
  #driveEtaChip,
  .drive-speed-chip,
  .drive-eta-chip{
    min-height:50px !important;
    height:50px !important;
    border-radius:19px !important;
  }

  .voice-row,
  .drive-voice-row{
    grid-template-columns:1fr 104px !important;
    gap:8px !important;
  }

  .voice-command-btn,
  .voice-seat-mini,
  .drive-voice-btn,
  .drive-voice-seat{
    min-height:64px !important;
    height:64px !important;
    border-radius:22px !important;
  }

  .voice-command-btn,
  .voice-command-btn span,
  .drive-voice-btn{
    font-size:19px !important;
  }

  .selected-stop-chip{
    min-height:48px !important;
    border-radius:20px !important;
    font-size:14px !important;
  }

  .legend{
    padding:9px 10px !important;
    gap:6px !important;
    overflow-x:auto !important;
    justify-content:flex-start !important;
    scrollbar-width:none !important;
  }

  .legend::-webkit-scrollbar{
    display:none !important;
  }

  .legend .mini-chip,
  .mini-chip{
    font-size:12px !important;
  }
}
'''

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-drive-panel-v23.css?v=ios-drive-panel-v23">'

def backup(p: Path):
    b = p.with_name(p.name + f".bak-ios-drive-panel-v23-{STAMP}")
    shutil.copy2(p, b)
    return b

print("===== IOS DRIVE PANEL DESIGN V23 =====")

for p in CSS_TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        backup(p)
    p.write_text(CSS.strip() + "\n", encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ios-drive-panel-v23.css" in s:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))
        continue

    b = backup(p)

    # En güvenli yer: mevcut patch css linklerinin sonuna ekle.
    anchor = '<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">'
    if anchor in s:
        s = s.replace(anchor, anchor + "\n" + LINK, 1)
    else:
        # fallback: ilk <div class="seats-shell"> öncesine ekle
        s = s.replace('<div class="seats-shell">', LINK + "\n<div class=\"seats-shell\">", 1)

    p.write_text(s, encoding="utf-8")
    print("✅ Template link eklendi:", p.relative_to(ROOT))
    print("   Yedek:", b.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in CSS_TARGETS:
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    print(p.relative_to(ROOT), "IOS_DRIVE_PANEL_DESIGN_V23:", txt.count("IOS_DRIVE_PANEL_DESIGN_V23"))

for p in TPL_TARGETS:
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    print(p.relative_to(ROOT), "ios-drive-panel-v23.css:", txt.count("ios-drive-panel-v23.css"))

print()
print("✅ V23 sadece tasarım yaması tamamlandı.")
