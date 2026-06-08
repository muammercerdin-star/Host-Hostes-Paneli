from pathlib import Path
import shutil

ROOT = Path(".").resolve()
ANDROID = ROOT / "android_app/app/src/main/python"

print("===== APK DETOX V33 - BACKUP TEMİZLİĞİ =====")

if not ANDROID.exists():
    print("❌ Android python klasörü yok:", ANDROID)
    raise SystemExit

remove_name_parts = [
    ".bak",
    ".before_",
    ".disabled_",
    "_disabled",
    "_archive_theme_trials",
    "backup",
    "bak-sync-before-apk",
]

removed = []
total_bytes = 0

def should_remove(p: Path):
    name = p.name.lower()
    return any(part.lower() in name for part in remove_name_parts)

# Önce klasörleri sil
for p in sorted(ANDROID.rglob("*"), key=lambda x: len(str(x)), reverse=True):
    if p.is_dir() and should_remove(p):
        size = 0
        for f in p.rglob("*"):
            if f.is_file():
                try:
                    size += f.stat().st_size
                except:
                    pass
        shutil.rmtree(p, ignore_errors=True)
        removed.append(str(p.relative_to(ROOT)))
        total_bytes += size

# Sonra dosyaları sil
for p in sorted(ANDROID.rglob("*")):
    if p.is_file() and should_remove(p):
        try:
            size = p.stat().st_size
        except:
            size = 0
        try:
            p.unlink()
            removed.append(str(p.relative_to(ROOT)))
            total_bytes += size
        except Exception as e:
            print("⚠️ Silinemedi:", p.relative_to(ROOT), e)

print("Silinen kayıt:", len(removed))
print("Temizlenen boyut:", round(total_bytes / 1024 / 1024, 2), "MB")

for x in removed[:80]:
    print("🧹", x)

if len(removed) > 80:
    print("... devamı var:", len(removed) - 80)

print()
print("===== KALAN EN BÜYÜK DOSYALAR =====")
files = []
for f in ANDROID.rglob("*"):
    if f.is_file():
        try:
            files.append((f.stat().st_size, f))
        except:
            pass

for size, f in sorted(files, reverse=True)[:40]:
    print(f"{size/1024/1024:8.2f} MB  {f.relative_to(ROOT)}")

print()
print("===== BACKUP KALDI MI =====")
left = []
for p in ANDROID.rglob("*"):
    if should_remove(p):
        left.append(p)

if not left:
    print("✅ Backup/disabled/archive kalmadı.")
else:
    print("⚠️ Hâlâ kalan var:")
    for p in left[:80]:
        print(p.relative_to(ROOT))

print()
print("✅ V33 detox tamam.")
