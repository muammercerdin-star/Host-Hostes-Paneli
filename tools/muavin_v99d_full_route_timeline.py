from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

APP = ROOT / "app.py"
AND_APP = ROOT / "android_app/app/src/main/python/app.py"

print("===== V99D FULL ROUTE TIMELINE =====")

for p in [APP, AND_APP]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99d-full-route-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

if not APP.exists():
    raise SystemExit("❌ app.py yok")

s = APP.read_text(encoding="utf-8", errors="ignore")
old = s

new_block = '''    # V99D_FULL_ROUTE_TIMELINE_START
    # Güzergah timeline artık kırpılmaz.
    # Bütün duraklar kart olarak görünür:
    # geçmiş = yeşil, canlı = kırmızı, sonraki = sarı, bekleyen = koyu.
    selected_stops = list(stops) if stops else []
    # V99D_FULL_ROUTE_TIMELINE_END'''

# Önce eski V99 passed block varsa komple değiştir
s2 = re.sub(
    r'    # V99_PASSED_STOPS_START.*?    # V99_PASSED_STOPS_END',
    new_block,
    s,
    flags=re.S
)

# Eğer eski block yoksa standart selected_stops satırını değiştir
if s2 == s:
    target = 'selected_stops = stops[show_start:show_start + 4] if stops else []'
    if target in s2:
        s2 = s2.replace(target, new_block.strip(), 1)
    else:
        print("❌ selected_stops hedefi bulunamadı")
        print("Rapor için:")
        print("grep -nE 'selected_stops|V99_PASSED|V99D_FULL' app.py | head -80")
        raise SystemExit(1)

APP.write_text(s2, encoding="utf-8")
print("✅ app.py full route timeline yapıldı")

if AND_APP.parent.exists():
    AND_APP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(APP, AND_APP)
    print("✅ android app.py senkron:", AND_APP)

print()
print("===== PYTHON SYNTAX =====")
r = subprocess.run(["python", "-m", "py_compile", "app.py"], cwd=ROOT)
if r.returncode != 0:
    raise SystemExit("❌ py_compile hata verdi")

print("✅ app.py syntax temiz")

print()
print("===== KONTROL =====")
txt = APP.read_text(encoding="utf-8", errors="ignore")
for key in [
    "V99D_FULL_ROUTE_TIMELINE_START",
    "selected_stops = list(stops) if stops else []",
    "V99_PASSED_STOPS_START",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99D full route timeline tamam")
