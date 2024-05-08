from flask import Blueprint, render_template
from model.categorie_don import CategorieDon
from model.don import Don
from utils.builder import builder_condition_don

dons = Blueprint("dons", __name__, url_prefix="/dons")


@dons.route("/", methods=["GET"])
def index():
    categories = CategorieDon.get_all()
    return render_template("dons/index.html", categories=categories)


@dons.route("/<string:nom_don>", methods=["GET"])
def don(nom_don):
    don = Don.get_by_nom(nom_don)
    conditions = builder_condition_don(don.Don.id_don)
    return render_template("dons/don.html", don=don, conditions=conditions)


@dons.route("categorie/<string:nom_categorie>", methods=["GET"])
def categorie(nom_categorie):
    categorie = CategorieDon.get_by_nom(nom_categorie)
    dons = Don.get_by_categories(categorie.id_categorie_don)
    return render_template("dons/categorie.html", categorie=categorie, dons=dons)
