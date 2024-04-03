from fields import server_dir

import yaml
import os


class FieldsConfig:
    def __init__(self):
        with open(os.path.dirname(server_dir) + "/config.yml", "r") as _config:
            config_data = yaml.load(_config, Loader=yaml.SafeLoader)

        self.address = config_data["host"]["address"]
        self.port = config_data["host"]["port"]

        self.debug_mode = config_data["flags"]["debug_mode"]
        self.threaded = config_data["flags"]["threaded"]

        self.static_url_path = config_data["vars"]["static_url_path"]
        self.static_folder = config_data["vars"]["static_folder"]
        self.template_folder = config_data["vars"]["template_folder"]


config = FieldsConfig()
