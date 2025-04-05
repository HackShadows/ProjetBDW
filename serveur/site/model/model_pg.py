import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from logzero import logger

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
	# if image is None: return None
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
	Dictionnaire (clés : nom, prénom, pseudo, année_naiss).
	"""
	query = 'SELECT nom, prénom, pseudo, année_naiss FROM joueur WHERE id_joueur=%s'
	return execute_select_query(connexion, query, [id_joueur])


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
	query = 'SELECT J.pseudo, P.score, P.taille_grille AS taille, P.difficulté FROM (%s) P JOIN joueur J USING(id_joueur)'
	result = execute_select_query(connexion, query, [query_parties])
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
	query = 'SELECT id_joueur, score, date_création AS date FROM partie WHERE taille_grille=%s AND difficulté=%s ORDER BY score DESC, date_création'
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

def score_min_max(connexion) -> dict[tuple[int, dict]]:
	"""
	Retourne les informations sur les joueurs ayant le meilleur et le pire score toutes parties confondues.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Dictionnaire (clés : mini, maxi, valeurs : (score, dictionnaire(clés : nom, prénom, pseudo, année_naiss))).
	"""
	query = 'SELECT id_joueur, score FROM partie ORDER BY score {ordre} LIMIT 1'
	tris = ['ASC', 'DESC']
	dico = {}
	for tri in tris:
		result = execute_select_query(connexion, query.format(ordre=tri))[0]
		joueur = get_infos_joueur(connexion, result["id_joueur"])
		dico["mini" if tri == 'ASC' else "maxi"] = (result['score'], joueur)
	return dico

# def insert_recipe(connexion, nom_recette, cat_recette):
#     """
#     Insère une nouvelle recette dans la BD
#     String nom_recette : nom de la recette
#     String cat_recette : catégorie de la recette
#     Retourne le nombre de tuples insérés, ou None
#     """
#     query = 'INSERT INTO recette (nom_recette, catégorie) VALUES(%s,%s)'
#     return execute_other_query(connexion, query, [nom_recette,cat_recette])

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
