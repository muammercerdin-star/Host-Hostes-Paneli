import os
import re
from pathlib import Path

ROOT = Path(".").resolve()

SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    "apk_payload", "android_app", ".mypy_cache", ".pytest_cache"
}

CODE_EXTS = {".py", ".html", ".css", ".js"}
SUSPECT_WORDS = re.compile(
    r"(bak|backup|old|eski|copy|kopya|deneme|trial|archive|final|test|tmp|temp|payload|apk)",
    re.I
)

def skip_path(p: Path):
    parts = set(p.parts)
    return bool(parts & SKIP_DIRS)

def all_project_files():
    files = []
    for p in ROOT.rglob("*"):
        if p.is_file() and not skip_path(p) and p.suffix in CODE_EXTS:
            files.append(p.relative_to(ROOT))
    return sorted(files, key=str)

def read_text(p):
    try:
        return (ROOT / p).read_text(errors="ignore")
    except Exception:
        return ""

files = all_project_files()
active = set()
suspect = set()
referenced_templates = set()
referenced_static = set()

# Ana dosyalar
for starter in ["app.py", "wsgi.py", "main.py", "run.py"]:
    if Path(starter) in files:
        active.add(Path(starter))

# Python dosyalarında import, render_template, Blueprint araması
for p in files:
    text = read_text(p)

    if p.suffix == ".py":
        # Flask render_template("x.html")
        for m in re.findall(r"render_template\s*\(\s*['\"]([^'\"]+\.html)['\"]", text):
            referenced_templates.add(Path("templates") / m)

        # template_folder veya static_folder geçen py dosyaları önemli olabilir
        if "Blueprint(" in text or "Flask(" in text or "render_template" in text or "@app.route" in text or ".route(" in text:
            active.add(p)

        # local module importlarını yakalamaya çalış
        for m in re.findall(r"^\s*(?:from|import)\s+([a-zA-Z_][\w\.]*)", text, flags=re.M):
            first = m.split(".")[0]
            candidate1 = Path(first + ".py")
            candidate2 = Path(first) / "__init__.py"
            if candidate1 in files:
                active.add(candidate1)
            if candidate2 in files:
                active.add(candidate2)

    if p.suffix == ".html":
        # Jinja extends/include
        for m in re.findall(r"{%\s*(?:extends|include)\s+['\"]([^'\"]+\.html)['\"]", text):
            referenced_templates.add(Path("templates") / m)

        # url_for('static', filename='...')
        for m in re.findall(r"url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]", text):
            referenced_static.add(Path("static") / m)

        # düz href/src static pathleri
        for m in re.findall(r"""(?:src|href)=['"](?:/)?static/([^'"]+)['"]""", text):
            referenced_static.add(Path("static") / m)

# Referans verilen template/static dosyalarını aktif say
for t in referenced_templates:
    if t in files:
        active.add(t)

for s in referenced_static:
    if s in files:
        active.add(s)

# Template dosyaları: base/index/login gibi temel isimleri ayrıca aktif kabul et
IMPORTANT_TEMPLATES = {
    "base.html", "index.html", "login.html", "seats.html", "continue_trip.html",
    "start_trip.html", "settings.html", "routes_list.html", "route_edit.html",
    "route_schedule_edit.html", "trip_report.html", "consignments.html",
    "rehber.html", "ai_console.html", "hesap.html"
}

for p in files:
    if p.parts and p.parts[0] == "templates" and p.name in IMPORTANT_TEMPLATES:
        active.add(p)

# Şüpheliler
for p in files:
    if SUSPECT_WORDS.search(str(p)):
        suspect.add(p)

unknown = set(files) - active - suspect

def write_list(filename, items):
    with open(filename, "w") as f:
        for p in sorted(items, key=str):
            f.write(str(p) + "\n")

write_list("ACTIVE_FILES.txt", active)
write_list("SUSPECT_BACKUP_FILES.txt", suspect)
write_list("UNKNOWN_FILES.txt", unknown)

print("=== RAPOR ===")
print("Toplam kod dosyasi:", len(files))
print("Aktif gorunen dosya:", len(active))
print("Yedek/deneme supheli:", len(suspect))
print("Belirsiz dosya:", len(unknown))
print()
print("Olusan raporlar:")
print("ACTIVE_FILES.txt")
print("SUSPECT_BACKUP_FILES.txt")
print("UNKNOWN_FILES.txt")
