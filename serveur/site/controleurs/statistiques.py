# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import moy_nb_parties, score_min_max, score_0, score_max

REQUEST_VARS['moyenne'] = moy_nb_parties(SESSION['CONNEXION'])
REQUEST_VARS['scores'] = score_min_max(SESSION['CONNEXION'])
REQUEST_VARS['score_0'] = score_0(SESSION['CONNEXION'])
REQUEST_VARS['score_max'] = score_max(SESSION['CONNEXION'])


# Score moyen en fonction du classement