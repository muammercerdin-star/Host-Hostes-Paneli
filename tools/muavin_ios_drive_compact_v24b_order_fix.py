from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TARGETS = [
    ROOT / "templates/seats.html",
    ROOT / "android_app/app/src/main/python/templates/seats.html",
]

LINK = '<link rel="stylesheet" href="/static/seats/patches/ios-drive-panel-compact-v24.css?v=2-order-last">'

print("===== IOS DRIVE COMPACT V24B ORDER FIX =====")

for p in TARGETS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    backup = p.with_name(p.name + f".bak-ios-drive-compact-v24b-order-{STAMP}")
    shutil.copy2(p, backup)

    lines = s.splitlines()

    # Eski compact-v24 linklerini kaldır
    lines = [ln for ln in lines if "ios-drive-panel-compact-v24.css" not in ln]

    # seats-shell'den önceki son stylesheet linkinin altına ekle
    insert_at = None
    for i, ln in enumerate(lines):
        if '<div class="seats-shell">' in ln:
            insert_at = i
            break

    if insert_at is None:
        insert_at = 0
        for i, ln in enumerate(lines):
            if '<link rel="stylesheet"' in ln:
                insert_at = i + 1

    lines.insert(insert_at, LINK)

    new = "\n".join(lines) + "\n"

    if new != old:
        p.write_text(new, encoding="utf-8")
        print("✅ Compact V24 en sona taşındı:", p.relative_to(ROOT))
        print("   Yedek:", backup.relative_to(ROOT))
    else:
        print("ℹ️ Değişiklik gerekmedi:", p.relative_to(ROOT))

print()
print("===== KONTROL =====")
for p in TARGETS:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    print()
    print("----", p.relative_to(ROOT), "----")
    for i, ln in enumerate(txt.splitlines(), 1):
        if "ios-drive" in ln or "hide-quick-fab" in ln or "seat-label-ghost-clean" in ln:
            print(f"{i}: {ln}")

print()
print("✅ V24B tamamlandı. Sayfayı yenile: /seats?v=24b")
