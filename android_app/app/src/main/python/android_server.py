import os
import socket
import threading
import time
import traceback
from pathlib import Path

SERVER_ERROR = None


def wait_for_port(host="127.0.0.1", port=5000, timeout=25):
    start = time.time()

    while time.time() - start < timeout:
        global SERVER_ERROR

        if SERVER_ERROR:
            raise RuntimeError("Flask başlatılamadı:\n" + SERVER_ERROR)

        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            time.sleep(0.4)

    raise RuntimeError("Flask 25 saniye içinde 127.0.0.1:5000 üzerinde başlamadı.")


def start_flask_server():
    global SERVER_ERROR

    try:
        base_dir = Path(__file__).resolve().parent
        os.chdir(str(base_dir))

        from app import app

        app.run(
            host="127.0.0.1",
            port=5000,
            debug=False,
            use_reloader=False,
            threaded=True,
        )

    except Exception:
        SERVER_ERROR = traceback.format_exc()
        print(SERVER_ERROR)


def start_in_background():
    t = threading.Thread(target=start_flask_server, daemon=True)
    t.start()

    wait_for_port("127.0.0.1", 5000, timeout=25)
    return True
