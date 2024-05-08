from utils.app_security import compare_passwords, encrypt_password
from model.shared_model import DB_SCHEMA, db


class Compte(db.Model):
    __tablename__ = 'compte'
    __table_args__ = {'schema': DB_SCHEMA}

    id_compte = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(50))
    mdp = db.Column(db.Text)
    creation = db.Column(db.Date)
    
    
    @staticmethod
    def get_compte_par_pseudo(pseudo):
        """
        Retournne le compte à partir de son pseudo
        
        :param pseudo: le pseudo du compte
        :return: classe compte
        """
        return Compte.query.with_entities(Compte.pseudo, Compte.id_compte).filter_by(pseudo=pseudo).first()

    @staticmethod
    def verifier_compte(pseudo):
        """
        Vérifie si le compte existe
        
        :param pseudo: le pseudo
        :return: le compte s'il existe, None sinon
        """
        return Compte.query.filter_by(pseudo=pseudo).first() is not None
    
    
    @staticmethod
    def verifier_mdp(pseudo, mdp):
        """
        Vérifie si le mot de passe est correct
        
        :param pseudo: le pseudo
        :param mdp: le mot de passe
        :return: True si le mot de passe est correct, False sinon
        """
        compte = Compte.query.filter_by(pseudo=pseudo).first()
        if compte is not None:
            return compare_passwords(mdp, compte.mdp)
        return False
    
    
    @staticmethod
    def creer_compte(pseudo, mdp):
        """
        Crée un compte
        
        :param pseudo: le pseudo
        :param mdp: le mot de passe
        :return: l'id du compte créé
        """
        mdp = encrypt_password(mdp)
        compte = Compte(pseudo=pseudo, mdp=mdp)
        db.session.add(compte)
        db.session.commit()
        
        return compte.id_compte