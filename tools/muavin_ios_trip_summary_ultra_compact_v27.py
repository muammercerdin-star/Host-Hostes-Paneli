from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_TARGETS = [
    ROOT / "static/seats/patches/ios-trip-summary-ultra-compact-v27.css",
    ROOT / "android_app/app/src/main/python/static/seats/patches/ios-trip-summary-ultra-compact-v27.css",
]

TPL_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS = r'''/* =========================================================
   IOS_TRIP_SUMMARY_ULTRA_COMPACT_V27
   Üst sefer kartını ciddi şekilde küçültür.
   Sadece tasarım yamasıdır. JS / işlem / kayıt mantığına dokunmaz.
========================================================= */

@media(max-width:700px){

  /* Ana üst kart */
  .topbar,
  .seats-shell > .topbar,
  body.drive-mode .topbar{
    margin:8px 8px 8px !important;
    padding:10px 10px 10px !important;
    border-radius:24px !important;
    min-height:0 !important;
    max-height:none !important;
    overflow:hidden !important;
  }

  /* Başlık bloğu */
  .topbar h1,
  .topbar .brand-title,
  .topbar .route-title,
  .topbar .top-title{
    font-size:24px !important;
    line-height:1.04 !important;
    margin:0 !important;
    padding:0 !important;
    max-width:100% !important;
    white-space:nowrap !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    letter-spacing:-.6px !important;
  }

  .topbar small,
  .topbar .trip-meta,
  .topbar .brand-sub,
  .topbar .route-sub{
    font-size:12px !important;
    line-height:1.22 !important;
    margin-top:3px !important;
    opacity:.82 !important;
  }

  /* Üst logo/otobüs ikonu */
  .topbar img,
  .topbar .brand-icon,
  .topbar .logo,
  .topbar .app-icon,
  .topbar .route-icon{
    width:44px !important;
    height:44px !important;
    min-width:44px !important;
    min-height:44px !important;
    border-radius:16px !important;
  }

  /* İçinde mini-chip olan satırı tek satır kompakt grid yap */
  .topbar div:has(> .mini-chip){
    display:grid !important;
    grid-template-columns:repeat(4, minmax(0,1fr)) !important;
    gap:6px !important;
    margin-top:8px !important;
  }

  .topbar .mini-chip{
    min-height:38px !important;
    height:38px !important;
    padding:5px 5px !important;
    border-radius:15px !important;

    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    gap:4px !important;

    background:rgba(255,255,255,.055) !important;
    border:1px solid rgba(148,163,184,.13) !important;
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.06),
      0 6px 14px rgba(0,0,0,.14) !important;

    overflow:hidden !important;
    white-space:nowrap !important;
  }

  /* Durak / Hız / Saat / Doluluk etiketlerini sakla, sadece değer kalsın */
  .topbar .mini-chip span{
    display:none !important;
  }

  .topbar .mini-chip b{
    font-size:12.5px !important;
    font-weight:1000 !important;
    line-height:1 !important;
    max-width:100% !important;
    overflow:hidden !important;
    text-overflow:ellipsis !important;
    white-space:nowrap !important;
  }

  /* Üst kart altındaki ev / hesap / emanet / beyin / bitir ikon satırını gizle */
  .topbar .quick-actions,
  .topbar .top-actions,
  .topbar .actions,
  .topbar .nav-actions,
  .topbar .menu-actions,
  .topbar div:has(> a + a),
  .topbar div:has(> button + button){
    display:none !important;
  }

  /* Kart ile koltuk planı arasındaki boşluğu azalt */
  .layout{
    gap:6px !important;
  }

  .board-card{
    margin-top:0 !important;
  }

  .board-inner{
    padding-top:12px !important;
  }

  /* Çok dar ekranda biraz daha sıkı */
  @media(max-width:380px){
    .topbar,
    .seats-shell > .topbar,
    body.drive-mode .topbar{
      margin:7px 6px 7px !important;
      padding:9px !important;
      border-radius:22px !important;
    }

    .topbar h1,
    .topbar .brand-title,
    .topbar .route-title,
    .topbar .top-title{
      font-size:22px !important;
    }

    .topbar .mini-chip{
      min-height:34px !important;
      height:34px !important;
      border-radius:14px !important;
    }

    .topbar .mini-chip b{
      font-size:11.5px !important;
    }
  }
}
'''

print("===== IOS TRIP SUMMARY ULTRA COMPACT V27 =====")

for p in CSS_TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)

    if p.exists():
        backup = p.with_name(p.name + f".bak-ios-trip-summary-ultra-v27-{STAMP}")
        shutil.copy2(p, backup)
        print("ℹ️ Eski CSS yedeklendi:", backup.relative_to(ROOT))

    p.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-trip-summary-ultra-compact-v27.css?v=1">'

for p in TPL_TARGETS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ios-trip-summary-ultra-compact-v27.css" in s:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))
        continue

    backup = p.with_name(p.name + f".bak-ios-trip-summary-ultra-v27-{STAMP}")
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
        print(p.relative_to(ROOT), "IOS_TRIP_SUMMARY_ULTRA_COMPACT_V27:", txt.count("IOS_TRIP_SUMMARY_ULTRA_COMPACT_V27"))

for p in TPL_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "ios-trip-summary-ultra-compact-v27:", txt.count("ios-trip-summary-ultra-compact-v27"))

print()
print("✅ V27 tamamlandı. Chrome’da yenile. Olmazsa adres sonuna ?v=27 ekle.")
