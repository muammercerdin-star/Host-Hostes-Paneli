from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB = ROOT / "templates/continue_trip.html"
AND = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

print("===== V98 TEMIZ ROLLBACK =====")

def restore_latest(target: Path):
    if not target.exists():
        print("❌ hedef yok:", target)
        return False

    current_backup = target.with_name(target.name + f".broken-v98-{STAMP}")
    shutil.copy2(target, current_backup)
    print("📦 bozuk ekran yedeği:", current_backup)

    candidates = sorted(
        target.parent.glob(target.name + ".bak-v98-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not candidates:
        print("❌ V98 öncesi backup bulunamadı:", target.parent)
        return False

    src = candidates[0]
    shutil.copy2(src, target)
    print("✅ geri alındı:", target)
    print("↩️ kaynak:", src)
    return True

ok1 = restore_latest(WEB)

if AND.exists():
    ok2 = restore_latest(AND)
else:
    ok2 = True
    print("⚠️ android template yok, geçildi")

print()
print("===== KONTROL =====")
txt = WEB.read_text(encoding="utf-8", errors="ignore")
for key in [
    "v97-real-page",
    "v97_proximity_preview.css",
    "v97_real_data.css",
    "v97_real_bind.js",
    "liveCurrentStopName",
    "liveDistanceValue",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("SONUC:", "✅ ROLLBACK TAMAM" if ok1 and ok2 else "⚠️ EK KONTROL GEREK")
