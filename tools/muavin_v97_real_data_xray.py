from pathlib import Path
from datetime import datetime
import re
import json
import hashlib

ROOT = Path(".").resolve()
OUT = ROOT / "tools" / "reports" / f"v97_real_data_xray_{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
OUT.parent.mkdir(parents=True, exist_ok=True)

TARGETS = [
    "app.py",
    "templates/continue_trip.html",
    "static/continue/continue_trip_core.js",
    "static/continue/continue_trip_ui.js",
    "static/continue/continue_bag_emanet.js",
    "static/continue/continue_flow_refresh.js",
    "static/continue/v97_proximity_preview.html",
    "static/continue/v97_proximity_preview.css",
    "static/continue/v97_proximity_preview.js",

    "android_app/app/src/main/python/app.py",
    "android_app/app/src/main/python/templates/continue_trip.html",
    "android_app/app/src/main/python/static/continue/continue_trip_core.js",
    "android_app/app/src/main/python/static/continue/continue_trip_ui.js",
    "android_app/app/src/main/python/static/continue/v97_proximity_preview.html",
    "android_app/app/src/main/python/static/continue/v97_proximity_preview.css",
    "android_app/app/src/main/python/static/continue/v97_proximity_preview.js",
]

TERMS = [
    "window.CONTINUE_BOOT",
    "runtimeGpsKm",
    "runtimeSpeed",
    "runtimeStop",
    "runtimeEta",
    "routeStops",
    "routeCoords",
    "scheduleItems",
    "live_summary",
    "live_current",
    "live_stops",
    "live_runtime",
    "liveCurrentStopName",
    "liveDistanceValue",
    "liveEtaValue",
    "liveOffloadCount",
    "liveBagajCount",
    "liveEmanetCount",
    "liveSpeedText",
    "liveClockText",
    "liveTopStatusText",
    "stop-distance-value",
    "updateAllDistances",
    "writeRuntime",
    "compute()",
    "function compute",
    "setText(\"#liveDistanceValue",
    "fetch(`/api/live-runtime-state",
    "/api/live-runtime-state",
    "/api/live-stop-detail",
    "/api/live-stop-summary",
    "continue_route_coords",
    "continue_schedule_items",
    "fetch_live_runtime_state",
    "upsert_live_runtime_state",
    "route_stop_coords",
    "route_segments",
    "get_stops",
    "STOPS =",
    "const STOPS",
    "setRing",
    "simKm",
    "buildTimeline",
]

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]

def section(out, title):
    out.append("")
    out.append("===== " + title + " =====")

def context(out, p: Path, term: str, before=8, after=12, limit=10):
    if not p.exists():
        return
    txt = read(p)
    low = txt.lower()
    t = term.lower()
    if t not in low:
        return

    lines = txt.splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        if t in line.lower():
            hits.append(i)

    out.append("")
    out.append(f"--- {rel(p)} | TERM: {term} | hit: {len(hits)} ---")

    used = set()
    for ln in hits[:limit]:
        a = max(1, ln - before)
        b = min(len(lines), ln + after)
        key = (a, b)
        if key in used:
            continue
        used.add(key)

        out.append(f"[context {a}-{b}]")
        for no in range(a, b + 1):
            out.append(f"{no}: {lines[no-1][:260]}")
        out.append("")

def extract_ids_classes(txt):
    found = []
    for m in re.finditer(r'\b(id|class)=["\']([^"\']+)["\']', txt, re.I):
        attr = m.group(1)
        val = m.group(2)
        low = val.lower()
        if any(x in low for x in [
            "v97", "live", "stop", "durak", "route", "distance", "eta",
            "speed", "clock", "bagaj", "emanet", "offload", "timeline",
            "ring", "prox", "gauge", "dock"
        ]):
            ln = txt[:m.start()].count("\n") + 1
            found.append((ln, attr, val))
    return found

def extract_boot_keys(txt):
    m = re.search(r'window\.CONTINUE_BOOT\s*=\s*\{([\s\S]*?)\};', txt)
    if not m:
        return []
    body = m.group(1)
    keys = []
    for km in re.finditer(r'^\s*([A-Za-z0-9_]+)\s*:', body, re.M):
        keys.append((body[:km.start()].count("\n") + 1, km.group(1)))
    return keys

def find_script_links(txt):
    rows = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "<script" in line or "<link" in line:
            if "continue" in line or "v97" in line or "css" in line or "js" in line:
                rows.append((i, line.strip()[:260]))
    return rows

def same_file(a, b):
    pa = ROOT / a
    pb = ROOT / b
    if not pa.exists() and not pb.exists():
        return "YOK/YOK"
    if not pa.exists():
        return "WEB YOK / ANDROID VAR"
    if not pb.exists():
        return "WEB VAR / ANDROID YOK"
    return "AYNI" if read(pa) == read(pb) else "FARKLI"

def main():
    out = []
    out.append("===== V97 GERÇEK VERİ BAĞLAMA RÖNTGENİ =====")
    out.append(f"ROOT: {ROOT}")
    out.append(f"OUT: {OUT}")
    out.append("NOT: Bu script sadece okuma/rapor yapar. Dosya değiştirmez.")
    out.append("")

    section(out, "1) HEDEF DOSYA VAR/YOK + HASH")
    for t in TARGETS:
        p = ROOT / t
        if p.exists():
            out.append(f"VAR  {t} | size={p.stat().st_size} | sha={sha(p)}")
        else:
            out.append(f"YOK  {t}")

    section(out, "2) WEB / ANDROID KOPYA DURUMU")
    pairs = [
        ("app.py", "android_app/app/src/main/python/app.py"),
        ("templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"),
        ("static/continue/continue_trip_core.js", "android_app/app/src/main/python/static/continue/continue_trip_core.js"),
        ("static/continue/continue_trip_ui.js", "android_app/app/src/main/python/static/continue/continue_trip_ui.js"),
        ("static/continue/v97_proximity_preview.html", "android_app/app/src/main/python/static/continue/v97_proximity_preview.html"),
        ("static/continue/v97_proximity_preview.css", "android_app/app/src/main/python/static/continue/v97_proximity_preview.css"),
        ("static/continue/v97_proximity_preview.js", "android_app/app/src/main/python/static/continue/v97_proximity_preview.js"),
    ]
    for a, b in pairs:
        out.append(f"{same_file(a,b):<24} {a} <-> {b}")

    section(out, "3) CONTINUE TEMPLATE YÜKLEME SIRASI")
    for t in ["templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"]:
        p = ROOT / t
        out.append("")
        out.append(f"--- {t} ---")
        if not p.exists():
            out.append("YOK")
            continue
        for ln, line in find_script_links(read(p)):
            out.append(f"{ln}: {line}")

    section(out, "4) CONTINUE_BOOT ANAHTARLARI")
    for t in ["templates/continue_trip.html", "android_app/app/src/main/python/templates/continue_trip.html"]:
        p = ROOT / t
        out.append("")
        out.append(f"--- {t} ---")
        if not p.exists():
            out.append("YOK")
            continue
        keys = extract_boot_keys(read(p))
        if not keys:
            out.append("CONTINUE_BOOT bulunamadı")
        else:
            for ln, key in keys:
                out.append(f"{ln}: {key}")

    section(out, "5) HTML ID / CLASS RÖNTGENİ")
    for t in [
        "templates/continue_trip.html",
        "static/continue/v97_proximity_preview.html",
        "android_app/app/src/main/python/templates/continue_trip.html",
        "android_app/app/src/main/python/static/continue/v97_proximity_preview.html",
    ]:
        p = ROOT / t
        out.append("")
        out.append(f"--- {t} ---")
        if not p.exists():
            out.append("YOK")
            continue
        found = extract_ids_classes(read(p))
        if not found:
            out.append("ilgili id/class bulunamadı")
        else:
            for ln, attr, val in found[:220]:
                out.append(f"{ln}: {attr}=\"{val}\"")

    section(out, "6) KRİTİK TERİM CONTEXTLERİ")
    for t in TARGETS:
        p = ROOT / t
        if not p.exists():
            continue
        txt_low = read(p).lower()
        if not any(term.lower() in txt_low for term in TERMS):
            continue
        for term in TERMS:
            if term.lower() in txt_low:
                context(out, p, term)

    section(out, "7) V97 DEMO VERİLERİ NEREDE SERT KODLU?")
    for t in ["static/continue/v97_proximity_preview.html", "static/continue/v97_proximity_preview.js"]:
        p = ROOT / t
        out.append("")
        out.append(f"--- {t} ---")
        if not p.exists():
            out.append("YOK")
            continue
        txt = read(p)
        for pat in [
            "DENİZLİ", "İSTANBUL", "45KH999", "38/45", "Uşak",
            "14:45", "const STOPS", "startKm", "currentKm", "simKm",
            "offloadCount", "bagajCount"
        ]:
            hits = []
            for i, line in enumerate(txt.splitlines(), 1):
                if pat in line:
                    hits.append((i, line.strip()[:220]))
            if hits:
                out.append(f"PATTERN: {pat}")
                for ln, line in hits[:20]:
                    out.append(f"  {ln}: {line}")

    section(out, "8) GERÇEK VERİ BAĞLAMA HARİTASI TASLAK")
    mapping = [
        ("V97 route başlığı", "trip['route']", "templates/continue_trip.html içindeki trip route"),
        ("V97 plaka", "trip['plate']", "templates/continue_trip.html / CONTINUE_BOOT tripKey"),
        ("V97 saat", "liveClockText veya JS Date", "mevcut core saat motoru"),
        ("V97 hız", "#liveSpeedText", "continue_trip_core.js speed engine"),
        ("V97 doluluk", "live_summary.passenger_count / total_seats", "app.py continue sayfası context"),
        ("V97 durum", "#liveTopStatusText veya #liveEtaValue", "continue_trip_ui.js syncV2Texts"),
        ("V97 canlı durak adı", "#liveCurrentStopName", "live_runtime.live_stop / live_current.name"),
        ("V97 km halkası", "#liveDistanceValue", "live_runtime.gps_km veya GPS compute sonucu"),
        ("V97 ETA", "#liveEtaValue", "live_runtime.eta_main / live_current.eta"),
        ("V97 inecek", "#liveOffloadCount", "live_current.off_count"),
        ("V97 bagaj", "#liveBagajCount + #liveEmanetCount", "live_current.bagaj_count / emanet"),
        ("V97 timeline", "live_stops[1:] veya CONTINUE_BOOT.routeStops + scheduleItems", "template/app.py context"),
        ("V97 route progress", "routeIndex canlı durak / routeStops length", "JS tarafında hesaplanabilir"),
    ]
    for a, b, c in mapping:
        out.append(f"- {a} <= {b} | kaynak: {c}")

    section(out, "9) SONUÇ / RİSK NOTU")
    out.append("- V97 preview şu an statik HTML/JS. Jinja değişkenlerini doğrudan okuyamaz.")
    out.append("- Gerçek veri için en temiz yol: continue_trip.html içine V97 layout bloğu eklemek veya ?ui=v97 ile alternatif template/branch açmak.")
    out.append("- Mevcut sağlam canlı durak korunacaksa ilk entegrasyon feature flag ile yapılmalı: /continue?ui=v97")
    out.append("- Core GPS motoru zaten #liveCurrentStopName, #liveDistanceValue, #liveEtaValue id'lerine yazıyor; V97 aynı id'leri kullanırsa gerçek zamanlı güncelleme daha az riskli olur.")
    out.append("- Android kopyalar FARKLI çıkarsa entegrasyon sonrası mutlaka sync gerekir.")

    OUT.write_text("\n".join(out), encoding="utf-8")

    print("===== RAPOR =====")
    print(OUT)
    print()
    print("===== İLK 260 SATIR =====")
    print("\n".join(out[:260]))

if __name__ == "__main__":
    main()
