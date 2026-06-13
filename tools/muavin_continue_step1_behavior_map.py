from pathlib import Path
from datetime import datetime
import hashlib
import re
from collections import Counter, defaultdict

ROOT = Path(".").resolve()
OUT = ROOT / "run_logs" / "continue_step1_behavior_map.txt"
OUT.parent.mkdir(exist_ok=True)

FILES = [
    ("TPL", "WEB", ROOT / "templates/continue_trip.html"),
    ("TPL", "ANDROID", ROOT / "android_app/app/src/main/python/templates/continue_trip.html"),

    ("CSS", "WEB", ROOT / "static/continue/continue_trip.css"),
    ("CSS", "WEB", ROOT / "static/continue/continue_trip_v99_clean.css"),
    ("CSS", "WEB", ROOT / "static/continue/continue_speed_final_v105.css"),

    ("CSS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css"),
    ("CSS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"),
    ("CSS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.css"),

    ("JS", "WEB", ROOT / "static/continue/continue_trip_core.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_bag_emanet.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_flow_refresh.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_trip_ui.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_refresh_button_v49.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_native_lock_alarm_v85.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_trip_v99_clean.js"),
    ("JS", "WEB", ROOT / "static/continue/continue_speed_final_v105.js"),
    ("JS", "WEB", ROOT / "static/seats/voice-tts.js"),

    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_bag_emanet.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_flow_refresh.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_ui.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_refresh_button_v49.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_native_lock_alarm_v85.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.js"),
    ("JS", "ANDROID", ROOT / "android_app/app/src/main/python/static/seats/voice-tts.js"),
]

PAIRS = [
    ("template", ROOT / "templates/continue_trip.html", ROOT / "android_app/app/src/main/python/templates/continue_trip.html"),
    ("continue_trip.css", ROOT / "static/continue/continue_trip.css", ROOT / "android_app/app/src/main/python/static/continue/continue_trip.css"),
    ("v99 css", ROOT / "static/continue/continue_trip_v99_clean.css", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.css"),
    ("v105 css", ROOT / "static/continue/continue_speed_final_v105.css", ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.css"),
    ("core js", ROOT / "static/continue/continue_trip_core.js", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_core.js"),
    ("bag emanet js", ROOT / "static/continue/continue_bag_emanet.js", ROOT / "android_app/app/src/main/python/static/continue/continue_bag_emanet.js"),
    ("flow refresh js", ROOT / "static/continue/continue_flow_refresh.js", ROOT / "android_app/app/src/main/python/static/continue/continue_flow_refresh.js"),
    ("ui js", ROOT / "static/continue/continue_trip_ui.js", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_ui.js"),
    ("refresh button js", ROOT / "static/continue/continue_refresh_button_v49.js", ROOT / "android_app/app/src/main/python/static/continue/continue_refresh_button_v49.js"),
    ("native alarm js", ROOT / "static/continue/continue_native_lock_alarm_v85.js", ROOT / "android_app/app/src/main/python/static/continue/continue_native_lock_alarm_v85.js"),
    ("v99 js", ROOT / "static/continue/continue_trip_v99_clean.js", ROOT / "android_app/app/src/main/python/static/continue/continue_trip_v99_clean.js"),
    ("v105 js", ROOT / "static/continue/continue_speed_final_v105.js", ROOT / "android_app/app/src/main/python/static/continue/continue_speed_final_v105.js"),
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def lines(p):
    return read(p).splitlines() if p.exists() else []

def nonempty(p):
    return sum(1 for x in lines(p) if x.strip())

def size(p):
    return p.stat().st_size if p.exists() else 0

def section(out, title):
    out.append("")
    out.append("===== " + title + " =====")

def hit_lines(txt, patterns, max_hits=120):
    res = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(re.search(pat, line) for pat in patterns):
            res.append((i, line.rstrip()[:260]))
            if len(res) >= max_hits:
                break
    return res

def find_markers(txt):
    # /* MARKER_START */ veya /* MARKER_END */
    ms = re.findall(r"/\*\s*([A-Z0-9][A-Z0-9_]*(?:START|END|FIX|PATCH|PULSE|CLEAN|BRIDGE|GUARD)[A-Z0-9_]*)\s*\*/", txt)
    return ms

def marker_bases(markers):
    bases = []
    for m in markers:
        b = re.sub(r"_(START|END)$", "", m)
        bases.append(b)
    return bases

def js_summary(path):
    txt = read(path)
    out = []

    out.append(f"FILE: {path}")
    out.append(f"EXISTS: {'YES' if path.exists() else 'NO'} lines={len(txt.splitlines())} nonempty={sum(1 for x in txt.splitlines() if x.strip())} size={size(path)} sha={sha(path)}")

    markers = find_markers(txt)
    base_counts = Counter(marker_bases(markers))

    out.append(f"markers={len(markers)} unique_marker_bases={len(base_counts)}")
    for b, c in base_counts.most_common(60):
      out.append(f"  MARKER {b} count={c}")

    funcs = []
    for i, line in enumerate(txt.splitlines(), 1):
        m = re.search(r"\bfunction\s+([A-Za-z0-9_$]+)\s*\(", line)
        if m:
            funcs.append((i, m.group(1), line.strip()[:180]))
            continue
        m = re.search(r"\b(?:const|let|var)\s+([A-Za-z0-9_$]+)\s*=\s*(?:async\s*)?function\b", line)
        if m:
            funcs.append((i, m.group(1), line.strip()[:180]))
            continue
        m = re.search(r"\b(?:const|let|var)\s+([A-Za-z0-9_$]+)\s*=\s*(?:\([^)]*\)|[A-Za-z0-9_$]+)\s*=>", line)
        if m:
            funcs.append((i, m.group(1), line.strip()[:180]))

    out.append(f"functions_detected={len(funcs)}")
    for i, name, line in funcs[:120]:
        out.append(f"  FN {i}: {name} :: {line}")
    if len(funcs) > 120:
        out.append("  ... functions kesildi")

    listeners = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "addEventListener" in line:
            listeners.append((i, line.strip()[:220]))
    out.append(f"event_listeners={len(listeners)}")
    for i, line in listeners[:120]:
        out.append(f"  EVT {i}: {line}")
    if len(listeners) > 120:
        out.append("  ... event listeners kesildi")

    globals_ = []
    for i, line in enumerate(txt.splitlines(), 1):
        if re.search(r"\bwindow\.[A-Za-z0-9_$]+\s*=", line):
            globals_.append((i, line.strip()[:220]))
    out.append(f"window_globals={len(globals_)}")
    for i, line in globals_[:80]:
        out.append(f"  WIN {i}: {line}")

    storage = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "localStorage" in line or "sessionStorage" in line:
            storage.append((i, line.strip()[:220]))
    out.append(f"storage_lines={len(storage)}")
    for i, line in storage[:120]:
        out.append(f"  STO {i}: {line}")
    if len(storage) > 120:
        out.append("  ... storage kesildi")

    fetches = []
    for i, line in enumerate(txt.splitlines(), 1):
        if "fetch(" in line or "XMLHttpRequest" in line or "/api/" in line:
            fetches.append((i, line.strip()[:240]))
    out.append(f"api_fetch_lines={len(fetches)}")
    for i, line in fetches[:120]:
        out.append(f"  API {i}: {line}")
    if len(fetches) > 120:
        out.append("  ... api kesildi")

    risky = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(x in line for x in ["stopImmediatePropagation", "preventDefault", "setInterval", "setTimeout", "MutationObserver", "location.reload", "innerHTML"]):
            risky.append((i, line.strip()[:240]))
    out.append(f"risk_attention_lines={len(risky)}")
    for i, line in risky[:140]:
        out.append(f"  RISK {i}: {line}")
    if len(risky) > 140:
        out.append("  ... risk kesildi")

    ids = Counter()
    classes = Counter()
    for m in re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", txt):
        ids[m] += 1
    for m in re.findall(r"querySelector(?:All)?\(['\"]#([^'\"]+)['\"]\)", txt):
        ids[m] += 1
    for m in re.findall(r"\.classList\.(?:add|remove|toggle|contains)\(['\"]([^'\"]+)['\"]", txt):
        classes[m] += 1

    out.append(f"dom_id_refs={len(ids)}")
    for k, c in ids.most_common(60):
        out.append(f"  IDREF #{k} count={c}")

    out.append(f"classList_refs={len(classes)}")
    for k, c in classes.most_common(60):
        out.append(f"  CLASS {k} count={c}")

    return out

def css_summary(path):
    txt = read(path)
    out = []
    out.append(f"FILE: {path}")
    out.append(f"EXISTS: {'YES' if path.exists() else 'NO'} lines={len(txt.splitlines())} nonempty={sum(1 for x in txt.splitlines() if x.strip())} size={size(path)} sha={sha(path)}")

    markers = find_markers(txt)
    base_counts = Counter(marker_bases(markers))
    out.append(f"markers={len(markers)} unique_marker_bases={len(base_counts)}")
    for b, c in base_counts.most_common(80):
        out.append(f"  MARKER {b} count={c}")

    out.append(f"important_count={txt.count('!important')}")
    out.append(f"media_queries={txt.count('@media')}")
    out.append(f"keyframes={txt.count('@keyframes')}")

    selectors = []
    for i, line in enumerate(txt.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("/*") or s.startswith("*") or s.startswith("@"):
            continue
        if "{" in s:
            selectors.append((i, s[:220]))
    out.append(f"selectors_approx={len(selectors)}")
    for i, line in selectors[:160]:
        out.append(f"  SEL {i}: {line}")
    if len(selectors) > 160:
        out.append("  ... selectors kesildi")

    risky = []
    for i, line in enumerate(txt.splitlines(), 1):
        if any(x in line for x in ["position:fixed", "z-index", "pointer-events", "overflow:hidden", "display:none", "!important"]):
            risky.append((i, line.strip()[:220]))
    out.append(f"css_attention_lines={len(risky)}")
    for i, line in risky[:160]:
        out.append(f"  CSSRISK {i}: {line}")
    if len(risky) > 160:
        out.append("  ... css risk kesildi")

    return out

def template_summary(path):
    txt = read(path)
    out = []
    out.append(f"FILE: {path}")
    out.append(f"EXISTS: {'YES' if path.exists() else 'NO'} lines={len(txt.splitlines())} nonempty={sum(1 for x in txt.splitlines() if x.strip())} size={size(path)} sha={sha(path)}")

    ids = re.findall(r'\bid=["\']([^"\']+)["\']', txt)
    dup_ids = [k for k, c in Counter(ids).items() if c > 1]

    out.append(f"html_ids={len(ids)} duplicate_ids={len(dup_ids)}")
    for d in dup_ids:
        out.append(f"  DUP_ID {d} count={Counter(ids)[d]}")

    out.append(f"jinja_vars={txt.count('{{')} jinja_blocks={txt.count('{%')}")
    out.append(f"inline_scripts={len(re.findall(r'<script(?![^>]+src=)', txt))}")

    out.append("CSS/JS ORDER:")
    for i, line in enumerate(txt.splitlines(), 1):
        if "<link " in line or "<script" in line:
            out.append(f"  {i}: {line.strip()[:260]}")

    out.append("IMPORTANT BLOCK LINES:")
    for needle in [
        "v99-gauges",
        "v99SpeedVal",
        "DOLULUK",
        "liveCurrentCard",
        "tlContainer",
        "endTripForm",
        "continue-boot-data",
        "CONTINUE_BOOT",
        "continue_trip_v99_clean.js",
        "continue_speed_final_v105.js",
    ]:
        found = []
        for i, line in enumerate(txt.splitlines(), 1):
            if needle in line:
                found.append(i)
        out.append(f"  {needle:<34} lines={found[:20]}")

    return out

def app_route_summary():
    app = ROOT / "app.py"
    txt = read(app)
    out = []
    out.append(f"FILE: {app}")
    out.append(f"EXISTS: {'YES' if app.exists() else 'NO'} lines={len(txt.splitlines())} size={size(app)} sha={sha(app)}")

    lines_ = txt.splitlines()

    # def continue_trip block rough range
    starts = []
    for i, line in enumerate(lines_, 1):
        if re.match(r"\s*def\s+continue_trip\s*\(", line):
            starts.append(i)

    for s in starts:
        e = len(lines_)
        for j in range(s + 1, len(lines_) + 1):
            if re.match(r"^\s*@app\.route|^\s*def\s+[A-Za-z0-9_]+\s*\(", lines_[j-1]) and j > s + 3:
                e = j - 1
                break
        out.append(f"continue_trip function approx: {s}-{e} lines={e-s+1}")

        for i in range(s, min(e, s + 260) + 1):
            line = lines_[i-1]
            if any(k in line for k in [
                "live_runtime", "live_summary", "live_stops", "render_template",
                "continue_route_coords", "continue_schedule_items",
                "live_current", "trip", "stops", "bagaj", "emanet"
            ]):
                out.append(f"  APP {i}: {line.strip()[:260]}")

    # route/API summary
    out.append("ROUTES/API containing live/continue:")
    for i, line in enumerate(lines_, 1):
        if "@app.route" in line and any(k in line for k in ["continue", "live", "runtime", "bagaj", "emanet"]):
            out.append(f"  ROUTE {i}: {line.strip()[:260]}")
        elif "def api_live" in line or "def continue" in line:
            out.append(f"  DEF {i}: {line.strip()[:260]}")

    return out

report = []
report.append("===== MUAVİN CONTINUE STEP-1 DAVRANIŞ HARİTASI =====")
report.append("TIME: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
report.append("ROOT: " + str(ROOT))
report.append("NOT: Bu script dosya değiştirmez.")
report.append("")

section(report, "1) DOSYA BOYUTLARI")
total = 0
for kind, side, p in FILES:
    l = len(lines(p))
    total += l if side == "WEB" else 0
    report.append(f"{kind:3} {side:7} {'VAR' if p.exists() else 'YOK'} lines={l:<5} nonempty={nonempty(p):<5} size={size(p):<7} sha={sha(p)} {p}")

report.append("")
report.append(f"WEB tarafı yaklaşık toplam satır: {total}")

section(report, "2) WEB / ANDROID SENKRON")
for name, web, android in PAIRS:
    ok = web.exists() and android.exists() and sha(web) == sha(android)
    report.append(f"{name:<22} {'AYNI ✅' if ok else 'FARKLI/YOK ❌'} web={sha(web)} android={sha(android)}")

section(report, "3) TEMPLATE HARİTASI")
report.extend(template_summary(ROOT / "templates/continue_trip.html"))

section(report, "4) JS HARİTALARI")
for kind, side, p in FILES:
    if kind == "JS" and side == "WEB":
        report.append("")
        report.append("----- JS MAP: " + p.name + " -----")
        report.extend(js_summary(p))

section(report, "5) CSS HARİTALARI")
for kind, side, p in FILES:
    if kind == "CSS" and side == "WEB":
        report.append("")
        report.append("----- CSS MAP: " + p.name + " -----")
        report.extend(css_summary(p))

section(report, "6) APP.PY CONTINUE ROUTE HARİTASI")
report.extend(app_route_summary())

section(report, "7) KISA SONUÇ")
report.append("Bu rapor düzeltme yapmadı.")
report.append("Bir sonraki adımda bu rapora göre core/v99/js/css modülleme planı çıkarılmalı.")
report.append("Öncelik: continue_trip_core.js ve continue_trip_v99_clean.js içindeki event/localStorage/API görevlerini ayırmak.")

out = "\n".join(report) + "\n"
print(out)
OUT.write_text(out, encoding="utf-8")
print("✅ Rapor kaydedildi:", OUT)
