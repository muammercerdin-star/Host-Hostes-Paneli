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

OPEN_OLD = '''    function openSheet(){
      backdrop.classList.add("show");
      sheet.classList.add("show");
      sheet.setAttribute("aria-hidden", "false");
    }'''

OPEN_NEW = '''    function openSheet(){
      // ROUTE_PICKER_UNLOCK_FIX_V14
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

CLOSE_OLD = '''    function closeSheet(){
      sheet.classList.remove("show");
      backdrop.classList.remove("show");
      sheet.setAttribute("aria-hidden", "true");
    }'''

CLOSE_NEW = '''    function closeSheet(){
      // ROUTE_PICKER_UNLOCK_FIX_V14
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

ROUTE_BLOCK_RE = re.compile(
    r'''    /\* Aktif sefer varken rota listesini de açtırma \*/\n'''
    r'''    if\(routeBtn\)\{\n'''
    r'''      routeBtn\.addEventListener\("click", function\(e\)\{\n'''
    r'''        e\.preventDefault\(\);\n'''
    r'''        e\.stopPropagation\(\);\n'''
    r'''        e\.stopImmediatePropagation\(\);\n'''
    r'''        showGuard\(\);\n'''
    r'''        return false;\n'''
    r'''      \}, true\);\n'''
    r'''    \}\n''',
    re.M
)

ACTIVE_FINAL_RE = re.compile(
    r'''\n<!-- ACTIVE_ROUTE_LOCK_FINAL_START -->.*?<!-- ACTIVE_ROUTE_LOCK_FINAL_END -->\n?''',
    re.S
)

def backup(p: Path):
    b = p.with_name(p.name + f".bak-route-picker-v14-{STAMP}")
    shutil.copy2(p, b)
    return b

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p)
        continue

    b = backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if OPEN_OLD in s:
        s = s.replace(OPEN_OLD, OPEN_NEW, 1)
    elif "ROUTE_PICKER_UNLOCK_FIX_V14" not in s:
        print("⚠️ openSheet kalıbı bulunamadı:", p)

    if CLOSE_OLD in s:
        s = s.replace(CLOSE_OLD, CLOSE_NEW, 1)
    elif "ROUTE_PICKER_UNLOCK_FIX_V14" not in s:
        print("⚠️ closeSheet kalıbı bulunamadı:", p)

    s = ROUTE_BLOCK_RE.sub(
        '''    /* ROUTE_PICKER_UNLOCK_FIX_V14
       Aktif sefer varken sadece Sefer Başlat kilitli kalır.
       Hat seçme butonu kilitlenmez; route sheet açılabilir.
    */
''',
        s
    )

    # WEB tarafındaki ikinci/tekrarlı final kilit bloğunu kaldır.
    if "ACTIVE_ROUTE_LOCK_FINAL_START" in s:
        s = ACTIVE_FINAL_RE.sub(
            "\n<!-- ACTIVE_ROUTE_LOCK_FINAL_REMOVED_BY_ROUTE_PICKER_UNLOCK_FIX_V14 -->\n",
            s
        )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Düzeltildi:", p.relative_to(ROOT))
        print("   Yedek:", b.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik yapılmadı:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print(p.relative_to(ROOT))
    print("  ROUTE_PICKER_UNLOCK_FIX_V14:", txt.count("ROUTE_PICKER_UNLOCK_FIX_V14"))
    print("  ACTIVE_ROUTE_LOCK_FINAL_START:", txt.count("ACTIVE_ROUTE_LOCK_FINAL_START"))
    print("  routeBtn prevent block:", txt.count("Aktif sefer varken rota listesini de açtırma"))
