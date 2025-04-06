from model.model_pg import nouvelle_partie

if POST and 'taille_grille' in POST and 'difficulté' in POST:
	nouvelle_partie(SESSION['CONNEXION'], POST['taille_grille'][0], POST['difficulté'][0], SESSION["joueur_actif"]["id_joueur"])