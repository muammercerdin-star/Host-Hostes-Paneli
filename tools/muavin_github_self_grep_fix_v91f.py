from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
WF = ROOT / ".github/workflows/android-debug-apk.yml"

print("===== V91F WORKFLOW KENDİNİ YAKALAMA FIX =====")

if not WF.exists():
    raise SystemExit("❌ workflow yok")

bak = WF.with_name(WF.name + f".bak-v91f-{STAMP}")
shutil.copy2(WF, bak)
print("📦 Workflow yedeği:", bak.relative_to(ROOT))

s = WF.read_text(encoding="utf-8", errors="ignore")
old = s

# Hatalı negatif kontrol .github klasörünü de aradığı için kendi satırını buluyordu.
s = s.replace(
    '! grep -R "1.13.11.13.1" -n android_app .github',
    '! grep -R --exclude="*.bak*" -n "1.13.11.13.1" android_app'
)

# Farklı format oluştuysa regex ile de düzelt
s = re.sub(
    r'!\s*grep\s+-R\s+["\']1\.13\.11\.13\.1["\']\s+-n\s+android_app\s+\.github',
    '! grep -R --exclude="*.bak*" -n "1.13.11.13.1" android_app',
    s
)

WF.write_text(s, encoding="utf-8")

print()
print("===== WORKFLOW KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in [
        "Verify build files",
        "grep ",
        "1.13.11.13.1",
        "assembleDebug",
        "muavinBuildProfile"
    ]):
        print(f"{i:4}: {line}")

print()
if s != old:
    print("✅ V91F workflow düzeltildi")
else:
    print("ℹ️ Değişiklik yok")

print("✅ V91F tamam.")
