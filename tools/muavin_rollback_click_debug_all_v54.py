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

print("===== V52 / V53 CLICK DEBUG TAM GERİ ALMA V54 =====")

for p in FILES:
    if not p.exists():
        print("YOK:", p.relative_to(ROOT))
        continue

    old = p.read_text(encoding="utf-8", errors="ignore")
    new = old

    for pat in PATTERNS:
        new = re.sub(pat, "", new, flags=re.S)

    # Çoklu boşlukları biraz toparla
    new = re.sub(r"\n{4,}", "\n\n\n", new)

    if new != old:
        bak = p.with_name(p.name + f".bak-rollback-debug-v54-{STAMP}")
        shutil.copy2(p, bak)
        p.write_text(new, encoding="utf-8")
        print("✅ Temizlendi:", p.relative_to(ROOT))
        print("📦 Yedek:", bak.relative_to(ROOT))
    else:
        print("ℹ️ Debug izi yok:", p.relative_to(ROOT))

# debug logları sil
for name in [
    "muavin_click_debug_v53.log",
    "muavin_click_response_audit_v51.txt",
]:
    f = ROOT / name
    if f.exists():
        f.unlink()
        print("🧹 Silindi:", name)

# ağır teşhis tool dosyalarını da kaldır
for name in [
    "tools/muavin_click_runtime_debug_v52.py",
    "tools/muavin_deep_click_api_probe_v53.py",
]:
    f = ROOT / name
    if f.exists():
        f.unlink()
        print("🧹 Tool silindi:", name)

print()
print("✅ V52/V53 debug tamamen kaldırıldı.")
print("Commit/push yok.")
