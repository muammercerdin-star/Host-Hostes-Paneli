from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_TARGETS = [
    ROOT / "static/seats/patches/ios-board-compact-v28.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-board-compact-v28.css",
]

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS = r'''/* =========================================================
   IOS_BOARD_COMPACT_V28
   Koltuk Planı kartındaki kalabalığı azaltır.
   Sadece tasarım yamasıdır. JS / kayıt / sefer mantığına dokunmaz.
========================================================= */

@media(max-width:700px){

  /* Ana koltuk kartını sıkılaştır */
  .board-card,
  .board-card.glass{
    margin:8px 8px 8px !important;
    border-radius:24px !important;
  }

  .board-inner{
    padding:12px 12px 14px !important;
  }

  /* Sade mod / sessiz üst satırı daha küçük */
  #seatSimpleModeToggle{
    height:42px !important;
    min-height:42px !important;
    border-radius:17px !important;
    padding:0 12px !important;
    font-size:14px !important;
    font-weight:950 !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
  }

  #ttsToggle{
    height:42px !important;
    min-height:42px !important;
    border-radius:17px !important;
    padding:0 12px !important;
    font-size:14px !important;
    font-weight:950 !important;
    white-space:nowrap !important;
  }

  /* Sürüş + rötar satırı daha kompakt */
  #driveInlineDock{
    margin:7px 0 8px !important;
    gap:8px !important;
    min-height:40px !important;
  }

  #driveModeToggle{
    height:40px !important;
    min-height:40px !important;
    border-radius:16px !important;
    font-size:14px !important;
    padding:0 10px !important;
  }

  #driveEtaChip,
  .drive-eta-chip{
    height:40px !important;
    min-height:40px !important;
    border-radius:16px !important;
    padding:5px 9px !important;
  }

  #driveEtaChip .drive-eta-top,
  .drive-eta-chip .drive-eta-top{
    font-size:13px !important;
    line-height:1 !important;
  }

  #driveEtaChip .drive-eta-sub,
  .drive-eta-chip .drive-eta-sub{
    font-size:10px !important;
    margin-top:2px !important;
  }

  /* Hız zaten üst sefer kartında var; orta kartta tekrar kalabalık yapmasın */
  #driveInlineDock #driveSpeedChip{
    display:none !important;
  }

  /* Koltuk Planı başlığı küçülsün */
  .board-title .board-kicker,
  .board-title small{
    display:none !important;
  }

  .board-title h2{
    font-size:32px !important;
    line-height:1.05 !important;
    margin:4px 0 10px !important;
    letter-spacing:-.8px !important;
  }

  .board-head{
    gap:8px !important;
    margin:0 !important;
  }

  .board-head-right{
    gap:8px !important;
  }

  /* Seçili durak rozeti daha ince */
  .selected-stop-chip{
    height:42px !important;
    min-height:42px !important;
    border-radius:17px !important;
    padding:0 14px !important;
    font-size:14px !important;
    margin:0 0 9px !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
  }

  .selected-stop-chip b{
    font-size:14px !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
  }

  /* Sesli komut satırını koru ama kısalt */
  #driveVoiceRow,
  .drive-voice-row{
    display:grid !important;
    grid-template-columns:1.75fr .95fr !important;
    gap:9px !important;
    margin:0 0 10px !important;
  }

  #btnDeckAIDrive,
  .drive-voice-btn,
  #btnDeckAI,
  .voice-command-btn{
    height:54px !important;
    min-height:54px !important;
    border-radius:20px !important;
    font-size:20px !important;
    padding:0 14px !important;
  }

  #driveVoiceSeatCard,
  .drive-voice-seat{
    height:54px !important;
    min-height:54px !important;
    border-radius:20px !important;
    padding:0 12px !important;
  }

  .drive-voice-seat-values b{
    font-size:24px !important;
  }

  /* Alt legend zaten sayfanın altında var; burada tekrar görünmesin */
  .board-head-right > .legend{
    display:none !important;
  }

  /* Durak akışı kartı biraz yukarı ve kompakt */
  .route-strip-shell,
  .route-flow-shell{
    margin-top:8px !important;
    padding:12px 12px 14px !important;
    border-radius:22px !important;
  }

  .route-strip-title{
    font-size:22px !important;
    line-height:1.05 !important;
    margin-bottom:10px !important;
  }

  .route-live-row{
    gap:8px !important;
    margin-bottom:10px !important;
  }

  .route-live-row .mini-chip{
    height:44px !important;
    min-height:44px !important;
    border-radius:16px !important;
    padding:0 10px !important;
    font-size:13px !important;
    overflow:hidden !important;
    white-space:nowrap !important;
  }

  .route-live-row .mini-chip b{
    max-width:92px !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    white-space:nowrap !important;
  }

  /* Çok dar ekranda daha sıkı */
  @media(max-width:380px){
    .board-inner{
      padding:10px 10px 12px !important;
    }

    .board-title h2{
      font-size:29px !important;
    }

    #btnDeckAIDrive,
    .drive-voice-btn,
    #btnDeckAI,
    .voice-command-btn,
    #driveVoiceSeatCard,
    .drive-voice-seat{
      height:50px !important;
      min-height:50px !important;
      border-radius:18px !important;
    }

    .selected-stop-chip{
      height:39px !important;
      min-height:39px !important;
      font-size:13px !important;
    }

    .route-strip-title{
      font-size:20px !important;
    }
  }
}
'''

print("===== IOS BOARD COMPACT V28 =====")

for p in CSS_TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)

    if p.exists():
        backup = p.with_name(p.name + f".bak-ios-board-compact-v28-{STAMP}")
        shutil.copy2(p, backup)
        print("ℹ️ Eski CSS yedeklendi:", backup.relative_to(ROOT))

    p.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-board-compact-v28.css?v=1">'

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ios-board-compact-v28.css" in s:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-ios-board-compact-v28-{STAMP}")
    shutil.copy2(p, backup)

    lines = s.splitlines()
    insert_at = None

    for i, line in enumerate(lines):
        if '<link rel="stylesheet"' in line and '/static/seats/patches/' in line:
            insert_at = i + 1

    if insert_at is None:
        print("⚠️ Link eklenecek yer bulunamadı:", p.relative_to(ROOT))
        continue

    lines.insert(insert_at, LINK)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("✅ Link eklendi:", p.relative_to(ROOT))
    print("   Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in CSS_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "IOS_BOARD_COMPACT_V28:", txt.count("IOS_BOARD_COMPACT_V28"))

for p in TPL_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "ios-board-compact-v28:", txt.count("ios-board-compact-v28"))

print()
print("✅ V28 tamamlandı. Chrome’da sayfayı yenile; olmazsa adres sonuna ?v=28 ekle.")
