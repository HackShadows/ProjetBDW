from model.model_pg import nouvelle_partie


if POST:
	if 'action' in POST and POST["action"][0] == "nouvelle_partie":
		REQUEST_VARS['AFFICHAGE'] = "FORMULAIRE"
	else:
		REQUEST_VARS['AFFICHAGE'] = "DEFAUT"
	if 'taille_grille' in POST and 'difficulté' in POST:
		nouvelle_partie(SESSION['CONNEXION'], POST['taille_grille'][0], POST['difficulté'][0], SESSION["joueur_actif"]["id_joueur"])
else:
	REQUEST_VARS['AFFICHAGE'] = "DEFAUT"