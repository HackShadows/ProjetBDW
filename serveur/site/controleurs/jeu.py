# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import nouvelle_partie, get_infos_partie, fin_partie
from model.model_pg import nouvelle_pioche, get_pioche, get_id_pioche, défausser_pioche, remplir_pioche
from model.model_pg import get_grille, grille_remplie
from model.model_pg import get_contraintes_validées, get_img_tuile
from model.model_pg import nouveau_tour, get_tour, maj_classement, get_rang


connexion = SESSION['CONNEXION']


# Arrivée sur la page jeu depuis parties

if POST and ('taille_grille' in POST and 'difficulté' in POST or 'partie' in POST):
	if "partie" in POST: id_partie = POST["partie"][0]
	else: id_partie = nouvelle_partie(connexion, int(POST['taille_grille'][0]), POST['difficulté'][0], SESSION["joueur_actif"][0]["id_joueur"])
	
	SESSION['partie_en_cours'] = get_infos_partie(connexion, id_partie)
	SESSION['num_tour'] = 0 if "partie" not in POST else get_tour(connexion, id_partie)
	
	if "partie" not in POST:
		id_pioche = nouvelle_pioche(connexion)
		nouveau_tour(connexion, id_partie, 0, id_pioche)
	else:
		id_pioche = get_id_pioche(connexion, id_partie, SESSION['num_tour'])


# Partie finie

if "partie_en_cours" in SESSION and SESSION['num_tour'] == -1: del SESSION['partie_en_cours']


# Page jeu

if "partie_en_cours" in SESSION:
	REQUEST_VARS['grille_id'] = get_grille(connexion, SESSION['partie_en_cours']['id_partie'])
	REQUEST_VARS['taille_grille'] = SESSION['partie_en_cours']['taille_grille']
	id_partie = SESSION['partie_en_cours']['id_partie']

	if 'id_pioche' not in globals(): id_pioche = get_id_pioche(connexion, id_partie, SESSION['num_tour'])

	if POST:
		
		# Phase de jeu
		if "emplacement" in POST and "choisie" in POST :
			x, y = POST["emplacement"][0].split(",")
			x = int(x)
			y = int(y)
			rg = int(POST["choisie"][0]) - 1
			
			id_tuile = get_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"]))[rg]
			REQUEST_VARS["grille_id"][y][x] = id_tuile
			SESSION["num_tour"] += 1
			
			id_pioche = défausser_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"] - 1), rg)
			nouveau_tour(connexion, id_partie, SESSION["num_tour"], id_pioche, rg, id_tuile, x, y)
		
		# Phase de défausse
		elif "choisie" in POST :
			rg = int(POST["choisie"][0]) - 1

			SESSION["num_tour"] += 1

			id_pioche = défausser_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"] - 1), rg)
			nouveau_tour(connexion, id_partie, SESSION["num_tour"], id_pioche, rg)



	if grille_remplie(connexion, id_partie) : 
		REQUEST_VARS['phase'] = 'resultats'
		REQUEST_VARS['resultat_grille'] = get_contraintes_validées(connexion, REQUEST_VARS['grille_id'])
		REQUEST_VARS['score'] = sum(REQUEST_VARS['resultat_grille']["colonne"] + REQUEST_VARS['resultat_grille']["ligne"])
		fin_partie(connexion, id_partie, REQUEST_VARS['score'])
		maj_classement(connexion, REQUEST_VARS['taille_grille'], SESSION['partie_en_cours']['difficulté'])
		REQUEST_VARS['rang'] = get_rang(connexion, REQUEST_VARS['taille_grille'], SESSION['partie_en_cours']['difficulté'], id_partie)
		SESSION['num_tour'] = -1
		
		
	# Sélection de la phase suivante et transmission des données à la vue
	elif SESSION["num_tour"] % 4 < 2 : 
		REQUEST_VARS['phase'] = "joue_carte"
		if SESSION["num_tour"] % 4 == 0 : remplir_pioche(connexion, id_pioche)

	else : REQUEST_VARS['phase'] = "defausse_carte"

	REQUEST_VARS['grille'] = [[get_img_tuile(connexion, id_tuile) if id_tuile is not None else None for id_tuile in ligne] for ligne in REQUEST_VARS['grille_id']]

	REQUEST_VARS['pioche'] = [get_img_tuile(connexion, id_tuile) if id_tuile is not None  else None for id_tuile in get_pioche(connexion, id_pioche)]
