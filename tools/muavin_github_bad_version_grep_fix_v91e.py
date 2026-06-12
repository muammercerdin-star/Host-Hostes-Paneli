from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
WF = ROOT / ".github/workflows/android-debug-apk.yml"

print("===== V91E GITHUB BAD VERSION GREP FIX =====")

if not WF.exists():
    raise SystemExit("❌ workflow yok")

bak = WF.with_name(WF.name + f".bak-v91e-{STAMP}")
shutil.copy2(WF, bak)
print("📦 Workflow yedeği:", bak.relative_to(ROOT))

s = WF.read_text(encoding="utf-8", errors="ignore")
old = s

# Yanlış negatif kontrol: doğru sürümü arıyordu, build'i düşürüyordu.
s = s.replace(
    '! grep -R "1.13.1" -n android_app .github',
    '! grep -R "1.13.11.13.1" -n android_app .github'
)

# Eğer farklı tırnak/boşlukla oluştuysa regex ile de temizle
s = re.sub(
    r'!\s*grep\s+-R\s+["\']1\.13\.1["\']\s+-n\s+android_app\s+\.github',
    '! grep -R "1.13.11.13.1" -n android_app .github',
    s
)

WF.write_text(s, encoding="utf-8")

print()
print("===== WORKFLOW KONTROL =====")
for i, line in enumerate(s.splitlines(), 1):
    if any(k in line for k in ["grep -R", "assembleDebug", "muavinBuildProfile", "python-version"]):
        print(f"{i:4}: {line}")

print()
print("1.13.11.13.1 kontrol satırı sayısı:", s.count('! grep -R "1.13.11.13.1"'))
print("yanlış ! grep 1.13.1 sayısı:", s.count('! grep -R "1.13.1"'))

if s != old:
    print("✅ V91E düzeltme yapıldı")
else:
    print("ℹ️ Değişiklik yok")

print("✅ V91E tamam.")
