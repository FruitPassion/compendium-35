from flask import Blueprint, render_template

sources = Blueprint("sources", __name__, url_prefix="/sources")


@sources.route("/", methods=["GET"])
def index():
    return render_template("sources/index.html")


@sources.route("/<string:nom>", methods=["GET"])
def source(nom):
    return render_template("sources/source.html")
