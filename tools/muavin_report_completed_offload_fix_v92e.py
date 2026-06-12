from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "app.py",
    ROOT / "android_app/app/src/main/python/app.py",
]

print("===== V92E RAPORDA TAMAMLA İNEN SAYILSIN =====")

OLD = '''        elif event == "offload":
            g["offload"].append(item)
            g["summary"]["offload_count"] += 1
'''

NEW = '''        elif event == "offload":
            g["offload"].append(item)
            g["summary"]["offload_count"] += 1

        elif event == "completed_v92c":
            try:
                completed_count = int(r["seats_for_stop"] or 0)
            except Exception:
                completed_count = 0

            # V92E:
            # "Tamamla" işlemi duraktaki yolcu/ayakta yolcu kayıtlarını toplu temizler.
            # Bu kayıtlar raporda da "inen yolcu" olarak sayılmalı.
            item["event_label"] = "Durak tamamlandı"
            item["completed_count"] = completed_count
            g["offload"].append(item)
            g["summary"]["offload_count"] += completed_count
'''

for path in FILES:
    if not path.exists():
        print("❌ Yok:", path.relative_to(ROOT))
        continue

    txt = path.read_text(encoding="utf-8", errors="ignore")

    if OLD not in txt:
        print("⚠️ Kalıp bulunamadı:", path.relative_to(ROOT))
        continue

    bak = path.with_name(path.name + f".bak-v92e-{STAMP}")
    shutil.copy2(path, bak)

    txt = txt.replace(OLD, NEW, 1)
    path.write_text(txt, encoding="utf-8")

    print("✅ Düzeltildi:", path.relative_to(ROOT))
    print("📦 Yedek:", bak.relative_to(ROOT))

print()
print("===== KONTROL =====")
for path in FILES:
    if not path.exists():
        continue
    txt = path.read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(txt.splitlines(), 1):
        if "completed_v92c" in line or "completed_count" in line or "offload_count" in line:
            if 4160 <= i <= 4250 or 4170 <= i <= 4260:
                print(f"{path.relative_to(ROOT)}:{i}: {line}")

print()
print("✅ V92E tamam. Artık completed_v92c raporda inen sayılacak.")
