from model.model_pg import get_joueurs, count_instances, parties_terminees, nb_parties

REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), get_joueurs(SESSION['CONNEXION']))
REQUEST_VARS['parties_terminées'] = parties_terminees(SESSION['CONNEXION'])
REQUEST_VARS['nb_parties'] = nb_parties(SESSION['CONNEXION'])
