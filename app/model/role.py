from model.possederole import PossederRole
from model.shared_model import DB_SCHEMA, db


class Role(db.Model):
    __tablename__ = "role"
    __table_args__ = {"schema": DB_SCHEMA}

    id_role = db.Column(db.Integer, primary_key=True)
    couleur = db.Column(db.String(7))
    libelle = db.Column(db.String(50))

    @staticmethod
    def get_all_roles():
        """
        Retourne la liste de tout les roles

        :return: Liste de classes roles
        """
        return Role.query.all()

    @staticmethod
    def get_role_of_compte(id_compte):
        """
        Retourne la liste des roles d'un compte

        :return: Liste de classes roles
        """
        return Role.query.join(PossederRole).filter_by(id_compte=id_compte).all()

    @staticmethod
    def get_role_par_libelle(libelle):
        """
        Retourne un role à partir de son libelle

        :return: Classe role
        """
        return Role.query.filter_by(libelle=libelle).first()

    @staticmethod
    def get_role_par_id(id_role):
        """
        Retourne un role à partir de son id

        :return: Classe role
        """
        return Role.query.filter_by(id_role=id_role).first()
