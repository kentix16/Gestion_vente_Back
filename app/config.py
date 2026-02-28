
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        print("hasattr")
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    print("!hasattr")
    return os.path.join(os.path.abspath(""), relative_path)


db_path = resource_path("app/vente.db")
DATABASE_URL = f"sqlite:///{db_path}"
url_base = "http://127.0.0.1:5000"
"sqlite:///{db_path}"""