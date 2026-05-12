from pathlib import Path
import re

ROOT = Path(".").resolve()

CODE_EXTS = {".py", ".html", ".css", ".js"}

ENV_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    ".mypy_cache", ".pytest_cache"
}

DEPLOY_DIRS = {
    "android_app", "apk_payload"
}

REPORT_NAMES = {
    "ACTIVE_FILES.txt",
    "SUSPECT_BACKUP_FILES.txt",
    "UNKNOWN_FILES.txt",
    "ACTIVE_TREE.txt",
    "BACKUP_TREE.txt",
    "CHECK_TREE.txt",
    "DEPLOY_COPY_TREE.txt",
    "PROJE_AGAC_RAPORU.md",
}

def rel(p: Path) -> Path:
    # Symlinkleri gerçek dış yola çözmeden proje içi göreceli yol üretir.
    return p.relative_to(ROOT)

def read_text(p: Path) -> str:
    try:
        return p.read_text(errors="ignore")
    except Exception:
        return ""

def is_env_file(p: Path) -> bool:
    return any(part in ENV_DIRS for part in p.parts)

def is_deploy_file(p: Path) -> bool:
    return any(part in DEPLOY_DIRS for part in p.parts)

def is_report_file(p: Path) -> bool:
    name = p.name
    low = name.lower()

    if name in REPORT_NAMES:
        return True

    if low.startswith("proje_") and p.suffix.lower() in {".txt", ".md"}:
        return True

    if low.startswith("aktif_") and p.suffix.lower() in {".txt", ".md"}:
        return True

    if low.endswith("_raporu.txt"):
        return True

    return False

def is_backup_file(p: Path) -> bool:
    low_name = p.name.lower()
    low_parts = [x.lower() for x in p.parts]

    # Klasör bazlı gerçek yedek/arşivler
    for part in low_parts:
        if part.startswith("_archive"):
            return True
        if part.startswith("archive_"):
            return True
        if part.startswith("rollback_backup"):
            return True
        if part == "_trash_review":
            return True
        if part == "_unused_review":
            return True

    # Dosya bazlı yedekler
    # Burada "backup" kelimesini tek başına yedek saymıyoruz.
    # Çünkü templates/settings_backup.html gibi çalışan özellik sayfaları olabilir.
    # Gerçek yedekler genelde .bak / .old / .orig / .tmp şeklindedir.
    backup_markers = [
        ".bak",
        ".old",
        ".orig",
        ".tmp",
    ]

    if low_name.endswith("~"):
        return True

    return any(marker in low_name for marker in backup_markers)

def count_lines(p: Path) -> int:
    if p.suffix.lower() not in CODE_EXTS:
        return 0
    try:
        return sum(1 for _ in p.open("r", errors="ignore"))
    except Exception:
        return 0

def tree_lines(paths):
    paths = sorted({Path(p) for p in paths}, key=lambda x: str(x))
    tree = {}

    for path in paths:
        node = tree
        for part in path.parts:
            node = node.setdefault(part, {})

    lines = []

    def walk(node, prefix=""):
        items = sorted(node.items(), key=lambda x: x[0])
        for i, (name, child) in enumerate(items):
            last = i == len(items) - 1
            branch = "└── " if last else "├── "
            lines.append(prefix + branch + name)
            if child:
                walk(child, prefix + ("    " if last else "│   "))

    walk(tree)
    return lines

def write_tree(filename, title, paths):
    paths = sorted({Path(p) for p in paths}, key=lambda x: str(x))
    total = sum(count_lines(ROOT / p) for p in paths)

    with open(filename, "w") as f:
        f.write(f"{title}\n")
        f.write("=" * len(title) + "\n")
        f.write(f"Dosya sayısı: {len(paths)}\n")
        f.write(f"Kod satırı: {total}\n\n")
        for line in tree_lines(paths):
            f.write(line + "\n")

def write_list(filename, paths):
    with open(filename, "w") as f:
        for p in sorted({Path(x) for x in paths}, key=lambda x: str(x)):
            f.write(str(p) + "\n")

def extract_templates_from_py(text: str):
    found = set()
    for m in re.findall(r"render_template\s*\(\s*['\"]([^'\"]+\.html)['\"]", text):
        found.add(Path("templates") / m)
    return found

def extract_templates_from_html(text: str):
    found = set()
    for m in re.findall(r"{%\s*(?:extends|include)\s+['\"]([^'\"]+\.html)['\"]", text):
        found.add(Path("templates") / m)
    return found

def extract_static_from_html(text: str):
    found = set()

    # url_for('static', filename='...')
    for m in re.findall(
        r"url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]",
        text
    ):
        found.add(Path("static") / m.split("?")[0])

    # /static/xxx.css veya /static/xxx.js
    for m in re.findall(r"/static/([^'\"\s>)]+)", text):
        clean = m.split("?")[0]
        found.add(Path("static") / clean)

    return found

def extract_static_from_css(css_path: Path, text: str):
    found = set()
    base = css_path.parent

    for m in re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", text):
        if m.startswith("data:") or m.startswith("http"):
            continue

        clean = m.split("?")[0].split("#")[0]
        candidate = (base / clean).resolve()

        try:
            found.add(candidate.relative_to(ROOT))
        except Exception:
            pass

    return found

# Bütün dosyalar
# .venv / android_app / apk_payload gibi klasörlere baştan girmiyoruz.
all_files_abs = []
for p in ROOT.rglob("*"):
    if not p.is_file():
        continue

    rp = p.relative_to(ROOT)
    parts = set(rp.parts)

    if parts & ENV_DIRS:
        continue

    all_files_abs.append(p)

all_files = [rel(p) for p in all_files_abs]

code_files = [
    p for p in all_files
    if p.suffix.lower() in CODE_EXTS
]

env_files = [p for p in code_files if is_env_file(p)]
deploy_files = [
    p for p in code_files
    if not is_env_file(p) and is_deploy_file(p)
]
backup_files = [
    p for p in code_files
    if not is_env_file(p)
    and not is_deploy_file(p)
    and is_backup_file(p)
]
report_files = [
    p for p in code_files
    if not is_env_file(p)
    and not is_deploy_file(p)
    and not is_backup_file(p)
    and is_report_file(p)
]

runtime_candidates = [
    p for p in code_files
    if not is_env_file(p)
    and not is_deploy_file(p)
    and not is_backup_file(p)
    and not is_report_file(p)
]

runtime_set = set(runtime_candidates)
active = set()

# Ana çalışan Python girişleri
for p in runtime_candidates:
    s = str(p)

    if s == "app.py":
        active.add(p)

    if s == "speedlimit.py":
        active.add(p)

    if s.startswith("modules/") and p.suffix == ".py":
        active.add(p)

# Python import + render_template taraması
changed = True
while changed:
    changed = False

    for p in list(active):
        abs_p = ROOT / p
        text = read_text(abs_p)

        if p.suffix == ".py":
            # render_template ile çağrılan template dosyaları
            for t in extract_templates_from_py(text):
                if t in runtime_set and t not in active:
                    active.add(t)
                    changed = True

            # Yerel importları yakala
            for m in re.findall(r"^\s*(?:from|import)\s+([a-zA-Z_][\w\.]*)", text, flags=re.M):
                parts = m.split(".")
                first = parts[0]

                candidates = [
                    Path(first + ".py"),
                    Path(first) / "__init__.py",
                    Path(*parts).with_suffix(".py"),
                    Path(*parts) / "__init__.py",
                ]

                for c in candidates:
                    if c in runtime_set and c not in active:
                        active.add(c)
                        changed = True

        if p.suffix == ".html":
            # extends/include
            for t in extract_templates_from_html(text):
                if t in runtime_set and t not in active:
                    active.add(t)
                    changed = True

            # static dosyaları
            for s in extract_static_from_html(text):
                if s in runtime_set and s not in active:
                    active.add(s)
                    changed = True

        if p.suffix == ".css":
            for s in extract_static_from_css(abs_p, text):
                if s in runtime_set and s not in active:
                    active.add(s)
                    changed = True

# Güvenli temel template kabulü:
# app.py bazı sayfaları dinamik çağırıyorsa kaçmasın diye canlı templates/*.html dosyalarını
# "çalışan aday" yerine aktife yakın tutuyoruz.
for p in runtime_candidates:
    if len(p.parts) >= 2 and p.parts[0] == "templates" and p.suffix == ".html":
        active.add(p)

# tools klasöründeki scriptler çalışan uygulama değil, araçtır
tool_files = [
    p for p in runtime_candidates
    if len(p.parts) >= 1 and p.parts[0] == "tools"
]

for p in tool_files:
    if p in active:
        active.remove(p)

check_files = sorted(set(runtime_candidates) - set(active) - set(tool_files), key=lambda x: str(x))

# Raporlar
write_tree("ACTIVE_TREE.txt", "ÇALIŞAN / AKTİF DOSYALAR", active)
write_tree("CHECK_TREE.txt", "SAHİPSİZ / KONTROL EDİLECEK DOSYALAR", check_files)
write_tree("BACKUP_TREE.txt", "YEDEK / ARŞİV DOSYALAR", backup_files)
write_tree("DEPLOY_COPY_TREE.txt", "APK / ANDROID KOPYA DOSYALAR", deploy_files)
write_tree("TOOL_TREE.txt", "ARAÇ / ANALİZ SCRIPT DOSYALARI", tool_files)

write_list("ACTIVE_PATHS.txt", active)
write_list("CHECK_PATHS.txt", check_files)
write_list("BACKUP_PATHS.txt", backup_files)
write_list("DEPLOY_COPY_PATHS.txt", deploy_files)
write_list("TOOL_PATHS.txt", tool_files)

total_active_lines = sum(count_lines(ROOT / p) for p in active)
total_check_lines = sum(count_lines(ROOT / p) for p in check_files)
total_backup_lines = sum(count_lines(ROOT / p) for p in backup_files)
total_deploy_lines = sum(count_lines(ROOT / p) for p in deploy_files)
total_tool_lines = sum(count_lines(ROOT / p) for p in tool_files)

with open("PROJE_AGAC_RAPORU.md", "w") as f:
    f.write("# Host-Hostes Paneli Proje Ağaç Raporu\n\n")

    f.write("## Özet\n\n")
    f.write(f"- Çalışan / aktif dosya: {len(active)} dosya, {total_active_lines} satır\n")
    f.write(f"- Sahipsiz / kontrol edilecek: {len(check_files)} dosya, {total_check_lines} satır\n")
    f.write(f"- Yedek / arşiv: {len(backup_files)} dosya, {total_backup_lines} satır\n")
    f.write(f"- APK / Android kopya: {len(deploy_files)} dosya, {total_deploy_lines} satır\n")
    f.write(f"- Araç / analiz scriptleri: {len(tool_files)} dosya, {total_tool_lines} satır\n\n")

    sections = [
        ("## 1. ÇALIŞAN / AKTİF DOSYALAR", active),
        ("## 2. SAHİPSİZ / KONTROL EDİLECEK DOSYALAR", check_files),
        ("## 3. YEDEK / ARŞİV DOSYALAR", backup_files),
        ("## 4. APK / ANDROID KOPYA DOSYALAR", deploy_files),
        ("## 5. ARAÇ / ANALİZ SCRIPT DOSYALARI", tool_files),
    ]

    for title, paths in sections:
        f.write(title + "\n\n")
        f.write("```text\n")
        for line in tree_lines(paths):
            f.write(line + "\n")
        f.write("```\n\n")

print("=== PROJE AĞAÇ RAPORU OLUŞTU ===")
print("Ana rapor: PROJE_AGAC_RAPORU.md")
print()
print("Ayrı ağaçlar:")
print("ACTIVE_TREE.txt")
print("CHECK_TREE.txt")
print("BACKUP_TREE.txt")
print("DEPLOY_COPY_TREE.txt")
print("TOOL_TREE.txt")
print()
print("Yol listeleri:")
print("ACTIVE_PATHS.txt")
print("CHECK_PATHS.txt")
print("BACKUP_PATHS.txt")
print("DEPLOY_COPY_PATHS.txt")
print("TOOL_PATHS.txt")
print()
print("Özet:")
print(f"Çalışan / aktif: {len(active)} dosya, {total_active_lines} satır")
print(f"Sahipsiz / kontrol: {len(check_files)} dosya, {total_check_lines} satır")
print(f"Yedek / arşiv: {len(backup_files)} dosya, {total_backup_lines} satır")
print(f"APK / Android kopya: {len(deploy_files)} dosya, {total_deploy_lines} satır")
print(f"Araç / analiz: {len(tool_files)} dosya, {total_tool_lines} satır")
