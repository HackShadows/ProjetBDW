# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import get_classements, infos_classement

if POST and 'grille' in POST:
	taille_grille, difficulté = POST['grille'][0].split(" ")
	REQUEST_VARS['infos_classement'] = infos_classement(SESSION['CONNEXION'], taille_grille, difficulté)
else:
	REQUEST_VARS['classements'] = get_classements(SESSION['CONNEXION'])