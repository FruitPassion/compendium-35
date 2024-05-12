INSERT INTO role (libelle, couleur)
VALUES ('Administrateur', '#8552b7'),
('Utilisateur', '#64e059');

INSERT INTO alignement (ethique, morale)
VALUES ('Loyal', 'Bon'),
 ('Loyal', 'Neutre'),
 ('Loyal', 'Mauvais'),
 ('Neutre', 'Bon'),
 ('Neutre', 'Absolue'),
 ('Neutre', 'Mauvais'),
 ('Chaotique', 'Bon'),
 ('Chaotique', 'Neutre'),
 ('Chaotique', 'Mauvais'),
 ('Aucun', 'Aucun');

INSERT INTO caracteristique (nom)
VALUES ('Force'),
 ('Dextérité'),
 ('Constitution'),
 ('Intelligence'),
 ('Sagesse'),
 ('Charisme'),
 ('Aucune');

INSERT INTO taille (categorie, attaque, ca, lutte, discretion, allonge_h, allonge_l)
VALUES ('Infime', 8, 8, -16, 16, 0, 0),
 ('Minuscule', 4, 4, -12, 12, 0, 0),
 ('Très petite', 2, 2, -8, 8, 0, 0),
 ('Petite', 1, 1, -4, 4, 1.5, 0),
 ('Moyen', 0, 0, 0, 0, 1.50, 1.50),
 ('Grande', -1, -1, 4, -4, 3, 1.5),
 ('Très Grande', -2, -2, 8, -8, 4.5, 3),
 ('Gigantesque', -4, -4, 12, -12, 6, 4.5),
 ('Colosalle', -8, -8, 16, -16, 9, 6);

INSERT INTO vitesse (type)
VALUES ('Sol'),
 ('Vol'),
 ('Nage');

INSERT INTO competence (libelle_competence, innee, malus_armure, description_courte, description_longue, id_caracteristique) VALUES
('Acrobaties',0,1,'Le personnage peut exécuter roulés-boulés, sauts périlleux et autres cabrioles.','<h5>Test de compétence</h5> <p>Le personnage atterrit sur ses pieds ou exécute un roulé-boulé lui permettant de se retrouver derrière l’ennemi. Il peut enchaîner les flips et autres sauts périlleux pour distraire un public (comme avec la compétence Représentation). Les DD des différentes tâches associées à la compétence Acrobatie sont donnés sur la table suivante.</p> <table><caption>Tableau : Tests d’Acrobaties</caption><thead>  <tr> <th>Tâche</th> <th>DD</th>  </tr></thead><tbody>  <tr> <td>Amortir sa chute (dont les dégâts sont calculés en retirant 3 mètres à la hauteur totale).</td> <td>15</td>  </tr>  <tr> <td>Pendant un mouvement normal, enchaîner les acrobaties (roulés-boulés, sauts, etc.) à la moitié de sa vitesse de déplacement habituelle sans que ce déplacement ne provoque d’attaque d’opportunité. Un test est nécessaire pour chaque adversaire à portée duquel le personnage passe (le joueur choisit l’ordre des tests en cas d’égalité). Chaque ennemi au-delà du premier augmente de DD de +2.</td> <td>15</td>  </tr>  <tr> <td>Pendant un mouvement normal, enchaîner les acrobaties à la moitié de sa vitesse de déplacement habituelle en traversant l’espace occupé par un adversaire (en passant à côté de lui, au-dessus, entre ses jambes) sans que cela ne provoque d’attaque d’opportunité. En cas d’échec, le personnage s’arrête juste devant l’espace occupé par l’adversaire et la manœuvre déclenche les attaques d’opportunité normales. Un test est nécessaire pour chaque adversaire. Chaque ennemi au-delà du premier augmente de DD de +2.</td> <td>25</td>  </tr>  <tr> <td>Pendant un mouvement normal, enchaîner les acrobaties à la moitié de sa vitesse de déplacement habituelle en traversant l’espace occupé par un adversaire (en passant à côté de lui, au-dessus, entre ses jambes) sans que cela ne provoque d’attaque d’opportunité. En cas d’échec, le personnage s’arrête juste devant l’espace occupé par l’adversaire et la manœuvre déclenche les attaques d’opportunité normales. Un test est nécessaire pour chaque adversaire. Chaque ennemi au-delà du premier augmente de DD de +2.</td> <td>25</td>  </tr></tbody> </table>  <p>Il est plus difficile de faire des acrobaties sur une surface encombrée ou dangereuse, comme le sol d’une caverne naturelle ou des taillis. Lorsque le personnage traverse un carré de ce type, le DD du test d’Acrobaties est alors modifié selon les données de la table suivante.</p> <table><caption>Tableau : Modificateurs de surface</caption><thead>  <tr> <th>La surface est...</th> <th>Modificateur au DD</th>  </tr></thead><tbody>  <tr> <td>Légèrement encombrée (éboulement, décombres épars, tourbière, taillis)</td> <td>+2</td>  </tr>  <tr> <td>Très encombrée (sol d’une caverne naturelle, décombres nombreux, taillis épais)</td> <td>+5</td>  </tr>  <tr> <td>Légèrement glissant (sol humide)</td> <td>+2</td>  </tr>  <tr> <td>Très glissant (verglas)</td> <td>+5</td>  </tr>  <tr> <td>Sol en pente ou abrupt</td> <td>+2</td>  </tr></tbody> </table><h5>Enchaînement d’acrobaties accéléré</h5> <p>Un personnage peut enchaîner les acrobaties à côté ou à travers les rangs ennemis plus rapidement, mais au prix d’un malus de –10 sur son test d’Acrobaties. Il peut alors se déplacer à sa vitesse normale (au lieu de la moitié de cette vitesse).</p> <h5>Action <p>Sans objet. Les acrobaties se font en même temps qu’un déplacement, et les tests d’Acrobaties font donc partie d’une action de mouvement.</p> <h5>Nouvelles tentatives <p>Généralement non. Un public qui a jugé défavorablement un acrobate n’a aucune chance d’être conquis par la suite. On ne peut tenter d’amortir sa chute qu’une fois par chute.</p> <h5>Spécial</h5> <p>Un personnage ayant un degré de maîtrise de 5 en Acrobaties bénéficie d’un bonus d’esquive de +3 à la CA lorsqu’il décide de combattre défensivement, au lieu du bonus normal de +2 (voir Combattre sur la défensive). <br> De même, tout personnage ayant un degré de maîtrise de 5 en Acrobaties bénéficie d’un bonus d’esquive de +6 à la CA lorsqu’il décide de se mettre en défense totale, au lieu du bonus normal de +4 (voir Défense totale).</p>', 2),
('Art de la magie',0,0,'Cette compétence sert à identifier les sorts actifs, mais aussi ceux que les autres personnages sont en train de lancer.','<h5>Test de compétence</h5> <p>L’utilisation de cette compétence permet d’identifier sorts et effets magiques. Les DD des tests associés à différentes tâches sont indiqués sur la table suivante.</p> <table><caption>Tableau : Art de la magie</caption><thead>  <tr> <th>Tâche</th> <th>DD d’Art de la magie</th>  </tr></thead><tbody><tr>  <td>Identifier un glyphe de garde à l’aide de lecture de la magie. Pas d’action nécessaire.</td>  <td>13</td></tr><tr>  <td>Reconnaître un sort à l’incantation (il faut voir la composante gestuelle ou entendre la composante verbale). Pas d’action nécessaire. Une seule tentative.</td>  <td>15 + niveau du sort</td></tr><tr>  <td>Apprendre un sort à partir d’un parchemin ou d’un grimoire (magiciens uniquement). Pas de nouvelle tentative avant que le degré de maîtrise d’Art de la magie n’ait augmenté de 1 (même si le personnage découvre une autre source proposant le même sort). Huit heures de travail.</td>  <td>15 + niveau du sort</td></tr><tr>  <td>Préparer un sort à partir d’un grimoire emprunté (magiciens uniquement). Une seule tentative par jour et par sort. Pas de temps supplémentaire nécessaire.</td>  <td>15 + niveau du sort</td></tr><tr>  <td>Déterminer l’école de magie associée à l’aura que l’on distingue autour des créatures et des objets en lançant détection de la magie. (Si l’aura ne provient pas d’un sort, le DD est égal à 15 + moitié du niveau de lanceur de sorts du créateur de l’effet.) Pas d’action nécessaire.</td>  <td>15 + niveau du sort</td></tr><tr>  <td>Identifier un symbole à l’aide de lecture de la magie.</td>  <td>19</td></tr><tr>  <td>Identifier un sort faisant déjà effet (le personnage doit le voir ou détecter ses effets) Pas d’action nécessaire. Une seule tentative.</td>  <td>20 + niveau du sort</td></tr><tr>  <td>Identifier les objets ou matériaux créés par magie (par exemple, comprendre qu’un mur métallique a été obtenu grâce au sort mur de fer ). Pas d’action nécessaire. Une seule tentative.</td>  <td>20 + niveau du sort</td></tr><tr>  <td>Déchiffrer un sort écrit (par exemple, sur un parchemin) sans avoir recours à lecture de la magie. Une tentative par jour. Nécessite une action complexe.</td>  <td>20 + niveau du sort</td></tr><tr>  <td>Identifier un sort ciblé sur le personnage après avoir joué un jet de sauvegarde contre ce sort. Pas d’action nécessaire. Une seule tentative</td>  <td>25 + niveau du sort</td></tr><tr>  <td>Identifier une potion. Une minute de travail. Une seule tentative.</td>  <td>25</td></tr><tr>  <td>Tracer un graphe permettant de lancer une ancre dimensionnelle sur un cercle magique. Dix minutes de travail. Une seule tentative. Test joué en secret.</td>  <td>20</td></tr><tr>  <td>Comprendre un effet magique étrange ou unique, comme celui que produirait par exemple une rivière de magie pure. Temps de travail variable. Une seule tentative.</td>  <td>30 ou plus</td></tr></tbody> </table> <h5>Action</h5> <p>Variable, selon la table précédente.</p> <h5>Nouvelles tentatives</h5> <p>Voir ci-dessus.</p> <h5>Spécial</h5> <p>Les magiciens spécialisés bénéficient d’un bonus de +2 au test de compétence lorsqu’ils sont en présence d’un sort de leur école de prédilection. En revanche, ils subissent un malus de –5 si le sort provient d’une école qui leur est interdite (dans ce cas, certaines possibilités leur sont même refusées, comme apprendre le sort en question).<br> De plus, certains sorts permettent d’obtenir des informations supplémentaires sur la magie à condition de réussir un test d’Art de la magie Lorsque c’est le cas, ces indications sont données dans la description du sort (voir par exemple détection de la magie).</p>',4),
('Art martial',0,0,"Cette compétence sert à identifier les manoeuvres dès qu'elles sont initiées.","<h5>Test de compétence.</h5>\n<p>L’utilisation de cette compétence permet d’identifier les manœuvres et disciplines utilisées par un combattant. Les DD des tests associés à différentes tâches sont indiqués sur la table suivante.</p>\n\n<table>\n  <caption>Test de compétence</caption>\n  <thead>\n <tr>\n<th>Tâche</th>\n<th>DD d’Art martial</th>\n </tr>\n  </thead>\n  <tbody>\n <tr>\n<td>Identifier une manoeuvre lorsqu'elle est initiée par quelqu\'un (il faut être capable de voir l\'adepte martial). Pas d’action nécessaire. Une seule tentative.</td>\n<td>10 + niveau de la manoeuvre</td>\n </tr>\n <tr>\n<td>Identifier une manoeuvre inscrite sur un script martial. Nécessite un round entier. Une seule tentative par jour.</td>\n<td>10 + niveau de la manoeuvre</td>\n </tr>\n <tr>\n<td>Déterminer l\'ensemble des disciplines connues par un adepte martial en le voyant initier une manoeuvre. Pas d\'action. Nouvelle tentative uniquement si l\'adepte martial initie une nouvelle manoeuvre.</td>\n<td>20 + niveau de la manoeuvre</td>\n </tr>\n  </tbody>\n</table>\n\n<h5>Action</h5>\n<p>Variable selon la tâche précédente.</p>\n<h5>Nouvelles tentatives</h5>\n<p>Voir ci-dessus.</p>\n<h5>Spécial</h5>\n<p>Un savant martial bénéficie d\'un bonus de +2 pour identifier une manoeuvre de sa discipline de prédilection.</p>",4),
('Art psi',0,0,'Cette compétence sert à identifier les facultés actives, mais aussi celles que les autres personnages sont en train de manifester.',"<h5>Test de compétence</h5>\n<p>L'utilisation de cette compétence permet d\'identifier facultés et effets psioniques. Les DD des tests associés à différentes tâches sont indiqués sur la table suivante.</p>\n\n<table>\n  <caption>Test de compétence d\'Art psi</caption>\n  <thead>\n <tr>\n<th>Tâche</th>\n<th>DD d\'Art psi</th>\n </tr>\n  </thead>\n  <tbody>\n <tr>\n<td>Reconnaître une faculté au cours de sa manifestation (il faut percevoir le signe apparent de la faculté ou voir quelque effet visible pour pouvoir identifier la faculté).</td>\n<td>15 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>Déterminer la discipline associée à l\'aura que l\'on distingue autour des créatures et des objets en lançant détection psionique. (Si l\'aura ne provient pas d\'une faculté, le DD est égal à 15 + moitié du niveau de manifestation du créateur de l\'effet.)</td>\n<td>15 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>S\'adresser à une pierre psionique pour déterminer la (ou les) faculté qu\'elle abrite.</td>\n<td>15 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>Identifier une faculté faisant déjà effet (le personnage doit la voir ou détecter ses effets).</td>\n<td>20 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>Identifier les objets ou matériaux créés ou modelés par effet psionique (par exemple, comprendre qu\'un objet particulier a été obtenu grâce à une faculté de métacréation).</td>\n<td>20 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>Identifier une faculté ciblée sur le personnage après avoir joué un jet de sauvegarde contre elle.</td>\n<td>25 + niveau de la faculté</td>\n </tr>\n <tr>\n<td>Identifier un tatouage psionique.</td>\n<td>25</td>\n </tr>\n <tr>\n<td>Tracer un graphe pour optimiser la manifestation d\'une ancre dimensionnelle psionique sur une créature convoquée.</td>\n<td>20</td>\n </tr>\n <tr>\n<td>Comprendre un effet psionique étrange ou unique, comme celui que produirait par exemple une saillie de cristalà résonance psionique.</td>\n<td>30 ou plus</td>\n </tr>\n  </tbody>\n</table>\n\n<p>De plus, certaines facultés permettent aux personnages d\'obtenir des renseignements sur les effets psioniques, à condition de réussir un test d\'Art psi conformément à ce qui est indiqué dans la description de la faculté.</p>\n\n<h5>Actions</h5>\n<p>Variable, selon la table précédente.</p>\n<h5>Nouvelles tentatives</h5>\n<p>Variable, selon la table précédente.</p>\n<h5>Spécial</h5>\n<p>Les psions bénéficient d\'un bonus de +2 au test de compétence lorsqu\'ils sont en présence d\'une faculté de leur discipline.</p>",4),
('Artisanat', 1, 0, 'Le personnage a appris un métier artisanal ou un art, comme par exemple l''alchimie, la calligraphie, fabrication d''arcs et de flèches etc.', '<p>completer</p>', 4),
('Bluff', 1, 0, 'Cette compétence permet de faire croire les propositions les plus extravagantes qui soient et de parler par sous-entendus ou mots de codes pour transmettre des messages secrets.', '<p>completer</p>', 6),
('Concentration', 1, 0, 'Le personnage est particulièrement doué pour arriver à se concentrer en toutes circonstances.', '<p>completer</p>', 3),
('Connaissance (Architecture et Ingénierie)', 0, 0, 'Vous pouvez identifier des bâtiments, aqueducs, ponts, fortifications', '<p>completer</p>', 4),
('Connaissance (Exploration souterraine)', 0, 0, 'Vous pouvez identifier des aberrations, cavernes, vases, spéléologie', '<p>completer</p>', 4),
('Connaissance (Folklore local)', 0, 0, 'Vous pouvez identifier des légendes, personnalités pittoresques, habitants, lois et traditions, coutumes, humanoïdes', '<p>completer</p>', 4),
('Connaissance (Géographie)', 0, 0, 'Vous pouvez identifier des pays, types de terrain, climat, peuples ', '<p>completer</p>', 4),
('Connaissance (Histoire)', 0, 0, 'Vous pouvez identifier des dynasties, guerres, colonies, migrations, fondation des villes et des pays', '<p>completer</p>', 4),
('Connaissance (Mystères)', 0, 0, 'Vous pouvez identifier des créatures artificielles, créatures magiques, dragons, mystères anciens, phrases incompréhensibles, symboles ésotériques, traditions magiques', '<p>completer</p>', 4),
('Connaissance (Nature)', 0, 0, 'Vous pouvez identifier des animaux, climat, cycles et saisons, fées, géants, humanoïdes monstrueux, plantes, vermines ', '<p>completer</p>', 4),
('Connaissance (Noblesse et Royauté)', 0, 0, 'Vous pouvez identifier des lignées, héraldique, coutumes, arbres généalogiques, devises, personnalités ', '<p>completer</p>', 4),
('Connaissance (Plans)', 0, 0, 'Vous pouvez identifier des plans extérieurs, plans intérieurs, plan Astral, plan Éthéré, Extérieurs, élémentaires, la magie et les plans', '<p>completer</p>', 4),
('Connaissance (Psionnique)', 0, 0, 'Vous pouvez identifier des tradition psionique, symboles psychiques, des expressions énigmatiques, créations astrales, races psioniques,.monstres psioniques et leurs pouvoirs spéciaux et vulnérabilités', '<p>completer</p>', 4),
('Connaissance (Religion)', 0, 0, 'Vous pouvez identifier des dieux et déesses, mythologie, tradition ecclésiastique, symboles sacrés, morts-vivants.', '<p>completer</p>', 4),
('Contrefaçon', 1, 0, 'Vous pouvez imiter des documents.', '<p>completer</p>', 4),
('Crochetage', 0, 0, 'Vous pouvez ouvrir des serrures et des mécanismes verrouillés.', '<p>completer</p>', 2),
('Décryptage', 0, 0, 'Vous pouvez déchiffrer les runes anciennes ou des textes dans une langue inconnue.', '<p>completer</p>', 4),
('Déguisement', 1, 0, 'Vous pouvez modifier l''aspect du personnage ou celui de quelqu''un d''autre.', '<p>completer</p>', 6),
('Déplacement silencieux', 1, 1, 'Vous pouvez vous déplacer sans faire de bruit.', '<p>completer</p>', 2),
('Désamorçage & sabotage', 1, 0, 'Vous pouvez désamorcer des pièges, bloquer une serrure ( en position ouverte ou fermée ) ou saboter une roue de chariot pour qu''elle sorte de son essieu au bout de quelques mètres.', '<p>completer</p>', 4),
('Détection', 1, 0, 'Détection sert à repérer des brigands s''appretant à tendre une embuscade, percer un déguisement ou lire sur les lèvres ou à voir un mille-pattes géant nichant dans un tas d''ordures.', '<p>completer</p>', 5),
('Diplomatie', 1, 0, 'On utilise cette compétence pour persuader un chambellan d''accorder une audience avec le roi, négocier la cessation des hostilités entre deux tribus barbares en guerre.', '<p>completer</p>', 6),
('Discrétion', 1, 1, 'Vous pouvez vous fondre dans les ombres', '<p>completer</p>', 2),
('Dressage', 0, 0, 'Vous pouvez dresser des animaux pour qu’ils vous obéissent.', '<p>completer</p>', 6),
('Equilibre', 1, 1, 'Vous pouvez vous déplacer sur des surfaces étroites ou instables sans risquer de tomber.', '<p>completer</p>', 2),
('Equitation', 1, 0, 'Vous pouvez monter à cheval et diriger des montures.', '<p>completer</p>', 2),
('Escalade', 1, 1, 'Vous pouvez escalader des surfaces verticales ou des parois inclinées.', '<p>completer</p>', 1),
('Escamotage', 0, 1, 'Vous pouvez voler de petits objets et dissimuler des objets sur votre personne.', '<p>completer</p>', 2),
('Estimation', 1, 0, 'Vous pouvez estimer la valeur d’un objet.', '<p>completer</p>', 4),
('Evasion', 1, 1, 'On utilise cette compétence pour se débarasser de ses liens, se faufiler par un étroit conduit ou échapper à l''étreinte d''un monstre.', '<p>completer</p>', 2),
('Fouille', 1, 0, 'Vous pouvez trouver des passages secrets, des pièges simples et compartiments cachés.', '<p>completer</p>', 4),
('Intimidation', 1, 0, 'Vous pouvez influencer les autres par la peur.', '<p>completer</p>', 6),
('Langue', 1, 0, 'Vous pouvez apprendre de nouvelles langues', '<p>completer</p>', 7),
('Maîtrise des cordes', 1, 0, 'Vous pouvez attacher des cordes et des nœuds complexes.', '<p>completer</p>', 2),
('Natation', 1, 1, 'Vous pouvez nager.', '<p>completer</p>', 1),
('Perception auditive', 1, 0, 'Vous pouvez entendre des bruits faibles ou distants.', '<p>completer</p>', 5),
('Premiers secours', 1, 0, 'Vous pouvez soigner des blessures et des maladies.', '<p>completer</p>', 5),
('Profession', 0, 0, 'Vous pouvez exercer un métier.', '<p>completer</p>', 5),
('Psychologie', 1, 0, 'Vous pouvez comprendre les motivations et les intentions des autres.', '<p>completer</p>', 5),
('Renseignement', 1, 0, 'Vous pouvez obtenir des informations et des rumeurs.', '<p>completer</p>', 6),
('Représentation', 1, 0, 'Vous pouvez divertir les autres par la musique, la danse, la poésie ou la comédie.', '<p>completer</p>', 6),
('Saut', 1, 1, 'Vous pouvez sauter par-dessus des failles béantes, de franchir les barrières d''un bond.', '<p>completer</p>', 1),
('Survie', 1, 0, 'Vous pouvez suivre des pistes et survivre dans la nature.', '<p>completer</p>', 5),
("Utilisation d'objets magiques", 0, 0, 'Vous pouvez utiliser des objets magiques.', '<p>completer</p>', 6),
("Utilisation d'objets psioniques", 0, 0, 'Vous pouvez utiliser des objets psionniques.', '<p>completer</p>', 6);

INSERT INTO synergie_competence (libelle_competence, libelle_competence_1, Special)
VALUES ('Acrobaties', 'Equilibre', NULL),
('Acrobaties', 'Saut', NULL),
('Art de la magie', "Utilisation d'objets magiques", 'associés aux parchemins'),
('Art psi', "Utilisation d'objets psioniques", 'liés aux pierres psioniques'),
('Artisanat', 'Estimation', 'liés aux objets produits par ce type d’artisanat'),
('Bluff', 'Déguisement', 'lorsque le personnage se sait observé'),
('Bluff', 'Diplomatie', NULL),
('Bluff', 'Intimidation', NULL),
('Bluff', 'Escamotage', NULL),
('Connaissance (Mystères)', 'Art de la magie', NULL),
('Connaissance (Psionnique)', 'Art psi', NULL),
('Connaissance (Noblesse et Royauté)', 'Diplomatie', NULL),
('Connaissance (Architecture et Ingénierie)', 'Fouille', 'joués pour trouver des passages ou compartiments secrets'),
('Connaissance (Folklore local)', 'Renseignement', NULL),
('Connaissance (Nature)', 'Survie', 'dans un environnement naturel à la surface'),
('Connaissance (Exploration souterraine)', 'Survie', 'sous terre'),
('Connaissance (Plans)', 'Survie', 'sur d’autres plans d’existence'),
('Connaissance (Géographie)', 'Survie', 'pour éviter de se perdre ou pour éviter des dangers'),
('Décryptage', 'Art de la magie', "pour identifier les pouvoirs d'un cercle runique"),
('Décryptage', "Utilisation d'objets magiques", 'associés aux parchemins'),
('Dressage', 'Equitation', NULL),
('Evasion', 'Maîtrise des cordes', 'lorsque l’on cherche à ligoter quelqu’un'),
('Fouille', 'Survie', 'joués pour trouver ou suivre une piste'),
('Maîtrise des cordes', 'Escalade', 'pour grimper à une corde, quelle qu’elle soit (à nœuds ou non, seule ou près d’un mur)'),
('Maîtrise des cordes', 'Evasion', 'quand on cherche à échapper à des cordes'),
('Psychologie', 'Diplomatie', NULL),
('Représentation', 'Concentration', "pour résister à un chahut lors d'une représentation de ce type"),
('Saut', 'Acrobaties', NULL),
('Survie', 'Connaissance (Nature)', NULL),
("Utilisation d'objets magiques", 'Art de la magie', "si l'on se sert de cette compétence pour déchiffrer un sort rédigé sur un parchemin"),
("Utilisation d'objets psioniques", 'Art psi',"visant à s'adresser aux pierres psioniques");

INSERT INTO source (nom, monde, systeme, officiel) 
VALUES ('Manuel du Joueur', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Manuel du Joueur II', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Guide du Maitre', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Guide du Maitre II', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Manuel des Monstres', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Manuel des Monstres 2', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Manuel des Monstres 3', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Manuel des Monstres 4', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Manuel des Monstres 5', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Grand Manuel des Psioniques', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Miniatures Handbook', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Chapitres Sacrés', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Fiend Folio', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Codex Martial', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Codex Divin', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Codex Profane', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Codex Aventureux', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Complete Psionnic', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Complete Champion', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Complete Mage', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Complete Scoundrel', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Draconomicon', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Dragon Magic', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Le Guide du Voyageur Planaire', 'Greyhoak', 'D&D 3.5', TRUE),
 ('FrostBurn', 'Greyhoak', 'D&D 3.5', TRUE),
 ('SandStorm', 'Greyhoak', 'D&D 3.5', TRUE),
 ('StormWrack', 'Greyhoak', 'D&D 3.5', TRUE),
 ('CityScape', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Les Arcanes Exhumées', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Libris Mortis', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Races de la Pierre', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Races of the Wild', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Races of Destiny', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Races of Dragon', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Lord of Madness', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Heroes of Horror', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Heroes of Battle', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Guide des personnages Monstrueux', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Compendium Arcanique', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Magic Item Compendium', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Dungeonscape', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Tome of Battle, The Book of Nnine Swords', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Magic of Incarnum', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Receuil de Magie', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Weapons of Legacy', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Fiendish Codex I - Hordes of the Abyss', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Fiendish Codex II - Tyrants of the Nine Hells', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Elder Evils', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Drow of the Underdark', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Exemplars of Evil', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Dieux et Demi-Dieux', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Les gardiens de la Foi', 'Greyhoak', 'D&D 3.0', TRUE),
 ("D'Ombre et de Lumière", 'Greyhoak', 'D&D 3.0', TRUE),
 ("Par l'Encre et le Sang", 'Greyhoak', 'D&D 3.0', TRUE),
 ('Manuel des Psionniques', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Campagnes Légendaires', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Chapitres Interdits', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Manuel des Plans', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Arms and Equipement', 'Greyhoak', 'D&D 3.0', TRUE),
 ('GhostWalk', 'Greyhoak', 'D&D 3.0', TRUE),
 ("Hero Builder's Guildebook", 'Greyhoak', 'D&D 3.0', TRUE),
 ('Manuel du constructeur de Donjon', 'Greyhoak', 'D&D 3.0', TRUE),
 ('Ennemies and Allies', 'Greyhoak', 'D&D 3.0', TRUE),
 ('DragonLance - Univers', 'DragonLance','D&D 3.0', TRUE),
 ('Eberron - Univers', 'Eberron','D&D 3.0', TRUE),
 ('Races of Eberron', 'Eberron','D&D 3.0', TRUE),
 ("Player's Guide to Eberron", 'Eberron','D&D 3.0', TRUE),
 ('Reliques et Rituels', 'Terres Balafrées','D&D 3.0', TRUE),
 ("Guide de l'Orient", 'Legend of Five Rings','D&D 3.0', TRUE),
 ("Manuel des Joueurs de Faerûn", 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Dogmes et Panthéons', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Races de Faerûn', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Magie de Faerûn', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Monstres de Faerûn', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Seigneurs des Ténèbres', 'Royaumes Oubliés','D&D 3.0', TRUE),
('Outreterre', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Champions of Ruin', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Champions of Valor', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ("Marche d'Argent", 'Royaumes Oubliés','D&D3.0', TRUE),
 ('Inaccessible Orient', 'Royaumes Oubliés','D&D 3.0', TRUE),
 ('Le Sud Etincellant', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Lost Empires of Faerûn', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Royaumes Serpents', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Dragons of Faerûn', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Power of Faerûn', 'Royaumes Oubliés','D&D 3.5', TRUE),
 ('Recueil de magie', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Reliques et Rituels','Sword and Sorcery','D&D 3.0', TRUE),
 ('Gemmaline', 'Gemmaline','D&D 3.5', False),
 ('Dragon Magazine', 'Greyhoak', 'D&D 3.5', TRUE),
 ('Dungeon Magazine', 'Greyhoak', 'D&D 3.5', TRUE),
 ("Book of Hallowed Might", 'Greyhoak', 'D&D 3.0', TRUE),
("Book of Words", 'Greyhoak', 'D&D 3.5', TRUE),
("City of Stormreach", 'Greyhoak', 'D&D 3.5', TRUE),
("Cité des Splendeurs - Eauprofonde", 'Greyhoak', 'D&D 3.5', TRUE),
("Compendium des révisions", 'Compendium', 'D&D 3.0', FALSE),
("Descent of Shadows", 'Greyhoak', 'D&D 3.5', TRUE),
("Domaine profane : Démons 9", 'Greyhoak', 'D&D 3.5', TRUE),
("Dragonmarked", 'Greyhoak', 'D&D 3.5', TRUE),
("Dragons of Eberron", 'Eberron', 'D&D 3.5', TRUE),
("Expedition to Undermountain", 'Greyhoak', 'D&D 3.5', TRUE),
("Expedition to the Demonweb Pits", 'Greyhoak', 'D&D 3.5', TRUE),
("Explorer’s Handbook", 'Greyhoak', 'D&D 3.5', TRUE),
("Faith of Eberron", 'Eberron', 'D&D 3.5', TRUE),
("Five Nations", 'Greyhoak', 'D&D 3.0', TRUE),
("Forge of War", 'Greyhoak', 'D&D 3.0', TRUE),
("Guide de l'orient Battle", 'Greyhoak', 'D&D 3.5', TRUE),
("Guide de l'orient Horror", 'Greyhoak', 'D&D 3.5', TRUE),
("Horrors of the Abyss", 'Greyhoak', 'D&D 3.5', TRUE),
("Le Divin et Le Déchu", 'Greyhoak', 'D&D 3.5', TRUE),
("Le Sud Etincelant", 'Greyhoak', 'D&D 3.5', TRUE),
("Les Maîtres de la Folie", 'Greyhoak', 'D&D 3.5', TRUE),
("Magic of Eberron", 'Eberron', 'D&D 3.5', TRUE),
("Planescape Campaign Setting",'Greyhoak', 'D&D 3.5', TRUE),
("Player’s Guide to Eberron", 'Eberron', 'D&D 3.5', TRUE),
("Races of the Dragon",'Greyhoak', 'D&D 3.5', TRUE),
("Ravenloft - Gazetter vol V",'Greyhoak', 'D&D 3.5', TRUE),
("Ravenloft - Van Richten's Arsenal",'Greyhoak', 'D&D 3.5', TRUE),
("Ravenloft- Legacy of the Blood",'Greyhoak', 'D&D 3.5', TRUE),
("Royaumes Oubliés",'Greyhoak', 'D&D 3.0', TRUE),
("Scénario - Anauroch the Empire of Shade",'Greyhoak', 'D&D 3.5', TRUE),
("Scénario - Le Bastion des Âmes Damnées",'Greyhoak', 'D&D 3.5', TRUE),
("Scénario - Le Cercle de Pierre",'Greyhoak', 'D&D 3.5', TRUE),
("Scénario - Le Maître de la Forteresse deFer",'Greyhoak', 'D&D 3.5', TRUE),
("Scénario - Legend of the Silver Skeleton,Stormwrack",'Greyhoak', 'D&D 3.5', TRUE),
("Scénario - Les Ombres de la DernièreGuerre",'Greyhoak', 'D&D 3.5', TRUE),
("Secrets of Sarlona",'Greyhoak', 'D&D 3.5', TRUE),
("Secrets of Xen’Drik",'Greyhoak', 'D&D 3.5', TRUE),
("Sharn - la Cité des Tours",'Greyhoak', 'D&D 3.5', TRUE),
("The Dread Codex",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-dwarfs",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-gnomes",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-half-elves",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-humans",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-halflings",'Greyhoak', 'D&D 3.5', TRUE),
("Advanced-race-codex-half-orcs",'Greyhoak', 'D&D 3.5', TRUE),
("Bastards-and-bloodline", 'Greyhoak', 'D&D 3.5', TRUE),
("Wizards of the Coast Web Enhancements", 'Greyhoak', 'D&D 3.5', TRUE);

INSERT INTO langue (nom, alphabet, description, type)
VALUES ('commun', 'commun', "Le commun est la langue la plus parlée à la surface, et celle utilisé pour la plus part des négociations et pour le commerce. A l'intérieur des royaumes humains, c'est la langue utilisée pour la vie de tous les jours. Elle est parlée par quasiment toutes les races intelligentes, mais celles plus barbares ou moins intelligentes ne la parle pas forcément, préférant leur propre langue. néanmoins, les érudits de ces groupes parlent le commun, que ce soit pour le commerce ou pour interroger des prisonniers.", "générale"),
('Commun des profondeurs', 'Elfique', "Cette langue est l'exact équivalent du commun à Outreterre. Cette langue permet de mieux parlé des galeries, tunnels et grottes qui parcourent ces lieux.", 'générale'),
('Aquatique des abimes', 'Aqueux', "L'aquatique des profondeurs est une langue parlé quasiment exclusivement dans les plus profondes des failles océaniques, par les quelques créatures vivant dans de telles profondeurs. C'est une langue dérivée de l'aquatique, mais adaptée à la faculté de communiqué sous une telle pression.", 'raciale'),
('Draconien', 'Draconien', "Le draconien est la langue des dragons et des races reptiliennes comme les hommes lézards ou les kobolds. Cette langue est parfois considérée comme la langue naturelle de la magie et de nombreux traités sur la magie sont écris dans cette langue. Néanmoins cette langue est assez complexe à parler pour les non-lézard car certains sont sont obtenus par claquement des dents.", 'raciale'),
('Drow', 'Elfique', "Parfois appelé 'Elfique des profondeurs', le drow est une langue aux intonations elfiques mêlées à de l'abyssal. Il s'agit de la seconde langue la plus utilisée à Outreterre, et il peut être bien vu de la connaître quand on marchande avec des elfes noirs", 'raciale');

INSERT INTO technique_astucieuse (nom, type, avantage, description, Id_Source)
VALUES ("Ascension accéléré", "Mouvement", "Lorsque le personnage réussit un jet d'escalade pour escalader au moins 3 mètres, il peut se déplacer de 3 mètres supplémentaire lors de la même action.", " Le personnage peut produire un boost de vitesse quand il escalade", 21),
      ("Attaque dans le dos acrobatique", "Mouvement", "Si le personnage réussit son test d'Acrobaties pour traverser la case d'un ennemi, il peut traiter cet ennemi comme étant pris au dépourvu pour sa prochaine attaque au corps à corps durant ce même tour.L'ennemi doit être debout sur le sol pour pouvoir utiliser cette technique.", "L'acrobatie du personnage esquive parfaitement l'attaque ennemie, le plaçant dans une position idéale pour une contre-attaque.", 21),
   ("Remise sur pieds", " Mouvement", " Si le personnage tombe au sol pour n'importe quel raison, il peut se relever au prix d'une action immédiate qui ne provoque aps d'attaque d'opportunité.", " Le personnage peut se remettre immédiatement debout s'il tombe. ", 21),
   ("Perché dans le coin", " Mouvement", "Lorsque le personnage réussit un test d'Escalade pour escalader une cheminée ou un angle, c'est à dire un mur où il peut se tenir à un mur parallèle ou perpendiculaire, le personnage est capable de se coincer avec ses jambes afin de garder ses mains libres. Il peut donc agir librement jusqu'à la fin de son prochain tour sans risque de chute. A la fin de son prochain tour de jeu, le personnage doit réussir un test d'Escalade contre le DD normal + 5 ou tombé à moins qu'il ait réussit un autre test d'Escalade pour monter ou descendre normalement avant cela. ", "Le personnage peut se coincé avec ses jambes en plein escalade afin de garder ses mains libres. ", 21),
 ("Attaque en descente", " Mouvement", "Si la monture du personnage s'est déplacée de plus de 3 mètres durant le round et que le personnage réussit un test d'Équitation pour descendre de selle rapidement, il peut réaliser une action simple pour attaquer un ennemi à proximité comme s'il venait de le charger.", "Le personnage peut frapper un ennemi dès la descente de la selle. " , 21),
 ("Attaque en évation", " Mouvement","Lorsque le personnage s'échappe d'une situation de lutte, il peut attaquer son adversaire avec une arme légère au prix d'une action rapide. Son adversaire est considéré comme pris au dépourvu face à cette attaque.
Le personnage doit avoir l'arme en main au début de son tour pour utiliser cette technique.", "Le personnage sait enchaîner une évasion d'une attaque rapide. ", 21),
   ("Bond extraordinaire", " Mouvement","Si le personnage a réalisé un saut horizontal d'au moins 3 mètres ce tour-ci, il peut se déplacer de 3 mètres au prix d'une action rapide.", "Les bonds extraordinaires du personnage peuvent le porter sur de grandes distances. ", 21),
    ("Escaladeur sautant", " Mouvement","Si le personnage commence une escalade en faisait un jet de saut au prix d'une action rapide, il peut ajouter la distance verticale de son saut à la distance escaladée ce round. Le jet de saut est traité avec élan même si le personnage ne s'est pas déplacé d'au moins 6 mètres. "," Il n'y a pas de meilleure façon de commencer une escalade qu'un bon saut. ", 21),
     ("Charge agile", " Mouvement","Le personnage peut charger ou courir sur une surface difficile sans avoir à réaliser un jet d'Équilibre. ", "Le personnage peut courir sur des surfaces accidentés aisément. " ,20),
   ("Debout en acrobatie", " Mouvement","Le personnage peut se relever sans provoquer d'attaque d'opportunité. ", "Le personnage peut se relever sans danger. " ,20),
    ("Nageur rapide", " Mouvement","Si le personnage réussit un jet de Natation pour nager d'au moins 3 mètres, il peut nager 3 mètres supplémentaire lors de cette même action. ", "Le personnage peut nager à grande vitesse. " ,20),
    ("Faufilage rapide", " Mouvement","Au prix d'une action rapide, le personnage peut se glisser dans un passage étroit en ignorant le coût additionnel en déplacement ou le malus à la CA. L'effet de cette technique dure jusqu'au début du prochain tour du personnage. ", "Le personnage peut se faufiler à travers des passages étroits sans ralentir. " ,20),
     ("Rampement acrobatie", " Mouvement","En réalisant un test d'Acrobaties (DD 15), le personnage peut ramper de 1,5 mètre au prix d'une action de mouvement sans provoquer d'attaque d'opportunité.
Ramper au sol provoque normalement des attaques d'opportunité. ", "Le personnage peut rouler en-dehors du danger. " ,20),
    ("Charge tournante", " Mouvement","Lorsque le personnage charge, il peut tourner une fois jusqu'à 90° lors de son déplacement. Le personnage ne peut se déplacer plus que de sa vitesse s'il utilise cette technique. Toutes les autres restrictions de la charge s'appliquent et il doit avoir une ligne de mire sur la créature qu'il charge au début de son tour. ", "Le personnage peut charger à 90° ", 21),
  ("En haut de la colline", " Mouvement","Le personnage peut se déplacer sur une pente douce ou sur des escaliers à sa vitesse normale au lieu de la moitié de sa vitesse. Cet effet dure un round.", " Le personnage peut monter aisément des pentes douces. " , 21),
   ("Marcher sur les murs", " Mouvement","Le personnage peut se déplacer sans effectuer de jet d'Escalade sur un mur sans pénalité au quart de sa vitesse normale.
Pour utiliser cette technique, il doit commencer et terminer son déplacement sur une surface horizontale. ", "Le personnage peut courir sur un mur pendant quelques secondes. ", 21),
   ("Saut mural", " Mouvement","Si le personnage a réussi un jet d'Escalade pour monter ou descendre d'un mur lors de ce tour ou le précédent, il peut sauter horizontalement de ce mur comme s'il avait pris de l'élan. ", "Il n'y a pas de meilleure manière de terminer une escalade que de sauter du mur. ", 21),
   ("Excentricité limitée", " Interaction","Lorsque le personnage imite une personne précise, il élimine le bonus de Détection normalement donné aux personnes familières.
Utiliser cette technique ne nécessite aucune action, mais le personnage ne peut maintenir la duperie qu'une heure par jour. ", "Le personnage est parfaitement capable d'imiter les habitudes et manière de parler d'une personne afin de ne pas éveiller les soupçons. ", 21),
   ("Feinte de groupe", " Interaction","Le personnage pour utiliser sa compétence Bluff pour feinter plus d'un adversaire. Chaque adversaire fait son jet de Psychologie de manière séparée. Le test de Bluff se réalise avec un malus cumulatif de -2 pour chaque adversaire après le premier. ", "Le personnage part à droite, va à gauche et laisse au final un groupe entier d'ennemis dans le vent. ", 21),
    ("Démoralisateur des foules", " Interaction","Lorsque le personnage utilise sa compétence Intimidation pour démoraliser un adversaire, il peut choisir d'affecter tous les ennemis à 3 mètres ou moins capables de le voir au lieu d'un seul ennemi. Chacun fait son test opposé individuellement, mais à part cela, le jet d'Intimidation se fait normalement.", "Le personnage peut démoraliser de multiples ennemis.", 21),
     ("Seconde impression", " Interaction","Si un personnage voit à travers le déguisement du personnage grâce à un jet de Détection, il peut au prix d'une action immédiate tenter un test de Bluff pour convaincre qu'il est bien ce qu'il prétend être. Ce test est un test opposé au résultat du jet de Détection de l'observateur. En cas de succès, l'observateur ignore l'évidence de ses sens et considère que ce que le déguisement montre est la vérité.
Le personnage doit être au courant que son déguisement est découvert pour utiliser cette technique. Il ne peut l'utiliser par exemple contre quelqu'un qui le regarde secrètement ou qui garde cette information secrète. Dans le doute, le MJ devrait autoriser le PJ a utilisé cette technique si il a une raison valable de craindre que son déguisement soit découvert.
Le personnage ne peut utiliser cette technique qu'une fois par jour, mais elle affecte tous les observateurs dans un rayon de 9 mètres. Ainsi, il sera efficace aussi bien face à une patrouille de gardes qu'une personne seul.
Cette technique n'est d'aucun secours si le déguisement a été démasqué par d'autres manières, comme par la magie. ", "Le personnage peut convaincre de sa fausse identité même après que son déguisement ait échoué. ", 21),
    ("Récupération sociale", " Interaction","Si le personnage échoue à un test de diplomatie pour modifier l'attitude d'un PNJ, Il peut tenter un test de Bluff au prix d'une action prenant un round entier de bavardage avec un malus de -10. Ce test est utilisé à la place du test de Diplomatie, si ce n'est qu'il ne peut améliorer l'attitude que d'un cran maximum.
une fois cette technique utilisée (avec succès ou non), il ne peut plus être utilisé face à la même personne pour 24 heures. ", "Le personnage peut utiliser sa verve pour se tirer des problèmes où son verbe l'a mis.", 21),
     ("Diversion totale", " Interaction","Lorsque le personnage réussit une feinte au combat, son adversaire ne peut réaliser d'attaque d'opportunité contre lui avant le début de son prochain tour. Cet effet vient en plus de l'effet normal de la feinte. ", "Les feintes du personnage sont telles que ses adversaires n'arrivent même plus à profiter de ses moments d'inattention. ", 21),
    ("Improvisateur rusé", "Manipulation","Lorsque le personnage réalise un test de Désamorçage/sabotage ou de Crochetage sans outil approprié, il ignore le malus normal de -2.
Cette technique peut être utilisée autant de fois que nécessaire par jour, jusqu'à ce que le personnage rate un test de Crochetage ou Désamorçage/sabotage sans outils. Après cela, le personnage ne peut plus utiliser cette technique avant de s'être reposé 8 heures. ", "Des outils? Pourquoi avoir besoin d'outils? Ce n'est qu'une combinaison d'une serrure et d'un piège à aiguille empoisonnée, après tout. ", 21),
    ("Lancement de sorts discret", "Manipulation","Le personnage peut lancer un sort sans que les autres s'en aperçoivent. le personnage réalise un jet d'Escamotage opposé à un test de Détection de ceux qui l'observent. Ceux qui ratent leur jet de Détection ne s'aperçoivent pas que le personnage est en train de jeter un sort, et n'ont donc pas le droit à une attaque d'opportunité ou de tenter de contrer le sort. ", "Le personnage peut lancer des sorts sans que les autres s'en aperçoivent. ", 21),
     ("Evasion aisée", "Manipulation","Si le personnage est en situation de lutte face à un adversaire de taille G ou plus, il gagne un bonus de circonstance à son test d'Évasion pour sortir de cette situation. Le bonus dépend de la taille de l'adversaire. 
Taille de l'adversaire
Bonus
G
+4
TG
+8
Gig
+12
C
+16
", "Le personnage peut glisser entre les doigts des ennemis de grande taille avec aisance.", 21),
    ("Fausse théurgie", "Manipulation","Au prix d'une action rapide, lorsque le personnage lance un sort, il peut ajuster les composantes gestuelles et verbales du sort pour qu'il ressemble à un autre sort du choix du personnage du même niveau. Toute créature utilisant Art de la magie ou un autre moyen pour identifier le sort croit que le personnage lance l'autre sort à la place.
Cette technique empêchant l'identification du sort, il empêche la méthode usuelle pour contrer, bien qu'il n'empêche pas l'utilisation de dissipation de la magie et sort semblable pour se faire. Bien sûr, une fois le sort lancé, il peut être identifié normalement. ", "Ce projectile magique fait-il mal? Oh, désolé, vous pensiez que je lançais sommeil? ", 21),
    ("Mains de soin", "Manipulation","Si le personnage réussit un test de Premiers secours pour stabiliser une créature mourante, celle-ci est aussi soignée de 1d6 dégâts. ", "Le personnage est presque capable de faire revenir un mourant à la vie. ", 21),
     ("Lame cachée", "Manipulation","Le personnage peut dégainer une arme dissimulée (voir la compétence Escamotage) par une action de mouvement. De plus, si l'adversaire n'est pas au courant de la présence de l'arme, il est traité comme étant pris au dépourvu face à la première attaque du personnage. ", "Le personnage peut sortir une arme dissimulée pour porter une attaque mortelle. ", 21),
        ("Piqure du moustique", "Manipulation","Si le personnage utilise une arme légère pour frapper un adversaire pris au dépourvu, il peut choisir de faire que cet adversaire ne se rende pas compte qu'il a été touché avant le début de son prochain tour. A la place, cet adversaire réagit comme si le coup l'avait manqué.
Utiliser cette technique n'est pas considéré comme une action de la part du personnage.
Cette technique n'autorise pas à ignorer les autres effets de l'attaque, comme des affaiblissements temporaires à cause du poison ou le fait de tomber inconscient si le PV sont réduits à 0 ou moins.", "Le personnage est capable de porter une attaque si vicieuse que son adversaire ne s'en rendra pas compte. ", 21),
      ("Coup ouvreur", "Manipulation","Au prix d'une action rapide, le personnage peut réaliser un test de crochetage avec un malus de -10 en tapant avec un objet dur et contondant, comme le pommeau d'une arme. Le personnage ne subit pas de malus supplémentaire pour ne pas utiliser d'outils adéquats.
Le personnage peut utiliser cette technique autant de fois qu'il le désire, tant qu'il n'échoue pas. Après un échec à un test de Crochetage fait avec cette technique, le personnage doit attendre de s'être reposé 8 heures avant de pouvoir à nouveau l'utiliser. ", "Pas de temps à perdre avec des outils! Un coup bien placé suffira! ", 21),
     ("Evasion rapide", "Manipulation","Cette technique a deux options. une seule d'entre elle peut être utilisée par rencontre.
Le personnage peut faire un test d' Évasion pour s'échapper d'une situation de lutte ou d'une immobilisation au prix d'une action rapide. Cette technique peut être utilisée même si le personnage a déjà tenté le même jet au prix d'une action simple.
Alternativement, le personnage peut faire un test d'Évasion au prix d'une action de mouvement alors qu'il aurait requis une action complexe. le personnage ne peut utiliser cette option plus d'une fois par jour pour le même type de liens. ", "En un clin d'œil, le personnage s'est échappé! ", 21),
   ("Danse nébuleuse", "Manipulation","Au prix d'une action simple, le personnage peut tenter un test de Discrétion (DD20). S'il réussit, il gagne un camouflage jusqu'à la fin de son tour.", " Le personnage est là où on ne l'attend pas. ", 21),
    ("Iaijutsu", "Manipulation","Si un adversaire provoque une attaque d'opportunité du personnage, celui-ci peut dégainer une arme dissimulée au prix d'une action immédiate pour délivrer une attaque d'opportunité contre cet adversaire. Cet adversaire est considéré comme pris au dépourvu face à cette attaque. ", "Le personnage peut tirer une arme dissimulée et attaquer dans la foulée. ", 21),
     ("Escaladeur au fouet", "Manipulation","Le personnage peut utiliser un fouet comme un grappin, l'enroulant autour d'un protubérance pour s'en servir d'aide pour escalader ou de balancier pour franchir un gouffre. Un jet d'Escalade se fera comme si le fouet était une corde normale.
Utiliser cette technique nécessite un jet de Maîtrise des cordes comme normal pour fixer un grappin, sauf qu'il s'agit alors d'une action de mouvement. ", "Le personnage peut utiliser un fouet pour profiter de prises. ", 21),
     ("Clarté de vision", "Mental","Au prix d'une action rapide, le personnage peut tenter un test de Détection DD 20. En cas de réussite, le personnage clarifie sa vision à un point où il peut situer les créatures invisibles à 9 mètres ou moins. La clarté dure jusqu'à la fin du tour du personnage.", " Le personnage peut brièvement voir les adversaires invisibles. ", 21),
     ("Collecteur d'histoire", "Mental","Lorsque le personnage réalise un test de Connaissances pour identifier une créature ou en apprendre plus sur elle, il gagne un bonus de compétence de +5 à ce jet.
Cette technique ne peut être utilisée que sur les tests de Connaissances dont le personnage possède un degré de maîtrise. ", "Le personnage a entendu tellement de récits sur les monstres légendaires qu'il se souvient de certains détails utiles. ", 21),
     ("Ecoute cela", "Mental","Lorsque le personnage réussit un test de Perception auditive pour entendre un son, il peut répéter ce son jusqu'à 1 heure plus tard, de si bonne manière que ses interlocuteurs auront l'impression d'avoir entendu le son d'origine.
Cette technique est particulièrement utile pour répéter une conversation entendue dont on ne maîtrise pas la langue. ", "Le personnage sait reproduire à la perfection ce qu'il a entendu. ", 21),
     ("Estimation magique", "Mental","Lorsque le personnage réussit de 5 points ou plus sont test d'Art de la magie pour trouver l'école de magie de l'aura entourant un objet magique (par le sort détection de la magie ou similaire), il peut passer 1 minute à se concentrer sur l'objet pour apprendre les propriétés de celui-ci, comme par le sort identification.
Cette technique peut être utilisée une fois par jour. ", "Le personnage peut juger de l'utilité des objets magiques. ", 21),
     ("Pointer du doigt", "Mental","Lorsque vous réussissez un test de Détection, vous
pouvez au prix d'une action immédiate accorder à un allié un test de Détection gratuit pour voir la même chose (avec un bonus de circonstances de +2).
Votre allié doit se trouver à moins de 9 mètres de vous et être capable de vous voir ou de vous entendre pour bénéficier de cet effet.", "Vous pouvez montrer aux autres ce que vous voyez.", 21),
     ("Trouver le point faible", "Mental","Au prix d'une action simple, le personnage peut tenter un jet de Détection pour trouver la faille dans la défense d'un ennemi. Le DD de ce test est égal à la classe d'armure de cette créature. Si le test réussit, la prochaine attaque du personnage contre cet adversaire (si elle est effectuée avant la fin de son prochain tour) est traitée comme une attaque de contact.
Si le personnage utilise une arme à distance, l'adversaire doit être à 9 mètres ou moins pour profiter de cette technique.", "Les yeux de lynx du personnage lui indiquent où placer ses attaques pour qu'elles fassent mal. ", 21), 
     ("Concentration duale", "Mental","Le personnage peut maintenir la concentration sur un sort ou effet similaire au prix d'une action rapide. ", "Le personnage est capable d'être concentrer tout en faisant autre chose. ", 20);

INSERT INTO dependre (libelle_competence, id_technique_astucieuse, valeur)
VALUES ('Escalade', 1, 5),
('Acrobaties', 2, 12),
('Acrobaties', 3, 12),
('Escalade', 4, 8),
('Equitation', 5, 5),
('Evasion', 6, 8),
('Saut', 7, 5),
('Saut', 8, 5),
('Escalade', 8, 5),
('Equilibre', 9, 5),
('Acrobaties', 10, 8),
('Natation', 11, 5),
('Evasion', 12 , 5),
('Acrobaties',  12, 5),
('Acrobaties', 13, 5),
('Equilibre', 14, 5),
('Acrobaties', 14, 5),
('Equilivre', 15, 5),
('Saut', 15, 5),
('Escalade', 16, 12),
('Acrobaties', 16, 5),
('Acrobaties', 17, 5),
('Saut', 17, 5),
('Déguisement', 18, 5),
('Bluff', 19, 8),
('Intimidation', 20, 8),
('Bluff', 21, 5),
('Déguisement', 21, 5),
('Bluff', 22, 8),
('Diplomatie', 22, 5),
('Bluff', 23, 8),
('Désamorçage/sabotage', 24, 5),
('Crochetage', 24, 5),
('Concentration', 25, 1),
('Escamotage', 25, 5),
('Art de la magie', 25, 1),
('Evasion', 26,8),
('Taille moyenne ou petite', 26, 15),
('Bluff ou Escamotage', 27, 8),
('Art de la magie', 27, 8),
('Premiers secours', 28, 5),
('Escamotage', 29, 5),
('Arme en main', 29, 5),
('Escamotage', 30, 12),
('Crochetage', 31, 12),
('Evasion', 32, 12),
('Discrétion', 33, 8),
('Représentation', 33, 5),
('Escamotage', 34, 8),
('Arme en main', 34, 5),
('Maîtrise des cordes', 35, 5),
('Maniement du fouet', 35, 12),
('Détection', 36, 12),
('Connaissance', 37, 5),
('Perception auditive', 38, 5),
('Esimation', 39, 5),
('Connaissance (Mystère)', 39, 5),
('Art de la magie', 39, 12),
('Détection', 40, 8),
('Détection', 41, 12),
('Concentration', 42, 12);

INSERT INTO bonus (nom)
VALUES ('bba');

INSERT INTO categorie_don (libelle, description, regles)
VALUES ('Création d''objets', 'Les lanceurs de sorts ont la possibilité de fabriquer des objets magiques durables. Cela les oblige toutefois à suivre un processus épuisant et à mettre un peu d''eux-même dans chacun des objets créés. Les dons de création permettent au personnage de fabriquer des objets du type correspondant. Tous ont des points communs, quel que soit le type d''objet concerné.', '<h5>Coût en points d''expérience</h5> <p>Le lanceur de sorts dépense une énergie considerable pour créer un objet magique, ce qui se traduit par une perte de PX égale à 1/25e du coût de l''objet en po (voir le Guide du Maître).<br>Un personnage ne peut jamais sacrifier de la sorte suffisamment de points d''expérience pour redescendre au niveau inférieur. Par contre, s''il gagne assez de PX pour gagner un nouveau niveau, il peut choisir de rester à son niveau actuel et d''affecter les PX nécessaires à la création de l''objet magique choisi.</p> <h5>Coût des matières premières</h5><p>La fabrication d''objets magiques requiert des matériaux et ingrédients particulièrement coûteux, qui sont pour la plupart détruits (brûlés, etc.) au cours du processus de création. Ils coûtent la moitié du prix de l''objet.<br> Par exemple, au niveau 12, Mialyë gagne le don Création d''anneaux magiques et décide de s''en servir pour fabriquer un anneau de parade +3. Un tel anneau coûte normalement 18 000 po, aussi sa création demande-t-elle 720 PX et 9000 po à la magicienne. Pour pouvoir mettre à profit un don de création d''objet, il faut également avoir accès à un laboratoire ou atelier de magie et à tous les ustensiles appropriés. Le personnage possède généralement tout ce dont il a besoin, sauf circonstances exceptionnelles (par exemple, s''il se retrouve loin de chez lui).</p><h5>Temps nécessaire</h5><p>Le temps de création de l''objet magique dépend du type d''objet et de son coût. Il ne peut pas être inférieur à 1 jour.</p><h5>Coût de l''objet</h5><p>Préparation de potions, Écriture de parchemins et Création de baguettes magiques créent des objets qui reproduisent directement l''effet d''un ou plusieurs sorts, et dont la puissance dépend du niveau de leur créateur. Les sorts lancés par ces objets ont la même puissance que s''ils étaient directement jetés par le créateur de l''objet. Ainsi, une baguette de boules de feu fabriquée par un magicien de niveau 8 lance des boules de feu infligeant 8d6 points de dégâts chacune à une portée maximale de 216 mètres. Le prix de ces objets (et donc le coût en PX et en matières premières) dépend lui aussi du niveau de leur créateur (qui doit nécessairement avoir atteint le niveau permettant de jeter le sort correspondant). Pour trouver le prix exact de l''objet, il suffit de multiplier le niveau du sort par celui du personnage et de multiplier le résultat obtenu par une constante.</p><h5>Parchemin</h5><p>prix de l''objet=niveau du sort x niveau du personnage x 25 po.</p><h5>Potion</h5><p>prix de l''objet=niveau du sort x niveau du personnage x 50 po.</p><h5>Baguette</h5><p>prix de l''objet=niveau du sort x niveau du personnage x 750 po.<br>Pour ce calcul, on considère les sorts du niveau 0 comme ayant 1/2 niveau.</p><h5>Coût supplémentaire</h5><p>Les potions, parchemins et baguettes qui stockent un sort nécessitant une composante matérielle coûteuse ou un sacrifice en termes de points d''expérience exigent une dépense supplémentaire. Pour une potion ou un parchemin, le personnage doit payer le prix indiqué dans la description du sort (tant en composantes matérielles qu''en PX). Pour une baguette, il doit acquitter cinquante fois le prix exigé par le sort (et sacrifier cinquante fois les PX correspondants, le cas échéant).<br>Certains objets s''accompagnent également d''un coût supplémentaire, indiqué dans leur description. Par exemple, un anneau de triple souhait exige une dépense de 15 000 PX en plus des coûts normaux (c''est-à-dire les PX requis pour lancer souhait à trois reprises).</p>'),
('Divin', 'Les dons de type Divin sont des dons qui permettent de canaliser la puissance divine pour obtenir des effets magiques. Ils sont généralement utilisés par les prêtres et les paladins, mais peuvent être utilisés par n''importe quel personnage capable de lancer des sorts divins du temps qu''ils appartiennent à sa liste.', '<p>Les dons de cette nouvelle catégorie ont en commun quelques caractéristiques. Tout d''abord, ils ont tous comme condition le pouvoir de renvoyer (ou, la plupart du temps, d''intimider) les morts-vivants. Aussi, ils sont ouverts aux prêtres, aux paladins de 3e niveau et plus, et à toutes les classes de prestige possédant ce pouvoir. <br>Ensuite, la force qui génère un don divin est le pouvoir de canaliser l’énergie positive ou négative afin de renvoyer ou intimider les morts-vivants. Chaque utilisation d''un don divin réduit de un le nombre des tentatives de renvoi/intimidation qui est alloué au personnage pour la journée. Si le personnage n’a plus de tentatives disponibles, il ne peut plus utiliser un tel don. Puisque le renvoi/intimidation est une action simple, l’activation d''un don lié à la puissance divine est également une action simple.<br> Enfin, il est impossible d''employer le don Renvoi rapide pour accélérer l’utilisation des dons divins.</p>'),
('Forme animale', 'Les dons appartenant à cette nouvelle catégorie sont associés au pouvoir de forme animale, qui constitue systématiquement l’une des conditions requise pour ce type de don.', "<p>N’importe quelle aptitude de classe dont le nom comprend les mots « forme animale » permet de remplir cette condition (c’est le cas de forme animale mineure, forme animale majeur et forme animale mortvivant). <br>Les dons de forme animale s’appliquent à toutes les versions de ce pouvoir. </p>"),
('Général', "Un don général est un don sélectionnable par tous et n'obéissant à d'autres règles que celle donnée plus haut.","<p>Les personnages de n'importe quelle classe et n'importe quel monstre peuvent piocher leurs dons dans cette liste. </p>"),
('Compétence', 'Ces dons améliorent les compétences du personnage ou confèrent de nouvelles utilisations de celle-ci.',"<p>Les personnages de n'importe quelle classe et n'importe quel monstre peuvent piocher leurs dons dans cette liste pour peu d'en remplir les conditions</p>"),
('Guerrier', 'Ces dons sont généralement des dons de combats.', "<p>Ils peuvent être chois par toutes les classes comme un don normal mais peuvent aussi être choisi comme dons bonus de guerrier </p>"),
('Magicien', 'Les dons de type Magicien sont des dons qui permettent de modifier les connaissances en sorts des magiciens', "<p>Un mage peut prendre ces dons en tant que dons supplémentaires de par ses niveaux de mage (niveaux 5, 10, 15 et 20).</p>"),
('Métamagie', "À mesure que le savoir magique d'un lanceur de sorts augmente, il peut apprendre à jeter ses sorts à l’aide de méthodes légèrement différentes de celles qu'on lui a enseignées. Il peut ainsi lancer un sort sans réciter d'incantation, augmenter son efficacité, ou encore le jeter par la pensée. Préparer et utiliser les sorts de cette manière présente davantage de difficultés que la magie habituelle, mais les dons de métamagie permettent d'en repousser les limites.","<p>Par exemple, au niveau 3, Mialyë gagne un don et choisit Incantation silencieuse, qui lui permet de lancer un sort sans prononcer le moindre mot. Pour pouvoir le faire, elle doit préparer son sort comme un enchantement du niveau supérieur. Si elle souhaite préparer de la sorte charme personne, elle le fait comme s'il s'agissait d'un sort du 2e niveau, mais le niveau du sort ne change pas (par exemple, le DD du jet de Volonté est toujours calculé comme pour un sort du 1e niveau). Bien que la puissance de l’enchantement n'ait pas changé, il occupe désormais la place d'un sort du 2e niveau dans l’esprit de Mialyë. Cette dernière est incapable de préparer un sort du 2e niveau pour le lancer à l’aide d'Incantation silencieuse, car il lui faudrait pour cela sacrifier un sort du 3e niveau et elle n'est pas encore capable d'en jeter. Elle pourra le faire quand elle aura atteint le niveau 5.</p><h5>Magiciens et pratiquants de la magie divine</h5> <p>Magiciens et pratiquants de la magie divine (prêtres, druides, paladins et rôdeurs) doivent préparer leurs sorts à l'avance. C'est à ce moment qu'ils décident ceux qu'ils souhaitent mémoriser de manière à les lancer à l’aide de dons de métamagie (ce qui les oblige à les prendre à la place de sorts de niveau supérieur).</p>
<h5>Bardes et ensorceleurs</h5><p>Pour leur part, bardes et ensorceleurs choisissent leurs sorts au moment de les jeter. Ils décident donc au dernier instant s'ils souhaitent augmenter la puissance de leur sort à l’aide d'un don de métamagie. Pour eux aussi, le sort prend la place d'un enchantement de niveau supérieur (invisibilité comptera donc comme un sort du 3e niveau ou plus). Comme le personnage ne prépare pas le sort à l’avance, il n'a pas d'autre choix que de rallonger son temps d'incantation afin d'incorporer le don de métamagie à la formule magique qu'il récite. Si le temps d'incantation normal du sort est égal à une action, un barde ou ensorceleur aura besoin d'une action complexe pour le lancer en tant que sort métamagique (c'est-à-dire modifié par un don de métamagie). Pour les sorts à incantation plus longue, il faut rajouter une action complexe au temps indiqué.</p><h5>Sorts spontanés et dons de métamagie</h5><p>Les prêtres lançant spontanément des sorts de soins ou de blessure peuvent également utiliser la métamagie. Par exemple, un prêtre de niveau 11 peut transformer un sort du 6e niveau en soins intensifs s'il souhaite jeter une version métamagique de ce sort (il perd un niveau de sort dans l'échange). Si le temps d'incantation normal du sort est d'une action, sa version métamagique nécessite une action complexe. Pour les sorts à incantation plus longue, il faut rajouter une action complexe au temps indiqué. Effet des dons métamagiques sur un sort. Un sort métamagique fonctionne à son niveau d'origine, même si on le prépare et le lance comme un sort de niveau supérieur. Le jet de sauvegarde n'est pas modifié (à moins que la description du don n'indique le contraire). Les changements mentionnés n’opèrent qu'à partir des sorts jetés directement par le personnage (il est par exemple impossible d'utiliser un don de métamagie pour augmenter la puissance d'un sort lancé par le biais d'un parchemin, baguette ou autre objet magique).<br>Les dons de métamagie ne peuvent pas être utilisés pour tous les sorts. Reportez-vous à la description de chaque don pour connaître les sorts qu'il ne peut pas affecter. Dons de métamagie multiples sur un même sort. II est. possible de multiplier les dons de métamagie utilisés avec un même sort, mais l’augmentation de complexité est cumulable. Ainsi, charme-personne sera considéré comme un sort du 3e niveau si l'on souhaite le lancer à l’aide d'Incantation statique et Incantation silencieuse.</p><h5>Objets magiques et dons de métamagie</h5><p>Avec le don de création d'objet approprié, il est possible de stocker un sort métamagique dans une potion, un parchemin ou une baguette. La limite de niveau concernant les parchemins et les potions s'applique au niveau augmenté du sort, ce qui prend en compte sa complexité. Il n'est pas nécessaire d'avoir le don de métamagie correspondant pour activer un tel objet.</p><h5>Contresorts et dons de métamagie</h5><p>Qu’un sort ait été modifié ou non par métamagie, il demeure aussi vulnérable aux contresorts, et lui-même reste un contresort tout aussi efficace.</p>"),
('Musique de barde', 'Ces dons, comme leur nom l’indique, exigent que le personnage dispose de l’aptitude de musique de barde et leur activation dépense des utilisations quotidiennes de ce pouvoir.', "<p>Tous les dons de musique de barde ne sont possibles, à un moment donné, que si le personnage est en mesure déjouer de la musique, même ceux qui ne prennent qu’une action libre et ceux qui ne demandent aucune action. Les aptitudes de classe qui se rapprochent de la musique de barde, comme la musique de chantre de guerre ou la musique de quêteur, peuvent se substituer à la condition « pouvoir de musique de barde » de ces dons.</p>"),
('Style d’arme', 'On peut reconnaître les aventuriers les plus célèbres autant par les armes qu’ils emploient, les techniques de combat uniques qu’ils maîtrisent et les manœuvres qu’ils ont inventées que par la description qu’en font les légendes.',"<p>N’importe quel guerrier peut utiliser sa force au mieux en prenant les dons Attaque en puissance, Enchaînement et Science de la destruction, ou étudier l’art de l’escrime grâce aux dons Expertise du combat et Science du désarmement, mais il n’y a probablement qu’un seul d’entre eux pour maîtriser la technique du Croissant de lune dans tout le royaume. Un don de style d’arme améliore grandement l’efficacité d’une arme ou d’une combinaison précise de deux armes, mais nécessite la connaissance des dons les plus utiles avec ces armes. </p>"),
('Epique', "Lancer un sort d'un simple claquement de doigts, tirer des flèches aussi loin que porte la vue. décapiter ses ennemis à mains nues, créer des objets magiques à la puissance inégalée, charmer des liches en leur chantant une mélopée.", "<p>Voici en quelques mots l'objet des dons épiques.<br>Un personnage épique se définit en partie par son choix de dons épiques. A l'instar du don ordinaire, le don épique est une faculté spéciale qui offre au personnage une nouvelle capacité ou qui améliore l'une de celles qu'il possède déjà. Néanmoins, le don épique transcende les facultés ordinaires et relève davantage du mythe. Les dons épiques permettent au personnage de faire un prodigieux bond en avant, de lancer de nombreux sorts par round ou de prendre la forme d'un dragon.<br>En plus des conditions spécifiées dans le don, un personnage doit être de niveau 21 ou plus pour sélectionner un don épique.</p>"),
('Environnemental', 'Les dons environnementaux sont généralement utilisés par les créatures qui vivent dans des environnements particuliers, comme les créatures aquatiques, les créatures des montagnes, les créatures des marais, etc.',"<p>Vous ne pouvez selectionner un don environnemental pour votre personnage si la ligne « Milieu naturel/climat » de la créature de base mentionne le type de milieu naturel ou de climat indiqué. Si cette ligne inclut plus d'un milieu naturel, elle peut aussi faire l'affaire pour d'autres dons environnementaux, à la discrétion du MD.</p>"),
('Monstrueux', "Comme leur nom l'indique, les dons monstrueux sont généralement utilisés par les monstres.", "<p>Ils demandent toujours une capacité, uen forme physique ou d'autres choses que les PJ ont fort rarement.<br>Une créature métamorphe peut prendre un tel don si une de ses formes valide les conditions, mais ce don ne sera utilisable que sous la ou les formes validant les conditions. Ainsi, un louo-garou peut choisir un don nécessitant des griffes, mais il ne bénéficiera pas de celui-ci sous forme humaine.</p>"),
('Métasouffle', 'Les dragons (et autres créatures) apprennent à contrôler leur souffle de manière à générer différents effets, tantôt subtils, tantôt directs.',"<p>Pour choisir un tel don, la créature doit disposer d'un souffle dont la fréquence d'utilisation est exprimée en cycle de rounds. Ainsi, un molosse satanique (capable de souffler 1 fois tous les 2d4 rounds) a le droit de prendre des dons de métasouffle, ce qui n'est pas le cas du béhir (souffle utilisable 1 fois par minute).</p><h5>Effets d'un don de métasouffle</h5><p>Un souffle profitant d'un tel don fonctionne de manière habituelle, à moins que le don n'en change certains aspects.<br>Pour utiliser ce type de don, le dragon doit fournir un effet à la fois mental et physique, ce qui a pour effet d'augmenter le laps de temps séparant l'utilisation de deux souffles. Normalement, un dragon qui vient de souffler doit patienter 1d4 rounds avant de pouvoir réutiliser cette forme d'attaque. Le fait d'utiliser un don de métasouffle augmente ce laps de temps de 1 round, voire plus. Par exemple, si un dragon utilise un souffle agrandi, il lui patienter pendant 1d4+l rounds avant de pouvoir utiliser de nouveau cette attaque.</p><h5>Dons de métasouffle multiples</h5><p>Un dragon a le droit d'utiliser plusieurs dons de métasouffle dans le cadre d'une même attaque de souffle. Il lui faut alors attendre d'autant plus avant de pouvoir réutiliser cette attaque. Par exemple, si un dragon use de Souffle agrandi et de Quintessence des souffles en même temps, il lui faut patienter 1d4+4 rounds avant de pouvoir utiliser une nouvelle fois cette forme d'attaque.<br>Un dragon peut également utiliser plusieurs fois un même don de métasouffle dans le cadre d'une seule et même attaque. Parfois, cela n'a aucun effet supplémentaire. Le reste du temps, ces effets sont cumulatifs. Appliquez l'effet du don une fois par application de celui-ci aux valeurs de base du souffle et cumulez le temps supplémentaire devant séparer le souffle actuel du suivant. Par exemple, un dragon de taille P pourvu d'un souffle en forme de ligne peut utiliser Souffle agrandi à deux reprises dans le cadre d'une même attaque. Comme la longueur de la ligne de base s'élève à 12 mètres, elle fait désormais 24 mètres de long (6 mètres supplémentaires par application du don). Notre dragon doit maintenant patienter 1d4+2 rounds avant de pouvoir réutiliser son souffle.<br>Quand un don de métasouffle est cumulable avec lui-même, cela est précisé dans la rubrique Spécial de sa description. </p>"),
("Créations d'objets psioniques", "Les personnages qui manifestent des facultés ont la possibilité d'utiliser ces facultés pour créer des objets psioniques durables. Cela les oblige toutefois à suivre un processus épuisant et à mettre un peu d'eux-mêmes dans chacun des objets créés.<br>Les dons de création d'objets permettent au personnage de fabriquer des objets psioniques du type correspondant. Tous ont des points communs, quel que soit le type d'objet concerné.", "<h5>Coût en points d'expérience</h5><p>Le personnage psionique dépense une énergie considérable pour créer un objet psionique, ce qui se traduit par une perte de PX égale à 1/25e du prix de base de l'objet en pièce d'or. Un personnage ne peut jamais sacrifier de la sorte un nombre de points d'expérience qui le ferait redescendre au niveau inférieur. Par contre, s'il gagne assez de PX pour gagner un nouveau niveau, il peut choisir de rester à son niveau actuel et d'affecter les PX nécessaires à la création de l'objet psionique choisi.</p><h5>Coût des matières premières</h5><p>La fabrication d'objets psioniques requiert des composantes particulièrement coûteuses, qui sont pour la plupart détruites durant le processus de création. Elles coûtent la moitié du prix de base de l'objet. Pour pouvoir mettre à profit un don de création d'objets, il faut également avoir accès à un laboratoire ou un atelier psionique, mais aussi à tous les ustensiles appropriés. Sauf circonstances exceptionnelles (par exemple, s'il se retrouve loin de chez lui), le personnage possède généralement tout ce dont il a besoin.</p><h5>Temps nécessaire</h5><p>Le temps de création de l'objet psionique dépend du type d'objet et de son prix. Il ne peut pas être inférieur à 1 jour.</p><h5>Objets de niveau variable</h5><p>Création de dorjés, Création de pierres psioniques et Création de tatouages psioniques créent des objets qui reproduisent directement l'effet d'une faculté. Leur puissance dépend de leur niveau de manifestation. Les facultés psioniques manifestées par le biais de ces objets fonctionnent alors exactement comme si elles avaient été manifestées par un psionique de ce niveau.<br> Un personnage peut fixer librement le niveau de manifestation d'un objet qu'il crée, tant qu'il est compris entre le niveau minimal nécessaire pour manifester la faculté et son propre niveau de manifestation. Dans la plupart des cas, les créateurs choisissent le niveau minimal possible (c'est du moins la règle que suivent les objets déterminés aléatoirement).<br>Il est possible de créer un objet en utilisant une faculté améliorée par une dépense de points psi supplémentaires, mais l'objet doit avoir un niveau de manifestation au moins égal à la dépense totale de points psi. Tous les paramètres de la faculté incrustée dans l'objet qui dépendent du niveau sont déterminés par le niveau de manifestation effectif.<br>Prenons l'exemple d'un dorjé de commotion créé sans amélioration. Il s'agit d'une faculté de 2e niveau qui inflige 1d6 points de dégâts et exige un niveau de manifestation minimal de 3. Si ce même dorjé est créé avec une amélioration de 6 points psi, le niveau de manifestation minimal augmente d'autant et atteint 9 (le niveau de la faculté reste le même : 2). Ce dorjé produit alors une commotion infligeant 4d6 points de dégâts. Tous les effets de la faculté qui dépendent du niveau sont augmentés ; pour cet objet, la portée de commotion passe de 39 à 57 mètres.<br>Le prix de base de ces objets (et donc le coût en PX, en matières premières et en temps) dépend de leur niveau de manifestation et du niveau de la faculté psionique qu'ils stockent, selon les formules suivantes.</p><h5>Pierres psioniques</h5><p>Prix de base=niveau de la faculté x niveau de manifestation x 25 po</p><h5>Tatouages psioniques</h5><p>Prix de base=niveau de la faculté x niveau de manifestation x 50 po</p><h5>Dorjés</h5><p>Prix de base=niveau de la faculté X niveau de manifestation X 750 po</p><h5>Objets de niveau fixe</h5><p>Les objets psioniques créés à l'aide des autres dons de création d'objets ont un niveau de manifestation fixe, indiqué dans leur description. Leur prix de base est généralement égal à leur prix de vente.</p><h5>Coût supplémentaire</h5><p>Les dorjés, pierres psioniques et tatouages psioniques stockant une faculté qui nécessite un sacrifice en termes de points d'expérience exigent une dépense supplémentaire. Pour une pierre psionique ou un tatouage psionique, le personnage doit payer le coût supplémentaire en PX indiqué dans la description de la faculté. Pour un dorjé, il doit s'acquitter de cinquante fois ce coût en PX.Certains objets psioniques s'accompagnent également d'un coût supplémentaire en PX, indiqué dans leur description.</p>"),
('Ectopique', 'Un don ectopique permet à un psionique capable de manifester la faculté Construction astrale de modifier cette dernière, lui donnant une autre forme et des pouvoirs supplémentaires.', "<p>On ne peut appliquer qu'un unique don ectopique à chaque création astrale, et un personnage ayant des dons ectopiques choisit le quel et s'il veut utiliser un tel don. Ce choix doit être fait à la manifestation de la faculté, et ne peut plus changer pour la durée de celle-ci.</p>"),
('Harmonie', "Les dons d'Harmonie sont liés à la faculté non seulement de créer mais d'améliorer le cristal psi pour un personnage psionique. Ces dons permettent au cristal psi d'être une véritable continuité de l'esprit de son créateur, entrant en symbiose total avec lui plus qu'une simple extension.", "<p>Tous les dons d'harmonie sont considérés comme des dons psioniques.</p>"),
('Héritage illithid', "Les dons d'héritage illithid sont ceux qui permettent à un personnage de découvrir et exploiter l'héritage illithid qui coule dans leur veine. Ces dons permettent au personnage de ressembler de plsu en plus à un illithid, aussi bien au niveau des capacités que du physique ou du mental.", '<p>Un don Héritage illithid est considéré comme un don psionique</p>'),
('Hôte', 'Les entités, sans formes précises, qui préfèrent être hébergées dans un corps physique ont une mystérieuse origine, bien que certaines d’entre elles se font appeler Quori. Les autres un nom qui leur est propre, mais toutes ont besoin d’un corps pour exister dans la réalité. Il est classique de voir ces entités être attirées par des dons d’hôte.', "<p>Les dons d’hôte ne peuvent être prit que par un personnage servant de réceptacle à une entité psionique. Une fois qu’une créature accepte une entité psionique et devient son hôte, elles ne forment plus qu’une seule créature à tout point de vue. L’entité ne peut être expulsée (sauf avec la faculté modification psychique ou dans ce cas l’entité peut être abandonnée). Une créature peut prendre autant de dons d’hôte qu’elle le souhaite. Les dons d’hôte sont considérés comme des dons psioniques.</p>"),
('Psionique', "Seuls les personnages et créatures qui manifestent des facultés psioniques ont accès aux dons psioniques (autrement dit ceux qui ont une réserve de points psi ou sont dotés de pouvoirs psioniques).", "<p>Leur utilisation ne peut être interrompue en plein combat (à l'inverse des facultés) et elle ne provoque généralement pas d'attaque d'opportunité (à moins que le contraire ne soit spécifié dans leur description). De plus, les pouvoirs surnaturels ne sont pas sujets à la résistance psionique et ne peuvent être dissipés. En revanche, ils ne fonctionnent pas dans une zone annulant les effets psioniques, telle qu'un champ d'exclusion psionique. Quitter une telle zone permet instantanément de recourir aux dons psioniques.<br>Certains dons psioniques n'accordent leurs avantages que tant que le personnage est psioniquement focalisé (cf. la compétence Concentration). D'autres lui permettent d'employer l'énergie psychique de sa focalisation psionique pour réaliser des exploits. Il doit pour cela « sacrifier » sa focalisation (mais il peut la rétablir ensuite). Sacrifier sa focalisation psionique n'exige aucune action, cela fait simplement partie d'une autre action. Quand un personnage sacrifie sa focalisation psionique, l'énergie libérée ne peut être utilisée que pour un seul usage. Ainsi, si un personnage possède les dons Arme psionique et Arme psionique percutante (qui exigent tous deux de sacrifier sa focalisation psionique), il doit choisir duquel des deux il veut bénéficier lorsqu'il sacrifie sa focalisation psionique.</p>"),
('Séquestre', "Alors que les origines des dons séquestres se perdent dans les annales du temps, de nombreux individus psioniques apprennent leurs secrets. En séquestrant une faculté psionique, en choisissant consciemment de ne pas manifester ce pouvoir, l'individu acquiert une capacité moindre qui peut être utilisée plus fréquemment, ou parfois une capacité qui est toujours active.", "<p>Séquestrer une faculté nécessite une action complexe qui provoque des attaques d'opportunité. Les facultés doivent être séquestrés individuellement, mais il n'y a pas de limite au nombre de facultés qu'un psionique peut séquestrer. De plus, une seule faculté séquestrée peut alimenter plusieurs dons séquestres. Un psionique ne peut pas manifester une faculté qui a été séquestrée. Les facultés séquestrées restent bloquées tant que le manifesteur maintient sa focalisation psionique. Si le psionique dépense ou perd sa focalisation psionique, la faculté n'est plus séquestré et le psionique récupère l'usage de la faculté. Un psionique peut choisir de libérer une faculté séquestrée par une action libre. Chaque fois qu'une faculté séquestrée est libérée, volontairement ou par la perte de la focalisation psionique, tous les dons alimentés par cette faculté cessent immédiatement de conférer le bénéfice associé.<br>Sauf mention contraire, activer l'effet d'un don séquestre est une action simple qui ne provoque pas d'attaque d'opportunité.Si une faculté séquestrée peut infliger des dégâts de plusieurs types d'énergie ou peut avoir plusieurs registres ou sous-types, le psionique doit choisir quel type d'énergie ou registre lors de la séquestration de la faculté à des fins de dons séquestres.<br>Sauf indication contraire, l'éventuel DD des dons séquestre est de 10 + niveau de la faculté séquestrée + moitié du niveau de manifestation du personnage.</p>"),
('Métapsionique', "À mesure que le savoir psionique d'un personnage capable de manifester des facultés augmente, il peut apprendre à manifester à l'aide de méthodes légèrement différentes de celles qu'on lui a enseignées ou de ce qui est prévu.","<p>Il peut ainsi apprendre à manifester une faculté pour qu'elle dure plus longtemps que la normale, qu'elle inflige plus de dégâts ou pour amplifier quelque autre critère. Bien entendu, manifester une faculté tout en recourant à un don métapsionique s'avère une opération plus coûteuse que la manifestation normale.</p><h5>Temps de manifestation</h5><p>Manifester une faculté associée à un don métapsionique prend autant de temps que manifester normalement la faculté, à moins que la description du don ne précise le contraire, comme c'est le cas pour Faculté instantanée.</p><h5>Dépense psi</h5><p>En recourant à un don métapsionique, le personnage doit d'une part sacrifier sa focalisation psionique et d'autre part s'acquitter d'une dépense supplémentaire de points psi, comme le précise la description du don. Faculté multiple, par exemple, augmente la dépense totale en points psi de 6 points.</p> <h5>Limite</h5><p>Comme c'est le cas pour toutes les facultés, les personnages ne peuvent dépenser plus de points psi en manifestant une faculté que leur niveau de manifestation. Les dons métapsioniques permettent simplement de manifester les facultés d'une manière différente, et non pas d'enfreindre cette règle.</p><h5>Effet des dons métapsioniques sur une faculté</h5><p>Une faculté métapsionique fonctionne à son niveau d'origine, même si on dépense davantage de points psi pour la manifester. Les changements mentionnés n'opèrent que sur les facultés directement manifestées par le personnage. Il est impossible d'utiliser un don métapsionique sur une faculté produite par le biais d'une pierre psionique, d'un dorjé ou de tout autre objet psionique.<br>Manifester une faculté instantanée (modifié par le don Faculté instantanée) ne provoque pas d'attaque d'opportunité.<br>Certains dons métapsioniques ne peuvent pas être utilisés pour toutes les facultés, comme le précise leur description.</p><h5>Objets psioniques et dons métapsioniques
</h5><p>Avec le don de création d'objets psioniques approprié, il est possible de stocker une faculté métapsionique dans une pierre psionique, un tatouage psionique ou un dorjé. La limite de niveau concernant les tatouages psioniques s'applique au niveau augmenté de la faculté. Ainsi, une faculté de 3e niveau modifiée par le don Faculté renforcée ne peut être stockée dans un tatouage psionique, car elle équivaudrait à une faculté de 5' niveau ce qui dépasserait la limite de niveau de faculté qu'un tatouage psionique est capable de contenir (3e).<br>Les personnages n'ont pas besoin d'être eux-mêmes dotés du don avec lequel la faculté a été stockée dans l'objet psionique pour pouvoir l'activer, mais le créateur de l'objet doit, lui, en disposer.</p>"),
('Initié', "Les sorts de domaine représentent dans une certaine mesure ce qui différencie les prêtres d'un dieu de ceux d'une autre divinité Les prêtres de Kossuth peuvent lancer mains brûlantes alors que ceux de Lolth disposent de lueur noire. Il ne s'agit néanmoins pas d'un facteur de distinction parfait car les prêtres de Gond et de Talos ont accès au domaine du Feu, et pas moins de quarante-quatre divinités permettent d'accéder au domaine du Bien.", "<p>Les seules caractéristiques qui distinguent certains prêtres d'autres sont les sorts propres aux dieux, des sorts que des dieux précis confèrent. Par exemple, seul Cyric octroie le sort crâne des secrets à ses prêtres, et seuls les prêtres de Mystra peuvent lancer étoile bénie. Un personnage peut donc parvenir à cette distinction en prenant un don d'initié, comme Initié de Cyric ou Initié de Mystra, qui n'est disponible qu'aux prêtres du. dieu en question. La plupart de ces dons exigent un niveau minimal de prêtre. En plus de l'avantage habituel, chacun ajoute des sorts à la liste du prêtre qui le choisit. Certains permettent même de les ajouter à la liste de sorts d'autres classes. Dans ce cas, le personnage doit choisir à quelle liste ajouter ces nouveaux sorts. Aucun personnage ne peut avoir plus d'un don d'initié car celui-ci décrit un niveau d'engagement profond envers un dieu.</p>"),
('Node', "La magie des nodes est une technique qui consiste à utiliser des nodes magiques.", "<p>En exploitant le pouvoir des nodes terrestres et en maîtrisant la magie des nodes, vous avez accès à une variété de prouesses de magie des nodes. Cette prouesse vous permet d'utiliser les puissantes énergies des nodes terrestres et d'effectuer des tâches liées à ces derniers avec compétence. Plutôt que de dépendre d'un test d'Intelligence, vous pouvez utiliser votre expertise en Art de la magie pour détecter les nodes proches et manipuler leurs divers pouvoirs de manière efficace.</p>"),
('Racial', "Un don racial est un don qui, de part la culture ou les capacités innées d'une race est réservée à une race, une sous-race ou un groupe de race.", "<p>Il faut faire partie de la race en question pour prendre le don. Pouvoir en prendre la forme et même les pouvoirs n'est pas suffisent. </p>"), 
('Régional', "Les dons régionaux sont des dons relatifs à un lieu donné.", "Ces dons ne peuvent être pris qu'à la création du personnage et on ne peut en prendre qu'un seul (y compris pour un humain) "),
('Rage', 'Les dons de rage sont des dons qui ne peuvent être pris que par des personnages capables de se mettre en rage.', "<p>Un personnage ne peut pas prendre un don de rage s'il ne peut pas se mettre en rage. Un personnage qui perd la capacité de se mettre en rage ne peux plus utiliser les dons de rage. </p>");

INSERT INTO don (nom, description, avantage, special, normal, effet, Id_Source)
VALUES ('Feinte de la meute', " Le personnage sait comment rendre confus un adversaire afin d'aider ses camarades.", "Lorsque le personnage utilise avec succès une action de feinte au combat, sa cible perd son bonus de Dextérité à la CA contre la prochaine attaque du personnage ainsi que la prochaine attaque d'un allié. Celui-ci doit être adjacent au personnage au moment où la feinte est réalisée. Ces deux attaques doivent être réalisées avant le début du prochain tour du personnage.", NULL, NULL, NULL, 88),
('Persuasion', " Le personnage a un talent pour obtenir ce qu’il veut, d’une façon ou d’une autre.", "Le personnage obtient un bonus de +2 sur tous ses tests de Bluff et Intimidation.", "Un Scelleur peut sélectionner Persuasion comme don supplémentaire", NULL, NULL, 1);

INSERT INTO don_appartenir_categorie (id_don, id_categorie_don)
VALUES (1, 4),
      (2, 4),
      (2, 5);

INSERT INTO conditions (special)
VALUES (NULL);

INSERT INTO condition_don (id_conditions, id_don)
VALUES (1, 1);

INSERT INTO requerir_comp (id_conditions, libelle_competence, degre_maitrise)
VALUES (1, 'Bluff', 3);

INSERT INTO requerir_caracteristique (id_conditions, Id_Caracteristique, valeur)
VALUES (1, 5, 13),
(1, 2, 13);

INSERT INTO requerir_bonus (id_conditions, Id_Bonus, valeur)
VALUES (1, 1, 3);

INSERT INTO don_augmente (id_don, libelle_competence, valeur)
VALUES (2, 'Bluff', 2),
(2, 'Intimidation', 2);