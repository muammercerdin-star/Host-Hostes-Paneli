from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== ROLLBACK VOICE ALERT V81 =====")

for p in TPLS:
    if not p.exists():
        print("⚠️ Template yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-rollback-voice-alert-v81-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # V81 sesli uyarı script çağrısını kaldır.
    s = re.sub(
        r'\n?\s*<script src="{{ url_for\(\'static\', filename=\'continue/continue_voice_alert_v81\.js\'\) }}\?v=voice-alert-v81"></script>\s*',
        '\n',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ V81 sesli uyarı çağrısı kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ V81 script çağrısı bulunamadı:", p.relative_to(ROOT))

print()
print("✅ V81 geri alındı. Dosya duruyor ama artık çağrılmıyor.")
