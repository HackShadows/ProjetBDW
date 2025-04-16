import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from logzero import logger
from datetime import datetime
from random import randint


# Fonctions générales
def execute_select_query(connexion, query :str, params :list=[]) -> list[dict]|None:
	"""
	Méthode générique pour exécuter une requête SELECT (qui peut retourner plusieurs instances).
	Utilisée par des fonctions plus spécifiques.

	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	query : str like
	    Requête pour le SELECT.
	params : list
	    Paramètres à ajouter à la requête.

	Renvoie
	-------
	Une liste de dictionnaires. Chaque dictionnaire correspond à une ligne.
	"""
	with connexion.cursor() as cursor:
		try:
			cursor.execute(query, params)
			cursor.row_factory = dict_row
			result = cursor.fetchall()
			return result 
		except psycopg.Error as e:
			logger.error(e)
	return None

def execute_other_query(connexion, query :str, params :list=[]) -> int|None:
	"""
	Méthode générique pour exécuter une requête INSERT, UPDATE, DELETE.
	Utilisée par des fonctions plus spécifiques.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	query : str like
	    Requête à exécuter.
	params : list
	    Paramètres à ajouter à la requête.

	Renvoie
	-------
	Le nombre d'enregistrements.
	"""
	with connexion.cursor() as cursor:
		try:
			cursor.execute(query, params)
			result = cursor.rowcount
			return result 
		except psycopg.Error as e:
			logger.error(e)
	return None

def get_instances(connexion, nom_table :str) -> list[dict]|None:
	"""
	Retourne les instances de la table 'nom_table'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	nom_table : str
	    Nom de la table.

	Renvoie
	-------
	Les enregistrements de la table 'nom_table'.
	"""
	query = sql.SQL('SELECT * FROM {table}').format(table=sql.Identifier(nom_table))
	return execute_select_query(connexion, query)

def count_instances(connexion, nom_table :str) -> int:
	"""
	Retourne le nombre d'instances de la table 'nom_table'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	nom_table : str
	    Nom de la table.

	Renvoie
	-------
	Le nombre d'enregistrements de la table 'nom_table'.
	"""
	query = sql.SQL('SELECT COUNT(*) AS nb FROM {table}').format(table=sql.Identifier(nom_table))
	nb = execute_select_query(connexion, query)
	return nb[0]['nb']


# Fonctions sécifiques utilisées par plusieurs contrôleurs
def get_img_tuile(connexion, id_tuile :int) -> str:
	"""
	Retourne l'image associée à la tuile d'identifiant 'id_tuile'

	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_tuile : int
	    Identifiant de la tuile.

	Renvoie
	-------
	Nom de l'image.
	"""
	query = 'SELECT chemin_texture FROM tuile WHERE id_tuile=%s'
	image = execute_select_query(connexion, query, [id_tuile])
	return image[0]['chemin_texture']

def get_elements_tuile(connexion, id_tuile :int) -> dict:
	"""
	Retourne les éléments présents sur la tuile jeu d'identifiant 'id_tuile'
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_tuile : int
	    Identifiant de la tuile jeu.

	Renvoie
	-------
	Dictionnaire (clés : noms des éléments, valeurs : nombre d'instances de cet élément sur la tuile).
	"""
	query = 'SELECT nom_élément, nombre FROM contient_element WHERE id_tuile=%s'
	liste = execute_select_query(connexion, query, [id_tuile])
	return {dic['nom_élément']:dic['nombre'] for dic in liste}

def get_joueurs(connexion) -> list[dict]:
	"""
	Retourne la liste de tous les joueurs triés par nom.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Liste de dictionnaires (clés : id_joueur, nom, prénom, pseudo, année_naiss).
	"""
	query = 'SELECT * FROM joueur ORDER BY nom, prénom'
	return execute_select_query(connexion, query)

def get_infos_joueur(connexion, id_joueur :int) -> dict:
	"""
	Retourne les informations sur le joueur d'identifiant 'id_joueur'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_joueur : int
	    Identifiant du joueur.

	Renvoie
	-------
	Dictionnaire (clés : id_joueur, nom, prénom, pseudo, année_naiss).
	"""
	query = 'SELECT * FROM joueur WHERE id_joueur=%s'
	return execute_select_query(connexion, query, [id_joueur])

def get_infos_partie(connexion, id_partie :int) -> dict:
	"""
	Retourne les informations sur la partie d'identifiant 'id_partie'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.

	Renvoie
	-------
	Dictionnaire (clés : attributs de partie).
	"""
	query = 'SELECT * FROM partie WHERE id_partie=%s'
	return execute_select_query(connexion, query, [id_partie])[0]

def id_disponible(connexion, nom_table :str) -> int:
	"""
	Retourne le plus petit identifiant disponible de la table 'nom_table'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	nom_table : str
	    Nom de la table.

	Renvoie
	-------
	Un identifiant non utilisé.
	"""
	query = f'SELECT id_{nom_table} FROM {nom_table} ORDER BY id_{nom_table}'
	result = execute_select_query(connexion, query)
	i = 1
	lg = len(result)
	while i <= lg and result[i-1][f"id_{nom_table}"] == i: i += 1
	return i


# Fonctions utilisées par le contrôleur accueil.py
def parties_terminees(connexion) -> list[dict]:
	"""
	Retourne les 10 dernières parties terminées, avec le pseudo du joueur et son score, 
	et la taille et la difficulté de la grille.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Liste de dictionnaires (clés : 'pseudo', 'score', 'taille', 'difficulté').
	"""
	query_parties = 'SELECT id_joueur, score, taille_grille, difficulté FROM partie WHERE en_cours = false ORDER BY date_création DESC LIMIT 10'
	query = f'SELECT J.pseudo, P.score, P.taille_grille AS taille, P.difficulté FROM ({query_parties}) P JOIN joueur J USING(id_joueur)'
	result = execute_select_query(connexion, query)
	return result

def nb_parties(connexion) -> dict:
	"""
	Retourne le nombre de parties en cours et terminées.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Dictionnaire (clés : 'en_cours', 'terminées', valeurs : nombre de parties).
	"""
	query = 'SELECT COUNT(*) AS nb FROM partie WHERE en_cours = %s'
	etats = ['en_cours', 'terminées']
	dico = {}
	for etat in etats:
		result = execute_select_query(connexion, query, [etat == 'en_cours'])
		dico[etat] = result[0]['nb']
	return dico


# Fonctions utilisées par le contrôleur regles.py
def get_tuiles_1element(connexion) -> dict:
	"""
	Retourne les images des tuiles à un seul élément, avec le nom de l'élément correspondant en clé.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Dictionnaire (clé = nom de l'élément, valeur = image de la tuile).
	"""
	query1 = 'SELECT id_tuile FROM contient_element GROUP BY id_tuile HAVING SUM(nombre) <= 1'
	query = f'SELECT id_tuile, nom_élément FROM contient_element WHERE id_tuile IN ({query1})'
	result = execute_select_query(connexion, query)
	return {dic["nom_élément"] : get_img_tuile(connexion, dic["id_tuile"]) for dic in result}


# Fonctions utilisées par le contrôleur classements.py
def infos_classement(connexion, taille_grille :int, difficulté :str) -> list[dict]:
	"""
	Récupère la liste des joueurs présents dans le classements souhaité.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	taille_grille : int
	    Taille des grilles du classement.
	difficulté : str
	    Difficulté des grilles du classement.

	Renvoie
	-------
	Liste de dictionnaires (clés : 'joueur', 'score', 'rang', 'date', 
	valeurs : dictionnaire(clés : nom, prénom, pseudo, année_naiss), score du joueur, rang du joueur, date de la partie).
	"""
	query = 'SELECT id_joueur, score, date_création AS date FROM partie WHERE en_cours=false AND taille_grille=%s AND difficulté=%s ORDER BY score DESC, date_création'
	result = execute_select_query(connexion, query, [taille_grille, difficulté])
	classement = []
	for rg, dic in enumerate(result):
		dic["joueur"] = get_infos_joueur(connexion, dic.pop("id_joueur"))
		dic['rang'] = rg + 1
		classement.append(dic)
	return classement


# Fonctions utilisées par le contrôleur statistiques.py
def moy_nb_parties(connexion) -> float:
	"""
	Retourne le nombre moyen de parties par joueur.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Nombre moyen de parties par joueur.
	"""
	return count_instances(connexion, "partie") / count_instances(connexion, "joueur")

def score_min_max(connexion) -> dict[tuple[int, dict]|str, None]:
	"""
	Retourne les informations sur les joueurs ayant le meilleur et le pire score toutes parties confondues.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Dictionnaire (clés : 'mini', 'maxi', valeurs : (score, dictionnaire(clés : nom, prénom, pseudo, année_naiss))).
	"""
	query = 'SELECT id_joueur, score FROM partie WHERE en_cours=false ORDER BY score {ordre}, date_création ASC LIMIT 1'
	tris = ['ASC', 'DESC']
	dico = {"mini":None, "maxi":None}
	for tri in tris:
		result_tmp = execute_select_query(connexion, query.format(ordre=tri))
		if len(result_tmp) > 0:
			result = result_tmp[0]
			joueur = get_infos_joueur(connexion, result["id_joueur"])
			dico["mini" if tri == 'ASC' else "maxi"] = (result['score'], joueur)
	return dico

def score_0(connexion) -> list[dict]:
	"""
	Retourne les informations sur les joueurs et les parties où le joueur n'a validé aucune contrainte.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Liste de dictionnaires (clés :'joueur', 'partie', valeurs : dictionnaire(clés : nom, prénom, pseudo, année_naiss), dictionnaire(clés : attributs de partie)).
	"""
	query = 'SELECT id_joueur, id_partie FROM partie WHERE en_cours=false AND score = 0'
	result = execute_select_query(connexion, query)
	return [{"joueur":get_infos_joueur(connexion, dic["id_joueur"]), "partie":get_infos_partie(connexion, dic["id_partie"])} for dic in result]


# Fonctions utilisées par le contrôleur parties.py
def parties_en_cours(connexion, id_joueur :int) -> list[dict]:
	"""
	Renvoie la liste des parties en cours du joueur d'identifiant 'id_joueur'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_joueur : int
	    Identifiant du joueur.

	Renvoie
	-------
	Liste de dictionnaires (clés :'id_partie', 'score', 'difficulté', 'taille').
	"""
	query1 = 'SELECT id_partie, score, id_grille FROM partie WHERE id_joueur = %s AND en_cours = true'
	query = f'SELECT P.id_partie, P.score, G.difficulté, G.taille FROM ({query1}) P JOIN grille G USING(id_grille)'
	return execute_select_query(connexion, query, [id_joueur])


# Fonctions utilisées par le contrôleur jeu.py
def nouvelle_partie(connexion, taille_grille :int, difficulté :str, id_joueur :int) -> int :
	"""
	Crée une nouvelle partie.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	taille_grille : int
	    Taille de la grille de la partie.
	difficulté : str
	    Difficulté de la grille de la partie.
	id_joueur : int
	    Identifiant du joueur associé à la partie.
	
	Renvoie
	-------
	L'identifiant de la nouvelle partie.
	"""
	query = 'INSERT INTO partie (id_partie, date_création, en_cours, score, id_joueur, taille_grille, difficulté, id_grille) ' \
	'VALUES (%s, %s, true, 0, %s, %s, %s, %s)'
	id_partie = id_disponible(connexion, "partie")
	date_création = datetime.now()
	id_grille = id_disponible(connexion, "grille")
	nouvelle_grille(connexion, id_grille, taille_grille, difficulté)
	
	query2 = 'SELECT COUNT(*) AS nb FROM classement WHERE taille_grille = %s AND difficulté=%s'
	result2 = execute_select_query(connexion, query2, [taille_grille, difficulté])
	if result2[0]['nb'] == 0 :
		nouveau_classement(connexion, taille_grille, difficulté, date_création)
	else : 
		maj_classement(connexion, taille_grille, difficulté, date_création)
	
	execute_other_query(connexion, query, [id_partie, date_création, id_joueur, taille_grille, difficulté, id_grille])
	return id_partie

def nouvelle_grille(connexion, id_grille :int, taille_grille :int, difficulté :str) :
	"""
	Crée une nouvelle grille.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_grille : int
	    Identifiant de la grille.
	taille_grille : int
	    Taille de la grille.
	difficulté : str
	    Difficulté de la grille.
	"""
	query = 'INSERT INTO grille (id_grille, taille, difficulté) VALUES (%s, %s, %s)'
	execute_other_query(connexion, query, [id_grille, taille_grille, difficulté])
	remplir_grille(connexion, id_grille, taille_grille, difficulté)

def remplir_grille(connexion, id_grille :int, taille_grille :int, difficulté :str) :
	"""
	Remplie la grille avec les tuiles contrainte.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_grille : int
	    Identifiant de la grille.
	taille_grille : int
	    Taille de la grille.
	difficulté : str
	    Difficulté de la grille.
	"""
	query = 'SELECT id_tuile FROM tuilecontrainte WHERE est_difficile=%s'
	insert_query = 'INSERT INTO contient_tuile_contrainte (id_tuile, id_grille, sur_ligne, position) VALUES (%s, %s, %s, %s)'

	if difficulté == "Moyenne" :
		tuiles_faciles = execute_select_query(connexion, query, [False])
		tuiles_difficiles = execute_select_query(connexion, query, [True])
		nb1 = len(tuiles_faciles)
		nb2 = len(tuiles_difficiles)
		for i in range(taille_grille):
			execute_other_query(connexion, insert_query, [tuiles_faciles[randint(0, nb1-1)]['id_tuile'], id_grille, True, i+1])
		for i in range(taille_grille):
			execute_other_query(connexion, insert_query, [tuiles_difficiles[randint(0, nb2-1)]['id_tuile'], id_grille, False, i+1])
	else :
		tuiles = execute_select_query(connexion, query, [difficulté=="Difficile"])
		nb = len(tuiles)
		for i in range(2*taille_grille):
			execute_other_query(connexion, insert_query, [tuiles[randint(0, nb-1)]['id_tuile'], id_grille, i<taille_grille, i%taille_grille +1])

def get_grille(connexion, id_grille :int) -> list[list[str|None]] :
	"""
	Renvoie la grille d'identifiant 'id_grille'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_grille : int
	    Identifiant de la grille.
	
	Renvoie
	-------
	Une liste contenant une liste pour chaque ligne, avec 
	None si la case est vide, le nom de l'image de la carte présente sinon.
	"""
	query = 'SELECT id_tuile FROM contient_tuile_contrainte WHERE id_grille=%s ORDER BY sur_ligne DESC, position'
	tuiles = execute_select_query(connexion, query, [id_grille])
	taille_grille = len(tuiles) // 2
	grille = [[None]]
	for i in range(taille_grille):
		grille[0].append(get_img_tuile(connexion, tuiles[i]["id_tuile"]))
		grille.append([get_img_tuile(connexion, tuiles[taille_grille + i]["id_tuile"])] + [None for _ in range(taille_grille)])
	return grille


def nouveau_classement(connexion, taille_grille :int, difficulté :str, date_création :datetime) :
	"""
	Crée un nouveau classement.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	taille_grille : int
	    Taille des parties du classement.
	difficulté : str
	    Difficulté des parties du classement.
	date_création : datetime
	    Date de création du classement.
	"""
	nom_classement = f"{taille_grille}x{taille_grille}-{difficulté}"
	query = 'INSERT INTO classement (taille_grille, difficulté, nom, date_création, date_maj) VALUES (%s, %s, %s, %s, %s)'
	return execute_other_query(connexion, query, [taille_grille, difficulté, nom_classement, date_création, date_création])

def maj_classement(connexion, taille_grille :int, difficulté :str, date_maj :datetime) :
	"""
	Met à jour la date du classement.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	taille_grille : int
	    Taille des parties du classement.
	difficulté : str
	    Difficulté des parties du classement.
	date_maj : datetime
	    Date de mise à jour du classement.
	"""
	query = 'UPDATE classement SET date_maj=%s WHERE taille_grille=%s AND difficulté=%s'
	return execute_other_query(connexion, query, [date_maj, taille_grille, difficulté])

def grille_remplie(connexion, id_partie :int) -> bool :
	"""
	Renvoie True si la grille est remplie, False sinon.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	
	Renvoie
	-------
	Le booléen correspondant.
	"""
	query = 'SELECT COUNT(*) AS nb FROM tour WHERE id_partie = %s'
	query_tmp = 'SELECT id_grille FROM partie WHERE id_partie = %s'
	query2 = f'SELECT taille FROM grille WHERE id_grille = ({query_tmp})'
	result = execute_select_query(connexion, query, [id_partie])[0]['nb']
	result2 = execute_select_query(connexion, query2, [id_partie])[0]['taille']
	return result == result2**2


# def get_table_like(connexion, nom_table, like_pattern):
#     """
#     Retourne les instances de la table nom_table dont le nom correspond au motif like_pattern
#     String nom_table : nom de la table
#     String like_pattern : motif pour une requête LIKE
#     """
#     motif = '%' + like_pattern + '%'
#     nom_att = 'nom'  # nom attribut dans ingrédient 
#     if nom_table == 'recette':  # à éviter
#         nom_att += '_recette'  # nom attribut dans recette 
#     query = sql.SQL("SELECT * FROM {} WHERE {} ILIKE {}").format(
#         sql.Identifier(nom_table),
#         sql.Identifier(nom_att),
#         sql.Placeholder())
#     #    like_pattern=sql.Placeholder(name=like_pattern))
#     return execute_select_query(connexion, query, [motif])


# def nouvelle_pioche(connexion, id_pioche :int, nb_tuiles_découvertes :int) :
# 	"""
# 	Crée une nouvelle pioche.
	
# 	Paramètres
# 	----------
# 	connexion : 
# 	    Connexion à la base de donnée.
# 	id_pioche : int
# 	    Identifiant de la pioche.
# 	nb_tuiles_découvertes : int
# 	    Nombre de tuiles à découvert.
# 	"""
# 	query = 'INSERT INTO pioche (id_pioche, nb_tuiles_découvertes) VALUES(%s, %s)'
# 	return execute_other_query(connexion, query, [id_pioche, nb_tuiles_découvertes])