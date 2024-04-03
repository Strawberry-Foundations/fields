from fields.core.app import app, config
from fields.core import App

import os

runtime = App(app, os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    runtime.run(config)
