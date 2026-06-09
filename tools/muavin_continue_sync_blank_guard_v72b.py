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

print("===== CONTINUE SYNC BLANK GUARD V72B =====")

patched_any = False

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-sync-blank-guard-v72b-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "SYNC_BLANK_GUARD_V72B" in s:
        print("ℹ️ V72B zaten var:", p.relative_to(ROOT))
        patched_any = True
        continue

    pattern = re.compile(
        r'if\s*\(\s*distEl\s*\)\s*\{\s*'
        r'distEl\.textContent\s*=\s*formatGpsKm\s*\(\s*s\.gps_km\s*\)\s*;\s*'
        r'\}',
        re.S
    )

    repl = '''// SYNC_BLANK_GUARD_V72B
        // API boş gps_km dönerse ekrandaki doğru mesafeyi "—" ile ezme.
        if(distEl && s.gps_km){
          distEl.textContent = formatGpsKm(s.gps_km);
        }'''

    s2, count = pattern.subn(repl, s, count=1)

    if count < 1:
        print("❌ Mesafe sync bloğu yine bulunamadı:", p.relative_to(ROOT))
        continue

    p.write_text(s2, encoding="utf-8")
    patched_any = True
    print("✅ Boş gps_km koruması eklendi:", p.relative_to(ROOT))

if patched_any:
    for p in TPLS:
        if not p.exists():
            print("⚠️ Yok:", p.relative_to(ROOT))
            continue

        b = p.with_name(p.name + f".bak-sync-blank-guard-v72b-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

        s = p.read_text(encoding="utf-8", errors="ignore")

        s = re.sub(
            r"continue_trip_core\.js'\) }}\?v=[^\"']+",
            "continue_trip_core.js') }}?v=sync-blank-guard-v72b",
            s
        )
        s = re.sub(
            r'continue_trip_core\.js"\) }}\?v=[^"\']+',
            'continue_trip_core.js") }}?v=sync-blank-guard-v72b',
            s
        )

        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))
else:
    print("⚠️ JS patch uygulanmadığı için cache güncellemesi yapılmadı.")

print()
print("✅ V72B bitti.")
