from pathlib import Path
import re
from collections import Counter

ROOT = Path(".").resolve()

FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
]

print("===== CONTINUE TEMPLATE AUDIT V73 =====")
print("ROOT:", ROOT)
print()

for p in FILES:
    print()
    print("==================================================")
    print("DOSYA:", p.relative_to(ROOT))
    print("==================================================")

    if not p.exists():
        print("❌ Dosya yok")
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")
    lines = s.splitlines()

    print("Satır:", len(lines))
    print("Karakter:", len(s))
    print()

    print("===== 1) HTML COMMENT / PATCH MARKERLARI =====")
    comment_hits = []
    for i, line in enumerate(lines, 1):
        if "<!--" in line or "-->" in line or re.search(r'\b(V\d+|PATCH|START|END|FIX|BRIDGE|DIAG|DEBUG|REFRESH|CLEAN)\b', line, re.I):
            comment_hits.append((i, line.strip()))

    if not comment_hits:
        print("✅ Marker/comment yok")
    else:
        for i, line in comment_hits:
            print(f"{i:4d}: {line}")

    print()
    print("===== 2) ÇAĞRILAN CSS / JS DOSYALARI =====")
    css = re.findall(r'href="{{\s*url_for\([^)]+filename=[\'"]([^\'"]+)[\'"][^)]+\)\s*}}\?v=([^\'"]+)"', s)
    js = re.findall(r'src="{{\s*url_for\([^)]+filename=[\'"]([^\'"]+)[\'"][^)]+\)\s*}}\?v=([^\'"]+)"', s)
    raw_js = re.findall(r'<script[^>]+src="([^"]+)"', s)

    print("CSS sayısı:", len(css))
    for f, v in css:
        print("CSS:", f, "v=", v)

    print()
    print("JS sayısı:", len(js))
    for f, v in js:
        print("JS:", f, "v=", v)

    print()
    print("Ham script src sayısı:", len(raw_js))
    for x in raw_js:
        print("SRC:", x)

    print()
    print("===== 3) INLINE SCRIPT BLOKLARI =====")
    script_blocks = list(re.finditer(r'<script(?![^>]+src=)[^>]*>(.*?)</script>', s, flags=re.S|re.I))
    print("Inline script blok sayısı:", len(script_blocks))

    for n, m in enumerate(script_blocks, 1):
        start_line = s[:m.start()].count("\n") + 1
        body = m.group(1)
        chars = len(body)
        body_lines = body.count("\n") + 1
        first = ""
        for ln in body.splitlines():
            if ln.strip():
                first = ln.strip()[:140]
                break
        print(f"{n:02d}. satır {start_line} | {body_lines} satır | {chars} karakter | {first}")

    print()
    print("===== 4) ŞÜPHELİ / TEST / DEBUG İZLERİ =====")
    suspicious_words = [
        "diagnostics", "diag", "debug", "test", "probe", "console.log",
        "alert(", "TODO", "FIXME", "refresh-v", "bridge", "patch"
    ]

    found = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(w.lower() in low for w in suspicious_words):
            found.append((i, line.strip()))

    if not found:
        print("✅ Şüpheli iz yok")
    else:
        for i, line in found:
            print(f"{i:4d}: {line}")

    print()
    print("===== 5) ID TEKRARI VAR MI =====")
    ids = re.findall(r'id="([^"]+)"', s)
    c = Counter(ids)
    dups = [(k, v) for k, v in c.items() if v > 1]

    print("ID sayısı:", len(ids))
    print("Tekil ID:", len(c))

    if not dups:
        print("✅ Duplicate id yok")
    else:
        for k, v in dups:
            print("❌", k, "x", v)

    print()
    print("===== 6) YORUM =====")
    print("Bu rapor sadece okuma/denetimdir. Silme/düzeltme yapmadı.")

print()
print("===== WEB / ANDROID TEMPLATE FARKI =====")
web = FILES[0]
andp = FILES[1]
if web.exists() and andp.exists():
    sw = web.read_text(encoding="utf-8", errors="ignore")
    sa = andp.read_text(encoding="utf-8", errors="ignore")
    if sw == sa:
        print("✅ Web ve Android continue_trip.html birebir aynı")
    else:
        print("⚠️ Web ve Android continue_trip.html farklı")
        print("Web karakter:", len(sw))
        print("Android karakter:", len(sa))
else:
    print("⚠️ Karşılaştırma yapılamadı")
