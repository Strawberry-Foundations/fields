from fields.core.config import config
from fields.utils.secret import load_secret

from fields.routes.index import index
from fields.routes.projects.code import all, view
from fields.routes.spkg import spkg_index

from flask import Flask

app = Flask(
    __name__,
    static_url_path=config.static_url_path,
    static_folder=config.static_folder,
    template_folder=config.template_folder
)

app.config["SECRET_KEY"] = load_secret()

app.add_url_rule("/", view_func=index)
app.add_url_rule("/packages", view_func=spkg_index)
app.add_url_rule("/projects/all/code", view_func=all)
app.add_url_rule("/projects/<string:project>/code", view_func=view)
