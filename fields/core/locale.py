from fields import server_dir
from flask import request
from enum import Enum

import json


class Languages(Enum):
    GERMAN = "de-de"
    ENGLISH = "en-us"


class Locale:
    def __init__(self):
        self.de_DE = None
        self.en_US = None

    def load_strings(self):
        with open(server_dir + "/locale/de_DE.json", "r", encoding="utf-8") as _locales:
            self.de_DE = json.load(_locales)

        with open(server_dir + "/locale/en_US.json", "r", encoding="utf-8") as _locales:
            self.en_US = json.load(_locales)


locales = Locale()
locales.load_strings()


class Strings:
    def __init__(self, lang: Languages):
        self.language = lang

    def load(self, string: str):
        lo_string = None

        match self.language:
            case "de-de": lo_string = locales.de_DE
            case "en-us": lo_string = locales.en_US
            case _: lo_string = locales.en_US

        string = lo_string[string]

        return string


def get_preferred_language():
    accept_language = request.headers.get('Accept-Language')

    if accept_language:
        languages = accept_language.replace(' ', '').split(',')

        preferred_language = languages[0].split(';')[0].lower()

        match preferred_language:
            case "de-de": return Languages.GERMAN.value
            case "en-us": return Languages.ENGLISH.value

    return None
