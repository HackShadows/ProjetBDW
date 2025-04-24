# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import get_joueurs, count_instances, get_infos_joueur, nouveau_joueur
from model.model_pg import parties_terminees, nb_parties

if POST and 'id_joueur' in POST: 
    SESSION['joueur_actif'] = get_infos_joueur(SESSION['CONNEXION'], POST['id_joueur'][0])
    if 'partie_en_cours' in SESSION: SESSION.pop("partie_en_cours")

REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), get_joueurs(SESSION['CONNEXION']))
REQUEST_VARS['parties_terminées'] = parties_terminees(SESSION['CONNEXION'])
REQUEST_VARS['nb_parties'] = nb_parties(SESSION['CONNEXION'])
