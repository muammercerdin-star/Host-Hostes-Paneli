from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import app, get_active_trip, get_active_trip_row

OUT = ROOT / "run_logs" / "continue_v98_auth.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

print("===== V98 AUTH RENDER TEST =====")
print("ROOT:", ROOT)

with app.app_context():
    try:
        tid = get_active_trip()
        row = get_active_trip_row()
        print("ACTIVE_TRIP_ID:", tid)

        if row:
            try:
                print("ACTIVE_TRIP:", row["route"], "|", row["plate"])
            except Exception:
                print("ACTIVE_TRIP_ROW:", dict(row))
        else:
            print("ACTIVE_TRIP_ROW: YOK")
    except Exception as e:
        print("ACTIVE_TRIP_OKUMA_HATA:", repr(e))

with app.test_client() as c:
    with c.session_transaction() as sess:
        sess["auth_ok"] = True

    r = c.get("/continue-trip?v=v98_auth_test", follow_redirects=False)
    html = r.get_data().decode("utf-8", errors="ignore")

    OUT.write_text(html, encoding="utf-8", errors="ignore")

    print()
    print("STATUS:", r.status_code)
    print("LOCATION:", r.headers.get("Location", ""))
    print("HTML_SIZE:", len(html))
    print("OUT:", OUT)

    print()
    print("===== V97 IZLERI =====")
    pats = [
        "v97-real-page",
        "v97_proximity_preview.css",
        "v97_real_data.css",
        "v97_real_bind.js",
        "liveCurrentStopName",
        "liveDistanceValue",
        "liveOffloadCount",
        "liveBagajCount",
        "ringFill",
        "routePct",
        "CONTINUE_BOOT",
        "v97-dock",
    ]

    for p in pats:
        print(("VAR  " if p in html else "YOK  ") + p)

    print()
    print("===== HATA IZLERI =====")
    err = re.findall(
        r"Traceback|UndefinedError|TemplateSyntaxError|Internal Server Error|jinja2|Aktif sefer yok|Redirecting|login",
        html,
        re.I
    )

    if err:
        print("HATA_IZI_VAR:", sorted(set(x.lower() for x in err)))
    else:
        print("HATA_IZI_YOK")

    print()
    print("===== ILK 35 SATIR =====")
    for i, line in enumerate(html.splitlines()[:35], 1):
        print(f"{i}: {line[:220]}")
