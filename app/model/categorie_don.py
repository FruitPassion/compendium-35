from model.shared_model import db, DB_SCHEMA


class CategorieDon(db.Model):
    __tablename__ = 'categorie_don'
    __table_args__ = {'schema': DB_SCHEMA}

    id_categorie_don = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50))
    description = db.Column(db.Text)
    regles = db.Column(db.Text)
    
    @staticmethod
    def get_all():
        """
        Récupère toutes les catégories de dons
        
        :return: list
        """
        return CategorieDon.query.with_entities(CategorieDon.description, CategorieDon.libelle).order_by(CategorieDon.libelle).all()
    
    @staticmethod
    def get_by_nom(nom):
        """
        Récupère une catégorie de don par son nom
        
        :param nom: str
        :return: CategorieDon
        """
        return CategorieDon.query.filter(CategorieDon.libelle == nom).first()