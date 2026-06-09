from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

HOOK = r'''
        // CONTINUE_STALE_LIVE_CLEAR_V60C_HOOK
        // Eski canlı durak 6 km'den fazla uzaktaysa bu ekran onu seçmez, sadece temizler.
        if(Number.isFinite(liveKm) && liveKm > 6){
          clearStaleLiveRuntimeV60B(liveName, gpsKm);
          return;
        }
'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-stale-live-clear-v60c-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== CONTINUE STALE LIVE CLEAR V60C HOOK =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "clearStaleLiveRuntimeV60B" not in s:
        print("❌ V60B fonksiyonu yok, önce V60B lazım:", p.relative_to(ROOT))
        continue

    if "CONTINUE_STALE_LIVE_CLEAR_V60C_HOOK" in s:
        print("ℹ️ V60C hook zaten var:", p.relative_to(ROOT))
        continue

    # liveKm hesaplanıp gpsKm formatlandıktan hemen sonra hook ekle
    pattern = re.compile(
        r'(const\s+liveKm\s*=\s*distKm\s*\(\s*lastPos\s*,\s*liveCoord\s*\)\s*;\s*\n\s*gpsKm\s*=\s*formatKm\s*\(\s*liveKm\s*\)\s*;)',
        re.M
    )

    m = pattern.search(s)
    if not m:
        print("❌ liveKm/gpsKm bloğu bulunamadı:", p.relative_to(ROOT))
        continue

    s = s[:m.end()] + "\n" + HOOK.rstrip() + s[m.end():]

    p.write_text(s, encoding="utf-8")
    print("✅ V60C hook eklendi:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=stale-clear-v60c",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=stale-clear-v60c',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V60C tamam.")
