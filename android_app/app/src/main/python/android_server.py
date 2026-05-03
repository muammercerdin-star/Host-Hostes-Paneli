import os
import threading
import time
from pathlib import Path


def start_flask_server():
    """
    Android içinde Flask sunucusunu başlatır.
    """
    base_dir = Path(__file__).resolve().parent
    os.chdir(str(base_dir))

    # Flask app import
    from app import app

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True,
    )


def start_in_background():
    t = threading.Thread(target=start_flask_server, daemon=True)
    t.start()
    time.sleep(1)
    return True
