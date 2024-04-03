import os.path

from flask import Flask
from fields import server_dir

import yaml


class Fields:
    def __init__(self):
        self.main_path = os.path.dirname(server_dir)

        self.app = Flask(__name__)

    def run(self):
        pass
