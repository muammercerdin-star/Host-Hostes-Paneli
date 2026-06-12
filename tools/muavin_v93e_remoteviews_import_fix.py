from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V93E REMOTEVIEWS IMPORT FIX =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

s = JAVA.read_text(encoding="utf-8", errors="ignore")
old = s

bak = JAVA.with_name(JAVA.name + f".bak-v93e-{STAMP}")
shutil.copy2(JAVA, bak)
print("📦 Yedek:", bak.relative_to(ROOT))

if "import android.widget.RemoteViews;" not in s:
    # Son import satırının altına ekle
    lines = s.splitlines()
    last_import = -1
    for i, line in enumerate(lines):
        if line.startswith("import "):
            last_import = i

    if last_import >= 0:
        lines.insert(last_import + 1, "import android.widget.RemoteViews;")
        s = "\n".join(lines) + "\n"
        print("✅ RemoteViews import eklendi.")
    else:
        # Çok düşük ihtimal: import bloğu yoksa package altına ekle
        s = re.sub(
            r"^(package\s+[^;]+;\s*)",
            r"\1\nimport android.widget.RemoteViews;\n",
            s,
            count=1,
            flags=re.M
        )
        print("✅ RemoteViews import package altına eklendi.")
else:
    print("ℹ️ RemoteViews import zaten var.")

JAVA.write_text(s, encoding="utf-8")

print()
print("===== IMPORT KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if "RemoteViews" in line or "setCustomContentView" in line or "setCustomBigContentView" in line:
        print(f"{i}: {line}")

print()
print("Değişiklik:", "YAPILDI ✅" if s != old else "YOK")
print("✅ V93E tamam.")
