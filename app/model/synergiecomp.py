from model.shared_model import DB_SCHEMA, db


class SynergieCompetence(db.Model):
    __tablename__ = "synergie_competence"
    __table_args__ = {"schema": DB_SCHEMA}

    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
    )
    libelle_competence_1 = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    special = db.Column(db.String(100))

    competence = db.relationship(
        "Competence",
        primaryjoin="SynergieCompetence.libelle_competence == Competence.libelle_competence",
    )
    competence1 = db.relationship(
        "Competence",
        primaryjoin="SynergieCompetence.libelle_competence_1 == Competence.libelle_competence",
    )

    @staticmethod
    def get_all():
        return SynergieCompetence.query.all()

    @staticmethod
    def get_by_nom(nom):
        return SynergieCompetence.query.filter(
            SynergieCompetence.libelle_competence == nom
        ).all()

    @staticmethod
    def get_by_nom_inverse(nom):
        return SynergieCompetence.query.filter(
            SynergieCompetence.libelle_competence_1 == nom
        ).all()
