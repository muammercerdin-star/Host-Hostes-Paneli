from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

print("===== V96 CANLI DURAK PROGRESS GERİ ALMA =====")
print("ROOT:", ROOT)

TARGETS = [
    "static/continue/css_parts/50-live-v2-top-glow.css",
    "static/continue/continue_trip_core.js",
    "static/continue/continue_trip.css",
    "templates/continue_trip.html",

    "android_app/app/src/main/python/static/continue/css_parts/50-live-v2-top-glow.css",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip.css",
    "android_app/app/src/main/python/templates/continue_trip.html",
]

def rel(p):
    return str(p.relative_to(ROOT))

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def backup_current(p):
    b = p.with_name(p.name + f".bak-before-rollback-v96-{STAMP}")
    shutil.copy2(p, b)
    return b

def find_pre_v96_backup(p):
    # En temiz geri dönüş: V96 ilk yamasından önce alınan backup
    pattern = p.name + ".bak-live-progress-v96-*"
    cands = sorted(p.parent.glob(pattern))
    if cands:
        return cands[0]

    # Eğer ilk backup yoksa, en eski V96 ailesi backup'ını kullanmayı dene
    fallback_patterns = [
        p.name + ".bak-v96b-runner-fix-*",
        p.name + ".bak-v96c-*",
        p.name + ".bak-v96c2-*",
    ]

    all_cands = []
    for pat in fallback_patterns:
        all_cands.extend(sorted(p.parent.glob(pat)))

    return sorted(all_cands)[0] if all_cands else None

restored = []
failed = []

for item in TARGETS:
    p = ROOT / item

    if not p.exists():
        print("⚠️ Dosya yok:", item)
        failed.append(item)
        continue

    src = find_pre_v96_backup(p)

    if not src or not src.exists():
        print("❌ Backup bulunamadı:", item)
        failed.append(item)
        continue

    cur_bak = backup_current(p)
    shutil.copy2(src, p)

    print("✅ Geri yüklendi:", item)
    print("   kaynak backup:", rel(src))
    print("   rollback öncesi yedek:", rel(cur_bak))

    restored.append(item)

print()
print("===== MARKER KONTROL =====")

MARKERS = [
    "LIVE_STOP_PROGRESS_BORDER_V96",
    "LIVE_STOP_PROGRESS_RUNNER_FIX_V96B",
    "LIVE_BORDER_RUNNER_PROGRESS_V96C",
    "LIVE_BORDER_RUNNER_PROGRESS_V96C2",
    "live-stop-progress-ready-v96",
    "live-border-progress-v96c2",
    "__liveBorderRunnerV96C2",
]

for item in TARGETS:
    p = ROOT / item
    if not p.exists():
        continue

    txt = read(p)
    hits = [m for m in MARKERS if m in txt]

    if hits:
        print("⚠️ Hâlâ marker var:", item, hits)
    else:
        print("OK:", item)

print()
if failed:
    print("⚠️ Bazı dosyalarda backup bulunamadı:")
    for x in failed:
        print(" -", x)
    print("Bunlar için ayrıca temizleme yaparız.")
else:
    print("✅ V96/V96B/V96C denemeleri geri alındı.")

print()
print("Şimdi sayfayı kapat-aç veya iki kere yenile.")
