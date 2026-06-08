from pathlib import Path
from datetime import datetime
import shutil
import re

ROOT = Path(".").resolve()
STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")

SERVER = ROOT / "android_app/app/src/main/python/android_server.py"

print("===== APK TIMEOUT EMBED LOG V39 =====")

if not SERVER.exists():
    print("❌ android_server.py yok")
    raise SystemExit

bak = SERVER.with_name(SERVER.name + f".bak-apk-timeout-embed-log-v39-{STAMP}")
shutil.copy2(SERVER, bak)
print("📦 Yedek:", bak.relative_to(ROOT))

s = SERVER.read_text(encoding="utf-8", errors="ignore")

if "def _read_startup_log_tail_v39" not in s:
    marker = "\ndef _http_ping(host=HOST, port=PORT, timeout=1.2):"
    helper = r'''

def _read_startup_log_tail_v39(limit=12000):
    try:
        global STARTUP_LOG

        candidates = []

        if STARTUP_LOG:
            candidates.append(Path(STARTUP_LOG))

        try:
            candidates.append(Path(__file__).resolve().parent / "_android_data" / "muavin_startup.log")
        except Exception:
            pass

        seen = set()
        parts = []

        for p in candidates:
            try:
                key = str(p)
                if key in seen:
                    continue
                seen.add(key)

                if p.exists():
                    txt = p.read_text(encoding="utf-8", errors="ignore")
                    if len(txt) > limit:
                        txt = txt[-limit:]
                    parts.append("LOG PATH: " + str(p) + "\n" + txt)
                else:
                    parts.append("LOG YOK: " + str(p))
            except Exception as e:
                parts.append("LOG OKUMA HATASI: " + str(p) + " => " + repr(e))

        if not parts:
            return "Startup log adayı yok."

        return "\n\n".join(parts)

    except Exception as e:
        return "Startup log tail okunamadı: " + repr(e)

'''
    if marker not in s:
        print("❌ _http_ping marker bulunamadı")
        raise SystemExit
    s = s.replace(marker, helper + marker, 1)
    print("✅ Log tail helper eklendi")
else:
    print("ℹ️ Log tail helper zaten var")

old = '''    raise RuntimeError(
        f"Flask {timeout} saniye içinde {host}:{port} üzerinde başlamadı."
    )
'''

new = '''    log_tail = _read_startup_log_tail_v39()
    raise RuntimeError(
        f"Flask {timeout} saniye içinde {host}:{port} üzerinde başlamadı.\\n\\n"
        f"===== APK STARTUP LOG V39 =====\\n{log_tail}"
    )
'''

if old in s:
    s = s.replace(old, new, 1)
    print("✅ Timeout hatasının içine startup log gömüldü")
elif "APK STARTUP LOG V39" in s:
    print("ℹ️ Timeout log gömme zaten var")
else:
    print("❌ Timeout raise bloğu bulunamadı")
    raise SystemExit

SERVER.write_text(s, encoding="utf-8")

print()
print("===== KONTROL =====")
txt = SERVER.read_text(encoding="utf-8", errors="ignore")
for key in ["_read_startup_log_tail_v39", "APK STARTUP LOG V39", "timeout=60", "Flask {timeout}"]:
    print(key, "=", txt.count(key))

print()
print("✅ V39 tamam.")
