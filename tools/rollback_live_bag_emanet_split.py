from pathlib import Path
import re, shutil, time

TS = time.strftime("%Y%m%d_%H%M%S")

targets = [
    Path("templates/continue_trip.html"),
    Path("android_app/app/src/main/python/templates/continue_trip.html"),
]

for p in targets:
    if not p.exists():
        print(f"YOK: {p}")
        continue

    shutil.copy2(p, str(p) + f".bak_rollback_bag_emanet_split_{TS}")

    s = p.read_text(encoding="utf-8", errors="ignore")
    old = s

    # CSS yamasını kaldır
    s = re.sub(
        r'\n?\s*<style id="live-bag-emanet-split-style">.*?</style>\s*',
        "\n",
        s,
        flags=re.S
    )

    # JS yamasını kaldır
    s = re.sub(
        r'\n?\s*<script id="live-bag-emanet-split-script">.*?</script>\s*',
        "\n",
        s,
        flags=re.S
    )

    # BAGAJ altına eklenen + emanet span satırını kaldır
    s = re.sub(
        r'\s*<span\s+id="liveEmanetCount"[^>]*>.*?</span>',
        "",
        s,
        flags=re.S
    )

    if s != old:
        p.write_text(s, encoding="utf-8")
        print(f"✅ temizlendi: {p}")
    else:
        print(f"ℹ️ değişiklik yok: {p}")

