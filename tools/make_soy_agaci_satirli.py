from pathlib import Path

ROOT = Path(".")
CODE_EXTS = {".py", ".html", ".css", ".js"}

GROUPS = [
    ("1. ÇALIŞAN / AKTİF DOSYALAR", "ACTIVE_PATHS.txt"),
    ("2. SAHİPSİZ / KONTROL EDİLECEK DOSYALAR", "CHECK_PATHS.txt"),
    ("3. YEDEK / ARŞİV / KARANTİNA DOSYALARI", "BACKUP_PATHS.txt"),
    ("4. APK / ANDROID KOPYA DOSYALARI", "DEPLOY_COPY_PATHS.txt"),
    ("5. ARAÇ / ANALİZ SCRIPT DOSYALARI", "TOOL_PATHS.txt"),
]

def count_lines(path: Path) -> int:
    if path.suffix.lower() not in CODE_EXTS:
        return 0
    try:
        return sum(1 for _ in path.open("r", errors="ignore"))
    except Exception:
        return 0

def read_paths(list_file: str):
    p = ROOT / list_file
    if not p.exists():
        return []
    paths = []
    for line in p.read_text(errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        paths.append(Path(line))
    return sorted(paths, key=lambda x: str(x))

def build_tree(paths):
    tree = {}

    for path in paths:
        node = tree
        for part in path.parts:
            node = node.setdefault(part, {})

    return tree

def subtree_total(prefix: Path, node) -> int:
    total = 0

    for name, child in node.items():
        current = prefix / name

        if child:
            total += subtree_total(current, child)
        else:
            total += count_lines(ROOT / current)

    return total

def render_tree(node, prefix=Path("."), indent=""):
    lines = []
    items = sorted(node.items(), key=lambda x: x[0])

    for i, (name, child) in enumerate(items):
        is_last = i == len(items) - 1
        branch = "└── " if is_last else "├── "
        next_indent = indent + ("    " if is_last else "│   ")
        current = prefix / name

        if child:
            total = subtree_total(current, child)
            lines.append(f"{indent}{branch}{name}/ — {total} satır")
            lines.extend(render_tree(child, current, next_indent))
        else:
            line_count = count_lines(ROOT / current)
            lines.append(f"{indent}{branch}{name} — {line_count} satır")

    return lines

def main():
    # Önce mevcut audit raporlarını güncellemek iyi olur.
    output = []

    output.append("# Host-Hostes Paneli Satır Sayılı Soy Ağacı")
    output.append("")
    output.append("Bu rapor dosya ağacını, dosya bazlı satır sayılarıyla birlikte gösterir.")
    output.append("")

    grand_total_files = 0
    grand_total_lines = 0

    summaries = []

    group_data = []

    for title, list_file in GROUPS:
        paths = read_paths(list_file)
        total_lines = sum(count_lines(ROOT / p) for p in paths)
        total_files = len(paths)

        group_data.append((title, paths, total_files, total_lines))
        summaries.append((title, total_files, total_lines))

        grand_total_files += total_files
        grand_total_lines += total_lines

    output.append("## Özet")
    output.append("")

    for title, total_files, total_lines in summaries:
        output.append(f"- {title}: {total_files} dosya / {total_lines} satır")

    output.append("")
    output.append(f"- GENEL TOPLAM: {grand_total_files} dosya / {grand_total_lines} satır")
    output.append("")

    for title, paths, total_files, total_lines in group_data:
        output.append(f"## {title}")
        output.append("")
        output.append(f"Dosya sayısı: {total_files}")
        output.append(f"Satır sayısı: {total_lines}")
        output.append("")
        output.append("```text")

        if paths:
            tree = build_tree(paths)
            output.extend(render_tree(tree))
        else:
            output.append("(dosya yok)")

        output.append("```")
        output.append("")

    Path("HOST_HOSTES_SOY_AGACI_SATIRLI.md").write_text("\n".join(output))
    print("HOST_HOSTES_SOY_AGACI_SATIRLI.md oluşturuldu.")

if __name__ == "__main__":
    main()
