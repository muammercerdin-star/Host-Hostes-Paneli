from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_CSS = ROOT / "static/seats/patches/ios-lower-board-compact-v31.css"
AND_CSS = ROOT / "android_app/app/src/main/python/static/seats/patches/ios-lower-board-compact-v31.css"

TEMPLATES = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS = r'''/* =========================================================
   IOS_LOWER_BOARD_COMPACT_V31
   Amaç: Üst sefer kartına dokunmadan alt Koltuk Planı bölümünü
   daha sade, daha kısa ve daha az kalabalık yapmak.
========================================================= */

@media (max-width: 520px){

  /* Alt ana kart: Koltuk Planı bölümünü biraz sıkıştır */
  .board-card.glass{
    margin-top:10px !important;
    border-radius:24px !important;
    padding:10px !important;
  }

  .board-inner{
    padding:0 !important;
  }

  /* Sürüş / rötar satırı daha kısa */
  #driveInlineDock{
    min-height:42px !important;
    height:auto !important;
    gap:8px !important;
    margin:0 0 8px 0 !important;
    padding:0 !important;
  }

  #driveModeToggle{
    height:42px !important;
    min-height:42px !important;
    border-radius:16px !important;
    font-size:15px !important;
    padding:0 12px !important;
  }

  #driveEtaChip,
  .drive-eta-chip{
    height:42px !important;
    min-height:42px !important;
    border-radius:16px !important;
    padding:6px 10px !important;
  }

  .drive-eta-top{
    font-size:14px !important;
    line-height:1 !important;
  }

  .drive-eta-top b{
    font-size:15px !important;
  }

  .drive-eta-sub{
    font-size:10px !important;
    margin-top:2px !important;
  }

  /* Alt başlığı sadeleştir */
  .board-head{
    margin:4px 0 0 0 !important;
    padding:0 !important;
    gap:8px !important;
  }

  .board-title{
    gap:0 !important;
  }

  .board-title .board-kicker,
  .board-title > small{
    display:none !important;
  }

  .board-title h2{
    margin:4px 0 8px 0 !important;
    font-size:clamp(31px, 8.4vw, 39px) !important;
    line-height:1.02 !important;
    letter-spacing:-1.2px !important;
  }

  /* Seçili durak kapsülü daha ince */
  .selected-stop-chip{
    min-height:40px !important;
    height:40px !important;
    margin:0 0 10px 0 !important;
    padding:0 14px !important;
    border-radius:17px !important;

    display:flex !important;
    align-items:center !important;
    gap:8px !important;

    font-size:15px !important;
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

  /* Eski sesli komut satırı yerine sürüş modu satırı kalsın */
  .voice-row{
    display:none !important;
  }

  .board-head-right{
    margin-top:0 !important;
    gap:8px !important;
  }

  #driveVoiceRow,
  .drive-voice-row{
    display:grid !important;
    grid-template-columns:minmax(0, 1fr) 108px !important;
    gap:8px !important;
    margin:0 0 10px 0 !important;
    align-items:stretch !important;
  }

  #btnDeckAIDrive,
  .drive-voice-btn{
    height:56px !important;
    min-height:56px !important;
    border-radius:20px !important;
    padding:0 16px !important;
    font-size:19px !important;
    justify-content:flex-start !important;
  }

  .drive-voice-seat{
    height:56px !important;
    min-height:56px !important;
    border-radius:20px !important;
    padding:8px 10px !important;
  }

  .drive-voice-seat-values{
    font-size:22px !important;
    line-height:1 !important;
  }

  /* Alttaki renk açıklama barı yer kaplamasın */
  .legend{
    display:none !important;
  }

  /* Durak Akışı kartı daha yukarı ve daha az şişkin */
  .route-strip-shell{
    margin-top:0 !important;
    padding:12px 10px !important;
    border-radius:22px !important;
  }

  .route-strip-title{
    margin:0 0 8px 0 !important;
    font-size:21px !important;
    line-height:1.1 !important;
  }

  .route-live-row{
    gap:8px !important;
    margin:0 0 8px 0 !important;
  }

  .route-live-row .mini-chip,
  .route-live-row > *,
  #routeLiveChip,
  #routeNextChip{
    min-height:44px !important;
    height:44px !important;
    border-radius:16px !important;
    padding:0 10px !important;
    font-size:15px !important;
    overflow:hidden !important;
  }

  .route-strip{
    gap:8px !important;
    padding-bottom:4px !important;
  }

  .route-stop,
  .route-stop-card,
  .stop-card{
    min-height:104px !important;
    border-radius:18px !important;
    padding:12px !important;
  }

  .route-stop h4,
  .route-stop-card h4,
  .stop-card h4,
  .route-stop .stop-name,
  .route-stop-card .stop-name{
    font-size:17px !important;
    line-height:1.1 !important;
  }

  .route-stop small,
  .route-stop-card small,
  .stop-card small,
  .route-stop .stop-meta,
  .route-stop-card .stop-meta{
    font-size:12px !important;
    line-height:1.2 !important;
  }
}

@media (max-width: 380px){
  #driveVoiceRow,
  .drive-voice-row{
    grid-template-columns:minmax(0, 1fr) 96px !important;
  }

  #btnDeckAIDrive,
  .drive-voice-btn{
    height:52px !important;
    min-height:52px !important;
    font-size:18px !important;
  }

  .drive-voice-seat{
    height:52px !important;
    min-height:52px !important;
  }

  .board-title h2{
    font-size:30px !important;
  }

  .route-live-row .mini-chip,
  .route-live-row > *,
  #routeLiveChip,
  #routeNextChip{
    font-size:14px !important;
  }
}
'''

print("===== IOS LOWER BOARD COMPACT V31 =====")

for css_path in [WEB_CSS, AND_CSS]:
    css_path.parent.mkdir(parents=True, exist_ok=True)

    if css_path.exists():
        backup = css_path.with_name(css_path.name + f".bak-v31-{STAMP}")
        shutil.copy2(css_path, backup)
        print("🧾 Eski CSS yedeklendi:", backup.relative_to(ROOT))

    css_path.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", css_path.relative_to(ROOT))

link = '<link rel="stylesheet" href="/static/seats/patches/ios-lower-board-compact-v31.css?v=1">\n'

for tpl in TEMPLATES:
    if not tpl.exists():
        print("⚠️ Template yok:", tpl.relative_to(ROOT))
        continue

    s = tpl.read_text(encoding="utf-8", errors="ignore")

    backup = tpl.with_name(tpl.name + f".bak-ios-lower-board-compact-v31-{STAMP}")
    shutil.copy2(tpl, backup)

    # Eski V31 linklerini temizle
    s = re.sub(
        r'^\s*<link\s+rel="stylesheet"\s+href="/static/seats/patches/ios-lower-board-compact-v31\.css[^"]*">\s*\n?',
        '',
        s,
        flags=re.M
    )

    # CSS linklerinin en sonuna, seats-shell başlamadan önce ekle
    marker = '<div class="seats-shell">'
    if marker in s:
        s = s.replace(marker, link + marker, 1)
    else:
        s = link + s

    tpl.write_text(s, encoding="utf-8")
    print("✅ Link eklendi:", tpl.relative_to(ROOT))
    print("   Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in [WEB_CSS, AND_CSS]:
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    print(p.relative_to(ROOT), "IOS_LOWER_BOARD_COMPACT_V31:", txt.count("IOS_LOWER_BOARD_COMPACT_V31"))

for tpl in TEMPLATES:
    if tpl.exists():
        txt = tpl.read_text(encoding="utf-8", errors="ignore")
        print(tpl.relative_to(ROOT), "ios-lower-board-compact-v31:", txt.count("ios-lower-board-compact-v31.css"))

print()
print("✅ V31 tamamlandı. Chrome’da sayfayı yenile; olmazsa /seats?v=31 aç.")
