from model.competence import Competence
from model.don import Don
from model.shared_model import (
    DB_SCHEMA,
    Alignement,
    Bonu,
    Capacite,
    CapaciteMartiale,
    CapacitePsi,
    CapaciteSort,
    Caracteristique,
    Classe,
    ConditionClasse,
    ConditionDon,
    Dependre,
    Race,
    RequerirAlignement,
    RequerirBonu,
    RequerirCapacite,
    RequerirCapaciteMartiale,
    RequerirCapacitePsi,
    RequerirCapaciteSort,
    RequerirCaracteristique,
    RequerirClasse,
    RequerirComp,
    RequerirDon,
    RequerirRace,
    RequerirTaille,
    Taille,
    db,
)


class Condition(db.Model):
    __tablename__ = "conditions"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(db.Integer, primary_key=True)
    special = db.Column(db.Text)

    @staticmethod
    def get_conditions_don(id_don):
        """
        Permet de récupérer les conditions pour un don

        :param id_don: int
        :return: list
        """
        return (
            db.session.query(
                Condition,
                Classe,
                RequerirCaracteristique,
                Caracteristique,
                Don,
                Capacite,
                RequerirBonu,
                Bonu,
                RequerirRace,
                Race,
                RequerirComp,
                Competence,
                CapaciteMartiale,
                CapacitePsi,
                CapaciteSort,
                Alignement,
                RequerirTaille,
                Taille,
            )
            .select_from(ConditionDon)
            .join(Condition)
            .outerjoin(RequerirClasse)
            .outerjoin(Classe)
            .outerjoin(RequerirCaracteristique)
            .outerjoin(Caracteristique)
            .outerjoin(RequerirDon)
            .outerjoin(Don)
            .outerjoin(RequerirCapacite)
            .outerjoin(Capacite)
            .outerjoin(RequerirBonu)
            .outerjoin(Bonu)
            .outerjoin(RequerirRace)
            .outerjoin(Race)
            .outerjoin(RequerirComp)
            .outerjoin(Competence)
            .outerjoin(RequerirCapaciteMartiale)
            .outerjoin(CapaciteMartiale)
            .outerjoin(RequerirCapacitePsi)
            .outerjoin(CapacitePsi)
            .outerjoin(RequerirCapaciteSort)
            .outerjoin(CapaciteSort)
            .outerjoin(RequerirAlignement)
            .outerjoin(Alignement)
            .outerjoin(RequerirTaille)
            .outerjoin(Taille)
            .filter(ConditionDon.id_don == id_don)
            .all()
        )

    @staticmethod
    def get_conditions_classe(id_classe):
        """
        Permet de récupérer les conditions pour une classe

        :param id_classe: int
        :return: list
        """
        return (
            db.session.query(
                Condition,
                Classe,
                RequerirCaracteristique,
                Caracteristique,
                Don,
                Capacite,
                RequerirBonu,
                Bonu,
                RequerirRace,
                Race,
                RequerirComp,
                Competence,
                CapaciteMartiale,
                CapacitePsi,
                CapaciteSort,
                Alignement,
                RequerirTaille,
                Taille,
            )
            .select_from(ConditionClasse)
            .join(Condition)
            .outerjoin(RequerirClasse)
            .outerjoin(Classe)
            .outerjoin(RequerirCaracteristique)
            .outerjoin(Caracteristique)
            .outerjoin(RequerirDon)
            .outerjoin(Don)
            .outerjoin(RequerirCapacite)
            .outerjoin(Capacite)
            .outerjoin(RequerirBonu)
            .outerjoin(Bonu)
            .outerjoin(RequerirRace)
            .outerjoin(Race)
            .outerjoin(RequerirComp)
            .outerjoin(Competence)
            .outerjoin(RequerirCapaciteMartiale)
            .outerjoin(CapaciteMartiale)
            .outerjoin(RequerirCapacitePsi)
            .outerjoin(CapacitePsi)
            .outerjoin(RequerirCapaciteSort)
            .outerjoin(CapaciteSort)
            .outerjoin(RequerirAlignement)
            .outerjoin(Alignement)
            .outerjoin(RequerirTaille)
            .outerjoin(Taille)
            .filter(ConditionClasse.id_classe == id_classe)
            .all()
        )

    @staticmethod
    def get_dons_requis_competence(nom):
        """
        Permet de récupérer les dons prérequis pour une compétence

        :param nom: str
        :return: list
        """
        return (
            db.session.query(
                Competence.libelle_competence, RequerirComp.degre_maitrise, Don.nom
            )
            .join(RequerirComp)
            .join(Condition)
            .join(ConditionDon)
            .join(Don)
            .filter(Competence.libelle_competence == nom)
            .all()
        )

    @staticmethod
    def get_conditions_technique_astucieuse_all():
        """
        Permet de récupérer les conditions pour une technique astucieuse

        :param id_technique_astucieuse: int
        :return: list
        """
        return db.session.query(Dependre, Competence).join(Competence).all()
