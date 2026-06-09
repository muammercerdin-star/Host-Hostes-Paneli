from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPLS = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

NEW_FMT_DELAY = '''  function fmtDelay(min){
    // ETA_DAY_ROLLOVER_FIX_V70
    // Plan saati yanlışlıkla ertesi güne kayınca 1356 dk erken gibi saçma değer çıkıyordu.
    // Şehirlerarası seferde gecikme/erkenlik hesabını en yakın 24 saat penceresine normalize et.
    let n = Number(min || 0);

    if(!Number.isFinite(n)){
      n = 0;
    }

    while(n <= -720){
      n += 1440;
    }

    while(n > 720){
      n -= 1440;
    }

    n = Math.round(n);

    if(n <= -1) return Math.abs(n) + " dk erken";
    if(n >= 1) return n + " dk geç";
    return "Planında";
  }'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-eta-day-v70-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== ETA DAY ROLLOVER FIX V70 =====")

for p in FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    if "ETA_DAY_ROLLOVER_FIX_V70" in s:
        print("ℹ️ V70 zaten var:", p.relative_to(ROOT))
        continue

    s2 = re.sub(
        r'\s*function\s+fmtDelay\s*\(\s*min\s*\)\s*\{.*?\n\s*\}',
        "\n" + NEW_FMT_DELAY,
        s,
        count=1,
        flags=re.S
    )

    if s2 == s:
        print("❌ fmtDelay bloğu bulunamadı:", p.relative_to(ROOT))
        continue

    p.write_text(s2, encoding="utf-8")
    print("✅ 24 saat ETA kayması düzeltildi:", p.relative_to(ROOT))

for p in TPLS:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=eta-day-rollover-v70",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=eta-day-rollover-v70',
        s
    )

    p.write_text(s, encoding="utf-8")
    print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V70 tamam. Sayfayı yenileyince 1356 dk erken yerine gerçek gecikme/erkenlik görünmeli.")
