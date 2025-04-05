from model.model_pg import get_instances, count_instances, parties_terminees, nb_parties

REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), get_instances(SESSION['CONNEXION'], "joueur"))
REQUEST_VARS['parties_terminées'] = parties_terminees(SESSION['CONNEXION'])
REQUEST_VARS['nb_parties'] = nb_parties(SESSION['CONNEXION'])
