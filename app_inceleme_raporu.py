from pathlib import Path
import re
from collections import Counter, defaultdict

p = Path("app.py")
s = p.read_text(encoding="utf-8", errors="ignore")
lines = s.splitlines()

out = []
out.append("APP.PY İNCELEME RAPORU")
out.append("=" * 70)
out.append(f"Toplam satır: {len(lines)}")
out.append("")

# Importlar
out.append("1) IMPORTLAR")
out.append("-" * 70)
for i, line in enumerate(lines, 1):
    if line.startswith("import ") or line.startswith("from "):
        out.append(f"{i}: {line}")

# Route haritası
out.append("")
out.append("2) ROUTE HARİTASI")
out.append("-" * 70)
routes = []
for i, line in enumerate(lines, 1):
    if "@app.route" in line:
        routes.append((i, line.strip()))
        out.append(f"{i}: {line.strip()}")

# Aynı route tekrarları
out.append("")
out.append("3) TEKRAR EDEN ROUTE VAR MI?")
out.append("-" * 70)
route_paths = []
for i, line in routes:
    m = re.search(r'@app\.route\(["\']([^"\']+)', line)
    if m:
        route_paths.append((m.group(1), i))

cnt = Counter(x[0] for x in route_paths)
dups = [r for r, c in cnt.items() if c > 1]
if not dups:
    out.append("Tekrar eden route görünmüyor.")
else:
    for r in dups:
        locs = [str(i) for path, i in route_paths if path == r]
        out.append(f"{r}: satırlar {', '.join(locs)}")

# Fonksiyon tekrarları
out.append("")
out.append("4) TEKRAR EDEN FONKSİYON VAR MI?")
out.append("-" * 70)
funcs = []
for i, line in enumerate(lines, 1):
    m = re.match(r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', line)
    if m:
        funcs.append((m.group(1), i))

fc = Counter(x[0] for x in funcs)
fdups = [f for f, c in fc.items() if c > 1]
if not fdups:
    out.append("Tekrar eden fonksiyon görünmüyor.")
else:
    for f in fdups:
        locs = [str(i) for name, i in funcs if name == f]
        out.append(f"{f}: satırlar {', '.join(locs)}")

# Riskli hardcoded ayarlar
out.append("")
out.append("5) RİSKLİ / DİKKAT EDİLECEK SATIRLAR")
out.append("-" * 70)
patterns = [
    "SECRET_KEY",
    "ADMIN_PASSWORD",
    "debug=True",
    "debug=False",
    "DB_PATH",
    "UPLOAD_DIR",
    "TODO",
    "FIXME",
    "print(",
    "except Exception",
    "pass",
    "confirm(",
]
for i, line in enumerate(lines, 1):
    t = line.strip()
    if any(pat in t for pat in patterns):
        out.append(f"{i}: {t}")

# DB tablo oluşturma alanları
out.append("")
out.append("6) VERİTABANI TABLO / INDEX OLUŞTURMA")
out.append("-" * 70)
for i, line in enumerate(lines, 1):
    t = line.strip()
    if "CREATE TABLE" in t or "CREATE INDEX" in t or "ALTER TABLE" in t:
        out.append(f"{i}: {t}")

# Redirect / render_template haritası
out.append("")
out.append("7) TEMPLATE KULLANIMLARI")
out.append("-" * 70)
for i, line in enumerate(lines, 1):
    if "render_template(" in line:
        out.append(f"{i}: {line.strip()}")

# API endpointleri
out.append("")
out.append("8) API ROUTE'LARI")
out.append("-" * 70)
for i, line in routes:
    if "/api/" in line:
        out.append(f"{i}: {line.strip()}")

Path("APP_INCELEME_RAPORU.txt").write_text("\n".join(out), encoding="utf-8")
print("OK: APP_INCELEME_RAPORU.txt oluşturuldu.")
