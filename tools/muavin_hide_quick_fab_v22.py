from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_REL = "static/seats/patches/hide-quick-fab-v22.css"
ANDROID_CSS_REL = "android_app/app/src/main/python/static/seats/patches/hide-quick-fab-v22.css"

TPLS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

CSS_TARGETS = [
    ROOT / CSS_REL,
    ROOT / ANDROID_CSS_REL,
]

CSS = """/* =========================================================
   HIDE_QUICK_FAB_V22
   Sol alttaki + / ₺ / indir hızlı işlem FAB butonlarını gizler.
   İşlem sekmesindeki normal Hızlı İşlemler ekranına dokunmaz.
========================================================= */

.fab-column,
.fab-column.fab-left-gap-moved,
body.drive-mode .fab-column,
body.drive-mode .fab-column.fab-left-gap-moved,
html.seat-simple-mode .fab-column,
html.seat-simple-mode .fab-column.fab-left-gap-moved{
  display:none !important;
  visibility:hidden !important;
  pointer-events:none !important;
}
"""

LINK = '<link rel="stylesheet" href="/static/seats/patches/hide-quick-fab-v22.css?v=1">'

print("===== HIZLI FAB GİZLEME V22 =====")

for css in CSS_TARGETS:
    css.parent.mkdir(parents=True, exist_ok=True)
    if css.exists():
        b = css.with_name(css.name + f".bak-hide-quick-fab-v22-{STAMP}")
        shutil.copy2(css, b)
        print("Yedek CSS:", b.relative_to(ROOT))
    css.write_text(CSS, encoding="utf-8")
    print("✅ CSS yazıldı:", css.relative_to(ROOT))

for tpl in TPLS:
    if not tpl.exists():
        print("⚠️ Template yok:", tpl.relative_to(ROOT))
        continue

    s = tpl.read_text(encoding="utf-8", errors="ignore")

    if "hide-quick-fab-v22.css" in s:
        print("ℹ️ Link zaten var:", tpl.relative_to(ROOT))
        continue

    backup = tpl.with_name(tpl.name + f".bak-hide-quick-fab-v22-{STAMP}")
    shutil.copy2(tpl, backup)

    marker = '<link rel="stylesheet" href="/static/seats/patches/seat-label-ghost-clean.css?v=1">'
    if marker in s:
        s = s.replace(marker, marker + "\n" + LINK, 1)
    else:
        s = s.replace('<div class="seats-shell">', LINK + '\n<div class="seats-shell">', 1)

    tpl.write_text(s, encoding="utf-8")
    print("✅ Link eklendi:", tpl.relative_to(ROOT))
    print("   Yedek:", backup.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in CSS_TARGETS + TPLS:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        print(p.relative_to(ROOT), "HIDE_QUICK_FAB_V22:", txt.count("HIDE_QUICK_FAB_V22"), "link:", txt.count("hide-quick-fab-v22.css"))

print()
print("✅ V22 tamam.")
