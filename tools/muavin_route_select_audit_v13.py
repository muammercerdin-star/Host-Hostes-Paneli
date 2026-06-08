from pathlib import Path
from datetime import datetime
import hashlib
import re

ROOT = Path(".").resolve()
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

TS = datetime.now().strftime("%Y%m%d-%H%M%S")
OUT = REPORTS / f"muavin_route_select_audit_v13_{TS}.md"

FILES = {
    "WEB index": ROOT / "templates/index.html",
    "ANDROID index": ROOT / "android_app/app/src/main/python/templates/index.html",
    "WEB app.py": ROOT / "app.py",
    "ANDROID app.py": ROOT / "android_app/app/src/main/python/app.py",
}

KEYS = [
    "routeSheet",
    "routeSheetBackdrop",
    "routePicker",
    "routePickerBtn",
    "routePickerText",
    "routeSelect",
    "set-route",
    "sefer-baslat",
    "tripGuard",
    "tripGuardGo",
    "tripGuardOk",
    "active-route-lock",
    "active-route-lock-final",
    "home-route-lock-fix",
    "home-route-link-fix",
    "route-sheet-no-flash-fix",
    "hidden",
    "disabled",
    "readonly",
    "pointer-events",
    "preventDefault",
    "stopPropagation",
    "stopImmediatePropagation",
    "active_trip",
    "current_trip",
    "continue",
    "devam",
    "kilit",
    "lock",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "-"

def lines(p):
    return len(read(p).splitlines()) if p.exists() else 0

def norm(s):
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def context_hits(p, keys):
    s = read(p)
    out = []
    arr = s.splitlines()
    for i, line in enumerate(arr, 1):
        low = line.lower()
        for k in keys:
            if k.lower() in low:
                out.append((i, k, line.rstrip()))
                break
    return out

def section_around(p, pattern, before=15, after=35):
    s = read(p).splitlines()
    for idx, line in enumerate(s, 1):
        if pattern.lower() in line.lower():
            a = max(1, idx-before)
            b = min(len(s), idx+after)
            return [(n, s[n-1]) for n in range(a, b+1)]
    return []

md = []
md.append("# Muavin Asistanı Route / Hat Seçimi Audit V13")
md.append("")
md.append(f"- Tarih: `{TS}`")
md.append("- Bu rapor sadece tespittir. Dosya değiştirmez.")
md.append("")

md.append("## 1) Dosya Durumu")
md.append("")
md.append("| Dosya | Var mı | Satır | Hash |")
md.append("| --- | --- | ---: | --- |")
for name, p in FILES.items():
    md.append(f"| {name} | {'VAR' if p.exists() else 'YOK'} | {lines(p)} | {sha(p)} |")

md.append("")
md.append("## 2) WEB ↔ ANDROID index.html Farkı")
web = FILES["WEB index"]
andp = FILES["ANDROID index"]
if web.exists() and andp.exists():
    md.append(f"- WEB hash: `{sha(web)}`")
    md.append(f"- ANDROID hash: `{sha(andp)}`")
    md.append(f"- Durum: **{'AYNI' if sha(web)==sha(andp) else 'FARKLI'}**")
else:
    md.append("- Karşılaştırma yapılamadı.")

md.append("")
md.append("## 3) WEB index.html Hat/Route/Kilit İzleri")
md.append("")
md.append("| Satır | Anahtar | İçerik |")
md.append("| ---: | --- | --- |")
for ln, k, content in context_hits(web, KEYS):
    c = content.replace("|", "\\|")
    if len(c) > 220:
        c = c[:220] + "..."
    md.append(f"| {ln} | `{k}` | `{c}` |")

md.append("")
md.append("## 4) ANDROID index.html Hat/Route/Kilit İzleri")
md.append("")
md.append("| Satır | Anahtar | İçerik |")
md.append("| ---: | --- | --- |")
for ln, k, content in context_hits(andp, KEYS):
    c = content.replace("|", "\\|")
    if len(c) > 220:
        c = c[:220] + "..."
    md.append(f"| {ln} | `{k}` | `{c}` |")

for title, pattern in [
    ("routeSheet bölgesi", "routeSheet"),
    ("routePicker bölgesi", "routePicker"),
    ("tripGuard bölgesi", "tripGuard"),
    ("home-route-lock-fix bölgesi", "home-route-lock-fix"),
    ("active-route-lock-final bölgesi", "active-route-lock-final"),
    ("route-sheet-no-flash-fix bölgesi", "route-sheet-no-flash-fix"),
]:
    md.append("")
    md.append(f"## 5) WEB {title}")
    md.append("")
    sec = section_around(web, pattern)
    if not sec:
        md.append("_Bulunamadı._")
    else:
        md.append("| Satır | İçerik |")
        md.append("| ---: | --- |")
        for ln, content in sec:
            c = content.replace("|", "\\|")
            if len(c) > 240:
                c = c[:240] + "..."
            md.append(f"| {ln} | `{c}` |")

md.append("")
md.append("## 6) app.py Sefer / Route Endpoint İzleri")
md.append("")
md.append("| Dosya | Satır | İçerik |")
md.append("| --- | ---: | --- |")
for name in ["WEB app.py", "ANDROID app.py"]:
    p = FILES[name]
    for ln, k, content in context_hits(p, ["set-route", "sefer-baslat", "start_trip", "active_trip", "current_trip", "route_id", "route_name"]):
        c = content.replace("|", "\\|")
        if len(c) > 220:
            c = c[:220] + "..."
        md.append(f"| {name} | {ln} | `{c}` |")

md.append("")
md.append("## 7) İlk Teknik Yorum")
md.append("")
md.append("- `disabled`, `hidden`, `pointer-events`, `preventDefault`, `tripGuard` ve `active-route-lock` satırları hat seçimini kilitleyebilir.")
md.append("- WEB ve ANDROID index.html farklıysa, APK’da hat seçme davranışı webden farklı çalışabilir.")
md.append("- Özellikle aktif sefer kilidi yeni sefer başlat ekranına yanlış uygulanıyorsa hat seçimi tıklanmaz hale gelir.")

OUT.write_text("\n".join(md), encoding="utf-8")

print("✅ Route / hat seçimi audit V13 hazır:")
print(OUT)
print()
print("===== KISA ÖZET =====")
for name, p in FILES.items():
    print(f"{name}: {'VAR' if p.exists() else 'YOK'} | satır={lines(p)} | hash={sha(p)}")

print()
print("Görmek için:")
print(f"sed -n '1,260p' {OUT}")
