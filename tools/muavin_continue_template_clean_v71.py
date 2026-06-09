from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== CONTINUE TEMPLATE CLEAN V71 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-template-clean-v71-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = s.replace(
        'href="{{ url_for("live_map_page") }}"',
        "href=\"{{ url_for('live_map_page') }}\""
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ url_for çift tırnak temizlendi:", p.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik yok:", p.relative_to(ROOT))

print()
print("✅ V71 temizliği bitti.")
