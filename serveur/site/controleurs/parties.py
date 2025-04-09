from model.model_pg import nouvelle_partie, parties_en_cours

if "joueur_actif" in SESSION:
	REQUEST_VARS['parties'] = parties_en_cours(SESSION['CONNEXION'], SESSION["joueur_actif"][0]["id_joueur"])
else:
	pass

if POST and 'action' in POST:
	if POST["action"][0] == "nouvelle_partie":
		REQUEST_VARS['AFFICHAGE'] = "FORMULAIRE"
	elif 'taille_grille' in POST and 'difficulté' in POST:
		nouvelle_partie(SESSION['CONNEXION'], POST['taille_grille'][0], POST['difficulté'][0], SESSION["joueur_actif"][0]["id_joueur"])
		REQUEST_VARS['AFFICHAGE'] = "DEFAUT"
	else:
		REQUEST_VARS['AFFICHAGE'] = "DEFAUT"
else:
	REQUEST_VARS['AFFICHAGE'] = "DEFAUT"