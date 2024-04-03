from fields.core.locale import get_preferred_language, Strings
from flask import render_template


async def index():
    language = get_preferred_language()
    strings = Strings(language)

    return render_template("index.html", **{
        "strings": strings
    })
