import os.path

from flask import Flask
from fields import server_dir
from fields.core.config import config


class Fields:
    def __init__(self, flask_app: Flask):
        self.main_path = os.path.dirname(server_dir)
        self.app = flask_app

    def run(self):
        self.app.run(
            host=config.address,
            port=config.port,
            debug=config.debug_mode,
            threaded=config.threaded
        )
