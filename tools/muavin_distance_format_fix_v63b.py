from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

JS_FILES = [
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js",
]

TPL_FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

NEW_FUNC = r'''  function formatGpsKm(value){
    const raw = String(value ?? "").trim();
    if(!raw) return "—";

    // DISTANCE_FORMAT_FIX_V63B
    // "439 m" hazır formatlı gelirse 439 km sanma.
    // "112 m", "50 m", "28.20 km" olduğu gibi gösterilir.
    const lower = raw.toLocaleLowerCase("tr-TR");

    if(/\bkm\b/.test(lower) || /km\s*$/.test(lower)){
      return raw;
    }

    if(/(^|\s|[0-9])m\s*$/.test(lower) && !/km\s*$/.test(lower)){
      return raw;
    }

    const cleaned = raw
      .replace(",", ".")
      .replace(/[^0-9.\-]/g, "")
      .trim();

    const km = Number(cleaned);
    if(!Number.isFinite(km)) return raw;

    if(km < 0) return "—";
    if(km < 1) return `${Math.round(km * 1000)} m`;
    return `${km.toFixed(2)} km`;
  }'''

def backup(p):
    if p.exists():
        b = p.with_name(p.name + f".bak-distance-format-v63b-{STAMP}")
        shutil.copy2(p, b)
        print("📦 Yedek:", b.relative_to(ROOT))

print("===== DISTANCE FORMAT FIX V63B =====")

for p in JS_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    if "DISTANCE_FORMAT_FIX_V63B" in s:
        print("ℹ️ V63B zaten var:", p.relative_to(ROOT))
        continue

    pattern = re.compile(
        r'  function formatGpsKm\(value\)\{\n.*?\n  \}',
        re.S
    )

    # ÖNEMLİ: lambda kullanıyoruz; böylece \s, \b gibi karakterler regex replacement olarak yorumlanmaz.
    s, n = pattern.subn(lambda m: NEW_FUNC, s, count=1)

    if n != 1:
        print("❌ formatGpsKm fonksiyonu bulunamadı/değişmedi:", p.relative_to(ROOT))
        continue

    p.write_text(s, encoding="utf-8")
    print("✅ formatGpsKm düzeltildi:", p.relative_to(ROOT))

for p in TPL_FILES:
    if not p.exists():
        print("⚠️ Yok:", p.relative_to(ROOT))
        continue

    backup(p)
    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    s = re.sub(
        r"continue_trip_core\.js'\) }}\?v=[^\"']+",
        "continue_trip_core.js') }}?v=distance-format-v63b",
        s
    )
    s = re.sub(
        r'continue_trip_core\.js"\) }}\?v=[^"\']+',
        'continue_trip_core.js") }}?v=distance-format-v63b',
        s
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print("✅ Cache kırıldı:", p.relative_to(ROOT))

print()
print("✅ V63B tamam. 439 m artık 439.00 km olmayacak.")
