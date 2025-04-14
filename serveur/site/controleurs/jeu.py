from model.model_pg import nouvelle_partie, get_infos_partie, grille_remplie

if 'taille_grille' in POST and 'difficulté' in POST:
	id_partie = nouvelle_partie(SESSION['CONNEXION'], int(POST['taille_grille'][0]), POST['difficulté'][0], SESSION["joueur_actif"][0]["id_joueur"])
	SESSION['partie_en_cours'] = get_infos_partie(SESSION['CONNEXION'], id_partie)

REQUEST_VARS['taille_grille'] = SESSION['partie_en_cours']['taille_grille']

if (grille_remplie(SESSION['CONNEXION'], SESSION['partie_en_cours']['id_partie'])) : REQUEST_VARS['phase'] = 'resultats'
else :
    pass

REQUEST_VARS['phase'] = "joue_carte" # 'defausse_carte'
REQUEST_VARS['grille'] = [
	[None       , 'tc111.png', 'tc111.png', 'tc111.png', 'tc111.png'],
	['tc111.png', 'tj42.png' , None       , 'tj42.png' , 'tj42.png' ],
	['tc111.png', None       , None       , None       , None       ],
	['tc111.png', None       , 'tj42.png' , None       , None       ],
	['tc111.png', None       , None       , None       , None       ],
]

REQUEST_VARS['pioche'] = ['tj01.png', None, 'tj03.png', 'tj04.png', 'tj05.png']

# REQUEST_VARS['score']
# REQUEST_VARS['resultat_grille'] = {
#	'colonne' : [0, 1, 5, 3],
#	'ligne'   : [9, 0, 0, 0],
# }
