from model.don import Don
from model.shared_model import DB_SCHEMA, Caracteristique, DonAugmente, db


class Competence(db.Model):
    __tablename__ = "competence"
    __table_args__ = {"schema": DB_SCHEMA}

    libelle_competence = db.Column(db.String(50), primary_key=True)
    innee = db.Column(db.Integer)
    malus_armure = db.Column(db.Integer)
    description_courte = db.Column(db.Text)
    description_longue = db.Column(db.Text)
    id_caracteristique = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.caracteristique.id_caracteristique"),
        nullable=False,
        index=True,
    )

    caracteristique = db.relationship(
        "Caracteristique",
        primaryjoin="Competence.id_caracteristique == Caracteristique.id_caracteristique",
    )

    @staticmethod
    def get_all():
        """
        Récupère toutes les compétences

        :return: list
        """
        return (
            db.session.query(Competence, Caracteristique)
            .join(Caracteristique)
            .order_by(Competence.libelle_competence)
            .all()
        )

    @staticmethod
    def get_by_nom(nom):
        """
        Récupère une compétence par son nom

        :param nom: str
        :return: Competence
        """
        return (
            db.session.query(Competence, Caracteristique)
            .join(Caracteristique)
            .filter(Competence.libelle_competence == nom)
            .order_by(Competence.libelle_competence)
            .first()
        )

    @staticmethod
    def get_dons_augmentes(nom):
        """
        Récupère les dons augmentés par une compétence

        :param nom: str
        :return: list
        """
        return (
            db.session.query(Competence.libelle_competence, DonAugmente.valeur, Don.nom)
            .select_from(Competence)
            .filter(Competence.libelle_competence == nom)
            .join(DonAugmente)
            .join(Don)
            .all()
        )
