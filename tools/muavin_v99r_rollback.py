from pathlib import Path
import shutil

ROOT = Path(".").resolve()

WEB_JS = ROOT / "static/continue/continue_trip_v99_clean.js"
AND_JS = ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"

print("===== V99R ROLLBACK =====")

def restore_latest(target: Path, pattern: str):
    backups = sorted(target.parent.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)

    if not backups:
        print("❌ backup bulunamadı:", target.parent / pattern)
        return False

    bak = backups[0]
    shutil.copy2(bak, target)
    print("✅ geri yüklendi:", target)
    print("📦 kullanılan backup:", bak)
    return True

ok1 = restore_latest(
    WEB_JS,
    "continue_trip_v99_clean.js.bak-v99r-doluluk-gate-*"
)

ok2 = True
if AND_JS.parent.exists():
    ok2 = restore_latest(
        AND_JS,
        "continue_trip_v99_clean.js.bak-v99r-doluluk-gate-*"
    )

print()
if ok1 and ok2:
    print("✅ V99R işlemi geri alındı.")
else:
    print("⚠️ Bazı dosyalarda backup bulunamadı. Üstteki satırlara bak.")

print()
print("===== KONTROL =====")
txt = WEB_JS.read_text(encoding="utf-8", errors="ignore") if WEB_JS.exists() else ""
for key in [
    "V99R_ONLY_DOLULUK_CLICK_GATE_START",
    "MuavinV99OnlyDolulukClickGate",
]:
    print(("VAR  " if key in txt else "YOK  ") + key)
