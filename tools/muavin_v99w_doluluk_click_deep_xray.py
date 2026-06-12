from pathlib import Path
from datetime import datetime
import hashlib
import re
import sys

ROOT = Path(".").resolve()

FILES = {
    "WEB_TEMPLATE": ROOT / "templates/continue_trip.html",
    "WEB_JS": ROOT / "static/continue/continue_trip_v99_clean.js",
    "WEB_CSS": ROOT / "static/continue/continue_trip_v99_clean.css",
    "ANDROID_TEMPLATE": ROOT / "android_app/app/src/main/python/templates/continue_trip.html",
    "ANDROID_JS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js",
    "ANDROID_CSS": ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css",
}

print("===== V99W DOLULUK CLICK DEEP RÖNTGEN =====")
print("ROOT:", ROOT)
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def show_contains(label, txt, keys):
    print()
    print("=====", label, "=====")
    for k in keys:
        print(("VAR  " if k in txt else "YOK  ") + k)

def print_lines(title, txt, patterns, pad=8, max_lines=260):
    print()
    print("=====", title, "=====")
    lines = txt.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if any(p.lower() in low for p in patterns):
            hits.append(i)

    print("HIT_COUNT:", len(hits))
    shown = set()

    for i in hits[:max_lines]:
        for n in range(max(1, i-pad), min(len(lines), i+pad)+1):
            if n in shown:
                continue
            shown.add(n)
            print(f"{n:5}: {lines[n-1][:260]}")
        print("-----")

    if len(hits) > max_lines:
        print("... kesildi")

print()
print("===== 1) DOSYA DURUMU / SENKRON =====")
for name, p in FILES.items():
    print(f"{name:18} {'VAR' if p.exists() else 'YOK'} size={p.stat().st_size if p.exists() else '-':<8} sha={sha(p)} {p}")

print()
print("===== 2) WEB / ANDROID AYNI MI =====")
for label, a, b in [
    ("TEMPLATE", FILES["WEB_TEMPLATE"], FILES["ANDROID_TEMPLATE"]),
    ("JS", FILES["WEB_JS"], FILES["ANDROID_JS"]),
    ("CSS", FILES["WEB_CSS"], FILES["ANDROID_CSS"]),
]:
    if a.exists() and b.exists():
        print(f"{label:10} {'AYNI' if sha(a)==sha(b) else 'FARKLI'} web={sha(a)} android={sha(b)}")
    else:
        print(f"{label:10} KONTROL_EDILEMEDI")

tpl = read(FILES["WEB_TEMPLATE"])
js = read(FILES["WEB_JS"])
css = read(FILES["WEB_CSS"])

show_contains("3) TEMPLATE KRİTİK İZLER", tpl, [
    "continue_trip_v99_clean.js",
    "v99-gauge-label",
    "DOLULUK",
    "HIZ",
    "DURUM",
    "v99-gauges",
    "v99m",
    "v99g-{{ trip['id'] }}'id']",
    "}}'id']",
])

show_contains("4) JS BLOK MARKER KONTROL", js, [
    "V99M_OCCUPANCY_PANEL_START",
    "V99M_OCCUPANCY_PANEL_END",
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
    "V99Q_ONLY_OCCUPANCY_CLICK_END",
    "V99U",
    "V99V_DOLULUK_DIRECT_CLICK_START",
    "V99V_DOLULUK_DIRECT_CLICK_END",
    "isDolulukTarget",
    "markDolulukCards",
    "openPanel",
    "closePanel",
    "v99mOccOverlay",
    "MuavinV99OccupancyPanel",
])

show_contains("5) CSS DOLULUK / PANEL İZLERİ", css, [
    "v99m-overlay",
    "v99m-panel",
    "v99m-occ-clickable",
    "pointer-events",
    "z-index",
    "display:none",
    "visibility:hidden",
])

print_lines("6) TEMPLATE SCRIPT SATIRLARI", tpl, [
    "<script",
    "continue_trip_v99_clean.js",
], pad=2)

print_lines("7) TEMPLATE ÜST HIZ/DOLULUK/DURUM BLOĞU", tpl, [
    "v99-gauge",
    "DOLULUK",
    "HIZ",
    "DURUM",
    "liveTopStatusText",
], pad=6)

print_lines("8) JS DOLULUK PANEL BLOĞU VE CLICK HANDLER", js, [
    "V99M_OCCUPANCY_PANEL_START",
    "V99M_OCCUPANCY_PANEL_END",
    "isDolulukTarget",
    "markDolulukCards",
    "document.addEventListener(\"click\"",
    "document.addEventListener('click'",
    "openPanel",
    "v99mOccOverlay",
    "v99m-occ-clickable",
    "MuavinV99OccupancyPanel",
], pad=12)

print_lines("9) JS ONLY DOLULUK / GUARD / ROLLBACK BLOKLARI", js, [
    "V99Q_ONLY_OCCUPANCY_CLICK_START",
    "V99Q_ONLY_OCCUPANCY_CLICK_END",
    "V99U",
    "V99V",
    "isDolulukCard",
    "isForbiddenTopClick",
    "stopImmediatePropagation",
    "preventDefault",
    "capture",
], pad=12)

print_lines("10) CSS PANEL / CLICKABLE SATIRLARI", css, [
    "v99m-overlay",
    "v99m-panel",
    "v99m-occ-clickable",
    "pointer-events",
    "z-index",
], pad=8)

print()
print("===== 11) JS BACKUP DOSYALARI VE İÇİNDEKİ MARKERLAR =====")
backup_files = sorted(
    FILES["WEB_JS"].parent.glob(FILES["WEB_JS"].name + ".bak-*"),
    key=lambda p: p.stat().st_mtime,
    reverse=True
)[:40]

for p in backup_files:
    t = read(p)
    marks = []
    for m in [
        "V99M_OCCUPANCY_PANEL_START",
        "V99Q_ONLY_OCCUPANCY_CLICK_START",
        "V99U",
        "V99V_DOLULUK_DIRECT_CLICK_START",
        "isDolulukTarget",
        "MuavinV99OccupancyPanel",
    ]:
        if m in t:
            marks.append(m)
    print(f"- {p.name} size={p.stat().st_size} sha={sha(p)} markers={marks}")

print()
print("===== 12) RENDER TEST / HTML GERÇEK ÇIKTI =====")
try:
    sys.path.insert(0, str(ROOT))
    from app import app

    out = ROOT / "run_logs" / "v99w_doluluk_click_render.html"
    out.parent.mkdir(exist_ok=True)

    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["auth_ok"] = True

        r = c.get("/continue-trip?v=v99w_xray", follow_redirects=False)
        html = r.get_data().decode("utf-8", errors="ignore")
        out.write_text(html, encoding="utf-8")

        print("STATUS:", r.status_code)
        print("HTML_SIZE:", len(html))
        print("OUT:", out)

        print()
        print("HTML SCRIPT SATIRLARI:")
        for i, line in enumerate(html.splitlines(), 1):
            if "<script" in line and "src=" in line:
                print(f"{i:5}: {line[:260]}")

        print()
        print("HTML ÜST GAUGE SATIRLARI:")
        for i, line in enumerate(html.splitlines(), 1):
            low = line.lower()
            if any(k.lower() in low for k in ["v99-gauge", "DOLULUK", "HIZ", "DURUM", "liveTopStatusText"]):
                print(f"{i:5}: {line[:260]}")

        print()
        print("HTML HATA İZLERİ:")
        for key in ["Traceback", "UndefinedError", "Internal Server Error", "TemplateSyntaxError"]:
            print(("VAR  " if key in html else "YOK  ") + key)

except Exception as e:
    print("RENDER_TEST_HATA:", repr(e))

print()
print("===== 13) KISA YORUM =====")
print("Bu röntgen dosyaya dokunmadı.")
print("Çıktıda özellikle şu üç yere bakacağız:")
print("1) Template script satırı bozulmuş mu?")
print("2) V99M panel bloğu duruyor mu?")
print("3) V99Q/V99U/V99V guard blokları panel clickini engelliyor mu?")

print()
print("===== RAPOR BİTTİ =====")
