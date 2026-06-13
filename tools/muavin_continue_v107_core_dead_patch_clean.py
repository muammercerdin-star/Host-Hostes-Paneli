from pathlib import Path
from datetime import datetime
import shutil
import re
import subprocess
import hashlib

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_core.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"

WEB_TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

print("===== V107 CORE ÖLÜ YAMA TEMİZLİĞİ =====")
print("ROOT:", ROOT)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def line_count_text(s):
    return len(s.splitlines())

def backup(p):
    if p.exists():
        bak = p.with_name(p.name + f".bak-v107-core-clean-{STAMP}")
        shutil.copy2(p, bak)
        print("📦 backup:", bak)

for p in [WEB_JS, AND_JS, WEB_TPL, AND_TPL]:
    backup(p)

if not WEB_JS.exists():
    raise SystemExit("❌ continue_trip_core.js yok")

s = WEB_JS.read_text(encoding="utf-8", errors="ignore")
old = s
before_lines = line_count_text(s)

changes = []

# 1) Kullanılmayan parseKmAny fonksiyonunu kaldır
s2, n = re.subn(
    r'\n\s*function\s+parseKmAny\s*\(\s*value\s*\)\s*\{.*?\n\s*\}\s*\n(?=\s*function\s+formatGpsKm\s*\()',
    "\n",
    s,
    count=1,
    flags=re.S
)
if n:
    changes.append(f"parseKmAny kaldırıldı ({n})")
s = s2

# 2) updateStatus içindeki eski/ölü selector satırlarını kaldır
s2, n1 = re.subn(
    r'\n\s*const\s+statusPill\s*=\s*q\("#liveCurrentCard \.status-pill\.live"\);\s*',
    "\n",
    s,
    count=1
)
s = s2

s2, n2 = re.subn(
    r'\n\s*if\s*\(\s*statusPill\s*\)\s*statusPill\.textContent\s*=\s*etaMain;\s*',
    "\n",
    s,
    count=1
)
s = s2

if n1 or n2:
    changes.append(f"eski statusPill selector temizlendi ({n1+n2})")

# 3) MIDPOINT_LIVE_STOP_V67 ana ölü bloğunu kaldır
# writeRuntime fonksiyonunu koruyarak ondan önceki V67 bloğunu çıkarır.
pat_mid_block = r'\n\s*// MIDPOINT_LIVE_STOP_V67[\s\S]*?(?=\n\s*function\s+writeRuntime\s*\()'
s2, n = re.subn(
    pat_mid_block,
    "\n",
    s,
    count=1
)
if n:
    changes.append(f"MIDPOINT_LIVE_STOP_V67 ana blok kaldırıldı ({n})")
s = s2

# 4) compute() içindeki MIDPOINT hook çağrısını kaldır
pat_hook = r'\n\s*// MIDPOINT_LIVE_STOP_V67_HOOK[\s\S]*?\n\s*if\s*\(\s*!liveName\s*\)\s*return;'
s2, n = re.subn(
    pat_hook,
    "\n    if(!liveName) return;",
    s,
    count=1
)
if n:
    changes.append(f"MIDPOINT_LIVE_STOP_V67_HOOK compute içinden kaldırıldı ({n})")
s = s2

WEB_JS.write_text(s, encoding="utf-8")

after_lines = line_count_text(s)

print()
print("===== DEĞİŞİKLİKLER =====")
if changes:
    for c in changes:
        print("✅", c)
else:
    print("⚠️ Temizlenecek hedef bulunamadı. Dosya zaten temiz olabilir.")

print(f"Satır önce: {before_lines}")
print(f"Satır sonra: {after_lines}")
print(f"Azalan satır: {before_lines - after_lines}")

# 5) Android JS senkron
if AND_JS.parent.exists():
    AND_JS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WEB_JS, AND_JS)
    print("✅ Android core JS senkron")

# 6) Template core.js cache versiyonunu v107 yap
if WEB_TPL.exists():
    t = WEB_TPL.read_text(encoding="utf-8", errors="ignore")
    old_t = t

    new_core_tag = """<script src="{{ url_for('static', filename='continue/continue_trip_core.js') }}?v=v107-core-clean-{{ trip['id'] }}"></script>"""

    t, tn = re.subn(
        r'''<script src="\{\{\s*url_for\('static',\s*filename='continue/continue_trip_core\.js'\)\s*\}\}\?v=[^"]*"></script>''',
        new_core_tag,
        t,
        count=1
    )

    WEB_TPL.write_text(t, encoding="utf-8")
    print("✅ template core.js cache güncellendi:", tn)

    if AND_TPL.parent.exists():
        shutil.copy2(WEB_TPL, AND_TPL)
        print("✅ Android template senkron")

print()
print("===== NODE SYNTAX CHECK =====")
try:
    res = subprocess.run(["node", "--check", str(WEB_JS)], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ core JS syntax OK")
    else:
        print("❌ core JS syntax HATA")
        print(res.stdout)
        print(res.stderr)
except FileNotFoundError:
    print("ℹ️ node yok, syntax check atlandı")

print()
print("===== KONTROL =====")
now = WEB_JS.read_text(encoding="utf-8", errors="ignore")
tpl = WEB_TPL.read_text(encoding="utf-8", errors="ignore") if WEB_TPL.exists() else ""

checks = [
    ("parseKmAny temiz", "parseKmAny" not in now),
    ("MIDPOINT_LIVE_STOP_V67 temiz", "MIDPOINT_LIVE_STOP_V67" not in now),
    ("isEmptyLiveNameV67 temiz", "isEmptyLiveNameV67" not in now),
    ("routeCoordItemsV67 temiz", "routeCoordItemsV67" not in now),
    ("pickMidpointLiveStopV67 temiz", "pickMidpointLiveStopV67" not in now),
    ("switchLiveStopMidpointV67 temiz", "switchLiveStopMidpointV67" not in now),
    ("eski status-pill selector temiz", "#liveCurrentCard .status-pill.live" not in now),

    ("formatGpsKm duruyor", "function formatGpsKm" in now),
    ("writeRuntime duruyor", "function writeRuntime" in now),
    ("compute duruyor", "function compute" in now),
    ("GPS watch duruyor", "navigator.geolocation.watchPosition" in now),
    ("runtime write API duruyor", "/api/live-runtime-state?write=1" in now),
    ("live-stop-sheet duruyor", "live-stop-sheet-script" in now),
    ("V45 seat map duruyor", "CONTINUE_SEAT_MAP_FULLSCREEN_V45_START" in now),

    ("template v107 core cache var", "v107-core-clean" in tpl),
    ("Web/Android core aynı", WEB_JS.exists() and AND_JS.exists() and sha(WEB_JS) == sha(AND_JS)),
    ("Web/Android template aynı", WEB_TPL.exists() and AND_TPL.exists() and sha(WEB_TPL) == sha(AND_TPL)),
]

for name, ok in checks:
    print(("✅ " if ok else "❌ ") + name)

print()
print("===== CORE SCRIPT SATIRI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if "continue_trip_core.js" in line:
        print(f"{i}: {line}")

print()
print("===== SHA =====")
print("core web:     ", sha(WEB_JS))
print("core android: ", sha(AND_JS))
print("tpl web:      ", sha(WEB_TPL))
print("tpl android:  ", sha(AND_TPL))

print()
print("✅ V107 core ölü yama temizliği tamam.")
print("Aç:")
print("http://127.0.0.1:5000/continue-trip?v=v107-core-clean")
