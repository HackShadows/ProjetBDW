from model.model_pg import parties_en_cours

if "joueur_actif" in SESSION:
	REQUEST_VARS['parties'] = parties_en_cours(SESSION['CONNEXION'], SESSION["joueur_actif"][0]["id_joueur"])
	REQUEST_VARS['AFFICHAGE'] = "DEFAUT"
	
	if POST and 'action' in POST and POST["action"][0] == "nouvelle_partie":
		REQUEST_VARS['AFFICHAGE'] = "FORMULAIRE"
		
else:
	REQUEST_VARS['AFFICHAGE'] = "ACCUEIL"