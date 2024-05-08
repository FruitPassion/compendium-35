from model.condition import Condition


def builder_condition_don(id_don):
    """
    Permet de creer la liste des conditions pour un don

    :param id_don: int
    :return: list
    """
    conditions = Condition.get_conditions_don(id_don)
    liste_conditions = []
    for condition in conditions:
        if condition[1] is not None:
            liste_conditions.append(
                "<li>Classe <a href='/classes/{}'>{}</a></li>".format(
                    condition[1].nom, condition[1].nom
                )
            )

        if condition[3] is not None:
            liste_conditions.append(
                "<li>{} {}</li>".format(condition[3].nom, condition[2].valeur)
            )

        if condition[4] is not None:
            liste_conditions.append(
                "<li>Necessite le don <a href='/dons/{}'>{}</a></li>".format(
                    condition[4].nom, condition[4].nom
                )
            )

        if condition[5] is not None:
            liste_conditions.append(
                "<li>Aptitude de classe de <a href='/capacites/classe/{}'>{}</a></li>".format(
                    condition[5].nom, condition[5].nom
                )
            )

        if condition[7] is not None:
            liste_conditions.append(
                "<li>Bonus au {} de +{}</li>".format(
                    condition[7].nom, condition[6].valeur
                )
            )

        if condition[9] is not None:
            if condition[8].ou == 1:
                soit = "Soit race"
            else:
                soit = "Race"
            liste_conditions.append(
                "<li>{} <a href='/races/{}'>{}</a></li>".format(
                    soit, condition[9].nom, condition[9].nom
                )
            )

        if condition[11] is not None:
            liste_conditions.append(
                "<li>Degré de maîtrise de {} en <a href='/competences/{}'>{}</a></li>".format(
                    condition[10].degre_maitrise,
                    condition[11].libelle_competence,
                    condition[11].libelle_competence,
                )
            )

        if condition[12] is not None:
            liste_conditions.append(
                "<li>Capacité martiale <a href='/capacites/martial/{}'>{}</a></li>".format(
                    condition[12].nom, condition[12].nom
                )
            )

        if condition[13] is not None:
            liste_conditions.append(
                "<li>Capacité psi <a href='/capacites/faculte/{}'>{}</a></li>".format(
                    condition[13].nom, condition[13].nom
                )
            )

        if condition[14] is not None:
            liste_conditions.append(
                "<li>Capacité sort <a href='/capacites/sort/{}'>{}</a></li>".format(
                    condition[14].nom, condition[14].nom
                )
            )

        if condition[15] is not None:
            liste_conditions.append(
                "<li>Alignement {} {}</li>".format(
                    condition[16].ethique, condition[16].morale
                )
            )

        if condition[17] is not None:
            if (
                condition[16].minimum_maximum is not None
                and condition[16].minimum_maximum == 0
            ):
                taille = "ou supérieur"
            elif (
                condition[16].minimum_maximum is not None
                and condition[16].minimum_maximum == 1
            ):
                taille = "ou inferieur"
            else:
                taille = ""
            liste_conditions.append(
                "<li>Taille {} {}</li>".format(condition[17].categorie, taille)
            )

        if condition[0].special:
            liste_conditions.append("<li>{}</li>".format(condition[0].special))

    liste_conditions = list(dict.fromkeys(liste_conditions))
    return liste_conditions
