from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_TARGETS = [
    ROOT / "static/seats/patches/ios-trip-summary-compact-v26.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-trip-summary-compact-v26.css",
]

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS = r'''/* =========================================================
   IOS_TRIP_SUMMARY_COMPACT_V26
   Seçenek B: Üst sefer özetini kompakt iOS tarzı yapar.
   Sadece tasarım yamasıdır. JS / kayıt / fonksiyonlara dokunmaz.
========================================================= */

@media(max-width:700px){

  /* ÜST SEFER KARTINI KOMPAKTLAŞTIR */
  .topbar,
  .seats-shell > .topbar,
  body.drive-mode .topbar{
    margin:10px 8px 8px !important;
    padding:12px 12px 12px !important;
    border-radius:26px !important;
    min-height:0 !important;
    overflow:hidden !important;
  }

  /* Başlık satırı: ikon + hat adı */
  .topbar .brand,
  .topbar .brand-row,
  .topbar .topbar-brand,
  .topbar .brand-line{
    display:grid !important;
    grid-template-columns:54px minmax(0,1fr) !important;
    align-items:center !important;
    gap:10px !important;
    margin:0 0 8px 0 !important;
  }

  .topbar .brand-icon,
  .topbar .logo,
  .topbar .app-icon,
  .topbar .route-icon{
    width:52px !important;
    height:52px !important;
    min-width:52px !important;
    min-height:52px !important;
    border-radius:18px !important;
  }

  .topbar h1,
  .topbar .brand-title,
  .topbar .route-title,
  .topbar .top-title{
    font-size:28px !important;
    line-height:1.05 !important;
    margin:0 !important;
    padding:0 !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    letter-spacing:-.5px !important;
  }

  .topbar .brand-sub,
  .topbar .route-sub,
  .topbar .trip-meta,
  .topbar small{
    font-size:13px !important;
    line-height:1.25 !important;
    margin-top:4px !important;
    white-space:normal !important;
    opacity:.86 !important;
  }

  /* 4 büyük bilgi kutusunu kompakt chip haline getir */
  .topbar .mini-grid,
  .topbar .top-mini,
  .topbar .mini-stats,
  .topbar .top-stats,
  .topbar .chips,
  .topbar .stats{
    display:grid !important;
    grid-template-columns:1fr 1fr !important;
    gap:8px !important;
    margin-top:10px !important;
  }

  .topbar .mini-chip{
    min-height:48px !important;
    height:auto !important;
    padding:9px 10px !important;
    border-radius:18px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    gap:7px !important;

    background:rgba(255,255,255,.065) !important;
    border:1px solid rgba(148,163,184,.14) !important;
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.07),
      0 8px 18px rgba(0,0,0,.16) !important;

    font-size:13px !important;
    line-height:1.1 !important;
    overflow:hidden !important;
  }

  .topbar .mini-chip span{
    font-size:12px !important;
    opacity:.72 !important;
    font-weight:850 !important;
    white-space:nowrap !important;
  }

  .topbar .mini-chip b{
    font-size:14px !important;
    font-weight:1000 !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    max-width:100% !important;
  }

  /* Alt ikon satırı: daha küçük ve daha sakin */
  .topbar .quick-actions,
  .topbar .top-actions,
  .topbar .actions,
  .topbar .nav-actions,
  .topbar .menu-actions{
    display:flex !important;
    align-items:center !important;
    gap:8px !important;
    margin-top:10px !important;
    padding:0 !important;
    flex-wrap:nowrap !important;
    overflow:hidden !important;
  }

  .topbar .quick-actions > *,
  .topbar .top-actions > *,
  .topbar .actions > *,
  .topbar .nav-actions > *,
  .topbar .menu-actions > *{
    width:44px !important;
    height:44px !important;
    min-width:44px !important;
    min-height:44px !important;
    border-radius:17px !important;
    font-size:20px !important;
    padding:0 !important;
  }

  /* Çok küçük ekranda daha da sıkılaştır */
  @media(max-width:380px){
    .topbar,
    .seats-shell > .topbar,
    body.drive-mode .topbar{
      margin:8px 6px 8px !important;
      padding:10px !important;
      border-radius:24px !important;
    }

    .topbar h1,
    .topbar .brand-title,
    .topbar .route-title,
    .topbar .top-title{
      font-size:25px !important;
    }

    .topbar .mini-chip{
      min-height:44px !important;
      padding:8px 9px !important;
      border-radius:16px !important;
    }

    .topbar .quick-actions > *,
    .topbar .top-actions > *,
    .topbar .actions > *,
    .topbar .nav-actions > *,
    .topbar .menu-actions > *{
      width:40px !important;
      height:40px !important;
      min-width:40px !important;
      min-height:40px !important;
      border-radius:15px !important;
      font-size:18px !important;
    }
  }
}

/* Koltuk kartı üst boşluğunu biraz azalt */
@media(max-width:700px){
  .layout{
    gap:8px !important;
  }

  .board-card{
    margin-top:0 !important;
  }
}
'''

print("===== IOS TRIP SUMMARY COMPACT V26 =====")

for p in CSS_TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        backup = p.with_name(p.name + f".bak-ios-trip-summary-v26-{STAMP}")
        shutil.copy2(p, backup)
        print("ℹ️ Eski CSS yedeklendi:", backup.relative_to(ROOT))

    p.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-trip-summary-compact-v26.css?v=1">'

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ios-trip-summary-compact-v26.css" in s:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-ios-trip-summary-v26-{STAMP}")
    shutil.copy2(p, backup)

    # Son patch CSS linkinden sonra ekle
    lines = s.splitlines()
    insert_at = None
    for i, line in enumerate(lines):
        if '<link rel="stylesheet"' in line and '/static/seats/patches/' in line:
            insert_at = i + 1

    if insert_at is None:
        for i, line in enumerate(lines):
            if '<link rel="stylesheet"' in line:
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
        print(p.relative_to(ROOT), "IOS_TRIP_SUMMARY_COMPACT_V26:", txt.count("IOS_TRIP_SUMMARY_COMPACT_V26"))

for p in TPL_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "ios-trip-summary-compact-v26:", txt.count("ios-trip-summary-compact-v26"))

print()
print("✅ V26 tamamlandı. Chrome’da sayfayı yenile. Olmazsa adres sonuna ?v=26 ekle.")
