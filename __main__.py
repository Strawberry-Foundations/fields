from fields.core.app import app, config
from fields.core import Fields

import os

fields = Fields(app, os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    fields.run(config)
