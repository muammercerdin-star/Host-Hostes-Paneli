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

OPEN_RE = re.compile(
    r'''function\s+openSheet\s*\(\)\s*\{\s*
\s*backdrop\.classList\.add\("show"\);\s*
\s*sheet\.classList\.add\("show"\);\s*
\s*sheet\.setAttribute\("aria-hidden",\s*"false"\);\s*
\s*\}''',
    re.M
)

CLOSE_RE = re.compile(
    r'''function\s+closeSheet\s*\(\)\s*\{\s*
\s*sheet\.classList\.remove\("show"\);\s*
\s*backdrop\.classList\.remove\("show"\);\s*
\s*sheet\.setAttribute\("aria-hidden",\s*"true"\);\s*
\s*\}''',
    re.M
)

OPEN_NEW = '''function openSheet(){
      // ROUTE_PICKER_UNLOCK_FIX_V14B
      if(backdrop){
        backdrop.hidden = false;
        backdrop.removeAttribute("hidden");
        backdrop.classList.add("show");
        backdrop.setAttribute("aria-hidden", "false");
      }

      if(sheet){
        sheet.hidden = false;
        sheet.removeAttribute("hidden");
        sheet.classList.add("show");
        sheet.setAttribute("aria-hidden", "false");
      }
    }'''

CLOSE_NEW = '''function closeSheet(){
      // ROUTE_PICKER_UNLOCK_FIX_V14B
      if(sheet){
        sheet.classList.remove("show");
        sheet.hidden = true;
        sheet.setAttribute("aria-hidden", "true");
      }

      if(backdrop){
        backdrop.classList.remove("show");
        backdrop.hidden = true;
        backdrop.setAttribute("aria-hidden", "true");
      }
    }'''

ROUTE_LOCK_RE = re.compile(
    r'''\n\s*/\*\s*Aktif sefer varken rota listesini de açtırma\s*\*/\s*
\s*if\s*\(\s*routeBtn\s*\)\s*\{\s*
\s*routeBtn\.addEventListener\("click",\s*function\(e\)\s*\{\s*
\s*e\.preventDefault\(\);\s*
\s*e\.stopPropagation\(\);\s*
\s*e\.stopImmediatePropagation\(\);\s*
\s*showGuard\(\);\s*
\s*return\s+false;\s*
\s*\},\s*true\);\s*
\s*\}\s*''',
    re.M
)

ACTIVE_FINAL_RE = re.compile(
    r'''\n<!-- ACTIVE_ROUTE_LOCK_FINAL_START -->.*?<!-- ACTIVE_ROUTE_LOCK_FINAL_END -->\n?''',
    re.S
)

def backup(p: Path):
    b = p.with_name(p.name + f".bak-route-picker-v14b-{STAMP}")
    shutil.copy2(p, b)
    return b

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p)
        continue

    b = backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s, open_count = OPEN_RE.subn(OPEN_NEW, s, count=1)
    s, close_count = CLOSE_RE.subn(CLOSE_NEW, s, count=1)

    s, route_lock_count = ROUTE_LOCK_RE.subn(
        '''
    /* ROUTE_PICKER_UNLOCK_FIX_V14B
       Aktif sefer varken sadece Sefer Başlat kartı kilitli kalır.
       Hat seçme butonu artık engellenmez.
    */
''',
        s
    )

    s, final_count = ACTIVE_FINAL_RE.subn(
        "\n<!-- ACTIVE_ROUTE_LOCK_FINAL_REMOVED_BY_ROUTE_PICKER_UNLOCK_FIX_V14B -->\n",
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Düzeltildi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
        print("   openSheet:", open_count)
        print("   closeSheet:", close_count)
        print("   routeBtn kilit bloğu kaldırıldı:", route_lock_count)
        print("   active final kaldırıldı:", final_count)
    else:
        print("ℹ️ Değişiklik yapılmadı:", p.relative_to(ROOT))

print()
print("===== SON KONTROL =====")
for p in TARGETS:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT))
    print("  V14B marker:", txt.count("ROUTE_PICKER_UNLOCK_FIX_V14B"))
    print("  Aktif sefer rota kilit yorumu:", txt.count("Aktif sefer varken rota listesini de açtırma"))
    print("  ACTIVE_ROUTE_LOCK_FINAL_START:", txt.count("ACTIVE_ROUTE_LOCK_FINAL_START"))
    print("  hitRoute:", txt.count("hitRoute"))
