from fields import server_dir
import os


def load_secret():
    with open(os.path.dirname(server_dir) + "/secret.key", "r") as _secret:
        return _secret.read()
