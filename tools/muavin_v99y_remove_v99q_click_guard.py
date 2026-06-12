from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99Y TEK TEMİZLİK: V99Q CLICK GUARD KALDIR =====")

if not WEB_JS.exists():
    raise SystemExit("❌ Web JS yok: " + str(WEB_JS))

for p in [WEB_JS, AND_JS]:
    if p.exists():
        bak = p.with_name(p.name + f".bak-v99y-remove-v99q-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")
old = s

pattern = r"\n?/\* V99Q_ONLY_OCCUPANCY_CLICK_START \*/.*?/\* V99Q_ONLY_OCCUPANCY_CLICK_END \*/\n?"

s2, n = re.subn(pattern, "\n", s, flags=re.S)

if n == 0:
    print("ℹ️ V99Q bloğu zaten yok. Dosya değiştirilmedi.")
else:
    WEB_JS.write_text(s2, encoding="utf-8")
    print("✅ Web JS içinden V99Q bloğu kaldırıldı. Adet:", n)

if AND_JS.parent.exists():
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android JS web'den senkronlandı")

print()
print("===== KONTROL =====")

txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

checks = [
    ("V99M panel duruyor", "V99M_OCCUPANCY_PANEL_START" in txt and "V99M_OCCUPANCY_PANEL_END" in txt),
    ("V99Q kaldırıldı", "V99Q_ONLY_OCCUPANCY_CLICK_START" not in txt and "V99Q_ONLY_OCCUPANCY_CLICK_END" not in txt),
    ("V99O koltuk renk/detay duruyor", "V99O_SEAT_GENDER_SELECTED_JS_START" in txt),
    ("Doluluk hedefinde v99-gauge-cell var", ".v99-gauge-cell" in txt),
    ("Doluluk sadece label ile açılıyor", 'return labelText === "DOLULUK"' in txt),
    ("Panel API duruyor", "MuavinV99OccupancyPanel" in txt),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== NODE JS SYNTAX CHECK =====")
try:
    res = subprocess.run(
        ["node", "--check", str(WEB_JS)],
        capture_output=True,
        text=True
    )
    if res.returncode == 0:
        print("✅ JS syntax OK")
    else:
        print("❌ JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KISA GREP =====")
for i, line in enumerate(txt.splitlines(), 1):
    if any(k in line for k in [
        "V99M_OCCUPANCY_PANEL_START",
        "V99M_OCCUPANCY_PANEL_END",
        "V99Q_ONLY_OCCUPANCY_CLICK",
        "function isDolulukTarget",
        "return labelText",
        ".v99-gauge-cell",
        "MuavinV99OccupancyPanel",
    ]):
        print(f"{i:5}: {line[:240]}")

print()
print("✅ V99Y temizlik bitti.")
print("Tarayıcıda şununla yenile:")
print("http://127.0.0.1:5000/continue-trip?v=v99y-clean")
