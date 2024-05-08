from model.shared_model import db, DB_SCHEMA, Source
from model.competence import Competence


class TechniqueAstucieuse(db.Model):
    __tablename__ = 'technique_astucieuse'
    __table_args__ = {'schema': DB_SCHEMA}

    id_technique_astucieuse = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    type = db.Column(db.String(50))
    avantage = db.Column(db.Text)
    description = db.Column(db.Text)
    id_source = db.Column(db.ForeignKey(f'{DB_SCHEMA}.source.id_source'), nullable=False, index=True)

    source = db.relationship('Source', primaryjoin='TechniqueAstucieuse.id_source == Source.id_source')


    @staticmethod
    def get_all():
        """
        Récupère toutes les techniques astucieuses
        
        :return: list
        """
        return db.session.query(TechniqueAstucieuse, Source).select_from(
            TechniqueAstucieuse).join(Source).order_by(TechniqueAstucieuse.nom).all()
