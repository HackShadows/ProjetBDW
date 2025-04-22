from model.model_pg import parties_en_cours

if True:
	REQUEST_VARS['parties'] = parties_en_cours(SESSION['CONNEXION'], 27)
	REQUEST_VARS['AFFICHAGE'] = "DEFAUT"
	
	if POST and 'action' in POST and POST["action"][0] == "nouvelle_partie":
		REQUEST_VARS['AFFICHAGE'] = "FORMULAIRE"
		
else:
	REQUEST_VARS['AFFICHAGE'] = "ACCUEIL"
