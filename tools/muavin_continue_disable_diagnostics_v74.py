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

print("===== CONTINUE DISABLE DIAGNOSTICS V74 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    b = p.with_name(p.name + f".bak-disable-diagnostics-v74-{STAMP}")
    shutil.copy2(p, b)
    print("📦 Yedek:", b.relative_to(ROOT))

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # Sadece teşhis/debug panelini çağıran script satırını kaldırır.
    s = re.sub(
        r'\n\s*<script\s+src="{{\s*url_for\([\'"]static[\'"],\s*filename=[\'"]continue/continue_live_diagnostics\.js[\'"]\)\s*}}\?v=[^"\']+"></script>',
        '',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ diagnostics script çağrısı kaldırıldı:", p.relative_to(ROOT))
    else:
        print("ℹ️ diagnostics script zaten yok veya desen değişmiş:", p.relative_to(ROOT))

print()
print("✅ V74 tamam. Dosya silinmedi, sadece template çağrısı kaldırıldı.")
