from pathlib import Path
from datetime import datetime
import re
import hashlib

ROOT = Path(".").resolve()
TPL = ROOT / "templates/continue_trip.html"
AND_TPL = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

OUT = ROOT / "run_logs" / "continue_trip_dependency_report.txt"
OUT.parent.mkdir(exist_ok=True)

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def count_lines(p):
    if not p.exists():
        return 0
    return len(read(p).splitlines())

def nonempty(p):
    if not p.exists():
        return 0
    return sum(1 for x in read(p).splitlines() if x.strip())

def size(p):
    return p.stat().st_size if p.exists() else 0

txt = read(TPL)

refs = []

# url_for static refs
for m in re.finditer(r"filename='([^']+)'", txt):
    refs.append(m.group(1))

# raw /static refs
for m in re.finditer(r'src="/static/([^"?]+)', txt):
    refs.append(m.group(1))

refs = list(dict.fromkeys(refs))

report = []
report.append("===== CONTINUE_TRIP BAĞIMLILIK RAPORU =====")
report.append("TIME: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
report.append("ROOT: " + str(ROOT))
report.append("")

report.append("===== 1) TEMPLATE =====")
report.append(f"WEB:     {TPL} lines={count_lines(TPL)} nonempty={nonempty(TPL)} size={size(TPL)} sha={sha(TPL)}")
report.append(f"ANDROID: {AND_TPL} lines={count_lines(AND_TPL)} nonempty={nonempty(AND_TPL)} size={size(AND_TPL)} sha={sha(AND_TPL)}")
report.append(f"SYNC:    {'AYNI ✅' if TPL.exists() and AND_TPL.exists() and sha(TPL)==sha(AND_TPL) else 'FARKLI ❌'}")
report.append("")

report.append("===== 2) TEMPLATE İÇİ JINJA İSKELET =====")
report.append(f"{{{{ değişken }}}} sayısı: {txt.count('{{')}")
report.append(f"{{% blok %}} sayısı:      {txt.count('{%')}")
report.append(f"Inline <script> sayısı:   {len(re.findall(r'<script(?![^>]+src=)', txt))}")
report.append(f"Static ref sayısı:        {len(refs)}")
report.append("")

report.append("===== 3) DIŞARIDAN GELEN CSS / JS DOSYALARI =====")

total_lines = count_lines(TPL)
total_nonempty = nonempty(TPL)
total_size = size(TPL)

for ref in refs:
    p = ROOT / "static" / ref if not ref.startswith("static/") else ROOT / ref
    kind = "CSS" if ref.endswith(".css") else "JS" if ref.endswith(".js") else "?"
    report.append(
        f"{kind:3} {ref:<55} "
        f"{'VAR' if p.exists() else 'YOK'} "
        f"lines={count_lines(p):<5} nonempty={nonempty(p):<5} size={size(p):<7} sha={sha(p)}"
    )
    total_lines += count_lines(p)
    total_nonempty += nonempty(p)
    total_size += size(p)

report.append("")
report.append("===== 4) TOPLAM GERÇEK EKRAN YÜKÜ =====")
report.append(f"Template satırı:      {count_lines(TPL)}")
report.append(f"Dış CSS/JS satırı:    {total_lines - count_lines(TPL)}")
report.append(f"Yaklaşık toplam satır:{total_lines}")
report.append(f"Yaklaşık dolu satır:  {total_nonempty}")
report.append(f"Yaklaşık toplam size: {total_size} byte")
report.append("")

report.append("===== 5) APP.PY / ROUTE ARAMA =====")
app = ROOT / "app.py"
app_txt = read(app)
patterns = [
    "continue_trip",
    "render_template('continue_trip.html'",
    'render_template("continue_trip.html"',
    "CONTINUE_BOOT",
    "live_summary",
    "live_runtime",
    "live_stops",
    "continue_route_coords",
    "continue_schedule_items",
]

for pat in patterns:
    hits = []
    for i, line in enumerate(app_txt.splitlines(), 1):
        if pat in line:
            hits.append((i, line.strip()[:220]))
    report.append(f"\n--- {pat} hit={len(hits)} ---")
    for i, line in hits[:40]:
        report.append(f"{i}: {line}")
    if len(hits) > 40:
        report.append("... kesildi")

report.append("")
report.append("===== 6) KISA YORUM =====")
report.append("continue_trip.html görünen iskelet dosyasıdır.")
report.append("Asıl davranışların büyük kısmı static/continue/*.js dosyalarından gelir.")
report.append("Asıl görünümün büyük kısmı static/continue/*.css dosyalarından gelir.")
report.append("Durak, hız, bagaj, rota gibi canlı veriler app.py tarafından Jinja değişkenleriyle basılır.")
report.append("Bu yüzden refactor yapacaksak sadece template değil, bağlı JS/CSS dosyalarını da beraber haritalamak gerekir.")

out = "\n".join(report) + "\n"
print(out)
OUT.write_text(out, encoding="utf-8")
print("✅ Rapor kaydedildi:", OUT)
