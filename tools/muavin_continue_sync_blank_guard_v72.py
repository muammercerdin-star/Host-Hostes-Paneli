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

print("===== CONTINUE SYNC BLANK GUARD V72 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sync-blank-guard-v72-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "SYNC_BLANK_GUARD_V72" in s:
        print("ℹ️ V72 zaten var:", p.relative_to(ROOT))
        continue

    old = '''        if(distEl){
          distEl.textContent = formatGpsKm(s.gps_km);
        }'''

    new = '''        // SYNC_BLANK_GUARD_V72
        // API boş gps_km dönerse ekrandaki doğru mesafeyi "—" ile ezme.
        if(distEl && s.gps_km){
          distEl.textContent = formatGpsKm(s.gps_km);
        }'''

    if old not in s:
        print("❌ Mesafe sync bloğu bulunamadı:", p.relative_to(ROOT))
        continue

    s = s.replace(old, new, 1)
    p.write_text(s, encoding="utf-8")
    print("✅ Boş gps_km koruması eklendi:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sync-blank-guard-v72-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=sync-blank-guard-v72",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=sync-blank-guard-v72',
        s
    )
    p.write_text(s, encoding="utf-8")
    print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V72 tamam. Boş API mesafesi artık doğru mesafeyi ezmeyecek.")
