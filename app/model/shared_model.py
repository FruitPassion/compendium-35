# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from utils.manage_config import read_config

db = SQLAlchemy()

config = read_config("config.txt")

DB_SCHEMA = "main"


class TextPage(db.Model):
    __tabelname__ = "text_page"
    __table_args__ = {"schema": DB_SCHEMA}

    id_text_page = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)


class Alteration(db.Model):
    __tablename__ = "alteration"
    __table_args__ = {"schema": DB_SCHEMA}

    id_alteration = db.Column(db.Integer, primary_key=True)
    cout = db.Column(db.Integer)
    arme_armure = db.Column(db.Integer)


class Alignement(db.Model):
    __tablename__ = "alignement"
    __table_args__ = {"schema": DB_SCHEMA}

    id_alignement = db.Column(db.Integer, primary_key=True)
    ethique = db.Column(db.String(50))
    morale = db.Column(db.String(50))


class Archetype(db.Model):
    __tablename__ = "archetype"
    __table_args__ = {"schema": DB_SCHEMA}

    id_archetype = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    austement_niveau = db.Column(db.Integer)
    armure_naturelle = db.Column(db.Integer)
    armure_naturelle_cumulable = db.Column(db.Integer)
    armure_caracteristique = db.Column(db.String(50))
    dv = db.Column(db.String(50))
    ajustement_niveau = db.Column(db.String(50))
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Archetype.id_source == Source.id_source"
    )


class Arme(db.Model):
    __tablename__ = "arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_arme = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    surnom = db.Column(db.String(50))
    catergorie = db.Column(db.String(50))
    encombrement = db.Column(db.String(50))
    zone_critique = db.Column(db.Integer)
    critique = db.Column(db.Integer)
    facteur_portee = db.Column(db.Integer)
    effet = db.Column(db.Text)
    type_degat = db.Column(db.String(50))
    deux_mains = db.Column(db.Integer)
    metallique = db.Column(db.Integer)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship("Source", primaryjoin="Arme.id_source == Source.id_source")


class Armure(db.Model):
    __tablename__ = "armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    surnom = db.Column(db.String(50))
    categorie = db.Column(db.String(50))
    bonus = db.Column(db.Integer)
    bonus_dex_max = db.Column(db.Integer)
    malus_test = db.Column(db.Integer)
    echec_sort = db.Column(db.Integer)
    effet = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Armure.id_source == Source.id_source"
    )


class Bonu(db.Model):
    __tablename__ = "bonus"
    __table_args__ = {"schema": DB_SCHEMA}

    id_bonus = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))


class BonusCapacite(db.Model):
    __tablename__ = "bonus_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_bonus = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    valeur = db.Column(db.Integer)


class Capacite(db.Model):
    __tablename__ = "capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(50))


class CapaciteMartiale(db.Model):
    __tablename__ = "capacite_martiale"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite_martiale = db.Column(db.Integer, primary_key=True)
    niveau = db.Column(db.Integer)
    manoeuvre_connues = db.Column(db.Integer)
    manoeuvre_preparees = db.Column(db.Integer)
    posture_connues = db.Column(db.Integer)
    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), nullable=False, index=True
    )

    classe = db.relationship(
        "Classe", primaryjoin="CapaciteMartiale.id_classe == Classe.id_classe"
    )


class CapacitePsi(db.Model):
    __tablename__ = "capacite_psi"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite_psi = db.Column(db.Integer, primary_key=True)
    niveau = db.Column(db.Integer)
    point_psi_jour = db.Column(db.Integer)
    faculte_connues = db.Column(db.Integer)
    niv_faculte_max = db.Column(db.Integer)
    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), nullable=False, index=True
    )

    classe = db.relationship(
        "Classe", primaryjoin="CapacitePsi.id_classe == Classe.id_classe"
    )


class CapaciteSort(db.Model):
    __tablename__ = "capacite_sort"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite_sort = db.Column(db.Integer, primary_key=True)
    paterne = db.Column(db.String(50))
    profane_divin = db.Column(db.Boolean)


class Caracteristique(db.Model):
    __tablename__ = "caracteristique"
    __table_args__ = {"schema": DB_SCHEMA}

    id_caracteristique = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))


class Classe(db.Model):
    __tablename__ = "classe"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    bb_reflexe = db.Column(db.Integer)
    bb_vigueur = db.Column(db.Integer)
    bb_volonte = db.Column(db.Integer)
    multiplicateur_competence = db.Column(db.Integer)
    dv = db.Column(db.Integer)
    multiplicateur_argent = db.Column(db.String(50))
    description = db.Column(db.Text)
    prestige = db.Column(db.Integer)
    type_bba = db.Column(db.Integer)
    categorie = db.Column(db.String(50))
    maitriser_type_arme = db.Column(db.String(50))
    maitriser_type_armure = db.Column(db.String(50))
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Classe.id_source == Source.id_source"
    )


class Domaine(db.Model):
    __tablename__ = "domaine"
    __table_args__ = {"schema": DB_SCHEMA}

    id_domaine = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    pouvoir = db.Column(db.Text)
    exception_1 = db.Column(db.Text)
    exception_2 = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Domaine.id_source == Source.id_source"
    )


class DonAugmente(db.Model):
    __tablename__ = "don_augmente"
    __table_args__ = {"schema": DB_SCHEMA}

    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"), primary_key=True, nullable=False
    )
    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    don = db.relationship("Don", primaryjoin="DonAugmente.id_don == Don.id_don")
    competence = db.relationship(
        "Competence",
        primaryjoin="DonAugmente.libelle_competence == Competence.libelle_competence",
    )


class DonnerDon(db.Model):
    __tablename__ = "donner_don"
    __table_args__ = {"schema": DB_SCHEMA}

    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"), primary_key=True, nullable=False
    )
    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    capacite = db.relationship(
        "Capacite", primaryjoin="DonnerDon.id_capacite == Capacite.id_capacite"
    )
    don = db.relationship("Don", primaryjoin="DonnerDon.id_don == Don.id_don")


class DonnerFaculte(db.Model):
    __tablename__ = "donner_faculte"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    id_faculte = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.faculte.id_faculte"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    capacite = db.relationship(
        "Capacite", primaryjoin="DonnerFaculte.id_capacite == Capacite.id_capacite"
    )
    faculte = db.relationship(
        "Faculte", primaryjoin="DonnerFaculte.id_faculte == Faculte.id_faculte"
    )


class Effet(db.Model):
    __tablename__ = "effet"
    __table_args__ = {"schema": DB_SCHEMA}

    id_effet = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.Text)
    cout = db.Column(db.String(50))
    po_alteration = db.Column(db.Integer)
    type = db.Column(db.String(50))
    sous_type = db.Column(db.String(50))
    arme_armure = db.Column(db.Integer)


class EnchanterArme(db.Model):
    __tablename__ = "enchanter_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"), primary_key=True, nullable=False
    )
    id_effet = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.effet.id_effet"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    arme = db.relationship("Arme", primaryjoin="EnchanterArme.id_arme == Arme.id_arme")
    effet = db.relationship(
        "Effet", primaryjoin="EnchanterArme.id_effet == Effet.id_effet"
    )


class EnchanterArmure(db.Model):
    __tablename__ = "enchanter_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"), primary_key=True, nullable=False
    )
    id_effet = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.effet.id_effet"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    armure = db.relationship(
        "Armure", primaryjoin="EnchanterArmure.id_armure == Armure.id_armure"
    )
    effet = db.relationship(
        "Effet", primaryjoin="EnchanterArmure.id_effet == Effet.id_effet"
    )


class Equipement(db.Model):
    __tablename__ = "equipement"
    __table_args__ = {"schema": DB_SCHEMA}

    id_equipement = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    emplacement = db.Column(db.String(50))
    prix = db.Column(db.Integer)
    effet = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Equipement.id_source == Source.id_source"
    )


class Faculte(db.Model):
    __tablename__ = "faculte"
    __table_args__ = {"schema": DB_SCHEMA}

    id_faculte = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    signes_apparents = db.Column(db.String(50))
    temps_manif = db.Column(db.String(50))
    portee = db.Column(db.String(50))
    taille_portee = db.Column(db.String(50))
    zone_effet = db.Column(db.String(50))
    cible = db.Column(db.String(50))
    duree = db.Column(db.String(50))
    sauvegarde = db.Column(db.String(50))
    res_psion = db.Column(db.Integer)
    effet = db.Column(db.String(50))
    cout = db.Column(db.Integer)
    amelioration = db.Column(db.String(50))
    description = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Faculte.id_source == Source.id_source"
    )


class Immunite(db.Model):
    __tablename__ = "immunite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_immunite = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(50))


class Langue(db.Model):
    __tablename__ = "langue"
    __table_args__ = {"schema": DB_SCHEMA}

    id_langue = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    alphabet = db.Column(db.String(50))
    description = db.Column(db.Text)
    type = db.Column(db.String(50))


class MaitriserArme(db.Model):
    __tablename__ = "maitriser_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    arme = db.relationship("Arme", primaryjoin="MaitriserArme.id_arme == Arme.id_arme")
    classe = db.relationship(
        "Classe", primaryjoin="MaitriserArme.id_classe == Classe.id_classe"
    )


class MaitriserArmure(db.Model):
    __tablename__ = "maitriser_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    armure = db.relationship(
        "Armure", primaryjoin="MaitriserArmure.id_armure == Armure.id_armure"
    )
    classe = db.relationship(
        "Classe", primaryjoin="MaitriserArmure.id_classe == Classe.id_classe"
    )


class MaitriserCompetence(db.Model):
    __tablename__ = "maitriser_competence"
    __table_args__ = {"schema": DB_SCHEMA}

    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
    )
    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    degre_maitrise = db.Column(db.Integer)

    personnage = db.relationship(
        "Personnage",
        primaryjoin="MaitriserCompetence.id_personnage == Personnage.id_personnage",
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="MaitriserCompetence.libelle_competence == Competence.libelle_competence",
    )


class Manoeuvre(db.Model):
    __tablename__ = "manoeuvre"
    __table_args__ = {"schema": DB_SCHEMA}

    id_manoeuvre = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    ecole = db.Column(db.String(50))
    type = db.Column(db.String(50))
    niveau_req = db.Column(db.Integer)
    prerequis = db.Column(db.Integer)
    action_init = db.Column(db.String(50))
    cible = db.Column(db.String(50))
    duree = db.Column(db.String(50))
    portée = db.Column(db.String(50))
    zone_effet = db.Column(db.String(50))
    sauvegarde = db.Column(db.String(50))
    description = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Manoeuvre.id_source == Source.id_source"
    )


class Materiel(db.Model):
    __tablename__ = "materiel"
    __table_args__ = {"schema": DB_SCHEMA}

    id_materiel = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    effet = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Materiel.id_source == Source.id_source"
    )


class MesurerArme(db.Model):
    __tablename__ = "mesurer_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"), primary_key=True, nullable=False
    )
    categorie = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.taille.categorie"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    prix = db.Column(db.Integer)
    degats_des = db.Column(db.Integer)
    degats_face = db.Column(db.Integer)

    taille = db.relationship(
        "Taille", primaryjoin="MesurerArme.categorie == Taille.categorie"
    )
    arme = db.relationship("Arme", primaryjoin="MesurerArme.id_arme == Arme.id_arme")


class MesurerArmure(db.Model):
    __tablename__ = "mesurer_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"), primary_key=True, nullable=False
    )
    categorie = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.taille.categorie"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    prix = db.Column(db.Integer)
    humanoide = db.Column(db.Integer)

    taille = db.relationship(
        "Taille", primaryjoin="MesurerArmure.categorie == Taille.categorie"
    )
    armure = db.relationship(
        "Armure", primaryjoin="MesurerArmure.id_armure == Armure.id_armure"
    )


class ObtenirCapacite(db.Model):
    __tablename__ = "obtenir_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    niveau = db.Column(db.Integer)
    nombre = db.Column(db.Integer)
    frequence = db.Column(db.String(50))

    capacite = db.relationship(
        "Capacite", primaryjoin="ObtenirCapacite.id_capacite == Capacite.id_capacite"
    )
    classe = db.relationship(
        "Classe", primaryjoin="ObtenirCapacite.id_classe == Classe.id_classe"
    )


class Personnage(db.Model):
    __tablename__ = "personnage"
    __table_args__ = {"schema": DB_SCHEMA}

    id_personnage = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    background = db.Column(db.Text)
    yeux = db.Column(db.String(50))
    cheuveux = db.Column(db.String(50))
    argent = db.Column(db.Integer)
    id_alignement = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.alignement.id_alignement"),
        nullable=False,
        index=True,
    )
    id_compte = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.compte.id_compte"), nullable=False, index=True
    )
    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), nullable=False, index=True
    )

    alignement = db.relationship(
        "Alignement", primaryjoin="Personnage.id_alignement == Alignement.id_alignement"
    )
    compte = db.relationship(
        "Compte", primaryjoin="Personnage.id_compte == Compte.id_compte"
    )
    race = db.relationship("Race", primaryjoin="Personnage.id_race == Race.id_race")


class Posseder(db.Model):
    __tablename__ = "posseder"
    __table_args__ = {"schema": DB_SCHEMA}

    id_caracteristique = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.caracteristique.id_caracteristique"),
        primary_key=True,
        nullable=False,
    )
    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    caracteristique = db.relationship(
        "Caracteristique",
        primaryjoin="Posseder.id_caracteristique == Caracteristique.id_caracteristique",
    )
    personnage = db.relationship(
        "Personnage", primaryjoin="Posseder.id_personnage == Personnage.id_personnage"
    )


class PossederAlteArme(db.Model):
    __tablename__ = "posseder_alte_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"), primary_key=True, nullable=False
    )
    id_alteration = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.alteration.id_alteration"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    alteration = db.relationship(
        "Alteration",
        primaryjoin="PossederAlteArme.id_alteration == Alteration.id_alteration",
    )
    arme = db.relationship(
        "Arme", primaryjoin="PossederAlteArme.id_arme == Arme.id_arme"
    )


class PossederAlteArmure(db.Model):
    __tablename__ = "posseder_alte_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"), primary_key=True, nullable=False
    )
    id_alteration = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.alteration.id_alteration"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    alteration = db.relationship(
        "Alteration",
        primaryjoin="PossederAlteArmure.id_alteration == Alteration.id_alteration",
    )
    armure = db.relationship(
        "Armure", primaryjoin="PossederAlteArmure.id_armure == Armure.id_armure"
    )


class PossederDon(db.Model):
    __tablename__ = "posseder_don"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_domaine = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.domaine.id_domaine"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    classe = db.relationship(
        "Classe", primaryjoin="PossederDon.id_classe == Classe.id_classe"
    )
    domaine = db.relationship(
        "Domaine", primaryjoin="PossederDon.id_domaine == Domaine.id_domaine"
    )


class PossederSort(db.Model):
    __tablename__ = "posseder_sort"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_capacite_sort = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_sort.id_capacite_sort"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    niveau_sort = db.Column(db.Integer)
    niveau_debut = db.Column(db.Integer)
    par_jour_connu = db.Column(db.Integer)

    capacite_sort = db.relationship(
        "CapaciteSort",
        primaryjoin="PossederSort.id_capacite_sort == CapaciteSort.id_capacite_sort",
    )
    classe = db.relationship(
        "Classe", primaryjoin="PossederSort.id_classe == Classe.id_classe"
    )


class PrendreArchetype(db.Model):
    __tablename__ = "prendre_archetype"
    __table_args__ = {"schema": DB_SCHEMA}

    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype",
        primaryjoin="PrendreArchetype.id_archetype == Archetype.id_archetype",
    )
    personnage = db.relationship(
        "Personnage",
        primaryjoin="PrendreArchetype.id_personnage == Personnage.id_personnage",
    )


class ProfiterArme(db.Model):
    __tablename__ = "profiter_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    arme = db.relationship("Arme", primaryjoin="ProfiterArme.id_arme == Arme.id_arme")
    race = db.relationship("Race", primaryjoin="ProfiterArme.id_race == Race.id_race")


class ProfiterBonu(db.Model):
    __tablename__ = "profiter_bonus"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_bonus = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.bonus.id_bonus"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    type = db.Column(db.String(50))
    valeur = db.Column(db.Integer)
    conditions = db.Column(db.Text)

    bonu = db.relationship("Bonu", primaryjoin="ProfiterBonu.id_bonus == Bonu.id_bonus")
    race = db.relationship("Race", primaryjoin="ProfiterBonu.id_race == Race.id_race")


class ProfiterCapacite(db.Model):
    __tablename__ = "profiter_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    conditions = db.Column(db.Text)

    capacite = db.relationship(
        "Capacite", primaryjoin="ProfiterCapacite.id_capacite == Capacite.id_capacite"
    )
    race = db.relationship(
        "Race", primaryjoin="ProfiterCapacite.id_race == Race.id_race"
    )


class ProfiterCaracteristique(db.Model):
    __tablename__ = "profiter_caracteristique"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_caracteristique = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.caracteristique.id_caracteristique"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    Valeur = db.Column(db.Integer)

    caracteristique = db.relationship(
        "Caracteristique",
        primaryjoin="ProfiterCaracteristique.id_caracteristique == Caracteristique.id_caracteristique",
    )
    race = db.relationship(
        "Race", primaryjoin="ProfiterCaracteristique.id_race == Race.id_race"
    )


class ProfiterCompetence(db.Model):
    __tablename__ = "profiter_competence"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)
    type_bonus = db.Column(db.String(50))
    description = db.Column(db.String(50))
    conditions = db.Column(db.String(100))

    race = db.relationship(
        "Race", primaryjoin="ProfiterCompetence.id_race == Race.id_race"
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="ProfiterCompetence.libelle_competence == Competence.libelle_competence",
    )


class ProfiterLangue(db.Model):
    __tablename__ = "profiter_langue"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_langue = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.langue.id_langue"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    langue = db.relationship(
        "Langue", primaryjoin="ProfiterLangue.id_langue == Langue.id_langue"
    )
    race = db.relationship("Race", primaryjoin="ProfiterLangue.id_race == Race.id_race")


class ProfiterMminute(db.Model):
    __tablename__ = "profiter_mminute"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_immunite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.immunite.id_immunite"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    immunite = db.relationship(
        "Immunite", primaryjoin="ProfiterMminute.id_immunite == Immunite.id_immunite"
    )
    race = db.relationship(
        "Race", primaryjoin="ProfiterMminute.id_race == Race.id_race"
    )


class ProfiterResistance(db.Model):
    __tablename__ = "profiter_resistance"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_resistance = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.resistance.id_resistance"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    race = db.relationship(
        "Race", primaryjoin="ProfiterResistance.id_race == Race.id_race"
    )
    resistance = db.relationship(
        "Resistance",
        primaryjoin="ProfiterResistance.id_resistance == Resistance.id_resistance",
    )


class ProfiterType(db.Model):
    __tablename__ = "profiter_type"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    race = db.relationship("Race", primaryjoin="ProfiterType.id_race == Race.id_race")
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="ProfiterType.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class ProfiterVitesse(db.Model):
    __tablename__ = "profiter_vitesse"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_vitesse = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.vitesse.id_vitesse"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    race = db.relationship(
        "Race", primaryjoin="ProfiterVitesse.id_race == Race.id_race"
    )
    vitesse = db.relationship(
        "Vitesse", primaryjoin="ProfiterVitesse.id_vitesse == Vitesse.id_vitesse"
    )


class Race(db.Model):
    __tablename__ = "race"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    espece = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    ajustement_niveau = db.Column(db.Integer)
    arme_naturelle = db.Column(db.Text)
    armure_naturelle = db.Column(db.Integer)
    resistance_magie = db.Column(db.String(50))
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )
    categorie = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.taille.categorie"), nullable=False, index=True
    )

    taille = db.relationship("Taille", primaryjoin="Race.categorie == Taille.categorie")
    source = db.relationship("Source", primaryjoin="Race.id_source == Source.id_source")


class RequerirTaille(db.Model):
    __tablename__ = "requerir_taille"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    categorie = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.taille.categorie"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    minimum_maximum = db.Column(db.Boolean)

    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirTaille.id_conditions == Condition.id_conditions",
    )
    taille = db.relationship(
        "Taille", primaryjoin="RequerirTaille.categorie == Taille.categorie"
    )


class RequerirAlignement(db.Model):
    __tablename__ = "requerir_alignement"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_alignement = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.alignement.id_alignement"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    alignement = db.relationship(
        "Alignement",
        primaryjoin="RequerirAlignement.id_alignement == Alignement.id_alignement",
    )
    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirAlignement.id_conditions == Condition.id_conditions",
    )


class RequerirBonu(db.Model):
    __tablename__ = "requerir_bonus"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_bonus = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.bonus.id_bonus"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    bonu = db.relationship("Bonu", primaryjoin="RequerirBonu.id_bonus == Bonu.id_bonus")
    condition = db.relationship(
        "Condition", primaryjoin="RequerirBonu.id_conditions == Condition.id_conditions"
    )


class RequerirCapacite(db.Model):
    __tablename__ = "requerir_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"), index=True
    )

    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirCapacite.id_conditions == Condition.id_conditions",
    )
    capacite = db.relationship(
        "Capacite", primaryjoin="RequerirCapacite.id_capacite == Capacite.id_capacite"
    )


class RequerirCapacitePsi(db.Model):
    __tablename__ = "requerir_cap_psi"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_capacite_psi = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_psi.id_capacite_psi"), index=True
    )

    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirCapacitePsi.id_conditions == Condition.id_conditions",
    )
    capacite_psi = db.relationship(
        "CapacitePsi",
        primaryjoin="RequerirCapacitePsi.id_capacite_psi == CapacitePsi.id_capacite_psi",
    )


class RequerirCapaciteMartiale(db.Model):
    __tablename__ = "requerir_cap_mart"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_capacite_martiale = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_martiale.id_capacite_martiale"), index=True
    )

    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirCapaciteMartiale.id_conditions == Condition.id_conditions",
    )
    capacite_martiale = db.relationship(
        "CapaciteMartiale",
        primaryjoin="RequerirCapaciteMartiale.id_capacite_martiale == CapaciteMartiale.id_capacite_martiale",
    )


class RequerirCapaciteSort(db.Model):
    __tablename__ = "requerir_cap_sort"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_capacite_sort = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_sort.id_capacite_sort"), index=True
    )

    capacite_sort = db.relationship(
        "CapaciteSort",
        primaryjoin="RequerirCapaciteSort.id_capacite_sort == CapaciteSort.id_capacite_sort",
    )
    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirCapaciteSort.id_conditions == Condition.id_conditions",
    )


class RequerirCaracteristique(db.Model):
    __tablename__ = "requerir_caracteristique"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_caracteristique = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.caracteristique.id_caracteristique"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    caracteristique = db.relationship(
        "Caracteristique",
        primaryjoin="RequerirCaracteristique.id_caracteristique == Caracteristique.id_caracteristique",
    )
    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirCaracteristique.id_conditions == Condition.id_conditions",
    )


class RequerirClasse(db.Model):
    __tablename__ = "requerir_classe"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    niveau = db.Column(db.Integer)

    classe = db.relationship(
        "Classe", primaryjoin="RequerirClasse.id_classe == Classe.id_classe"
    )
    condition = db.relationship(
        "Condition",
        primaryjoin="RequerirClasse.id_conditions == Condition.id_conditions",
    )


class RequerirComp(db.Model):
    __tablename__ = "requerir_comp"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    degre_maitrise = db.Column(db.Integer)

    condition = db.relationship(
        "Condition", primaryjoin="RequerirComp.id_conditions == Condition.id_conditions"
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="RequerirComp.libelle_competence == Competence.libelle_competence",
    )


class RequerirDon(db.Model):
    __tablename__ = "requerir_don"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    condition = db.relationship(
        "Condition", primaryjoin="RequerirDon.id_conditions == Condition.id_conditions"
    )
    don = db.relationship("Don", primaryjoin="RequerirDon.id_don == Don.id_don")


class RequerirRace(db.Model):
    __tablename__ = "requerir_race"
    __table_args__ = {"schema": DB_SCHEMA}

    id_race = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.race.id_race"), primary_key=True, nullable=False
    )
    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    ou = db.Column(db.Boolean, default=False)

    condition = db.relationship(
        "Condition", primaryjoin="RequerirRace.id_conditions == Condition.id_conditions"
    )
    race = db.relationship("Race", primaryjoin="RequerirRace.id_race == Race.id_race")


class Resistance(db.Model):
    __tablename__ = "resistance"
    __table_args__ = {"schema": DB_SCHEMA}

    id_resistance = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    valeur = db.Column(db.Integer)


class Source(db.Model):
    __tablename__ = "source"
    __table_args__ = {"schema": DB_SCHEMA}

    id_source = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    monde = db.Column(db.String(100), nullable=False)
    systeme = db.Column(db.String(50), nullable=False)
    officiel = db.Column(db.Boolean, nullable=False)
    image = db.Column(db.String(400))


class Substituer(db.Model):
    __tablename__ = "substituer"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    id_capacite_1 = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    conditions = db.Column(db.String(50))

    capacite = db.relationship(
        "Capacite", primaryjoin="Substituer.id_capacite == Capacite.id_capacite"
    )
    capacite1 = db.relationship(
        "Capacite", primaryjoin="Substituer.id_capacite_1 == Capacite.id_capacite"
    )


class Supplement(db.Model):
    __tablename__ = "supplement"
    __table_args__ = {"schema": DB_SCHEMA}

    nom = db.Column(db.String(50), primary_key=True)
    prix = db.Column(db.Integer)
    effet = db.Column(db.Text)
    id_source = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.source.id_source"), nullable=False, index=True
    )

    source = db.relationship(
        "Source", primaryjoin="Supplement.id_source == Source.id_source"
    )


class SynergieCapacite(db.Model):
    __tablename__ = "synergie_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    special = db.Column(db.String(50))

    capacite = db.relationship(
        "Capacite", primaryjoin="SynergieCapacite.id_capacite == Capacite.id_capacite"
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="SynergieCapacite.libelle_competence == Competence.libelle_competence",
    )


class Taille(db.Model):
    __tablename__ = "taille"
    __table_args__ = {"schema": DB_SCHEMA}

    categorie = db.Column(db.String(50), primary_key=True)
    attaque = db.Column(db.Integer)
    ca = db.Column(db.Integer)
    lutte = db.Column(db.Integer)
    discretion = db.Column(db.Integer)
    allonge_h = db.Column(db.Numeric(15, 2))
    allonge_l = db.Column(db.Numeric(15, 2))


class TstBonu(db.Model):
    __tablename__ = "tst_bonus"
    __table_args__ = {"schema": DB_SCHEMA}

    id_bonus = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.bonus.id_bonus"), primary_key=True, nullable=False
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    attribut_trait = db.Column(db.Integer)

    bonu = db.relationship("Bonu", primaryjoin="TstBonu.id_bonus == Bonu.id_bonus")
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstBonu.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TstCapacite(db.Model):
    __tablename__ = "tst_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    attribut_trait = db.Column(db.Integer)

    capacite = db.relationship(
        "Capacite", primaryjoin="TstCapacite.id_capacite == Capacite.id_capacite"
    )
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstCapacite.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TstCaracRetirer(db.Model):
    __tablename__ = "tst_carac_retirer"
    __table_args__ = {"schema": DB_SCHEMA}

    id_caracteristique = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.caracteristique.id_caracteristique"),
        primary_key=True,
        nullable=False,
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    attribut_trait = db.Column(db.Integer)

    caracteristique = db.relationship(
        "Caracteristique",
        primaryjoin="TstCaracRetirer.id_caracteristique == Caracteristique.id_caracteristique",
    )
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstCaracRetirer.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TstImmunite(db.Model):
    __tablename__ = "tst_immunite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_immunite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.immunite.id_immunite"),
        primary_key=True,
        nullable=False,
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    attribut_trait = db.Column(db.Integer)

    immunite = db.relationship(
        "Immunite", primaryjoin="TstImmunite.id_immunite == Immunite.id_immunite"
    )
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstImmunite.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TstResistance(db.Model):
    __tablename__ = "tst_resistance"
    __table_args__ = {"schema": DB_SCHEMA}

    id_resistance = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.resistance.id_resistance"),
        primary_key=True,
        nullable=False,
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    attribut_trait = db.Column(db.String(50))

    resistance = db.relationship(
        "Resistance",
        primaryjoin="TstResistance.id_resistance == Resistance.id_resistance",
    )
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstResistance.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TstSpecial(db.Model):
    __tablename__ = "tst_special"
    __table_args__ = {"schema": DB_SCHEMA}

    id_tst_special = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        nullable=False,
        index=True,
    )

    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="TstSpecial.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class TypeSousType(db.Model):
    __tablename__ = "type_sous_type"
    __table_args__ = {"schema": DB_SCHEMA}

    id_type_sous_type = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    type_soustype = db.Column(db.Integer)
    description = db.Column(db.Text)
    dv = db.Column(db.String(50))


class Vitesse(db.Model):
    __tablename__ = "vitesse"
    __table_args__ = {"schema": DB_SCHEMA}

    id_vitesse = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))


class AccederFaculte(db.Model):
    __tablename__ = "acceder_faculte"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite_psi = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_psi.id_capacite_psi"),
        primary_key=True,
        nullable=False,
    )
    id_faculte = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.faculte.id_faculte"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    capacite_psi = db.relationship(
        "CapacitePsi",
        primaryjoin="AccederFaculte.id_capacite_psi == CapacitePsi.id_capacite_psi",
    )
    faculte = db.relationship(
        "Faculte", primaryjoin="AccederFaculte.id_faculte == Faculte.id_faculte"
    )


class AccederManoeuvre(db.Model):
    __tablename__ = "acceder_manoeuvre"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite_martiale = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite_martiale.id_capacite_martiale"),
        primary_key=True,
        nullable=False,
    )
    id_manoeuvre = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.manoeuvre.id_manoeuvre"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    capacite_martiale = db.relationship(
        "CapaciteMartiale",
        primaryjoin="AccederManoeuvre.id_capacite_martiale == CapaciteMartiale.id_capacite_martiale",
    )
    manoeuvre = db.relationship(
        "Manoeuvre",
        primaryjoin="AccederManoeuvre.id_manoeuvre == Manoeuvre.id_manoeuvre",
    )


class AcqeurirTaille(db.Model):
    __tablename__ = "acquerir_taille"
    __table_args__ = {"schema": DB_SCHEMA}

    categorie = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.taille.categorie"), primary_key=True, nullable=False
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    taille = db.relationship(
        "Taille", primaryjoin="AcqeurirTaille.categorie == Taille.categorie"
    )
    archetype = db.relationship(
        "Archetype", primaryjoin="AcqeurirTaille.id_archetype == Archetype.id_archetype"
    )


class Acquerir(db.Model):
    __tablename__ = "acquerir"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    niveau = db.Column(db.Integer)

    classe = db.relationship(
        "Classe", primaryjoin="Acquerir.id_classe == Classe.id_classe"
    )
    personnage = db.relationship(
        "Personnage", primaryjoin="Acquerir.id_personnage == Personnage.id_personnage"
    )


class AcquerirCapacite(db.Model):
    __tablename__ = "acquerir_capacite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype",
        primaryjoin="AcquerirCapacite.id_archetype == Archetype.id_archetype",
    )
    capacite = db.relationship(
        "Capacite", primaryjoin="AcquerirCapacite.id_capacite == Capacite.id_capacite"
    )


class AcquerirImmunite(db.Model):
    __tablename__ = "acquerir_immunite"
    __table_args__ = {"schema": DB_SCHEMA}

    id_immunite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.immunite.id_immunite"),
        primary_key=True,
        nullable=False,
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype",
        primaryjoin="AcquerirImmunite.id_archetype == Archetype.id_archetype",
    )
    immunite = db.relationship(
        "Immunite", primaryjoin="AcquerirImmunite.id_immunite == Immunite.id_immunite"
    )


class AcquerirLangue(db.Model):
    __tablename__ = "acquerir_langue"
    __table_args__ = {"schema": DB_SCHEMA}

    id_langue = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.langue.id_langue"), primary_key=True, nullable=False
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype", primaryjoin="AcquerirLangue.id_archetype == Archetype.id_archetype"
    )
    langue = db.relationship(
        "Langue", primaryjoin="AcquerirLangue.id_langue == Langue.id_langue"
    )


class AcquerirResistance(db.Model):
    __tablename__ = "acquerir_resistance"
    __table_args__ = {"schema": DB_SCHEMA}

    id_resistance = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.resistance.id_resistance"),
        primary_key=True,
        nullable=False,
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype",
        primaryjoin="AcquerirResistance.id_archetype == Archetype.id_archetype",
    )
    resistance = db.relationship(
        "Resistance",
        primaryjoin="AcquerirResistance.id_resistance == Resistance.id_resistance",
    )


class AcquerirType(db.Model):
    __tablename__ = "acquerir_type"
    __table_args__ = {"schema": DB_SCHEMA}

    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
    )
    id_type_sous_type = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.type_sous_type.id_type_sous_type"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    archetype = db.relationship(
        "Archetype", primaryjoin="AcquerirType.id_archetype == Archetype.id_archetype"
    )
    type_sous_type = db.relationship(
        "TypeSousType",
        primaryjoin="AcquerirType.id_type_sous_type == TypeSousType.id_type_sous_type",
    )


class AcquerirVitesse(db.Model):
    __tablename__ = "acquerir_vitesse"
    __table_args__ = {"schema": DB_SCHEMA}

    id_vitesse = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.vitesse.id_vitesse"),
        primary_key=True,
        nullable=False,
    )
    id_archetype = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.archetype.id_archetype"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    prendre = db.Column(db.Integer)

    archetype = db.relationship(
        "Archetype",
        primaryjoin="AcquerirVitesse.id_archetype == Archetype.id_archetype",
    )
    vitesse = db.relationship(
        "Vitesse", primaryjoin="AcquerirVitesse.id_vitesse == Vitesse.id_vitesse"
    )


class Ajouter(db.Model):
    __tablename__ = "ajouter"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"), primary_key=True, nullable=False
    )
    nom = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.supplement.nom"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    armure = db.relationship(
        "Armure", primaryjoin="Ajouter.id_armure == Armure.id_armure"
    )
    supplement = db.relationship(
        "Supplement", primaryjoin="Ajouter.nom == Supplement.nom"
    )


class AjouterBonus(db.Model):
    __tablename__ = "ajouter_bonus"
    __table_args__ = {"schema": DB_SCHEMA}

    id_capacite = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.capacite.id_capacite"),
        primary_key=True,
        nullable=False,
    )
    id_bonus = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.bonus_capacite.id_bonus"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    bonus_capacite = db.relationship(
        "BonusCapacite", primaryjoin="AjouterBonus.id_bonus == BonusCapacite.id_bonus"
    )
    capacite = db.relationship(
        "Capacite", primaryjoin="AjouterBonus.id_capacite == Capacite.id_capacite"
    )


class Alternatif(db.Model):
    __tablename__ = "alternatif"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_classe_1 = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    classe = db.relationship(
        "Classe", primaryjoin="Alternatif.id_classe == Classe.id_classe"
    )
    classe1 = db.relationship(
        "Classe", primaryjoin="Alternatif.id_classe_1 == Classe.id_classe"
    )


class Apprendre(db.Model):
    __tablename__ = "apprendre"
    __table_args__ = {"schema": DB_SCHEMA}

    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"), primary_key=True, nullable=False
    )
    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    don = db.relationship("Don", primaryjoin="Apprendre.id_don == Don.id_don")
    personnage = db.relationship(
        "Personnage", primaryjoin="Apprendre.id_personnage == Personnage.id_personnage"
    )


class ComposerArme(db.Model):
    __tablename__ = "composer_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"), primary_key=True, nullable=False
    )
    id_materiel = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.materiel.id_materiel"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    arme = db.relationship("Arme", primaryjoin="ComposerArme.id_arme == Arme.id_arme")
    materiel = db.relationship(
        "Materiel", primaryjoin="ComposerArme.id_materiel == Materiel.id_materiel"
    )


class ComposerArmure(db.Model):
    __tablename__ = "composer_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"), primary_key=True, nullable=False
    )
    id_materiel = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.materiel.id_materiel"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    armure = db.relationship(
        "Armure", primaryjoin="ComposerArmure.id_armure == Armure.id_armure"
    )
    materiel = db.relationship(
        "Materiel", primaryjoin="ComposerArmure.id_materiel == Materiel.id_materiel"
    )


class ConditionClasse(db.Model):
    __tablename__ = "condition_classe"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    classe = db.relationship(
        "Classe", primaryjoin="ConditionClasse.id_classe == Classe.id_classe"
    )
    condition = db.relationship(
        "Condition",
        primaryjoin="ConditionClasse.id_conditions == Condition.id_conditions",
    )


class ConditionDon(db.Model):
    __tablename__ = "condition_don"
    __table_args__ = {"schema": DB_SCHEMA}

    id_conditions = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.conditions.id_conditions"),
        primary_key=True,
        nullable=False,
    )
    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    condition = db.relationship(
        "Condition", primaryjoin="ConditionDon.id_conditions == Condition.id_conditions"
    )
    don = db.relationship("Don", primaryjoin="ConditionDon.id_don == Don.id_don")


class ContenirCompetence(db.Model):
    __tablename__ = "contenir_competence"
    __table_args__ = {"schema": DB_SCHEMA}

    id_classe = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.classe.id_classe"), primary_key=True, nullable=False
    )
    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    classe = db.relationship(
        "Classe", primaryjoin="ContenirCompetence.id_classe == Classe.id_classe"
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="ContenirCompetence.libelle_competence == Competence.libelle_competence",
    )


class Dependre(db.Model):
    __tablename__ = "dependre"
    __table_args__ = {"schema": DB_SCHEMA}

    libelle_competence = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.competence.libelle_competence"),
        primary_key=True,
        nullable=False,
    )
    id_technique_astucieuse = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.technique_astucieuse.id_technique_astucieuse"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    valeur = db.Column(db.Integer)

    technique_astucieuse = db.relationship(
        "TechniqueAstucieuse",
        primaryjoin="Dependre.id_technique_astucieuse == TechniqueAstucieuse.id_technique_astucieuse",
    )
    competence = db.relationship(
        "Competence",
        primaryjoin="Dependre.libelle_competence == Competence.libelle_competence",
    )


class DetenirArme(db.Model):
    __tablename__ = "detenir_arme"
    __table_args__ = {"schema": DB_SCHEMA}

    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
    )
    id_arme = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.arme.id_arme"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    Porter = db.Column(db.Integer)

    arme = db.relationship("Arme", primaryjoin="DetenirArme.id_arme == Arme.id_arme")
    personnage = db.relationship(
        "Personnage",
        primaryjoin="DetenirArme.id_personnage == Personnage.id_personnage",
    )


class DetenirArmure(db.Model):
    __tablename__ = "detenir_armure"
    __table_args__ = {"schema": DB_SCHEMA}

    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
    )
    id_armure = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.armure.id_armure"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    porter = db.Column(db.Integer)

    armure = db.relationship(
        "Armure", primaryjoin="DetenirArmure.id_armure == Armure.id_armure"
    )
    personnage = db.relationship(
        "Personnage",
        primaryjoin="DetenirArmure.id_personnage == Personnage.id_personnage",
    )


class DetenirEquipement(db.Model):
    __tablename__ = "detenir_equipement"
    __table_args__ = {"schema": DB_SCHEMA}

    id_equipement = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.equipement.id_equipement"),
        primary_key=True,
        nullable=False,
    )
    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    porter = db.Column(db.Integer)

    equipement = db.relationship(
        "Equipement",
        primaryjoin="DetenirEquipement.id_equipement == Equipement.id_equipement",
    )
    personnage = db.relationship(
        "Personnage",
        primaryjoin="DetenirEquipement.id_personnage == Personnage.id_personnage",
    )


class ApprendreTechnique(db.Model):
    __tablename__ = "apprendre_technique"
    __table_args__ = {"schema": DB_SCHEMA}

    id_personnage = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.personnage.id_personnage"),
        primary_key=True,
        nullable=False,
    )
    id_technique_astucieuse = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.technique_astucieuse.id_technique_astucieuse"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    personnage = db.relationship(
        "Personnage",
        primaryjoin="ApprendreTechnique.id_personnage == Personnage.id_personnage",
    )
    technique_astucieuse = db.relationship(
        "TechniqueAstucieuse",
        primaryjoin="ApprendreTechnique.id_technique_astucieuse == TechniqueAstucieuse.id_technique_astucieuse",
    )


class DonAppartenirCategorie(db.Model):
    __tablename__ = "don_appartenir_categorie"
    __table_args__ = {"schema": DB_SCHEMA}

    id_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.don.id_don"), primary_key=True, nullable=False
    )
    id_categorie_don = db.Column(
        db.ForeignKey(f"{DB_SCHEMA}.categorie_don.id_categorie_don"),
        primary_key=True,
        nullable=False,
        index=True,
    )

    don = db.relationship(
        "Don", primaryjoin="DonAppartenirCategorie.id_don == Don.id_don"
    )
    categorie_don = db.relationship(
        "CategorieDon",
        primaryjoin="DonAppartenirCategorie.id_categorie_don == CategorieDon.id_categorie_don",
    )
