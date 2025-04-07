from model.model_pg import get_joueurs, count_instances, parties_terminees, nb_parties, get_infos_joueur

if POST and 'id_joueur' in POST: SESSION['joueur_actif'] = get_infos_joueur(SESSION['CONNEXION'], POST['id_joueur'][0])

# REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), sorted(get_instances(SESSION['CONNEXION'], "joueur"), key=lambda d : d["nom"]))
REQUEST_VARS['joueurs'] = (count_instances(SESSION['CONNEXION'], "joueur"), get_joueurs(SESSION['CONNEXION']))
REQUEST_VARS['parties_terminées'] = parties_terminees(SESSION['CONNEXION'])
REQUEST_VARS['nb_parties'] = nb_parties(SESSION['CONNEXION'])
