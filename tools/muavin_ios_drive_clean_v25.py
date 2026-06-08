from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_REL = "static/seats/patches/ios-drive-clean-v25.css"
ANDROID_CSS_REL = "android_app/app/src/main/python/static/seats/patches/ios-drive-clean-v25.css"

CSS = r'''
/* =========================================================
   IOS_DRIVE_CLEAN_V25
   Amaç: Sürüş/Koltuk ekranında kalabalığı azaltmak.
   Sadece görünüm yaması. JS / kayıt / koltuk mantığına dokunmaz.
========================================================= */

@media(max-width:700px){

  /* ÜST SEFER KARTINI SADELEŞTİR */
  .seats-shell > :first-child{
    margin:10px 10px 8px !important;
    padding:14px 16px !important;
    border-radius:24px !important;
    min-height:auto !important;
  }

  .seats-shell > :first-child h1,
  .seats-shell > :first-child h2{
    font-size:26px !important;
    line-height:1.08 !important;
    margin:0 0 6px !important;
  }

  .seats-shell > :first-child .mini-chip,
  .seats-shell > :first-child a,
  .seats-shell > :first-child button,
  .seats-shell > :first-child .topbar-actions,
  .seats-shell > :first-child .quick-actions,
  .seats-shell > :first-child .action-row,
  .seats-shell > :first-child .actions{
    display:none !important;
  }

  /* KARTLAR ARASI BOŞLUĞU AZALT */
  .layout{
    gap:8px !important;
  }

  .board-card.glass{
    margin-top:8px !important;
    border-radius:26px !important;
  }

  .board-inner{
    padding:14px 14px 16px !important;
  }

  /* SÜRÜŞ / ETA SATIRINI 2 KUTUYA DÜŞÜR */
  #driveInlineDock{
    display:grid !important;
    grid-template-columns:minmax(0,1fr) minmax(112px,.72fr) !important;
    gap:10px !important;
    margin:0 0 10px 0 !important;
    min-height:0 !important;
    overflow:visible !important;
  }

  #driveSpeedChip{
    display:none !important;
  }

  #driveModeToggle{
    width:100% !important;
    height:52px !important;
    min-height:52px !important;
    border-radius:20px !important;
    font-size:17px !important;
    font-weight:1000 !important;
    padding:0 12px !important;
  }

  #driveEtaChip{
    height:52px !important;
    min-height:52px !important;
    border-radius:20px !important;
    padding:7px 10px !important;
  }

  .drive-eta-top{
    font-size:15px !important;
  }

  .drive-eta-sub{
    font-size:10.5px !important;
  }

  /* KOLTUK PLANI BAŞLIK KALABALIĞINI KALDIR */
  .board-head{
    display:block !important;
    margin:0 !important;
    padding:0 !important;
  }

  .board-title{
    display:block !important;
    margin:0 !important;
    padding:0 !important;
  }

  .board-kicker,
  .board-title h2,
  .board-title > small{
    display:none !important;
  }

  /* SEÇİLİ DURAK TEK SADE BAR */
  .selected-stop-chip{
    width:100% !important;
    min-height:44px !important;
    height:44px !important;
    margin:0 0 10px 0 !important;
    padding:0 14px !important;

    display:flex !important;
    align-items:center !important;
    gap:8px !important;

    border-radius:18px !important;
    font-size:14px !important;
    line-height:1 !important;

    white-space:nowrap !important;
    overflow:hidden !important;
  }

  .selected-stop-chip b{
    min-width:0 !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    white-space:nowrap !important;
  }

  /* ESKİ SES SATIRINI GİZLE, DRIVE SES SATIRI KALSIN */
  .voice-row{
    display:none !important;
  }

  .board-head-right{
    width:100% !important;
    margin:0 !important;
    padding:0 !important;
  }

  #driveVoiceRow{
    display:grid !important;
    grid-template-columns:minmax(0,1fr) 116px !important;
    gap:10px !important;
    margin:0 0 10px 0 !important;
  }

  #btnDeckAIDrive,
  .drive-voice-btn{
    height:58px !important;
    min-height:58px !important;
    border-radius:22px !important;
    font-size:18px !important;
    font-weight:1000 !important;
  }

  #driveVoiceSeatCard,
  .drive-voice-seat{
    height:58px !important;
    min-height:58px !important;
    border-radius:22px !important;
    padding:0 10px !important;
  }

  .drive-voice-seat-values{
    font-size:22px !important;
  }

  /* ÜSTTEKİ LEJAND KALDIRILSIN; ALTAKİ SABİT LEJAND ZATEN VAR */
  .board-head-right .legend,
  .legend{
    display:none !important;
  }

  /* DURAK AKIŞI DAHA KOMPAKT */
  .route-strip-shell{
    margin-top:8px !important;
    border-radius:22px !important;
    padding:12px !important;
    max-height:238px !important;
    overflow:hidden !important;
  }

  .route-strip-title{
    font-size:18px !important;
    line-height:1.1 !important;
    margin:0 0 10px 0 !important;
  }

  .route-live-row{
    display:grid !important;
    grid-template-columns:minmax(0,1fr) minmax(0,1fr) 48px !important;
    gap:8px !important;
    margin-bottom:8px !important;
  }

  .route-live-row .mini-chip{
    min-height:42px !important;
    height:42px !important;
    border-radius:16px !important;
    padding:0 10px !important;
    font-size:12.5px !important;
    overflow:hidden !important;
  }

  .route-live-row .mini-chip span,
  .route-live-row .mini-chip b{
    min-width:0 !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
  }

  .route-strip,
  .route-cards,
  .route-stop-list{
    gap:8px !important;
  }

  .route-stop-card,
  .route-card,
  .stop-card{
    min-height:106px !important;
    border-radius:20px !important;
    padding:12px !important;
  }

  /* Alttaki koltuk planı biraz yukarı gelsin */
  .deck-wrap{
    margin-top:8px !important;
  }
}

@media(max-width:380px){
  .seats-shell > :first-child h1,
  .seats-shell > :first-child h2{
    font-size:23px !important;
  }

  #driveInlineDock{
    grid-template-columns:minmax(0,1fr) 108px !important;
    gap:8px !important;
  }

  #driveModeToggle,
  #driveEtaChip{
    height:48px !important;
    min-height:48px !important;
  }

  #driveVoiceRow{
    grid-template-columns:minmax(0,1fr) 106px !important;
    gap:8px !important;
  }

  #btnDeckAIDrive,
  .drive-voice-btn,
  #driveVoiceSeatCard,
  .drive-voice-seat{
    height:54px !important;
    min-height:54px !important;
  }
}
'''

TARGETS = [
    ROOT / CSS_REL,
    ROOT / ANDROID_CSS_REL,
]

TPLS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-drive-clean-v25.css?v=1">'

print("===== IOS DRIVE CLEAN V25 =====")

for p in TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    backup = p.with_name(p.name + f".bak-ios-drive-clean-v25-{STAMP}")
    shutil.copy2(p, backup)

    lines = s.splitlines()

    # Eski V25 linki varsa temizle
    lines = [ln for ln in lines if "ios-drive-clean-v25.css" not in ln]

    # seats-shell'den hemen önce en son CSS olarak ekle
    insert_at = None
    for i, ln in enumerate(lines):
        if '<div class="seats-shell">' in ln:
            insert_at = i
            break

    if insert_at is None:
        insert_at = 0
        for i, ln in enumerate(lines):
            if '<link rel="stylesheet"' in ln:
                insert_at = i + 1

    lines.insert(insert_at, LINK)
    new = "\n".join(lines) + "\n"

    if new != old:
        p.write_text(new, encoding="utf-8")
        print("✅ Link eklendi/en sona alındı:", p.relative_to(ROOT))
        print("   Yedek:", backup.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik yok:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), "IOS_DRIVE_CLEAN_V25:", txt.count("IOS_DRIVE_CLEAN_V25"))

for p in TPLS:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT), "ios-drive-clean-v25:", txt.count("ios-drive-clean-v25"))

print()
print("✅ V25 tamamlandı. Chrome’da /seats?v=25 ile yenile.")
