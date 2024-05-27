from fields.core.locale import get_preferred_language, Strings
from fields import root_dir
from flask import render_template

import os


async def spkg_index():
    language = get_preferred_language()
    strings = Strings(language)

    package_dirs = os.listdir(f"{root_dir}/fields_data/packages")

    return render_template("spkg/index.html", **{
        "strings": strings,
        "title": strings.load("spkg_browser"),
        "package_dirs": package_dirs
    })
