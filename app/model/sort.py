from operator import or_
from sqlalchemy import distinct
from model.shared_model import db, DB_SCHEMA
from model.shared_model import Source

class Sort(db.Model):
    __tablename__ = 'sort'
    __table_args__ = {'schema': DB_SCHEMA}

    id_sort = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    ecole = db.Column(db.String(50))
    branche = db.Column(db.String(100))
    registre = db.Column(db.String(100))
    temps_incantation = db.Column(db.String(200))
    composante = db.Column(db.String(200))
    portee = db.Column(db.String(200))
    effet = db.Column(db.String(200))
    cible = db.Column(db.String(200))
    duree = db.Column(db.String(200))
    sauvegarde = db.Column(db.String(200))
    res_magie = db.Column(db.String(200))
    zone_effet = db.Column(db.String(200))
    composante_div = db.Column(db.Text)
    focaliseur_div = db.Column(db.Text)
    cout_xp = db.Column(db.String(500))
    divers = db.Column(db.Text)
    description = db.Column(db.Text)
    id_source = db.Column(db.ForeignKey(f'{DB_SCHEMA}.source.id_source'), nullable=False, index=True)

    source = db.relationship('Source', primaryjoin='Sort.id_source == Source.id_source')
    
    @staticmethod
    def get_sorts(page=1, per_page=50):
        """
        Permet de récupérer les 100 premiers sorts
        """
        return db.session.query(Sort, Source).join(Source).order_by(Sort.nom.asc()).offset((page-1)*per_page).limit(per_page).all()
    
    @staticmethod
    def get_number_of_sorts():
        """
        Permet de récupérer le nombre de sorts
        """
        return db.session.query(Sort).count()
    
    @staticmethod
    def get_liste_sort_par_nom(sort_nom):
        """
        Permet de récupérer un sort
        """
        return db.session.query(Sort, Source).join(Source).filter(Sort.nom.like(f'%{sort_nom}%')).all()
    
    @staticmethod
    def get_sort(sort_nom):
        """
        Permet de récupérer un sort
        """
        return db.session.query(Sort, Source).filter(Sort.nom == sort_nom).join(Source).first()
    
    @staticmethod
    def get_recherche_sorts_par_source():
        """
        Permet de récupérer les sources de sorts
        """
        return db.session.query(Source.nom, db.func.count(Sort.id_sort)).join(Sort).group_by(Source.nom).all()
    
    @staticmethod
    def get_number_of_sorts_par_source(source):
        """
        Permet de récupérer le nombre de sorts
        """
        return db.session.query(Sort).join(Source).filter(Source.nom == source).count()
    
    @staticmethod
    def get_liste_sorts_par_source(source, page=1, per_page=50):
        """
        Permet de récupérer les sorts par source
        """
        return db.session.query(Sort, Source).join(Source).filter(Sort.id_source == Source.id_source).filter(Source.nom == source).order_by(Sort.nom.asc()).offset((page-1)*per_page).limit(per_page).all()
    
    @staticmethod
    def get_recherche_sorts_par_ecole():
        """
        Permet de récupérer les sorts par école
        """
        return db.session.query(Sort.ecole, Sort.branche).\
            filter(Sort.ecole.notlike('%/%')).\
            filter(or_(Sort.branche.notlike('% ou %'), Sort.branche.is_(None))).\
            filter(or_(Sort.branche.notlike('%,%'), Sort.branche.is_(None))).\
            order_by(Sort.ecole.asc(), Sort.branche.asc()).\
            distinct().all()
    
    @staticmethod
    def get_number_of_sorts_par_ecole(ecole):
        """
        Permet de récupérer le nombre de sorts par école
        """
        return db.session.query(Sort).filter(Sort.ecole.like(f'%{ecole}%')).count()
    
    @staticmethod
    def get_number_of_sorts_par_ecole_branche(ecole, branche):
        """
        Permet de récupérer le nombre de sorts par école et branche
        """
        return db.session.query(Sort).filter(Sort.ecole.like(f'%{ecole}%')).filter(Sort.branche.like(f'%{branche}%')).count()
    
    @staticmethod
    def get_liste_sorts_par_ecole(ecole, page=1, per_page=50):
        """
        Permet de récupérer les sorts par école
        """
        return db.session.query(Sort, Source).join(Source).filter(Sort.ecole.like(f'%{ecole}%')).order_by(Sort.nom.asc()).offset((page-1)*per_page).limit(per_page).all()
    
    @staticmethod
    def get_liste_sorts_par_ecole_branche(ecole, branche, page=1, per_page=50):
        """
        Permet de récupérer les sorts par école
        """
        return db.session.query(Sort, Source).join(Source).filter(Sort.ecole.like(f'%{ecole}%')).filter(Sort.branche.like(f'%{branche}%')).order_by(Sort.nom.asc()).offset((page-1)*per_page).limit(per_page).all()
    
    @staticmethod
    def get_recherche_sorts_par_registre():
        """
        Permet de récupérer les registre
        """
        return db.session.query(distinct(Sort.registre)).\
    filter(Sort.registre.isnot(None)).\
    filter(~Sort.registre.like('%description%')).\
    filter(~Sort.registre.like('%texte%')).\
    filter(~Sort.registre.like('%,%')).\
    filter(~Sort.registre.like('%.%')).\
    filter(~Sort.registre.like('% ou %')).\
    order_by(Sort.registre.asc()).all()
            
    @staticmethod
    def get_number_of_sorts_par_registre(registre):
        """
        Permet de récupérer le nombre de sorts par registre
        """
        return db.session.query(Sort).filter(Sort.registre.like(f'%{registre}%')).count()
    
    @staticmethod
    def get_liste_sorts_par_registre(registre, page=1, per_page=50):
        """
        Permet de récupérer les sorts par registre
        """
        return db.session.query(Sort, Source).join(Source).filter(Sort.registre.like(f'%{registre}%')).order_by(Sort.nom.asc()).offset((page-1)*per_page).limit(per_page).all()
    
    


class DonnerSort(db.Model):
    __tablename__ = 'donner_sort'
    __table_args__ = {'schema': DB_SCHEMA}

    id_capacite = db.Column(db.ForeignKey(f'{DB_SCHEMA}.capacite.id_capacite'), primary_key=True, nullable=False)
    id_sort = db.Column(db.ForeignKey(f'{DB_SCHEMA}.sort.id_sort'), primary_key=True, nullable=False, index=True)
    nombre = db.Column(db.Integer)

    capacite = db.relationship('Capacite', primaryjoin='DonnerSort.id_capacite == Capacite.id_capacite')
    sort = db.relationship('Sort', primaryjoin='DonnerSort.id_sort == Sort.id_sort')



class AccederSort(db.Model):
    __tablename__ = 'acceder_sort'
    __table_args__ = {'schema': DB_SCHEMA}

    id_capacite_sort = db.Column(db.ForeignKey(f'{DB_SCHEMA}.capacite_sort.id_capacite_sort'), primary_key=True, nullable=False)
    id_sort = db.Column(db.ForeignKey(f'{DB_SCHEMA}.sort.id_sort'), primary_key=True, nullable=False, index=True)

    capacite_sort = db.relationship('CapaciteSort', primaryjoin='AccederSort.id_capacite_sort == CapaciteSort.id_capacite_sort')
    sort = db.relationship('Sort', primaryjoin='AccederSort.id_sort == Sort.id_sort')


class ContenirSort(db.Model):
    __tablename__ = 'contenir_sort'
    __table_args__ = {'schema': DB_SCHEMA}

    id_sort = db.Column(db.ForeignKey(f'{DB_SCHEMA}.sort.id_sort'), primary_key=True, nullable=False)
    id_domaine = db.Column(db.ForeignKey(f'{DB_SCHEMA}.domaine.id_domaine'), primary_key=True, nullable=False, index=True)
    excep_1 = db.Column(db.Integer)
    excep_2 = db.Column(db.Integer)

    domaine = db.relationship('Domaine', primaryjoin='ContenirSort.id_domaine == Domaine.id_domaine')
    sort = db.relationship('Sort', primaryjoin='ContenirSort.id_sort == Sort.id_sort')


