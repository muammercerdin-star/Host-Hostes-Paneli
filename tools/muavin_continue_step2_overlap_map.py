from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
import re
import hashlib

ROOT = Path(".").resolve()
OUT = ROOT / "run_logs" / "continue_step2_overlap_map.txt"
OUT.parent.mkdir(exist_ok=True)

FILES = [
    ROOT / "templates/continue_trip.html",
    ROOT / "static/continue/continue_trip_core.js",
    ROOT / "static/continue/continue_bag_emanet.js",
    ROOT / "static/continue/continue_flow_refresh.js",
    ROOT / "static/continue/continue_trip_ui.js",
    ROOT / "static/continue/continue_refresh_button_v49.js",
    ROOT / "static/continue/continue_native_lock_alarm_v85.js",
    ROOT / "static/continue/continue_trip_v99_clean.js",
    ROOT / "static/continue/continue_speed_final_v105.js",
    ROOT / "static/seats/voice-tts.js",
    ROOT / "static/continue/continue_trip_v99_clean.css",
    ROOT / "static/continue/continue_speed_final_v105.css",
]

KEYWORDS = {
    "HIZ / SPEED": ["speed", "hız", "kmh", "km/sa", "v99SpeedVal", "liveSpeedText"],
    "KM / DISTANCE": ["distance", "mesafe", "gps_km", "ringKm", "liveDistanceValue", "stop-distance-value"],
    "ETA / STATUS": ["eta", "arrival", "varış", "liveEtaValue", "liveTopStatusText", "continueEtaUpdated"],
    "DOLULUK": ["doluluk", "occupancy", "v99m", "passenger_count", "male_count", "female_count"],
    "KOLTUK": ["seat", "koltuk", "seat_no", "live-seat-map", "v99-seat"],
    "BAGAJ / EMANET": ["bagaj", "emanet", "consignment", "cargo", "liveBagaj", "liveEmanet"],
    "CANLI DURAK": ["live_stop", "liveStop", "liveCurrentStopName", "currentStop", "runtime"],
    "TIMELINE": ["timeline", "tlContainer", "v99-tl", "routeBar", "distPct"],
    "SHEET / MODAL": ["sheet", "modal", "overlay", "liveStopSheet", "endTripOverlay"],
    "TTS / SES": ["speak", "tts", "voice", "SeatsSpeak", "anons"],
}

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def rel(p):
    try:
        return str(p.relative_to(ROOT))
    except Exception:
        return str(p)

def lines(p):
    return read(p).splitlines()

def file_kind(p):
    if p.suffix == ".css":
        return "CSS"
    if p.suffix == ".html":
        return "TPL"
    return "JS"

def find_functions(txt):
    out = []
    for i, line in enumerate(txt.splitlines(), 1):
        for pat in [
            r"\bfunction\s+([A-Za-z0-9_$]+)\s*\(",
            r"\b(?:const|let|var)\s+([A-Za-z0-9_$]+)\s*=\s*(?:async\s*)?function\b",
            r"\b(?:const|let|var)\s+([A-Za-z0-9_$]+)\s*=\s*(?:\([^)]*\)|[A-Za-z0-9_$]+)\s*=>",
        ]:
            m = re.search(pat, line)
            if m:
                out.append((m.group(1), i, line.strip()[:200]))
                break
    return out

def find_ids(txt):
    ids = []
    patterns = [
        r"getElementById\(['\"]([^'\"]+)['\"]\)",
        r"querySelector(?:All)?\(['\"]#([^'\"]+)['\"]\)",
        r"\bid=['\"]([^'\"]+)['\"]",
    ]
    for i, line in enumerate(txt.splitlines(), 1):
        for pat in patterns:
            for m in re.finditer(pat, line):
                ids.append((m.group(1), i, line.strip()[:220]))
    return ids

def find_classes(txt):
    out = []
    patterns = [
        r"querySelector(?:All)?\(['\"]\.([^'\" >:]+)",
        r"\.classList\.(?:add|remove|toggle|contains)\(['\"]([^'\"]+)['\"]",
        r"\bclass=['\"]([^'\"]+)['\"]",
    ]
    for i, line in enumerate(txt.splitlines(), 1):
        for pat in patterns:
            for m in re.finditer(pat, line):
                value = m.group(1)
                if " " in value:
                    for c in value.split():
                        out.append((c, i, line.strip()[:220]))
                else:
                    out.append((value, i, line.strip()[:220]))
    return out

def find_api(txt):
    out = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "fetch(" in line or "/api/" in line:
            for m in re.finditer(r"(/api/[A-Za-z0-9_\-/{}`?$&=.:+%#]+)", line):
                out.append((m.group(1), i, line.strip()[:240]))
            if "/api/" in line and not re.search(r"(/api/[A-Za-z0-9_\-/{}`?$&=.:+%#]+)", line):
                out.append(("API_LINE", i, line.strip()[:240]))
    return out

def find_timers(txt):
    out = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "setInterval" in line or "setTimeout" in line or "MutationObserver" in line:
            out.append((i, line.strip()[:240]))
    return out

def find_events(txt):
    out = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "addEventListener" in line:
            m = re.search(r"addEventListener\(['\"]([^'\"]+)['\"]", line)
            ev = m.group(1) if m else "?"
            out.append((ev, i, line.strip()[:220]))
    return out

def keyword_hits(txt):
    low = txt.lower()
    result = {}
    for group, keys in KEYWORDS.items():
        count = 0
        sample = []
        for key in keys:
            c = low.count(key.lower())
            count += c
        if count:
            for i, line in enumerate(txt.splitlines(), 1):
                if any(k.lower() in line.lower() for k in keys):
                    sample.append((i, line.strip()[:180]))
                    if len(sample) >= 6:
                        break
            result[group] = (count, sample)
    return result

report = []
report.append("===== CONTINUE STEP-2 ÇAKIŞMA HARİTASI =====")
report.append("TIME: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
report.append("ROOT: " + str(ROOT))
report.append("NOT: Bu script dosya değiştirmez.")
report.append("")

report.append("===== 1) DOSYA ÖZETİ =====")
for p in FILES:
    txt = read(p)
    report.append(f"{file_kind(p):3} {'VAR' if p.exists() else 'YOK'} lines={len(txt.splitlines()):<5} size={p.stat().st_size if p.exists() else 0:<7} sha={sha(p)} {rel(p)}")

func_map = defaultdict(list)
id_map = defaultdict(list)
class_map = defaultdict(list)
api_map = defaultdict(list)
event_map = defaultdict(list)
timer_map = defaultdict(list)
keyword_map = defaultdict(list)

for p in FILES:
    txt = read(p)
    if not txt:
        continue

    for name, i, line in find_functions(txt):
        func_map[name].append((p, i, line))

    for name, i, line in find_ids(txt):
        id_map[name].append((p, i, line))

    for name, i, line in find_classes(txt):
        class_map[name].append((p, i, line))

    for api, i, line in find_api(txt):
        api_map[api].append((p, i, line))

    for ev, i, line in find_events(txt):
        event_map[ev].append((p, i, line))

    for i, line in find_timers(txt):
        timer_map[rel(p)].append((i, line))

    for group, (count, sample) in keyword_hits(txt).items():
        keyword_map[group].append((p, count, sample))

report.append("")
report.append("===== 2) TEKRAR EDEN FONKSİYON İSİMLERİ =====")
dups = {k:v for k,v in func_map.items() if len(v) > 1}
for name, arr in sorted(dups.items(), key=lambda x: (-len(x[1]), x[0]))[:120]:
    files = ", ".join(f"{rel(p)}:{i}" for p, i, _ in arr[:12])
    report.append(f"{name:<32} count={len(arr):<3} {files}")

report.append("")
report.append("===== 3) AYNI ID'YE DOKUNAN DOSYALAR =====")
for idname, arr in sorted(id_map.items(), key=lambda x: (-len(set(rel(p) for p,_,__ in x[1])), x[0]))[:120]:
    files = sorted(set(rel(p) for p, _, _ in arr))
    if len(files) <= 1 and len(arr) <= 2:
        continue
    report.append(f"#{idname:<32} refs={len(arr):<3} files={len(files)}")
    for p, i, line in arr[:10]:
        report.append(f"  {rel(p)}:{i}: {line}")

report.append("")
report.append("===== 4) AYNI CLASS'A DOKUNAN DOSYALAR =====")
for cname, arr in sorted(class_map.items(), key=lambda x: (-len(set(rel(p) for p,_,__ in x[1])), x[0]))[:100]:
    files = sorted(set(rel(p) for p, _, _ in arr))
    if len(files) <= 1:
        continue
    report.append(f".{cname:<32} refs={len(arr):<3} files={len(files)} -> {', '.join(files[:6])}")

report.append("")
report.append("===== 5) API / FETCH ÇAĞRILARI =====")
for api, arr in sorted(api_map.items(), key=lambda x: (-len(x[1]), x[0])):
    files = sorted(set(rel(p) for p, _, _ in arr))
    report.append(f"{api:<55} refs={len(arr):<3} files={len(files)}")
    for p, i, line in arr[:8]:
        report.append(f"  {rel(p)}:{i}: {line}")

report.append("")
report.append("===== 6) EVENT LISTENER DAĞILIMI =====")
for ev, arr in sorted(event_map.items(), key=lambda x: (-len(x[1]), x[0])):
    report.append(f"{ev:<24} count={len(arr)}")
    for p, i, line in arr[:16]:
        report.append(f"  {rel(p)}:{i}: {line}")

report.append("")
report.append("===== 7) TIMER / OBSERVER DAĞILIMI =====")
for fname, arr in sorted(timer_map.items(), key=lambda x: -len(x[1])):
    report.append(f"{fname:<65} count={len(arr)}")
    for i, line in arr[:20]:
        report.append(f"  {i}: {line}")

report.append("")
report.append("===== 8) GÖREV ALANINA GÖRE DOSYA YOĞUNLUĞU =====")
for group, arr in keyword_map.items():
    report.append("")
    report.append(f"--- {group} ---")
    for p, count, sample in sorted(arr, key=lambda x: -x[1]):
        report.append(f"{rel(p):<60} hits={count}")
        for i, line in sample[:4]:
            report.append(f"  {i}: {line}")

report.append("")
report.append("===== 9) OTOMATİK REFACTOR ÖNERİSİ =====")

report.append("1) continue_trip_core.js çok fazla iş yapıyor: canlı sheet, offload, emanet, GPS, ETA, seat map aynı dosyada.")
report.append("2) continue_trip_v99_clean.js içinde hem görsel sync hem km engine hem doluluk paneli hem koltuk renklendirme var.")
report.append("3) Hız/KM/ETA tarafı core.js + v99_clean.js + flow_refresh.js + v105.js arasında paylaşılıyor. Yeni yama burada çakışma üretir.")
report.append("4) İlk güvenli refactor düzeltme değil, modül çıkarma olmalı: önce bağımsız küçük dosyaları ayırmak.")
report.append("5) En güvenli ilk taşıma adayı: template içindeki end-trip inline script. Çünkü ekran davranışlarından izole.")
report.append("6) İkinci aday: continue_speed_final_v105 zaten ayrı dosya; bu haliyle kalsın, ana dosyaya gömülmesin.")
report.append("7) Üçüncü aday: continue_trip_core.js içindeki canlı sheet/offload/emanet işleri ayrı modüle bölünmeli ama bu daha riskli.")

out = "\n".join(report) + "\n"
print(out)
OUT.write_text(out, encoding="utf-8")
print("✅ Rapor kaydedildi:", OUT)
