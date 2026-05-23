from pathlib import Path
import re

ROOT = Path(".").resolve()

def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except Exception:
        return str(p)

def read(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def line_no(text, idx):
    return text.count("\n", 0, idx) + 1

def print_head(title):
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)

def print_file_lines(path, start=1, end=None):
    if not path.exists():
        print(f"{rel(path)} yok")
        return
    lines = read(path).splitlines()
    if end is None:
        end = len(lines)
    end = min(end, len(lines))
    print(f"\n--- {rel(path)} | satır {start}-{end} ---")
    for i in range(start, end + 1):
        print(f"{i:5d}: {lines[i-1]}")

def extract_function(path, func_name):
    if not path.exists():
        return
    text = read(path)
    marker = f"function {func_name}"
    start = text.find(marker)
    if start < 0:
        print(f"\n--- {rel(path)} | {func_name} bulunamadı ---")
        return

    brace = text.find("{", start)
    if brace < 0:
        print(f"\n--- {rel(path)} | {func_name} gövde başlangıcı bulunamadı ---")
        return

    depth = 0
    end = None
    for i in range(brace, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    if end is None:
        end = min(len(text), start + 12000)

    start_ln = line_no(text, start)
    end_ln = line_no(text, end)
    lines = text.splitlines()

    print(f"\n--- {rel(path)} | {func_name}() | satır {start_ln}-{end_ln} ---")
    for i in range(start_ln, end_ln + 1):
        print(f"{i:5d}: {lines[i-1]}")

def css_links_from_seats():
    seats = Path("templates/seats.html")
    if not seats.exists():
        return []
    text = read(seats)
    rx = re.compile(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*>', re.I)
    out = []
    for m in rx.finditer(text):
        href = m.group(1)
        clean = href.split("?")[0].split("#")[0]
        if clean.startswith("/"):
            clean = clean[1:]
        if clean.startswith("static/"):
            p = Path(clean)
            if p.exists():
                out.append(p)
    return out

def collect_tokens_from_html(path):
    text = read(path) if path.exists() else ""
    ids = sorted(set(re.findall(r'id=["\']([^"\']+)["\']', text)))
    classes = []
    for cls in re.findall(r'class=["\']([^"\']+)["\']', text):
        for c in cls.split():
            c = c.strip()
            if c:
                classes.append(c)
    classes = sorted(set(classes))
    return ids, classes

def show_css_hits(css_paths, ids, classes):
    selectors = []
    for x in ids:
        selectors.append("#" + x)
    for x in classes:
        if len(x) >= 3:
            selectors.append("." + x)

    extra = [
        "route-flow", "routeFlow", "stop-flow", "route-stop", "stop-card",
        "live-stop", "current-stop", "next-stop", "timeline", "passed",
        "selected", "active", "live", "next", "waiting", "bag", "metric",
        "eta", "plan", "distance", "flow"
    ]

    print_head("3) CSS içinde route_flow seçicilerini kim eziyor?")

    for p in css_paths:
        text = read(p)
        lines = text.splitlines()
        hits = []

        for i, line in enumerate(lines, 1):
            low = line.lower()
            ok = False

            for s in selectors:
                if s.lower() in low:
                    ok = True
                    break

            if not ok:
                for e in extra:
                    if e.lower() in low:
                        ok = True
                        break

            if ok:
                hits.append(i)

        if not hits:
            continue

        print(f"\n--- {rel(p)} | eşleşme: {len(hits)} ---")
        shown = set()
        for ln in hits[:160]:
            a = max(1, ln - 2)
            b = min(len(lines), ln + 5)
            key = (a, b)
            if key in shown:
                continue
            shown.add(key)
            print(f"\n[Satır {ln} civarı]")
            for j in range(a, b + 1):
                print(f"{j:5d}: {lines[j-1]}")
        if len(hits) > 160:
            print(f"\n... {len(hits)-160} eşleşme daha var.")

def show_inline_style_hits():
    seats = Path("templates/seats.html")
    if not seats.exists():
        return
    text = read(seats)
    style_rx = re.compile(r'<style\b([^>]*)>(.*?)</style>', re.I | re.S)

    print_head("4) seats.html inline style bloklarında route flow etkisi var mı?")

    for m in style_rx.finditer(text):
        attrs = m.group(1) or ""
        body = m.group(2) or ""
        start_ln = line_no(text, m.start())
        idm = re.search(r'id=["\']([^"\']+)["\']', attrs, re.I)
        sid = idm.group(1) if idm else "-"

        terms = [
            "route-flow", "routeFlow", "stop-flow", "route-stop",
            "live", "next", "bag", "metric", "timeline", "flow"
        ]

        if not any(t.lower() in body.lower() for t in terms):
            print(f"{start_ln:5d}: style id={sid} -> route flow ile ilgili görünmüyor")
            continue

        print(f"\n--- style id={sid} | başlangıç satırı {start_ln} ---")
        body_lines = body.splitlines()
        for i, line in enumerate(body_lines, 1):
            if any(t.lower() in line.lower() for t in terms):
                a = max(1, i - 2)
                b = min(len(body_lines), i + 5)
                print(f"\n[Satır {start_ln+i} civarı]")
                for j in range(a, b + 1):
                    print(f"{start_ln+j:5d}: {body_lines[j-1]}")

def show_js_dom_hits():
    js = Path("static/seats/seats.js")
    if not js.exists():
        return
    text = read(js)
    lines = text.splitlines()

    terms = [
        "routeFlow", "renderRouteStrip", "route-strip", "route-stop",
        "stopDistanceKmByName", "computeNextStopName",
        "liveStopOperationCount", "liveStopBag", "bag",
        "planMap", "etaItems", "getDisplayLiveStop"
    ]

    print_head("5) seats.js içinde route flow DOM / veri bağlantıları")

    hits = []
    for i, line in enumerate(lines, 1):
        if any(t in line for t in terms):
            hits.append(i)

    for ln in hits[:220]:
        print(f"{ln:5d}: {lines[ln-1]}")
    if len(hits) > 220:
        print(f"... {len(hits)-220} satır daha var.")

route_flow = Path("templates/seats_parts/route_flow.html")
seats_js = Path("static/seats/seats.js")
css_paths = css_links_from_seats()

print_head("1) route_flow.html tam kaynak")
print_file_lines(route_flow)

ids, classes = collect_tokens_from_html(route_flow)

print_head("2) route_flow.html ID ve CLASS listesi")
print("ID'ler:")
for x in ids:
    print("  #" + x)
print("\nClass'lar:")
for x in classes:
    print("  ." + x)

show_css_hits(css_paths, ids, classes)
show_inline_style_hits()

print_head("6) Ana JS fonksiyonları tam blok")
for fn in [
    "renderRouteStrip",
    "computeNextStopName",
    "stopDistanceKmByName",
    "buildActualSchedule",
    "scheduleOffsetsForRoute",
    "renderTimeline",
    "renderAI",
    "liveStopOperationCount",
]:
    extract_function(seats_js, fn)

show_js_dom_hits()

print_head("7) Yorum")
print("Bu rapordan sonra karar vereceğiz:")
print("1) Sadece CSS patch yeterli mi?")
print("2) route_flow.html yapısını değiştirmek gerekir mi?")
print("3) renderRouteStrip() HTML üretiyorsa JS patch gerekir mi?")
print("4) V2 renkleri mevcut selectorlara mı uygulanacak, yoksa yeni scoped wrapper mı açılacak?")
