from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
JAVA = ROOT / "android_app/app/src/main/java/com/muavinasistani/app/LiveStopAlertService.java"

print("===== V93F STABİL BİLDİRİME DÖN =====")

if not JAVA.exists():
    raise SystemExit("❌ LiveStopAlertService.java yok")

# En sağlam yol: V93B öncesi yedeğe dönmek.
backups = sorted(JAVA.parent.glob("LiveStopAlertService.java.bak-v93b-*"), key=lambda p: p.stat().st_mtime, reverse=True)

if backups:
    current_bak = JAVA.with_name(JAVA.name + f".bak-v93f-before-restore-{STAMP}")
    shutil.copy2(JAVA, current_bak)
    print("📦 Mevcut bozuk Java yedeklendi:", current_bak.relative_to(ROOT))

    shutil.copy2(backups[0], JAVA)
    print("✅ V93B öncesi stabil Java geri yüklendi:", backups[0].relative_to(ROOT))
else:
    print("⚠️ V93B öncesi yedek bulunamadı. Manuel temizlik yapılacak.")

    s = JAVA.read_text(encoding="utf-8", errors="ignore")
    current_bak = JAVA.with_name(JAVA.name + f".bak-v93f-manual-{STAMP}")
    shutil.copy2(JAVA, current_bak)

    # Custom notification zincirlerini kaldır
    s = re.sub(r"\n\s*\.setCustomContentView\(buildLiveStopCollapsedV93B\(\)\)", "", s)
    s = re.sub(r"\n\s*\.setCustomBigContentView\(buildLiveStopBigV93B\(\)\)", "", s)
    s = re.sub(r"\n\s*\.setStyle\(new Notification\.DecoratedCustomViewStyle\(\)\)", "", s)

    # RemoteViews importunu kaldır
    s = s.replace("import android.widget.RemoteViews;\n", "")

    # V93B helper bloğunu kaldır
    s = re.sub(
        r"\n\s*// V93B_CUSTOM_NOTIFICATION_CARD.*?\n\s*private void updateForegroundMonitor\(",
        "\n    private void updateForegroundMonitor(",
        s,
        flags=re.S
    )

    JAVA.write_text(s, encoding="utf-8")
    print("✅ Custom notification temizlendi.")

print()
print("===== KONTROL =====")
s = JAVA.read_text(encoding="utf-8", errors="ignore")
for i, line in enumerate(s.splitlines(), 1):
    if "setSmallIcon" in line or "setCustom" in line or "DecoratedCustomViewStyle" in line or "RemoteViews" in line:
        print(f"{i}: {line.strip()}")

print()
print("✅ V93F tamam. Şimdi derle.")
