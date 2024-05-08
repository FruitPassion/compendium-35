from flask import Blueprint, render_template

site = Blueprint("site", __name__)


@site.route("/", methods=["GET"])
def accueil():
    return render_template("site/index.html")