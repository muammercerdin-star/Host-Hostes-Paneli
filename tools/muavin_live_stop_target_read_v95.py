from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
OUT = ROOT / "tools" / "reports" / f"live_stop_target_read_v95_{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
OUT.parent.mkdir(parents=True, exist_ok=True)

WEB_FILES = [
    "app.py",
    "templates/continue_trip.html",
    "static/continue/continue_trip.css",
    "static/continue/continue_trip_ui.js",
    "static/continue/continue_trip_core.js",
    "static/continue/continue_bag_emanet.js",
    "static/continue/continue_flow_refresh.js",
    "static/continue/continue_live_diagnostics.js",
    "static/continue/continue_refresh_button_v49.js",
    "static/continue/continue_industrial_v75.css",
    "static/continue/continue_ring_v75.js",
    "static/continue/continue_v76.css",
    "static/continue/continue_v76.js",
    "static/continue/continue_voice_alert_v81.js",
    "static/continue/continue_native_lock_alarm_v85.js",
]

for p in sorted((ROOT / "static/continue/css_parts").glob("*.css")):
    WEB_FILES.append(str(p.relative_to(ROOT)))

ANDROID_FILES = []
for f in WEB_FILES:
    if f == "app.py":
        ANDROID_FILES.append("android_app/app/src/main/python/app.py")
    elif f.startswith("templates/"):
        ANDROID_FILES.append("android_app/app/src/main/python/" + f)
    elif f.startswith("static/"):
        ANDROID_FILES.append("android_app/app/src/main/python/" + f)

TARGETS = WEB_FILES + ANDROID_FILES

TERMS = [
    "Canlı Durak Akışı",
    "liveCurrentStopName",
    "liveDistanceValue",
    "liveEtaValue",
    "liveStopName",
    "currentStop",
    "nextStop",
    "stopDistanceKmByName",
    "distKm",
    "formatKm",
    "gps_km",
    "eta_main",
    "eta_sub",
    "writeRuntime",
    "syncRuntime",
    "fetchRuntime",
    "routeCoords",
    "setText",
    "Kalan mesafe",
    "Ortahan",
    "Belenyaka",
]

CSS_TERMS = [
    "live",
    "stop",
    "current",
    "next",
    "card",
    "border",
    "box-shadow",
    "glow",
    "pulse",
    "animation",
    "keyframes",
    "conic-gradient",
]

def read(path):
    return path.read_text(encoding="utf-8", errors="ignore")

def exists(rel):
    return (ROOT / rel).exists()

def add(report, s=""):
    report.append(s)

def context(report, rel, term, before=8, after=14):
    p = ROOT / rel
    if not p.exists():
        return

    txt = read(p)
    lines = txt.splitlines()
    hits = []

    for i, line in enumerate(lines, 1):
        if term.lower() in line.lower():
            hits.append(i)

    if not hits:
        return

    add(report)
    add(report, f"--- {rel} | TERM: {term} | hit: {len(hits)} ---")

    used = set()
    for ln in hits[:10]:
        start = max(1, ln - before)
        end = min(len(lines), ln + after)
        key = (start, end)
        if key in used:
            continue
        used.add(key)

        add(report, f"[context {start}-{end}]")
        for no in range(start, end + 1):
            add(report, f"{no}: {lines[no-1][:280]}")
        add(report)

def main():
    report = []
    add(report, "===== LIVE STOP TARGET READ V95 =====")
    add(report, f"ROOT: {ROOT}")
    add(report, f"OUT: {OUT}")
    add(report, "NOT: Sadece aktif canlı durak dosyalarını okur. Yama yok.")
    add(report)

    add(report, "===== 1) HEDEF DOSYA VAR/YOK =====")
    for rel in TARGETS:
        add(report, ("VAR: " if exists(rel) else "YOK: ") + rel)

    add(report)
    add(report, "===== 2) CONTINUE TEMPLATE YÜKLEME SIRASI =====")
    for rel in ["templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"]:
        p = ROOT / rel
        if not p.exists():
            continue
        add(report)
        add(report, f"--- {rel} ---")
        lines = read(p).splitlines()
        for i, line in enumerate(lines, 1):
            if "static/continue" in line or "continue_" in line or "css_parts" in line:
                add(report, f"{i}: {line[:280]}")

    add(report)
    add(report, "===== 3) HTML / JS KRİTİK CONTEXT =====")
    for rel in TARGETS:
        if not exists(rel):
            continue
        if not rel.endswith((".html", ".js", ".py", ".java")):
            continue
        txt = read(ROOT / rel).lower()
        if not any(t.lower() in txt for t in TERMS):
            continue
        for term in TERMS:
            if term.lower() in txt:
                context(report, rel, term)

    add(report)
    add(report, "===== 4) CSS CANLI KART / BORDER / GLOW CONTEXT =====")
    for rel in TARGETS:
        if not exists(rel):
            continue
        if not rel.endswith(".css"):
            continue

        txt = read(ROOT / rel)
        lines = txt.splitlines()

        hits = []
        for i, line in enumerate(lines, 1):
            low = line.lower()
            if any(t in low for t in CSS_TERMS):
                # sadece canlı durakla ilişkili görünen CSS'i öne al
                window = "\n".join(lines[max(0, i-5):min(len(lines), i+8)]).lower()
                if any(x in window for x in ["live", "stop", "current", "next", "route", "eta", "distance"]):
                    hits.append(i)

        if not hits:
            continue

        add(report)
        add(report, f"--- {rel} | css hit: {len(hits)} ---")

        used = set()
        for ln in hits[:18]:
            start = max(1, ln - 6)
            end = min(len(lines), ln + 10)
            key = (start, end)
            if key in used:
                continue
            used.add(key)

            add(report, f"[context {start}-{end}]")
            for no in range(start, end + 1):
                add(report, f"{no}: {lines[no-1][:280]}")
            add(report)

    add(report)
    add(report, "===== 5) WEB / ANDROID KOPYA KARŞILAŞTIRMA =====")
    for web in WEB_FILES:
        if web == "app.py":
            android = "android_app/app/src/main/python/app.py"
        elif web.startswith("templates/"):
            android = "android_app/app/src/main/python/" + web
        elif web.startswith("static/"):
            android = "android_app/app/src/main/python/" + web
        else:
            continue

        wp = ROOT / web
        ap = ROOT / android

        if not wp.exists() and not ap.exists():
            add(report, f"YOK/YOK: {web} <-> {android}")
        elif not wp.exists():
            add(report, f"WEB YOK / ANDROID VAR: {web} <-> {android}")
        elif not ap.exists():
            add(report, f"WEB VAR / ANDROID YOK: {web} <-> {android}")
        else:
            add(report, ("AYNI: " if read(wp) == read(ap) else "FARKLI: ") + f"{web} <-> {android}")

    OUT.write_text("\n".join(report), encoding="utf-8")

    print("===== RAPOR =====")
    print(OUT)
    print()
    print("===== ÖZET İLK 260 SATIR =====")
    print("\n".join(report[:260]))

if __name__ == "__main__":
    main()
