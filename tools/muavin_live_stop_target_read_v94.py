from pathlib import Path
import re
from datetime import datetime

ROOT = Path(".").resolve()
OUT = ROOT / "tools" / "reports" / f"live_stop_target_read_v94_{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
OUT.parent.mkdir(parents=True, exist_ok=True)

SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".gradle", "build", "dist",
    ".idea", ".vscode", "tools"
}

EXTS = {".html", ".js", ".css", ".py", ".java"}

TERMS = [
    "liveCurrentStopName",
    "liveDistanceValue",
    "liveEtaValue",
    "liveStopName",
    "live_stop",
    "gps_km",
    "eta_main",
    "eta_sub",
    "Canlı Durak Akışı",
    "Kalan mesafe",
    "Ortahan",
    "Belenyaka",
    "routeCoords",
    "stopDistanceKmByName",
    "distKm",
    "writeRuntime",
    "fetch_live_runtime_state",
    "save_live_runtime_state",
    "live_runtime_state",
]

def rel(p):
    return str(p.relative_to(ROOT))

def good_file(p):
    if not p.is_file():
        return False
    if p.suffix.lower() not in EXTS:
        return False
    if any(part in SKIP_DIRS for part in p.parts):
        return False
    name = p.name.lower()
    if ".bak" in name or "backup" in name or "old" in name or "copy" in name:
        return False
    return True

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def add_context(report, p, term, before=8, after=14):
    txt = read(p)
    lines = txt.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        if term.lower() in line.lower():
            hits.append(i)

    if not hits:
        return

    report.append("")
    report.append(f"--- {rel(p)} | TERM: {term} | hit: {len(hits)} ---")

    used = set()
    for ln in hits[:8]:
        start = max(1, ln - before)
        end = min(len(lines), ln + after)
        key = (start, end)
        if key in used:
            continue
        used.add(key)

        report.append(f"[context {start}-{end}]")
        for no in range(start, end + 1):
            report.append(f"{no}: {lines[no-1][:260]}")
        report.append("")

def main():
    report = []
    report.append("===== LIVE STOP TARGET READ V94 =====")
    report.append(f"ROOT: {ROOT}")
    report.append(f"OUT: {OUT}")
    report.append("NOT: Sadece okuma yapar. Yama yok.")
    report.append("")

    files = [p for p in ROOT.rglob("*") if good_file(p)]

    report.append("===== 1) DOSYA ADI ADAYLARI =====")
    for p in files:
        low = rel(p).lower()
        if any(x in low for x in ["continue", "seat", "route", "live", "stop"]):
            report.append(rel(p))

    report.append("")
    report.append("===== 2) KRİTİK TERİM CONTEXTLERİ =====")
    for p in files:
        txt_low = read(p).lower()
        if not any(t.lower() in txt_low for t in TERMS):
            continue
        for term in TERMS:
            if term.lower() in txt_low:
                add_context(report, p, term)

    report.append("")
    report.append("===== 3) HTML ID / CLASS ÖZETİ =====")
    for p in files:
        if p.suffix.lower() != ".html":
            continue
        txt = read(p)
        found = []
        for m in re.finditer(r'\b(id|class)=["\']([^"\']+)["\']', txt, re.I):
            val = m.group(2)
            low = val.lower()
            if any(x in low for x in ["live", "stop", "durak", "route", "distance", "eta", "current", "next"]):
                ln = txt[:m.start()].count("\n") + 1
                found.append((ln, m.group(1), val))
        if found:
            report.append("")
            report.append(f"--- {rel(p)} ---")
            for ln, attr, val in found[:160]:
                report.append(f"{ln}: {attr}=\"{val}\"")

    report.append("")
    report.append("===== 4) ANDROID / WEB KOPYA DURUMU =====")
    pairs = [
        ("templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"),
        ("static/continue_trip_core.js", "android_app/app/src/main/python/static/continue_trip_core.js"),
        ("static/app.js", "android_app/app/src/main/python/static/app.js"),
        ("templates/seats.html", "android_app/app/src/main/python/templates/seats.html"),
        ("static/seats/seats.js", "android_app/app/src/main/python/static/seats/seats.js"),
    ]

    for a, b in pairs:
        pa = ROOT / a
        pb = ROOT / b
        if not pa.exists() and not pb.exists():
            report.append(f"YOK/YOK: {a} <-> {b}")
        elif not pa.exists():
            report.append(f"WEB YOK: {a} | ANDROID VAR: {b}")
        elif not pb.exists():
            report.append(f"WEB VAR: {a} | ANDROID YOK: {b}")
        else:
            same = read(pa) == read(pb)
            report.append(("AYNI: " if same else "FARKLI: ") + f"{a} <-> {b}")

    OUT.write_text("\n".join(report), encoding="utf-8")

    print("===== RAPOR =====")
    print(OUT)
    print("")
    print("===== İLK 320 SATIR =====")
    print("\n".join(report[:320]))

if __name__ == "__main__":
    main()
