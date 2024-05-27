from fields.core.locale import get_preferred_language, Strings
from fields.core.spkg.parser import read
from fields.core.spkg import SpkgBuild

from fields import root_dir
from flask import render_template

import os


async def spkg_index():
    language = get_preferred_language()
    strings = Strings(language)

    package_dirs = os.listdir(f"{root_dir}/fields_data/packages")
    packages = []

    for package in package_dirs:
        data = read(f"{root_dir}/fields_data/packages/{package}/compose.spkg")
        packages.append(data)

    return render_template("spkg/index.html", **{
        "strings": strings,
        "title": strings.load("spkg_browser"),
        "packages": packages
    })
