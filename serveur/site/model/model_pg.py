# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

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

def get_rang(connexion, taille_grille :int, difficulté :str, id_partie :int) -> int:
	"""
	Renvoie le rang du joueur passé en paramètre dans le classement souhaité.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	taille_grille : int
	    Taille des grilles du classement.
	difficulté : str
	    Difficulté des grilles du classement.
	id_partie : int
	    Identifiant de la partie.

	Renvoie
	-------
	Rang du joueur dans le classement, 0 si le joueur n'apparaît pas dans le classement.
	"""
	query = 'SELECT id_partie FROM partie WHERE en_cours=false AND taille_grille=%s AND difficulté=%s ORDER BY score DESC, date_création'
	result = execute_select_query(connexion, query, [taille_grille, difficulté])
	for rg, dic in enumerate(result):
		if int(dic["id_partie"]) == id_partie: return rg+1
	return 0


# Fonctions utilisées par le contrôleur accueil.py
def nouveau_joueur(connexion, nom :str, prénom :str, pseudo :str, année :int) :
	"""
	Permet d'ajouter un nouveau joueur à la base de donnée.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	nom : str
	    Nom du nouveau joueur.
	prénom : str
	    Prénom du nouveau joueur.
	pseudo : str
	    Pseudonyme du nouveau joueur.
	année : int
	    Année de naissance du nouveau joueur.
	"""
	assert len(nom) <= 64 and len(prénom) <= 64 and len(pseudo) <= 64
	id_joueur = id_disponible(connexion, "joueur")
	query = 'INSERT INTO joueur (id_joueur, nom, prénom, pseudo, année_naiss) VALUES (%s, %s, %s, %s, %s)'
	execute_other_query(connexion, query, [id_joueur, nom, prénom, pseudo, année])

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
def infos_classement(connexion, taille_grille :int, difficulté :str) -> tuple[str, list[dict]]:
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
	Nom du classement + liste de dictionnaires (clés : 'joueur', 'score', 'rang', 'date', 'id_partie'
	valeurs : dictionnaire(clés : id_joueur, nom, prénom, pseudo, année_naiss), score du joueur, rang du joueur, date de la partie).
	"""
	query = 'SELECT id_joueur, score, date_création AS date, id_partie FROM partie WHERE en_cours=false AND taille_grille=%s AND difficulté=%s ORDER BY score DESC, date_création'
	query_nom = 'SELECT nom FROM classement WHERE taille_grille=%s AND difficulté=%s'
	result = execute_select_query(connexion, query, [taille_grille, difficulté])
	nom_classement = execute_select_query(connexion, query_nom, [taille_grille, difficulté])[0]['nom']
	classement = []
	for rg, dic in enumerate(result):
		dic["joueur"] = get_infos_joueur(connexion, dic.pop("id_joueur"))[0]
		dic['rang'] = rg + 1
		classement.append(dic)
	return (nom_classement, classement)

def get_classements(connexion) -> list[dict]:
	"""
	Renvoie la liste de tous les classements contenants au moins une partie.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Liste de dictionnaires (clés : attributs de 'classement').
	"""
	query1 = 'SELECT taille_grille, difficulté FROM partie WHERE en_cours=false GROUP BY taille_grille, difficulté'
	difficile = "difficulté = 'Difficile'"
	non_difficile = "difficulté != 'Difficile'"
	query_non_difficile = f'SELECT * FROM classement WHERE {non_difficile} AND (taille_grille, difficulté) IN ({query1}) ORDER BY difficulté, taille_grille'
	query_difficile = f'SELECT * FROM classement WHERE {difficile} AND (taille_grille, difficulté) IN ({query1}) ORDER BY difficulté, taille_grille'
	return execute_select_query(connexion, query_non_difficile) + execute_select_query(connexion, query_difficile)


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

def score_max(connexion) -> list[dict]:
	"""
	Retourne les informations sur les joueurs et les parties où le joueur a validé toutes les contraintes.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.

	Renvoie
	-------
	Liste de dictionnaires (clés :'joueur', 'partie', valeurs : dictionnaire(clés : nom, prénom, pseudo, année_naiss), dictionnaire(clés : attributs de partie)).
	"""
	query1 = 'SELECT SUM(T.nb_points) AS total, C.id_grille FROM tuilecontrainte T JOIN contient_tuile_contrainte C USING(id_tuile) GROUP BY C.id_grille'
	query2 = 'SELECT id_joueur, id_partie, score, id_grille FROM partie'
	query = f'SELECT P.id_joueur, P.id_partie FROM ({query1}) T JOIN ({query2}) P USING(id_grille) WHERE P.score = T.total'
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
	Liste de dictionnaires (clés :'id_partie', 'date_création', 'difficulté', 'taille').
	"""
	query = 'SELECT id_partie, date_création, taille_grille AS taille, difficulté FROM partie WHERE id_joueur = %s AND en_cours = true ORDER BY date_création DESC'
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
	id_tuiles_possibles = [i for i in range(101, 135)]
	for i in range(6): id_tuiles_possibles.append(145 + i)
	for i in range(2): id_tuiles_possibles.append(153 + i)
	if taille_grille >= 3: 
		for i in range(135, 145): id_tuiles_possibles.append(i)
		id_tuiles_possibles.append(151)
		for i in range(155, 158): id_tuiles_possibles.append(i)
		for i in range(160, 164): id_tuiles_possibles.append(i)
	if taille_grille >= 4:
		id_tuiles_possibles.append(152) 
		for i in range(2): id_tuiles_possibles.append(158 + i)
		id_tuiles_possibles.append(164)
	if taille_grille >= 5:
		for i in range(max(7, taille_grille-4)): id_tuiles_possibles.pop(153 + i)
	
	query = 'SELECT id_tuile FROM tuilecontrainte WHERE est_difficile=%s AND id_tuile IN (' + ",".join(map(str, id_tuiles_possibles)) + ')'
	insert_query = 'INSERT INTO contient_tuile_contrainte (id_tuile, id_grille, sur_ligne, position) VALUES (%s, %s, %s, %s)'

	if difficulté == "Moyenne" :
		tuiles_faciles = execute_select_query(connexion, query, [False])
		tuiles_difficiles = execute_select_query(connexion, query, [True])
		positions = [i < taille_grille for i in range(2*taille_grille)]
		nb1 = len(tuiles_faciles)
		nb2 = len(tuiles_difficiles)
		ligne = 1
		colonne = 1
		for i in range(taille_grille):
			position = positions.pop(randint(0, 2*taille_grille-1-i))
			execute_other_query(connexion, insert_query, [tuiles_faciles[randint(0, nb1-1)]['id_tuile'], id_grille, position, ligne if position else colonne])
			if position : ligne += 1
			else : colonne += 1
		for i in range(taille_grille):
			position = positions.pop(randint(0, taille_grille-1-i))
			execute_other_query(connexion, insert_query, [tuiles_difficiles[randint(0, nb2-1)]['id_tuile'], id_grille, position, ligne if position else colonne])
			if position : ligne += 1
			else : colonne += 1
	else :
		tuiles = execute_select_query(connexion, query, [difficulté=="Difficile"])
		nb = len(tuiles)
		for i in range(2*taille_grille):
			execute_other_query(connexion, insert_query, [tuiles[randint(0, nb-1)]['id_tuile'], id_grille, i<taille_grille, i%taille_grille +1])

def get_grille(connexion, id_partie :int) -> list[list[str|None]] :
	"""
	Renvoie la grille d'identifiant contenant l'ensemble des tuiles ayant été jouées durant la partie.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	
	Renvoie
	-------
	Une liste contenant une liste pour chaque ligne, avec 
	None si la case est vide, l'identifiant de la tuile présente sinon.
	"""
	query = 'SELECT id_tuile FROM contient_tuile_contrainte WHERE id_grille=%s ORDER BY sur_ligne DESC, position'
	query_id = 'SELECT id_grille FROM partie WHERE id_partie=%s'
	query2 = 'SELECT pos_x, pos_y, id_tuile FROM tour WHERE id_partie=%s and pos_x is not null order by pos_y, pos_x;'
	id_grille = int(execute_select_query(connexion, query_id, [id_partie])[0]['id_grille'])
	tuiles_contraintes = execute_select_query(connexion, query, [id_grille])
	taille_grille = len(tuiles_contraintes) // 2
	grille = [[None]]
	for i in range(taille_grille):
		grille[0].append(tuiles_contraintes[i]["id_tuile"])
		grille.append([tuiles_contraintes[taille_grille + i]["id_tuile"]] + [None for _ in range(taille_grille)])
	tuiles_jeu = execute_select_query(connexion, query2, [id_partie])
	for tuile in tuiles_jeu: grille[tuile['pos_y']][tuile['pos_x']] = int(tuile['id_tuile'])
	return grille


def get_pioche(connexion, id_pioche :int) -> list[int|None] :
	"""
	Renvoie la pioche d'identifiant 'id_pioche'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_pioche : int
	    Identifiant de la pioche.
	
	Renvoie
	-------
	Une liste contenant None si la case est vide, l'identifiant de la tuile présente sinon.
	"""
	query = 'SELECT id_tuile, rang FROM contient_tuile_jeu WHERE id_pioche=%s'
	tuiles = execute_select_query(connexion, query, [id_pioche])
	pioche = [None for _ in range(5)]
	for tuile in tuiles:
		pioche[tuile['rang']] = tuile["id_tuile"]
	return pioche

def get_id_pioche(connexion, id_partie :int, id_tour :int) -> int :
	"""
	Renvoie l'identifiant de la pioche associée au tour correspondant.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	id_tour : int
	    Identifiant du tour de jeu.
	
	Renvoie
	-------
	L'identifiant de la pioche.
	"""
	query = 'SELECT id_pioche FROM tour WHERE id_partie=%s AND id_tour=%s'
	return execute_select_query(connexion, query, [id_partie, id_tour])[0]["id_pioche"]


def nouveau_tour(connexion, id_partie :int, id_tour :int, id_pioche :int, rang :int|None = None, id_tuile :int|None = None, posx :int|None = None, posy :int|None = None) :
	"""
	Crée un nouveau tour de jeu dans la partie d'identifiant 'id_partie'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	id_tour : int
	    Identifiant du tour de jeu.
	id_pioche : int
	    Identifiant de la pioche associée au tour.
	rang : int
	    Position de la tuile jeu prise dans la pioche (0 -> 4).
	id_tuile : int
	    Identifiant de la tuile venant d'être jouée.
	posx : int
	    Numéro de la colonne où la tuile jeu a été placée.
	posy : int
	    Numéro de la ligne où la tuile jeu a été placée.
	"""
	query = 'INSERT INTO tour (id_tour, id_partie, pos_x, pos_y, rang, id_pioche, id_tuile) VALUES (%s, %s, %s, %s, %s, %s, %s)'
	execute_other_query(connexion, query, [id_tour, id_partie, posx, posy, rang, id_pioche, id_tuile])

def get_tour(connexion, id_partie :int) -> int :
	"""
	Renvoie l'identifiant du dernier tour de la partie en cours.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	
	Renvoie
	-------
	L'identifiant du tour.
	"""
	query = 'SELECT MAX(id_tour) AS max FROM tour WHERE id_partie=%s'
	return execute_select_query(connexion, query, [id_partie])[0]["max"]


def nouvelle_pioche(connexion) -> int :
	"""
	Crée un nouvelle pioche.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	
	Renvoie
	-------
	L'identifiant de la pioche créée.
	"""
	id_pioche = id_disponible(connexion, "pioche")
	query = 'INSERT INTO pioche (id_pioche, nb_tuiles_découvertes) VALUES (%s, 5)'
	execute_other_query(connexion, query, [id_pioche])
	remplir_pioche(connexion, id_pioche)
	return id_pioche

def remplir_pioche(connexion, id_pioche :int) :
	"""
	Remplie la pioche d'identifiant 'id_pioche'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_pioche : int
	    Identifiant de la pioche à remplir.
	"""
	tuiles_jeu = get_instances(connexion, "tuilejeu")
	query = 'SELECT rang FROM contient_tuile_jeu WHERE id_pioche = %s'
	rangs = [rang['rang'] for rang in execute_select_query(connexion, query, [id_pioche])]
	insert_query = 'INSERT INTO contient_tuile_jeu (id_tuile, id_pioche, rang) VALUES (%s, %s, %s)'
	nb = len(rangs)
	nb_tuiles = len(tuiles_jeu)
	rg = 0
	for _ in range(5-nb):
		while rg in rangs: rg += 1
		execute_other_query(connexion, insert_query, [tuiles_jeu[randint(0, nb_tuiles-1)]["id_tuile"], id_pioche, rg])
		rg += 1

def défausser_pioche(connexion, id_pioche :int, rang :int) -> int :
	"""
	Retire une tuile jeu de la pioche d'identifiant 'id_pioche'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_pioche : int
	    Identifiant de la pioche.
	rang : int
	    Rang de la tuile à retirer de la pioche (0 -> 4).
	
	Renvoie
	-------
	L'identifiant de la nouvelle pioche obtenue.
	"""
	assert 0 <= rang <= 4
	query = 'SELECT id_tuile, rang FROM contient_tuile_jeu WHERE id_pioche = %s'
	tuiles = [(tuile['id_tuile'], tuile["rang"]) for tuile in execute_select_query(connexion, query, [id_pioche]) if tuile["rang"] != rang]
	
	new_id_pioche = id_disponible(connexion, "pioche")
	insert_query1 = 'INSERT INTO pioche (id_pioche, nb_tuiles_découvertes) VALUES (%s, %s)'
	execute_other_query(connexion, insert_query1, [new_id_pioche, len(tuiles)])
	
	insert_query2 = 'INSERT INTO contient_tuile_jeu (id_tuile, id_pioche, rang) VALUES (%s, %s, %s)'
	for id_tuile, rang in tuiles:
		execute_other_query(connexion, insert_query2, [id_tuile, new_id_pioche, rang])
	
	return new_id_pioche


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

def maj_classement(connexion, taille_grille :int, difficulté :str, date_maj :datetime = None) :
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
	if date_maj is None : date_maj = datetime.now()
	query = 'UPDATE classement SET date_maj=%s WHERE taille_grille=%s AND difficulté=%s'
	return execute_other_query(connexion, query, [date_maj, taille_grille, difficulté])

def fin_partie(connexion, id_partie :int, score :int) :
	"""
	Ajoute la partie à son classement.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_partie : int
	    Identifiant de la partie.
	score : int
	    Score de la partie.
	"""
	query = 'UPDATE partie SET en_cours=false, score=%s WHERE id_partie=%s'
	return execute_other_query(connexion, query, [score, id_partie])


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
	query = 'SELECT COUNT(*) AS nb FROM tour WHERE id_partie = %s AND pos_x IS NOT NULL'
	query_tmp = 'SELECT id_grille FROM partie WHERE id_partie = %s'
	query2 = f'SELECT taille FROM grille WHERE id_grille = ({query_tmp})'
	result = execute_select_query(connexion, query, [id_partie])[0]['nb']
	result2 = execute_select_query(connexion, query2, [id_partie])[0]['taille']
	return result == result2**2


def get_contraintes(connexion, id_tuile :int) -> dict :
	"""
	Renvoie les informations de la tuile contrainte d'identifiant 'id_tuile'.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	id_tuile : int
	    Identifiant de la tuile contrainte.
	
	Renvoie
	-------
	Dictionnaire (clés :'type', 'nb_points', 'nombre' et ('type_contrainte' ou 'nom_élément')).
	"""
	query = 'SELECT id_contrainte FROM associe_contrainte WHERE id_tuile = %s'
	query_nombre = 'SELECT type_contrainte, nombre FROM contraintenombre WHERE id_contrainte = %s'
	query_élément = 'SELECT nom_élément, nombre FROM contrainteelement WHERE id_contrainte = %s'
	query_score = 'SELECT nb_points FROM tuilecontrainte WHERE id_tuile = %s'
	contraintes = execute_select_query(connexion, query, [id_tuile])
	score = int(execute_select_query(connexion, query_score, [id_tuile])[0]["nb_points"])
	nb_contraintes = len(contraintes)
	
	if nb_contraintes == 0: raise AssertionError("Pas de contrainte associée à cette tuile !")
	elif nb_contraintes == 1:
		contrainte_nombre = execute_select_query(connexion, query_nombre, [contraintes[0]['id_contrainte']])
		if len(contrainte_nombre) != 1: 
			contrainte_élément = execute_select_query(connexion, query_élément, [contraintes[0]['id_contrainte']])
			if len(contrainte_élément) != 1 : raise AssertionError("Problème !")
			return {"type" : "élément", "nb_points" : score, "nom_élément" : contrainte_élément[0]["nom_élément"], "nombre" : contrainte_élément[0]["nombre"]}
		else:
			return {"type" : "nombre", "nb_points" : score, "type_contrainte" : contrainte_nombre[0]["type_contrainte"], "nombre" : contrainte_nombre[0]["nombre"]}
	else:
		dico = {"type" : "élément", "nb_points" : score, "nom_élément" : [], "nombre" : []}
		for contrainte in contraintes:
			contrainte_élément = execute_select_query(connexion, query_élément, [contrainte['id_contrainte']])
			if len(contrainte_élément) != 1 : raise AssertionError("Problème !")
			dico['nom_élément'].append(contrainte_élément[0]["nom_élément"])
			dico['nombre'].append(contrainte_élément[0]["nombre"])
		return dico

def contrainte_nombre_valide(connexion, type_contrainte :str, nombre :int, tuiles_jeu :list[int]) -> bool :
	"""
	Indique si la contrainte nombre a été validée.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	type_contrainte : str
	    Type de contrainte (NB_Elts_Exact, NB_Diff_Elts, NB_Elt_Fix_Exact).
	nombre : int
	    Nombre associée à la contrainte.
	tuiles_jeu : list[int]
	    Liste des identifiants des tuiles jeu qui doivent vérifier la contrainte.
	
	Renvoie
	-------
	True si la contrainte est vérifiée, False sinon.
	"""
	if type_contrainte == "NB_Elts_Exact":
		return nombre == sum([sum(get_elements_tuile(connexion, id_tuile).values()) for id_tuile in tuiles_jeu])
	elif type_contrainte == "NB_Diff_Elts":
		return nombre == len(set(clé for id_tuile in tuiles_jeu for clé in get_elements_tuile(connexion, id_tuile).keys()))
	elif type_contrainte == "NB_Elt_Fix_Exact":
		dico = {}
		for id_tuile in tuiles_jeu :
			for k, v in get_elements_tuile(connexion, id_tuile).items() : dico[k] = v if k not in dico else v + dico[k]
		return nombre in dico.values()
	else:
		raise AssertionError("Type_contrainte incorrect !")

def contrainte_élément_valide(connexion, nom_élément :str, nombre :int|None, tuiles_jeu :list[int]) -> bool :
	"""
	Indique si la contrainte élément a été validée.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	nom_élément : str
	    Nom de l'élément (Kraken, Dragon, Maelstrom, Epave, Sable, Rocher).
	nombre : int|None
	    Nombre d'éléments devant être présent (None si l'élément est majoritaire).
	tuiles_jeu : list[int]
	    Liste des identifiants des tuiles jeu qui doivent vérifier la contrainte.
	
	Renvoie
	-------
	True si la contrainte est vérifiée, False sinon.
	"""
	if nombre is None:
		elts = {}
		for id_tuile in tuiles_jeu:
			assert id_tuile is not None
			elements = get_elements_tuile(connexion, id_tuile)
			for k, v in elements.items():
				if k in elts: elts[k] += v
				else: elts[k] = v
		if nom_élément not in elts: return False
		nb = elts[nom_élément]
		for v in elts.values():
			if v > nb : return False
		return True
	else:
		nb = 0
		for id_tuile in tuiles_jeu:
			assert id_tuile is not None
			elements = get_elements_tuile(connexion, id_tuile)
			if nom_élément in elements: nb += elements[nom_élément]
		return nb == nombre

def get_contraintes_validées(connexion, grille :list[list[int|None]]) -> dict[list[int]] :
	"""
	Renvoie les scores des différentes tuiles contraintes ayant été validées.
	
	Paramètres
	----------
	connexion : 
	    Connexion à la base de donnée.
	grille : list[list[int|None]]
	    Grille de la partie en cours composée des identifiants des tuiles.
	
	Renvoie
	-------
	Dictionnaire (clés :'colonne', 'ligne', valeurs : list[0 si la tuile n'est pas validée son score sinon]).
	"""
	dico = {"colonne" : [], "ligne" : []}

	# Vérification des contraintes de la colonne
	for ligne in grille[1:]:
		contraintes = get_contraintes(connexion, ligne[0])
		if contraintes["type"] == "élément":
			if isinstance(contraintes["nom_élément"], list):
				ajouter = True
				nb = len(contraintes["nom_élément"])
				for i in range(nb):
					if not contrainte_élément_valide(connexion, contraintes["nom_élément"][i], contraintes["nombre"][i], ligne[1:]):
						ajouter = False
						break
				dico['colonne'].append(contraintes["nb_points"] if ajouter else 0)
			else:
				dico['colonne'].append(contraintes["nb_points"] if contrainte_élément_valide(connexion, contraintes["nom_élément"], contraintes["nombre"], ligne[1:]) else 0)
		elif contraintes["type"] == "nombre":
			dico['colonne'].append(contraintes["nb_points"] if contrainte_nombre_valide(connexion, contraintes["type_contrainte"], contraintes["nombre"], ligne[1:]) else 0)
	
	# Vérification des contraintes de la ligne
	taille = len(grille)
	for colonne in range(1, taille):
		contraintes = get_contraintes(connexion, grille[0][colonne])
		tuiles_jeu = [ligne[colonne] for ligne in grille[1:]]
		if contraintes["type"] == "élément": 
			if isinstance(contraintes["nom_élément"], list):
				ajouter = True
				nb = len(contraintes["nom_élément"])
				for i in range(nb):
					if not contrainte_élément_valide(connexion, contraintes["nom_élément"][i], contraintes["nombre"][i], tuiles_jeu):
						ajouter = False
						break
				dico['ligne'].append(contraintes["nb_points"] if ajouter else 0)
			else:
				dico['ligne'].append(contraintes["nb_points"] if contrainte_élément_valide(connexion, contraintes["nom_élément"], contraintes["nombre"], tuiles_jeu) else 0)
		elif contraintes["type"] == "nombre":
			dico['ligne'].append(contraintes["nb_points"] if contrainte_nombre_valide(connexion, contraintes["type_contrainte"], contraintes["nombre"], tuiles_jeu) else 0)
	
	return dico

		
	
	

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