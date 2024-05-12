from flask import Blueprint, abort, redirect, render_template, request, url_for
from model.shared_model import TextPage
from model.sort import Sort

sorts = Blueprint("sorts", __name__, url_prefix="/sorts")


@sorts.route("/", methods=["GET"])
def index():
    index_text = TextPage.query.filter_by(title="index_sorts").first().content
    return render_template("sorts/index.html", index_text=index_text)


@sorts.route("/recherche/", methods=["GET"])
def recherche():
    return render_template("sorts/recherche.html", c_sorts=Sort)


@sorts.route("/recherche/<string:sort_nom>", methods=["GET"])
def sort(sort_nom):
    sort = Sort.get_sort(sort_nom)
    if not sort:
        abort(404)
    return render_template("sorts/sort.html", sort=sort)


@sorts.route("/resultat-recherche/", methods=["GET", "POST"])
def resultat_recherche():
    sort = request.form.get("sort-nom")
    sorts = Sort.get_liste_sort_par_nom(sort)
    return render_template(
        "sorts/liste.html", sorts=sorts, nbr_sorts=len(sorts), page=1, nb_pages=1
    )


@sorts.route("/liste/", defaults={"page": 1}, methods=["GET"])
@sorts.route("/liste/<int:page>", methods=["GET"])
def liste(page):
    nbr_sorts = Sort.get_number_of_sorts()

    sort_par_page = 50
    nb_pages = int(nbr_sorts / sort_par_page + 1)
    if nb_pages < page:
        return redirect(url_for("sorts.liste", page=nb_pages))
    elif page < 1:
        return redirect(url_for("sorts.liste", page=1))

    sorts = Sort.get_sorts(page, per_page=sort_par_page)
    return render_template(
        "sorts/liste.html",
        sorts=sorts,
        nbr_sorts=nbr_sorts,
        page=page,
        nb_pages=nb_pages,
    )


@sorts.route("/registre/<string:registre>/", defaults={"page": 1}, methods=["GET"])
@sorts.route("/registre/<string:registre>/<int:page>", methods=["GET"])
def registre(registre, page):
    nbr_sorts = Sort.get_number_of_sorts_par_registre(registre)

    if nbr_sorts == 0:
        abort(404)

    sort_par_page = 50
    nb_pages = int(nbr_sorts / sort_par_page + 1)
    if nb_pages < page:
        return redirect(url_for("sorts.registre", registre=registre, page=nb_pages))
    elif page < 1:
        return redirect(url_for("sorts.registre", registre=registre, page=1))

    sorts = Sort.get_liste_sorts_par_registre(registre, page)
    if len(sorts) == 0:
        return redirect(url_for("sorts.recherche"))
    return render_template(
        "sorts/liste.html",
        sorts=sorts,
        nbr_sorts=nbr_sorts,
        page=page,
        nb_pages=nb_pages,
    )


@sorts.route("/source/<string:source>/", defaults={"page": 1}, methods=["GET"])
@sorts.route("/source/<string:source>/<int:page>", methods=["GET"])
def source(source, page):
    nbr_sorts = Sort.get_number_of_sorts_par_source(source)

    if nbr_sorts == 0:
        abort(404)

    sort_par_page = 50
    nb_pages = int(nbr_sorts / sort_par_page + 1)
    if nb_pages < page:
        return redirect(url_for("sorts.source", source=source, page=nb_pages))
    elif page < 1:
        return redirect(url_for("sorts.source", source=source, page=1))

    sorts = Sort.get_liste_sorts_par_source(source, page)
    if len(sorts) == 0:
        return redirect(url_for("sorts.recherche"))
    return render_template(
        "sorts/liste.html",
        sorts=sorts,
        nbr_sorts=nbr_sorts,
        page=page,
        nb_pages=nb_pages,
    )


@sorts.route("/ecole/<string:ecole>/", defaults={"page": 1}, methods=["GET"])
@sorts.route("/ecole/<string:ecole>/<int:page>", methods=["GET"])
def ecole(ecole, page):
    nbr_sorts = Sort.get_number_of_sorts_par_ecole(ecole)

    if nbr_sorts == 0:
        abort(404)

    sort_par_page = 50
    nb_pages = int(nbr_sorts / sort_par_page + 1)
    if nb_pages < page:
        return redirect(url_for("sorts.ecole", ecole=ecole, page=nb_pages))
    elif page < 1:
        return redirect(url_for("sorts.ecole", ecole=ecole, page=1))

    sorts = Sort.get_liste_sorts_par_ecole(ecole, page)
    if len(sorts) == 0:
        return redirect(url_for("sorts.recherche"))
    return render_template(
        "sorts/liste.html",
        sorts=sorts,
        nbr_sorts=nbr_sorts,
        page=page,
        nb_pages=nb_pages,
    )


@sorts.route(
    "/branche/<string:ecole>/<string:branche>/", defaults={"page": 1}, methods=["GET"]
)
@sorts.route("/branche/<string:ecole>/<string:branche>/<int:page>", methods=["GET"])
def branche(ecole, branche, page):
    nbr_sorts = Sort.get_number_of_sorts_par_ecole_branche(ecole, branche)

    if nbr_sorts == 0:
        abort(404)

    sort_par_page = 50
    nb_pages = int(nbr_sorts / sort_par_page + 1)
    if nb_pages < page:
        return redirect(
            url_for("sorts.branche", ecole=ecole, brancher=branche, page=nb_pages)
        )
    elif page < 1:
        return redirect(url_for("sorts.branche", ecole=ecole, brancher=branche, page=1))

    sorts = Sort.get_liste_sorts_par_ecole_branche(ecole, branche, page)
    if len(sorts) == 0:
        return redirect(url_for("sorts.recherche"))
    return render_template(
        "sorts/liste.html",
        sorts=sorts,
        nbr_sorts=nbr_sorts,
        page=page,
        nb_pages=nb_pages,
    )
