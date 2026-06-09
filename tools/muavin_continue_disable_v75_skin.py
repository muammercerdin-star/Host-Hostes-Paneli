from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== DISABLE CONTINUE V75 SKIN =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-disable-v75-skin-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r'\n\s*<link rel="stylesheet" href="{{ url_for\(\'static\', filename=\'continue/continue_industrial_v75\.css\'\) }}\?v=[^"]+">',
        '',
        s
    )

    s = re.sub(
        r'\n\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_ring_v75\.js\'\) }}\?v=[^"]+"></script>',
        '',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ V75 tasarım kabuğu kapatıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ V75 satırı bulunamadı:", p.relative_to(ROOT))

print()
print("✅ V75 kapandı. Dosyalar silinmedi, sadece template çağrısı kaldırıldı.")
