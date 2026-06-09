from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

CSS_FILES = [
    ROOT / "static/continue/continue_v76.css",
    ROOT / "android_app/app/src/main/python/static/continue/continue_v76.css",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

MARKER = "CONTINUE_V76_SHEET_BEAUTY_V79"

def remove_marker_block(s, marker):
    m = re.search(r'\n\s*/\*\s*' + re.escape(marker) + r'\s*\*/', s)
    if not m:
        return s, False

    start = m.start()

    # Bir sonraki CONTINUE_* yamasına kadar sil. Yoksa dosya sonuna kadar sil.
    rest = s[m.end():]
    n = re.search(r'\n\s*/\*\s*CONTINUE_[A-Z0-9_]+\s*\*/', rest)
    end = m.end() + n.start() if n else len(s)

    return s[:start].rstrip() + "\n" + s[end:].lstrip(), True

print("===== ROLLBACK SHEET BEAUTY V79 =====")

for p in CSS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-rollback-v79-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    s2, changed = remove_marker_block(s, MARKER)

    if changed:
        p.write_text(s2, encoding="utf-8")
        print("✅ V79 modal süsleme kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ V79 yaması bulunamadı:", p.relative_to(ROOT))

print()
print("===== CACHE V78'E AL =====")

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-rollback-v79-cache-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue/continue_v76\.css'\) }}\?v=[^\"']+",
        "continue/continue_v76.css') }}?v=prototype-layout-v78",
        s
    )

    p.write_text(s, encoding="utf-8")
    print("✅ Cache V78'e çekildi:", p.relative_to(ROOT))

print()
print("✅ V79 geri alındı. V78 sheet konumlandırma düzeltmesi duruyor.")
