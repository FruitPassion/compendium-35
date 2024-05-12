from flask import Blueprint, flash, redirect, render_template, session, url_for
from model.compte import Compte
from model.possederole import PossederRole
from model.role import Role
from utils.custom_form import LoginForm, RegisterForm

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/connexion/", methods=["GET", "POST"])
def connexion():
    form = LoginForm()
    erreurs = []

    if form.validate_on_submit():
        if Compte.verifier_compte(form.login.data):
            if Compte.verifier_mdp(form.login.data, form.password.data):
                compte = Compte.get_compte_par_pseudo(form.login.data)
                session["nom_compte"] = compte.pseudo
                session["id_compte"] = compte.id_compte
                session["roles"] = [
                    role.libelle for role in Role.get_role_of_compte(compte.id_compte)
                ]
                flash("Vous êtes connecté en tant que {}".format(form.login.data))
                return redirect(url_for("site.accueil"))
            else:
                erreurs.append("Le mot de passe est incorrect")
        else:
            erreurs.append("Ce compte n'existe pas")
    return render_template("auth/connexion.html", form=form, erreurs=erreurs)


@auth.route("/inscription/", methods=["GET", "POST"])
def inscription():
    form = RegisterForm()
    erreurs = []

    if form.validate_on_submit():
        if Compte.verifier_compte(form.login.data):
            erreurs.append("Ce pseudo est déjà pris")
        else:
            id_compte = Compte.creer_compte(form.login.data, form.password.data)
            PossederRole.set_role(id_compte, 2)
            flash("Votre compte a bien été créé")
            return redirect(url_for("auth.connexion"))
    else:
        for _, error_messages in form.errors.items():
            erreurs.append(error_messages[0])
    return render_template("auth/inscription.html", form=form, erreurs=erreurs)


@auth.route("/deconnexion/", methods=["GET"])
def deconnexion():
    session.pop("nom_compte", None)
    flash("Vous êtes déconnecté")
    return redirect(url_for("site.accueil"))
