from pathlib import Path
import re
from datetime import datetime

ROOT = Path(".").resolve()

TPL = ROOT / "templates/continue_trip.html"
JS_CORE = ROOT / "static/continue/continue_trip_core.js"
JS_V99 = ROOT / "static/continue/continue_trip_v99_clean.js"

print("===== V99I MEVCUT MESAFE MOTORU RONTGEN =====")
print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

tpl = read(TPL)
core = read(JS_CORE)
v99 = read(JS_V99)

print()
print("===== 1) DOSYA DURUMU =====")
for p in [TPL, JS_CORE, JS_V99]:
    print(("VAR " if p.exists() else "YOK "), p, "size=", p.stat().st_size if p.exists() else "-")

print()
print("===== 2) CORE MESAFE MOTORU IZLERI =====")
for key in [
    "stop-distance-value",
    "data-stop-name",
    "updateAllDistances",
    "liveDistanceValue",
    "routeCoords",
    "runtimeGpsKm",
    "formatKm",
    "distance",
    "haversine",
    "compute",
]:
    print(("CORE VAR  " if key in core else "CORE YOK  ") + key)

print()
print("===== 3) TEMPLATE V99 MESAFE BAGLANTI IZLERI =====")
for key in [
    "v99-tl-m-val",
    "v99-tl-m-lbl",
    "stop-distance-value",
    "data-stop-name",
    "liveDistanceValue",
    "liveCurrentStopName",
]:
    print(("TPL VAR   " if key in tpl else "TPL YOK   ") + key)

print()
print("===== 4) V99 JS MESAFE IZLERI =====")
for key in [
    "stop-distance-value",
    "data-stop-name",
    "setDistance",
    "setRouteProgress",
    "segment",
    "distance",
    "km",
]:
    print(("V99JS VAR " if key in v99 else "V99JS YOK ") + key)

print()
print("===== 5) TEMPLATE ICINDE MESAFE SATIRLARI =====")
for i, line in enumerate(tpl.splitlines(), 1):
    if (
        "MESAFE" in line
        or "Mesafe" in line
        or "mesafe" in line
        or "v99-tl-m-val" in line
        or "stop-distance-value" in line
        or "liveDistanceValue" in line
    ):
        print(f"{i:4}: {line[:220]}")

print()
print("===== 6) CORE stop-distance-value KULLANIM SATIRLARI =====")
for i, line in enumerate(core.splitlines(), 1):
    if "stop-distance-value" in line or "updateAllDistances" in line or "liveDistanceValue" in line:
        print(f"{i:4}: {line[:220]}")

print()
print("===== RAPOR BITTI =====")
