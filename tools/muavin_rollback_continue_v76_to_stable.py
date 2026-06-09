from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

PAIRS = [
    (
        ROOT / "templates/continue_trip.html",
        ROOT / "templates"
    ),
    (
        ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
        ROOT / "android_app/app/src/main/python/templates"
    ),
]

print("===== ROLLBACK CONTINUE V76 TO STABLE =====")

def latest_backup(folder):
    files = sorted(
        folder.glob("continue_trip.html.bak-prototype-v76-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )
    return files[0] if files else None

for target, folder in PAIRS:
    if not target.exists():
        print("⚠️ Hedef yok:", target.relative_to(ROOT))
        continue

    backup = latest_backup(folder)
    if not backup:
        print("❌ V76 öncesi backup bulunamadı:", folder.relative_to(ROOT))
        continue

    safety = target.with_name(target.name + f".bak-before-rollback-v76-{STAMP}")
    shutil.copy2(target, safety)
    print("📦 Mevcut dosya yedeği:", safety.relative_to(ROOT))

    shutil.copy2(backup, target)
    print("✅ V76 öncesi backup geri yüklendi:", backup.relative_to(ROOT), "->", target.relative_to(ROOT))

    s = target.read_text(encoding="utf-8", errors="ignore")

    # V75 kötü görünen tasarım çağrıları restore backup içinde kaldıysa kapat.
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

    # V76 çağrısı kaldıysa kapat.
    s = re.sub(
        r'\n\s*<link rel="stylesheet" href="{{ url_for\(\'static\', filename=\'continue/continue_v76\.css\'\) }}\?v=[^"]+">',
        '',
        s
    )
    s = re.sub(
        r'\n\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_v76\.js\'\) }}\?v=[^"]+"></script>',
        '',
        s
    )

    # Core cache çalışan V72B'de kalsın.
    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=sync-blank-guard-v72b",
        s
    )

    target.write_text(s, encoding="utf-8")
    print("✅ Deneysel V75/V76 çağrıları temizlendi:", target.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]:
    if not p.exists():
        continue
    s = p.read_text(encoding="utf-8", errors="ignore")
    bad = []
    for key in ["continue_v76", "continue_industrial_v75", "continue_ring_v75", "prototype-layout-v", "industrial-v75"]:
        if key in s:
            bad.append(key)

    print(p.relative_to(ROOT), "=>", "⚠️ kaldı: " + ", ".join(bad) if bad else "✅ temiz")

print()
print("✅ V76 rollback tamam.")
