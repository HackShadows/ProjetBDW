# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import get_instances, infos_classement

if POST and 'grille' in POST:
	taille_grille, difficulté = POST['grille'][0].split(" ")
	REQUEST_VARS['infos_classement'] = infos_classement(SESSION['CONNEXION'], taille_grille, difficulté)
	print(REQUEST_VARS['infos_classement'])
else:
	REQUEST_VARS['classements'] = get_instances(SESSION['CONNEXION'], "classement")