from flask import Flask


class Fields:
    def __init__(self, flask_app: Flask, main_path: str):
        self.app = flask_app
        self.main_path = main_path

    def run(self, config):
        pass