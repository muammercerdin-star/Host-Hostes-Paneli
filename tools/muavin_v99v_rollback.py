from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99V DOLULUK DIRECT CLICK ROLLBACK =====")

def latest_backup(p, marker):
    files = sorted(p.parent.glob(p.name + marker), key=lambda x: x.stat().st_mtime, reverse=True)
    return files[0] if files else None

for p in [WEB_JS, AND_JS]:
    if not p.exists():
        print("YOK:", p)
        continue

    safe = p.with_name(p.name + f".bak-before-v99v-rollback-{STAMP}")
    shutil.copy2(p, safe)
    print("📦 rollback öncesi backup:", safe)

# 1) Önce gerçek V99V backup varsa ona dön
web_bak = latest_backup(WEB_JS, ".bak-v99v-doluluk-direct-*")
and_bak = latest_backup(AND_JS, ".bak-v99v-doluluk-direct-*") if AND_JS.exists() else None

if web_bak:
    shutil.copy2(web_bak, WEB_JS)
    print("✅ web JS eski yedeğe döndü:", web_bak)
else:
    print("⚠️ web V99V backup bulunamadı, blok temizleme yapılacak")
    s = WEB_JS.read_text(encoding="utf-8", errors="ignore")
    s2 = re.sub(
        r"\n?/\* V99V_DOLULUK_DIRECT_CLICK_START \*/.*?/\* V99V_DOLULUK_DIRECT_CLICK_END \*/\n?",
        "\n",
        s,
        flags=re.S
    )
    WEB_JS.write_text(s2, encoding="utf-8")
    print("✅ web JS içinden V99V bloğu temizlendi")

if AND_JS.parent.exists():
    if and_bak:
        shutil.copy2(and_bak, AND_JS)
        print("✅ android JS eski yedeğe döndü:", and_bak)
    else:
        shutil.copy2(WEB_JS, AND_JS)
        print("✅ android JS web'den senkronlandı")

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore")

for key in [
    "V99V_DOLULUK_DIRECT_CLICK_START",
    "hitTopCardByGeometry",
    "v99v-doluluk-direct",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)

print()
print("✅ V99V geri alındı. Tarayıcıda /continue-trip?v=rollbackv99v ile yenile.")
