from flask import Blueprint, abort, render_template
from model.competence import Competence
from model.condition import Condition
from model.synergiecomp import SynergieCompetence
from model.techniques_astucieuses import TechniqueAstucieuse

competences = Blueprint("competences", __name__, url_prefix="/competences")


@competences.route("/", methods=["GET"])
def index():
    competences = Competence.get_all()
    synergie = SynergieCompetence.get_all()
    return render_template(
        "competences/index.html", competences=competences, synergie=synergie
    )


@competences.route("/recherche/<string:nom>", methods=["GET"])
def competence(nom):
    competence = Competence.get_by_nom(nom)
    if not competence:
        abort(404)
    synergies = SynergieCompetence.get_by_nom(nom)
    synergies_inverse = SynergieCompetence.get_by_nom_inverse(nom)
    dons_requis = Condition.get_dons_requis_competence(nom)
    dons_augmentes = Competence.get_dons_augmentes(nom)
    return render_template(
        "competences/competence.html",
        competence=competence,
        synergies=synergies,
        dons_requis=dons_requis,
        dons_augmentes=dons_augmentes,
        synergies_inverse=synergies_inverse,
    )


@competences.route("/techniques-astucieuses", methods=["GET"])
def techniques_astucieuses():
    techniques = TechniqueAstucieuse.get_all()
    condtions = Condition.get_conditions_technique_astucieuse_all()
    return render_template(
        "competences/techniques_astucieuses.html",
        techniques=techniques,
        condtions=condtions,
    )
