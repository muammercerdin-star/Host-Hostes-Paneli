from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",

    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",

    ROOT / "templates/index.html",
    ROOT / "android_app/app/src/main/python/templates/index.html",

    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

PATTERNS = [
    r"# ===== MUAVIN_DEEP_CLICK_API_PROBE_V53_START =====.*?# ===== MUAVIN_DEEP_CLICK_API_PROBE_V53_END =====\n?",
    r"<!-- MUAVIN_DEEP_CLICK_API_PROBE_V53_START -->.*?<!-- MUAVIN_DEEP_CLICK_API_PROBE_V53_END -->",
    r"<!-- MUAVIN_CLICK_RUNTIME_DEBUG_V52_START -->.*?<!-- MUAVIN_CLICK_RUNTIME_DEBUG_V52_END -->",
]

print("===== CLICK DEBUG V52/V53 GERİ ALMA =====")

for p in FILES:
    if not p.exists():
        print("YOK:", p.relative_to(ROOT))
        continue

    old = p.read_text(encoding="utf-8", errors="ignore")
    new = old

    for pat in PATTERNS:
        new = re.sub(pat, "", new, flags=re.S)

    if new != old:
        bak = p.with_name(p.name + f".bak-rollback-click-debug-{STAMP}")
        shutil.copy2(p, bak)
        p.write_text(new, encoding="utf-8")
        print("✅ Temizlendi:", p.relative_to(ROOT))
        print("📦 Yedek:", bak.relative_to(ROOT))
    else:
        print("ℹ️ Debug izi yok:", p.relative_to(ROOT))

log = ROOT / "muavin_click_debug_v53.log"
if log.exists():
    log.unlink()
    print("🧹 Log silindi:", log.relative_to(ROOT))

print()
print("✅ V52/V53 debug tamamen kaldırıldı.")
