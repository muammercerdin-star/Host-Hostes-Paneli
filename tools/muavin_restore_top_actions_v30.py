from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== RESTORE TOP ACTIONS V30 =====")

CSS_NAME = "restore-top-actions-v30.css"
LINK = f'<link rel="stylesheet" href="/static/seats/patches/{CSS_NAME}?v=1">'

CSS_TEXT = r'''
/* =========================================================
   RESTORE_TOP_ACTIONS_V30
   Amaç:
   - V26/V27 kompakt yamalarının gizlediği üst ikonları geri getirir.
   - Ana Sayfa / Hesap / Emanet / AI Console ikonları görünür olur.
   - Sadece topbar action alanına dokunur.
========================================================= */

.topbar .top-actions,
.seats-shell > .topbar .top-actions,
body.drive-mode .topbar .top-actions{
  display:flex !important;
  visibility:visible !important;
  opacity:1 !important;

  height:auto !important;
  min-height:42px !important;
  max-height:none !important;

  overflow:visible !important;
  pointer-events:auto !important;

  align-items:center !important;
  justify-content:center !important;
  gap:10px !important;

  margin-top:10px !important;
  padding:0 !important;
}

.topbar .top-actions > *,
.topbar .top-actions .icon-btn,
.seats-shell > .topbar .top-actions > *,
body.drive-mode .topbar .top-actions > *{
  display:flex !important;
  visibility:visible !important;
  opacity:1 !important;
  pointer-events:auto !important;
}

.topbar .top-actions .icon-btn{
  width:44px !important;
  height:44px !important;
  min-width:44px !important;
  min-height:44px !important;

  border-radius:17px !important;
  align-items:center !important;
  justify-content:center !important;

  font-size:21px !important;
  text-decoration:none !important;

  background:rgba(255,255,255,.075) !important;
  border:1px solid rgba(148,163,184,.20) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.10),
    0 10px 22px rgba(0,0,0,.22) !important;
}

.topbar .top-actions .icon-btn:active{
  transform:scale(.94) !important;
}

@media(max-width:430px){
  .topbar .top-actions,
  .seats-shell > .topbar .top-actions,
  body.drive-mode .topbar .top-actions{
    gap:8px !important;
    min-height:40px !important;
    margin-top:8px !important;
  }

  .topbar .top-actions .icon-btn{
    width:40px !important;
    height:40px !important;
    min-width:40px !important;
    min-height:40px !important;
    border-radius:15px !important;
    font-size:20px !important;
  }
}
'''

CSS_TARGETS = [
    ROOT / "static/seats/patches" / CSS_NAME,
    ROOT / "android_app/app/src/main/python/static/seats/patches" / CSS_NAME,
]

HTML_TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

TOPBAR_TARGETS = [
    ROOT / "templates/seats_parts/topbar.html",
    ROOT / "android_app/app/src/main/python/templates/seats_parts/topbar.html",
]

def backup(p):
    b = p.with_name(p.name + f".bak-v30-{STAMP}")
    shutil.copy2(p, b)
    return b

# 1) CSS yaz
for p in CSS_TARGETS:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        backup(p)
    p.write_text(CSS_TEXT, encoding="utf-8")
    print("✅ CSS yazıldı:", p.relative_to(ROOT))

# 2) CSS linkini en sona, V27'den sonra ekle
for p in HTML_TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if CSS_NAME in s:
        print("ℹ️ Link zaten var:", p.relative_to(ROOT))
        continue

    old = s
    marker = 'ios-trip-summary-ultra-compact-v27.css'
    lines = s.splitlines()

    insert_at = None
    for i, line in enumerate(lines):
        if marker in line:
            insert_at = i + 1

    if insert_at is None:
        for i, line in enumerate(lines):
            if '<div class="seats-shell">' in line:
                insert_at = i
                break

    if insert_at is None:
        print("❌ Link eklenecek yer bulunamadı:", p.relative_to(ROOT))
        continue

    lines.insert(insert_at, LINK)
    s = "\n".join(lines) + "\n"

    if s != old:
        b = backup(p)
        p.write_text(s, encoding="utf-8")
        print("✅ Link eklendi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))

# 3) Topbar AI Console yanlış logout ise düzelt
for p in TOPBAR_TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'<a\s+href="\{\{\s*url_for\([\'"]logout[\'"]\)\s*\}\}"\s+class="icon-btn"\s+title="AI Console">🧠</a>',
        '<a href="/ai-console" class="icon-btn" title="AI Console">🧠</a>',
        s
    )

    if s != old:
        b = backup(p)
        p.write_text(s, encoding="utf-8")
        print("✅ AI Console logout bağlantısı düzeltildi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
    else:
        print("ℹ️ AI Console logout bağlantısı bulunmadı veya zaten doğru:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in HTML_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), CSS_NAME, txt.count(CSS_NAME))

for p in TOPBAR_TARGETS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "logout AI:", txt.count('title=\"AI Console\"') and txt.count("url_for('logout')"))

print()
print("✅ V30 tamamlandı. Chrome’da sayfayı yenile. Gerekirse /seats?v=30 aç.")
