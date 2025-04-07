# from tempfile import mkstemp
# from os.path import isfile, basename
# from os import access, R_OK

# if POST and 'bouton_generer' in POST:  # formulaire soumis
#     filepath = mkstemp(suffix='.txt', dir=SESSION['DIR_HISTORIQUE'])[1]  # mkstemp retourne un tuple
#     with open(filepath, 'w') as fp:  # écriture de l'historique dans le fichier temporaire
#         for d, a in SESSION['HISTORIQUE'].items():
#             fp.write(f"{d} - {a}\n")
#     if isfile(filepath) and access(filepath, R_OK):
#         REQUEST_VARS['fichier_genere'] = basename(filepath)
#     else:
#         REQUEST_VARS['message'] = f"Erreur : le fichier d'historique n'est pas disponible."
#         REQUEST_VARS['message_class'] = "alert-error"

from model.model_pg import get_instances, infos_classement

if POST and 'taille_grille' in POST and 'difficulté' in POST:
	taille_grille, difficulté = POST['grille'][0].split(" ")
	REQUEST_VARS['infos_classement'] = infos_classement(SESSION['CONNEXION'], taille_grille, difficulté)
else:
	REQUEST_VARS['classements'] = get_instances(SESSION['CONNEXION'], "classement")