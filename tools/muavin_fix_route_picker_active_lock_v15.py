from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    ROOT / "templates/index.html",
    ROOT / "android_app/app/src/main/python/templates/index.html",
]

OLD_COMMENT_RE = re.compile(
    r'''\n\s*/\*\s*ROUTE_PICKER_UNLOCK_FIX_V14B\s*
\s*Aktif sefer varken sadece Sefer Başlat kartı kilitli kalır\.\s*
\s*Hat seçme butonu artık engellenmez\.\s*
\s*\*/\s*''',
    re.M
)

NEW_LOCK = '''
    /* ROUTE_PICKER_ACTIVE_TRIP_LOCK_V15
       Aktif sefer varken hat değiştirilemez.
       Aktif sefer yoksa premium route picker normal açılır.
    */
    if(routeBtn){
      routeBtn.setAttribute("aria-disabled", "true");
      routeBtn.setAttribute("title", "Aktif sefer varken hat değiştirilemez");

      routeBtn.addEventListener("click", function(e){
        e.preventDefault();
        e.stopPropagation();
        if(e.stopImmediatePropagation) e.stopImmediatePropagation();
        showGuard();
        return false;
      }, true);
    }
'''

def backup(p: Path):
    b = p.with_name(p.name + f".bak-active-route-lock-v15-{STAMP}")
    shutil.copy2(p, b)
    return b

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p)
        continue

    b = backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "ROUTE_PICKER_ACTIVE_TRIP_LOCK_V15" in s:
        print("ℹ️ V15 zaten var:", p.relative_to(ROOT))
        continue

    s, count = OLD_COMMENT_RE.subn(NEW_LOCK, s, count=1)

    if count == 0:
        print("⚠️ V14B yorum bloğu bulunamadı:", p.relative_to(ROOT))
    elif s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Aktif sefer hat kilidi eklendi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
        print("   değişen blok:", count)

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT))
    print("  V14B open/close marker:", txt.count("ROUTE_PICKER_UNLOCK_FIX_V14B"))
    print("  V15 active lock marker:", txt.count("ROUTE_PICKER_ACTIVE_TRIP_LOCK_V15"))
    print("  eski ACTIVE_ROUTE_LOCK_FINAL:", txt.count("ACTIVE_ROUTE_LOCK_FINAL_START"))
    print("  hitRoute eski blok:", txt.count("hitRoute"))
