from model.model_pg import get_instances, count_instances, parties_terminees, nb_parties, get_infos_joueur

if POST and 'id_joueur' in POST: SESSION['pseudo'] = get_infos_joueur(SESSION['CONNEXION'], POST['id_joueur'])["pseudo"]

REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), get_instances(SESSION['CONNEXION'], "joueur"))
REQUEST_VARS['parties_terminées'] = parties_terminees(SESSION['CONNEXION'])
REQUEST_VARS['nb_parties'] = nb_parties(SESSION['CONNEXION'])
