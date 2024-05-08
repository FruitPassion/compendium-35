from model.shared_model import DB_SCHEMA, db


class PossederRole(db.Model):
    __tablename__ = 'posseder_role'
    __table_args__ = {'schema': DB_SCHEMA}

    id_compte = db.Column(db.ForeignKey(f'{DB_SCHEMA}.compte.id_compte'), primary_key=True, nullable=False)
    id_role = db.Column(db.ForeignKey(f'{DB_SCHEMA}.role.id_role'), primary_key=True, nullable=False, index=True)

    compte = db.relationship('Compte', primaryjoin='PossederRole.id_compte == Compte.id_compte')
    role = db.relationship('Role', primaryjoin='PossederRole.id_role == Role.id_role')
    
    
    @staticmethod
    def set_role(id_compte, id_role):
        """
        Ajoute un role à un compte
        
        :param pseudo: le pseudo
        :param id_role: l'id du role à ajouter
        :return: None
        """
        possederole = PossederRole(id_compte=id_compte, id_role=id_role)
        db.session.add(possederole)
        db.session.commit()
        
    
    @staticmethod
    def remove_role(id_compte, id_role):
        """
        Ajoute un role à un compte
        
        :param pseudo: le pseudo
        :param id_role: l'id du role à ajouter
        :return: None
        """
        possederole = PossederRole(id_compte=id_compte, id_role=id_role)
        db.session.add(possederole)
        db.session.commit()