from model.model_pg import nouvelle_partie

if POST and 'taille_grille' in POST and 'difficulté' in POST:
	nouvelle_partie(SESSION['CONNEXION'], POST['taille_grille'], POST['difficulté'], SESSION["joueur_actif"]["id_joueur"])