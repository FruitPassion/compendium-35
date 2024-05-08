from model.categorie_don import CategorieDon
from model.shared_model import DB_SCHEMA, DonAppartenirCategorie, Source, db


class Don(db.Model):
    __tablename__ = "don"
    __table_args__ = {"schema": DB_SCHEMA}

    id_don = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(400))
    avantage = db.Column(db.Text)
    special = db.Column(db.Text)
    normal = db.Column(db.Text)
    effet = db.Column(db.Text)
    duplicata = db.Column(db.Integer)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship("Source", primaryjoin="Don.id_source == Source.id_source")

    @staticmethod
    def get_all():
        """
        Récupère tous les dons

        :return: list
        """
        return (
            db.session.query(
                Don, db.func.group_concat(CategorieDon.libelle).label("categories")
            )
            .outerjoin(
                DonAppartenirCategorie, Don.id_don == DonAppartenirCategorie.id_don
            )
            .outerjoin(
                CategorieDon,
                DonAppartenirCategorie.id_categorie_don
                == CategorieDon.id_categorie_don,
            )
            .join(Source, Don.id_source == Source.id_source)
            .group_by(Don.id_don)
            .all()
        )

    @staticmethod
    def get_by_nom(nom):
        """
        Récupère un don par son nom

        :param nom: str
        :return: Don
        """
        return (
            db.session.query(
                Don,
                db.func.group_concat(CategorieDon.libelle).label("categories"),
                Source,
            )
            .outerjoin(
                DonAppartenirCategorie, Don.id_don == DonAppartenirCategorie.id_don
            )
            .outerjoin(
                CategorieDon,
                DonAppartenirCategorie.id_categorie_don
                == CategorieDon.id_categorie_don,
            )
            .join(Source, Don.id_source == Source.id_source)
            .filter(Don.nom == nom)
            .group_by(Don.id_don)
            .first()
        )

    @staticmethod
    def get_by_categories(id_categorie_don):
        """
        Récupère les dons par catégories

        :param categories: list
        :return: list
        """
        return (
            db.session.query(Don.nom, Don.description)
            .join(DonAppartenirCategorie)
            .filter(DonAppartenirCategorie.id_categorie_don == id_categorie_don)
            .all()
        )
