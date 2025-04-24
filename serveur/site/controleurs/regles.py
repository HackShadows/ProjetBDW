# Contributeur 1 : CISERANE Marius p2303380
# Contributeur 2 : BOULLOT Matthias p2306662

from model.model_pg import get_tuiles_1element

REQUEST_VARS['tuiles_uniques'] = get_tuiles_1element(SESSION['CONNEXION'])