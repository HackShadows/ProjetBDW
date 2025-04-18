from model.model_pg import nouvelle_partie, get_infos_partie, fin_partie
from model.model_pg import nouvelle_pioche, get_pioche, get_id_pioche, défausser_pioche, remplir_pioche
from model.model_pg import get_grille, grille_remplie
from model.model_pg import get_contraintes_validées, get_img_tuile
from model.model_pg import nouveau_tour, maj_classement


connexion = SESSION['CONNEXION']


# Arrivée sur la page jeu depuis parties

if POST and 'taille_grille' in POST and 'difficulté' in POST:
	id_partie = nouvelle_partie(connexion, int(POST['taille_grille'][0]), POST['difficulté'][0], SESSION["joueur_actif"][0]["id_joueur"])
	SESSION['partie_en_cours'] = get_infos_partie(connexion, id_partie)
	SESSION['grille'] = get_grille(connexion, SESSION['partie_en_cours']['id_grille'])
	SESSION['num_tour'] = 0
	id_pioche = nouvelle_pioche(connexion)
	nouveau_tour(connexion, id_partie, 0, id_pioche)



# Page jeu

REQUEST_VARS['taille_grille'] = SESSION['partie_en_cours']['taille_grille']
id_partie = SESSION['partie_en_cours']['id_partie']

if POST:
	
	if "emplacement" in POST and "choisie" in POST :
		x, y = POST["emplacement"][0].split(",")
		x = int(x)
		y = int(y)
		rg = int(POST["choisie"][0]) - 1
		
		SESSION["grille"][y][x] = get_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"]))[rg]
		SESSION["num_tour"] += 1
		
		id_pioche = défausser_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"] - 1), rg)
		nouveau_tour(connexion, id_partie, SESSION["num_tour"], id_pioche, rg, x, y)
	
	elif "choisie" in POST :
		rg = int(POST["choisie"][0]) - 1

		SESSION["num_tour"] += 1

		id_pioche = défausser_pioche(connexion, get_id_pioche(connexion, id_partie, SESSION["num_tour"] - 1), rg)
		nouveau_tour(connexion, id_partie, SESSION["num_tour"], id_pioche, rg)



if grille_remplie(connexion, id_partie) : 
	REQUEST_VARS['phase'] = 'resultats'
	REQUEST_VARS['resultat_grille'] = get_contraintes_validées(connexion, SESSION['grille'])
	REQUEST_VARS['score'] = sum(REQUEST_VARS['resultat_grille']["colonne"] + REQUEST_VARS['resultat_grille']["ligne"])
	fin_partie(connexion, id_partie, REQUEST_VARS['score'])
	maj_classement(connexion, REQUEST_VARS['taille_grille'], SESSION['partie_en_cours']['difficulté'])
	

elif SESSION["num_tour"] % 4 < 2 : 
	REQUEST_VARS['phase'] = "joue_carte"
	if SESSION["num_tour"] % 4 == 0 : remplir_pioche(connexion, id_pioche)

else : REQUEST_VARS['phase'] = "defausse_carte"

REQUEST_VARS['grille'] = [[get_img_tuile(connexion, id_tuile) if id_tuile is not None else None for id_tuile in ligne] for ligne in SESSION['grille']]

REQUEST_VARS['pioche'] = [get_img_tuile(connexion, id_tuile) if id_tuile is not None  else None for id_tuile in get_pioche(connexion, id_pioche)]
