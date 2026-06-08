from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/live_map.html",
    ROOT / "android_app/app/src/main/python/templates/live_map.html",
]

FILES = [
    ROOT / "static/live_map/live-seats-overlay-v40.css",
    ROOT / "static/live_map/live-seats-overlay-v40.js",
    ROOT / "android_app/app/src/main/python/static/live_map/live-seats-overlay-v40.css",
    ROOT / "android_app/app/src/main/python/static/live_map/live-seats-overlay-v40.js",
]

print("===== ROLLBACK LIVE SEATS OVERLAY V40 =====")

for tpl in TPLS:
    if not tpl.exists():
        print("⚠️ Template yok:", tpl.relative_to(ROOT))
        continue

    backup = tpl.with_name(tpl.name + f".bak-rollback-live-seats-v40-{STAMP}")
    shutil.copy2(tpl, backup)

    s = tpl.read_text(encoding="utf-8", errors="ignore")
    old = s

    lines = []
    for line in s.splitlines():
        if "live-seats-overlay-v40.css" in line:
            continue
        if "live-seats-overlay-v40.js" in line:
            continue
        lines.append(line)

    s = "\n".join(lines) + "\n"
    tpl.write_text(s, encoding="utf-8")

    if s != old:
        print("✅ Linkler kaldırıldı:", tpl.relative_to(ROOT))
    else:
        print("ℹ️ V40 link bulunmadı:", tpl.relative_to(ROOT))

    print("📦 Yedek:", backup.relative_to(ROOT))

for f in FILES:
    if f.exists():
        f.unlink()
        print("🗑️ Silindi:", f.relative_to(ROOT))
    else:
        print("ℹ️ Zaten yok:", f.relative_to(ROOT))

print()
print("===== KONTROL =====")
hits = 0
for p in TPLS + FILES:
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        c = txt.count("live-seats-overlay-v40") + txt.count("LIVE_SEATS_OVERLAY_V40")
        hits += c
        print(p.relative_to(ROOT), "V40 iz:", c)

print()
if hits == 0:
    print("✅ V40 tamamen geri alındı.")
else:
    print("⚠️ Hâlâ V40 izi var:", hits)
