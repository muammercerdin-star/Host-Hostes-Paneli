from pathlib import Path
from datetime import datetime
import hashlib
import re

ROOT = Path(".").resolve()

WEB = ROOT / "templates/continue_trip.html"
AND = ROOT / "android_app/app/src/main/python/templates/continue_trip.html"

OUT = ROOT / "run_logs" / "continue_trip_line_report.txt"
OUT.parent.mkdir(exist_ok=True)

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def line_count(txt):
    return len(txt.splitlines())

def count_nonempty(txt):
    return sum(1 for x in txt.splitlines() if x.strip())

def find_line(txt, needle):
    for i, line in enumerate(txt.splitlines(), 1):
        if needle in line:
            return i
    return None

def all_lines(txt, needles):
    out = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(n in line for n in needles):
            out.append((i, line.strip()))
    return out

def block_ranges(txt):
    lines = txt.splitlines()
    targets = [
        ("HEAD", "<head", "</head>"),
        ("HEADER", '<header class="v99-hdr"', "</header>"),
        ("ROUTE BAR", '<div class="v99-route-bar"', "</div>"),
        ("GAUGES", '<div class="v99-gauges"', "</div>"),
        ("MAIN", '<main class="v99-main"', "</main>"),
        ("BOTTOM NAV", '<nav class="v99-dock', "</nav>"),
        ("END TRIP MODAL", '<div class="end-trip-overlay"', "</div>"),
        ("BOOT DATA", '<script id="continue-boot-data"', "</script>"),
    ]

    result = []
    for name, start, end in targets:
        s = None
        e = None
        depth = 0

        for i, line in enumerate(lines, 1):
            if s is None and start in line:
                s = i

                # Basit bloklar için script/head/header/nav/main özel kapanış
                if end.startswith("</") and end in line:
                    e = i
                    break

                continue

            if s is not None and i > s:
                if end in line:
                    e = i
                    break

        if s:
            result.append((name, s, e, (e - s + 1) if e else None))

    return result

def make_report():
    txt = read(WEB)
    atxt = read(AND)

    if not WEB.exists():
        return "❌ templates/continue_trip.html bulunamadı\n"

    lines = txt.splitlines()

    report = []
    report.append("===== CONTINUE_TRIP.HTML SATIR RAPORU =====")
    report.append("TIME: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    report.append("ROOT: " + str(ROOT))
    report.append("")

    report.append("===== 1) DOSYA DURUMU =====")
    report.append(f"WEB:     {'VAR' if WEB.exists() else 'YOK'} size={WEB.stat().st_size if WEB.exists() else '-'} sha={sha(WEB)} {WEB}")
    report.append(f"ANDROID: {'VAR' if AND.exists() else 'YOK'} size={AND.stat().st_size if AND.exists() else '-'} sha={sha(AND)} {AND}")
    report.append(f"SENKRON: {'AYNI ✅' if WEB.exists() and AND.exists() and sha(WEB)==sha(AND) else 'FARKLI ❌'}")
    report.append("")

    report.append("===== 2) SATIR ÖZETİ =====")
    report.append(f"Toplam satır:       {line_count(txt)}")
    report.append(f"Dolu satır:         {count_nonempty(txt)}")
    report.append(f"Boş satır:          {line_count(txt) - count_nonempty(txt)}")
    report.append(f"Karakter sayısı:    {len(txt)}")
    report.append("")

    report.append("===== 3) JINJA / HTML YOĞUNLUK =====")
    report.append(f"{{{{ ... }}}} sayısı: {txt.count('{{')}")
    report.append(f"{{% ... %}} sayısı: {txt.count('{%')}")
    report.append(f"if kullanımı:       {len(re.findall(r'\\{%\\s*if\\b', txt))}")
    report.append(f"for kullanımı:      {len(re.findall(r'\\{%\\s*for\\b', txt))}")
    report.append(f"set kullanımı:      {len(re.findall(r'\\{%\\s*set\\b', txt))}")
    report.append("")

    report.append("===== 4) SCRIPT / CSS REFERANSLARI =====")
    css_refs = all_lines(txt, ['<link rel="stylesheet"', '<link '])
    script_refs = all_lines(txt, ['<script src=', '<script id=', '<script>'])

    report.append(f"CSS/link satırı:    {len(css_refs)}")
    for i, line in css_refs:
        report.append(f"{i}: {line}")

    report.append("")
    report.append(f"Script satırı:      {len(script_refs)}")
    for i, line in script_refs:
        report.append(f"{i}: {line}")

    report.append("")
    report.append("===== 5) ANA BÖLÜM SATIR ARALIKLARI =====")
    for name, s, e, n in block_ranges(txt):
        report.append(f"{name:16} başlangıç={s:<4} bitiş={str(e):<4} satır={n}")

    report.append("")
    report.append("===== 6) ÖNEMLİ ID / BLOK KONUMU =====")
    needles = [
        "v99SpeedVal",
        "liveSpeedText",
        "DOLULUK",
        "liveCurrentCard",
        "liveOffloadMetric",
        "liveBagajMetric",
        "tlContainer",
        "endTripForm",
        "continue-boot-data",
        "continue_trip_v99_clean.js",
        "continue_speed_final_v105.js",
    ]

    for n in needles:
        report.append(f"{n:32} line={find_line(txt, n)}")

    report.append("")
    report.append("===== 7) HIZ YAMA TEMİZLİĞİ KONTROL =====")
    speed_terms = [
        "continue_speed_toggle_v100",
        "continue_speed_widget_v101",
        "continue_speed_overlay_v102",
        "continue_speed_bar_v103",
        "continue_speed_final_v105",
    ]

    for term in speed_terms:
        report.append(("VAR  " if term in txt else "YOK  ") + term)

    report.append("")
    report.append("===== 8) KISA YORUM =====")
    total = line_count(txt)

    if total <= 250:
        report.append("Durum: Dosya makul boyutta.")
    elif total <= 500:
        report.append("Durum: Orta boy. Şimdilik yönetilir ama parçalama planı iyi olur.")
    else:
        report.append("Durum: Büyük dosya. Template parçalama/refactor önerilir.")

    if "continue_speed_final_v105" in txt:
        report.append("Hız tarafında aktif görünen son paket: V105 final polish.")
    else:
        report.append("Hız tarafında ayrı aktif paket görünmüyor.")

    if WEB.exists() and AND.exists() and sha(WEB)==sha(AND):
        report.append("Web ve Android template birebir aynı.")
    else:
        report.append("Web ve Android template farklı olabilir, sync kontrolü lazım.")

    return "\n".join(report) + "\n"

report = make_report()
print(report)
OUT.write_text(report, encoding="utf-8")
print("✅ Rapor kaydedildi:", OUT)
