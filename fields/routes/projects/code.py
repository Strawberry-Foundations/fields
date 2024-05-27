from fields import root_dir
from fields.core.locale import get_preferred_language, Strings
from flask import render_template, request, send_file

import os


async def all():
    language = get_preferred_language()
    strings = Strings(language)

    source_dirs = os.listdir(f"{root_dir}/fields_data/src")

    return render_template("code/all.html", **{
        "strings": strings,
        "title": strings.load("browse_code"),
        "source_dirs": source_dirs,
    })


async def view(project: str):
    language = get_preferred_language()
    strings = Strings(language)

    directory = request.args.get("dir", "")

    if not directory:
        directory = "/"

    try:
        source_dirs = os.listdir(f"{root_dir}/fields_data/src/{project}/{directory}")

    except NotADirectoryError:
        return send_file(f"{root_dir}/fields_data/src/{project}/{directory}")

    return render_template("code/view.html", **{
        "strings": strings,
        "title": strings.load("browse_code"),
        "source_dirs": source_dirs,
        "project": project,
        "directory": directory,
    })
