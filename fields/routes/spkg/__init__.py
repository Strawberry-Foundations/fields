from fields.core.locale import get_preferred_language, Strings
from flask import render_template


async def spkg_index():
    language = get_preferred_language()
    strings = Strings(language)

    return render_template("spkg/index.html", **{
        "strings": strings,
        "title": strings.load("spkg_browser")
    })
