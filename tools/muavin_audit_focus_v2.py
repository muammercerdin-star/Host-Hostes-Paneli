from pathlib import Path
from datetime import datetime
import re
from collections import defaultdict, Counter

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"

reports = sorted(REPORTS.glob("muavin_full_audit_*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
if not reports:
    print("❌ Full audit raporu bulunamadı.")
    raise SystemExit

SRC = reports[0]
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_focus_decision_{STAMP}.md"

text = SRC.read_text(encoding="utf-8", errors="ignore")

def section(title_start):
    lines = text.splitlines()
    out = []
    capture = False
    for line in lines:
        if line.startswith("## ") and title_start in line:
            capture = True
            out.append(line)
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            out.append(line)
    return "\n".join(out).strip()

def rows_from_section(sec):
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        if "---" in line:
            continue
        cols = [c.strip().replace("\\|", "|") for c in line.strip("|").split("|")]
        rows.append(cols)
    if rows:
        return rows[1:]
    return []

sections = {
    "same_content": section("6) Aynı İçeriğe Sahip Dosyalar"),
    "same_name": section("7) Aynı İsimli Dosyalar"),
    "android": section("8) Android/Web Gölge Kopya Kontrolü"),
    "backup": section("9) Backup / Eski / Test / Audit Dosya Adayları"),
    "routes": section("10) Flask Route Haritası"),
    "renders": section("11) render_template Haritası"),
    "deps": section("12) Template"),
    "missing": section("13) Eksik Local Static"),
    "orphan": section("14) Referans Verilmeyen Static Dosyalar"),
    "inline": section("15) Inline Style"),
    "dup_id": section("16) Aynı HTML Dosyası İçinde Duplicate ID"),
    "global_id": section("17) Farklı Dosyalarda Aynı ID"),
    "js_dup_file": section("18) Aynı Dosya İçinde Tekrar Eden JS"),
    "js_dup_global": section("19) Farklı Dosyalarda Aynı JS"),
    "py_dup_file": section("20) Aynı Dosya İçinde Tekrar Eden Python"),
    "py_dup_global": section("21) Farklı Dosyalarda Aynı Python"),
    "css_dup": section("22) CSS Selector Tekrarları"),
    "patch": section("23) Yama / Patch / Fix İzleri"),
    "debug": section("25) Debug / TODO / Alert İzleri"),
}

same_name_rows = rows_from_section(sections["same_name"])
android_rows = rows_from_section(sections["android"])
backup_rows = rows_from_section(sections["backup"])
missing_rows = rows_from_section(sections["missing"])
orphan_rows = rows_from_section(sections["orphan"])
dup_id_rows = rows_from_section(sections["dup_id"])
global_id_rows = rows_from_section(sections["global_id"])
js_dup_file_rows = rows_from_section(sections["js_dup_file"])
js_dup_global_rows = rows_from_section(sections["js_dup_global"])
py_dup_file_rows = rows_from_section(sections["py_dup_file"])
py_dup_global_rows = rows_from_section(sections["py_dup_global"])
css_dup_rows = rows_from_section(sections["css_dup"])
patch_rows = rows_from_section(sections["patch"])
debug_rows = rows_from_section(sections["debug"])
inline_rows = rows_from_section(sections["inline"])

same_name_conflicts = [r for r in same_name_rows if any("FARKLI" in c or "ÇAKIŞMA" in c for c in r)]
android_conflicts = [r for r in android_rows if any("FARKLI" in c or "ANA KOPYA YOK" in c for c in r)]

def md_table(headers, rows, limit=80):
    rows = rows[:limit]
    if not rows:
        return "_Kayıt yok._"
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        rr = list(r)[:len(headers)]
        while len(rr) < len(headers):
            rr.append("")
        out.append("| " + " | ".join(str(x).replace("\n", " ") for x in rr) + " |")
    return "\n".join(out)

# Backup klasör/isim gruplama
backup_path_counter = Counter()
backup_ext_counter = Counter()
backup_big = []

for r in backup_rows:
    if not r:
        continue
    path = r[0]
    parts = path.split("/")
    top = parts[0] if parts else "."
    backup_path_counter[top] += 1
    ext = Path(path).suffix.lower() or "[uzantısız]"
    backup_ext_counter[ext] += 1
    try:
        size = int(str(r[1]).strip())
    except:
        size = 0
    backup_big.append((path, size, r[2] if len(r) > 2 else ""))

backup_big.sort(key=lambda x: x[1], reverse=True)

# Eksik static türleri
missing_by_caller = Counter()
missing_by_ext = Counter()
for r in missing_rows:
    if len(r) >= 3:
        caller, ref, expected = r[:3]
        missing_by_caller[caller] += 1
        missing_by_ext[Path(expected).suffix.lower() or "[uzantısız]"] += 1

# Orphan static türleri
orphan_ext = Counter()
for r in orphan_rows:
    if r:
        orphan_ext[Path(r[0]).suffix.lower() or "[uzantısız]"] += 1

md = []
md.append("# Muavin Asistanı Odak Karar Raporu")
md.append("")
md.append(f"- Kaynak rapor: `{SRC}`")
md.append(f"- Yeni karar raporu: `{OUT}`")
md.append("")
md.append("## 1) Kritik Sayılar")
md.append("")
md.append(f"- Aynı isimli çakışma adayı: **{len(same_name_conflicts)}**")
md.append(f"- Android/Web senkron çakışması: **{len(android_conflicts)}**")
md.append(f"- Eksik static/ref: **{len(missing_rows)}**")
md.append(f"- Referans verilmeyen static adayı: **{len(orphan_rows)}**")
md.append(f"- Backup/eski/test adayı: **{len(backup_rows)}**")
md.append(f"- Aynı HTML içinde duplicate ID: **{len(dup_id_rows)}**")
md.append(f"- Farklı dosyalarda aynı ID: **{len(global_id_rows)}**")
md.append(f"- Aynı dosyada tekrar JS fonksiyonu: **{len(js_dup_file_rows)}**")
md.append(f"- Farklı dosyalarda aynı JS fonksiyonu: **{len(js_dup_global_rows)}**")
md.append(f"- Aynı dosyada tekrar Python fonksiyonu: **{len(py_dup_file_rows)}**")
md.append(f"- Farklı dosyalarda aynı Python fonksiyonu: **{len(py_dup_global_rows)}**")
md.append(f"- CSS selector tekrar adayı: **{len(css_dup_rows)}**")
md.append(f"- Patch/yama token satırı: **{len(patch_rows)}**")
md.append(f"- Debug/TODO/alert satırı: **{len(debug_rows)}**")
md.append("")

md.append("## 2) İlk Karar")
md.append("")
md.append("Şu aşamada silme yapılmayacak. Önce şu sırayla ilerlenmeli:")
md.append("")
md.append("1. Android/Web farklı kopyalar incelenecek.")
md.append("2. Aynı isimli ama farklı içerikli dosyalar sınıflandırılacak.")
md.append("3. Eksik static referansları düzeltilecek veya referans kaldırma adayı yapılacak.")
md.append("4. Backup/eski/test dosyaları aktif çağrılıyor mu kontrol edilecek.")
md.append("5. Duplicate ID ve JS fonksiyon tekrarları uygulama hatası çıkarıyor mu incelenecek.")
md.append("6. Son aşamada temizlik paketi hazırlanacak.")
md.append("")

md.append("## 3) Android/Web Senkron Çakışmaları")
md.append(md_table(["Alt yol", "Durum", "Ana kopya", "Android kopya"], android_conflicts, 120))
md.append("")

md.append("## 4) Aynı İsimli Ama Farklı İçerikli Dosyalar")
md.append(md_table(["Dosya adı", "Adet", "Durum", "Konumlar"], same_name_conflicts, 160))
md.append("")

md.append("## 5) Eksik Static/Local Referanslar - Çağıran Dosyaya Göre")
md.append(md_table(["Çağıran dosya", "Eksik ref sayısı"], missing_by_caller.most_common(80), 80))
md.append("")
md.append("### Eksik referansların uzantı dağılımı")
md.append(md_table(["Uzantı", "Adet"], missing_by_ext.most_common(40), 40))
md.append("")
md.append("### Eksik referanslardan ilk 160 kayıt")
md.append(md_table(["Çağıran HTML", "Referans", "Beklenen yol"], missing_rows, 160))
md.append("")

md.append("## 6) Referans Verilmeyen Static Dosyalar")
md.append("")
md.append("Bu liste tehlikelidir: JS dinamik çağırıyor olabilir. Direkt silinmez.")
md.append("")
md.append("### Uzantı dağılımı")
md.append(md_table(["Uzantı", "Adet"], orphan_ext.most_common(40), 40))
md.append("")
md.append("### İlk 160 kayıt")
md.append(md_table(["Static dosya", "Byte", "Uzantı"], orphan_rows, 160))
md.append("")

md.append("## 7) Backup / Eski / Test Adayları")
md.append("")
md.append("### Ana klasöre göre dağılım")
md.append(md_table(["Klasör", "Adet"], backup_path_counter.most_common(40), 40))
md.append("")
md.append("### Uzantıya göre dağılım")
md.append(md_table(["Uzantı", "Adet"], backup_ext_counter.most_common(40), 40))
md.append("")
md.append("### En büyük 120 backup/eski/test adayı")
md.append(md_table(["Dosya", "Byte", "Satır"], backup_big, 120))
md.append("")

md.append("## 8) Duplicate ID")
md.append("")
md.append("### Aynı HTML içinde")
md.append(md_table(["ID", "Tekrar", "Dosya"], dup_id_rows, 120))
md.append("")
md.append("### Farklı dosyalarda")
md.append(md_table(["ID", "Dosya sayısı", "Dosyalar"], global_id_rows, 120))
md.append("")

md.append("## 9) JS Fonksiyon Tekrarları")
md.append("")
md.append("### Aynı dosya içinde")
md.append(md_table(["Fonksiyon", "Tekrar", "Dosya"], js_dup_file_rows, 120))
md.append("")
md.append("### Farklı dosyalarda")
md.append(md_table(["Fonksiyon", "Dosya sayısı", "Dosyalar"], js_dup_global_rows, 120))
md.append("")

md.append("## 10) Python Fonksiyon Tekrarları")
md.append("")
md.append("### Aynı dosya içinde")
md.append(md_table(["Fonksiyon", "Tekrar", "Dosya"], py_dup_file_rows, 120))
md.append("")
md.append("### Farklı dosyalarda")
md.append(md_table(["Fonksiyon", "Dosya sayısı", "Dosyalar"], py_dup_global_rows, 120))
md.append("")

md.append("## 11) CSS Selector Tekrarları")
md.append(md_table(["Selector", "Tekrar", "Dosyalar"], css_dup_rows, 160))
md.append("")

md.append("## 12) Inline Script/Style Şişkinliği")
md.append(md_table(["HTML", "Inline style", "Inline script"], inline_rows, 80))
md.append("")

md.append("## 13) Patch/Yama Tokenları")
md.append(md_table(["Yama token", "Geçiş", "Dosyalar"], patch_rows, 160))
md.append("")

md.append("## 14) Debug/TODO/Alert İzleri")
md.append(md_table(["Dosya", "Satır", "Satır içeriği"], debug_rows, 160))
md.append("")

md.append("## 15) Temizlik İçin Güven Sınıfları")
md.append("")
md.append("### A - Şimdilik dokunulmayacak")
md.append("- `app.py`, `templates/*.html`, aktif `static/*.js`, aktif `static/*.css`")
md.append("- Android içindeki aktif çalışan kopyalar")
md.append("- Route/render_template içinde görünen dosyalar")
md.append("")
md.append("### B - İncelenecek")
md.append("- Android/Web farklı kopyalar")
md.append("- Aynı isimli ama farklı içerikli dosyalar")
md.append("- Duplicate ID olan template dosyaları")
md.append("- Aynı dosya içinde tekrar eden JS fonksiyonları")
md.append("")
md.append("### C - Silme adayı olabilir ama önce aktif çağrı kontrolü şart")
md.append("- `.bak`, `backup`, `old`, `eski`, `copy`, `tmp`, `deneme`, `test`, `step`, `audit` geçen dosyalar")
md.append("- Referans verilmeyen static dosyalar")
md.append("")
md.append("### D - Asla direkt silinmeyecek")
md.append("- `android_app/app/src/main/python` altındaki dosyalar")
md.append("- `templates` içindeki ana ekranlar")
md.append("- `static/seats`, `static/js`, `static/css` gibi canlı bağlı klasörler")
md.append("- Veritabanı veya kullanıcı kayıt dosyaları")
md.append("")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Odak karar raporu hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
print("Kaynak rapor:", SRC)
print("Aynı isimli çakışma:", len(same_name_conflicts))
print("Android/Web çakışma:", len(android_conflicts))
print("Eksik static/ref:", len(missing_rows))
print("Referanssız static:", len(orphan_rows))
print("Backup/eski/test:", len(backup_rows))
print("Duplicate ID:", len(dup_id_rows))
print("JS tekrar:", len(js_dup_file_rows))
print("Python tekrar:", len(py_dup_file_rows))
print()
print("İlk 260 satırı görmek için:")
print(f"sed -n '1,260p' {OUT}")
