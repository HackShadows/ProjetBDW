import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from logzero import logger

def execute_select_query(connexion, query :str, params :list=[]) -> list[dict]|None:
    """
    Méthode générique pour exécuter une requête SELECT (qui peut retourner plusieurs instances).
    Utilisée par des fonctions plus spécifiques.

    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    query : str like
        Requête pour le SELECT.
    params : list
        Paramètres à ajouter à la requête.

    Renvoie
    -------
    Une liste de dictionnaires. Chaque dictionnaire correspond à une ligne.
    """
    with connexion.cursor() as cursor:
        try:
            cursor.execute(query, params)
            cursor.row_factory = dict_row
            result = cursor.fetchall()
            return result 
        except psycopg.Error as e:
            logger.error(e)
    return None

def execute_other_query(connexion, query :str, params :list=[]) -> int|None:
    """
    Méthode générique pour exécuter une requête INSERT, UPDATE, DELETE.
    Utilisée par des fonctions plus spécifiques.
    
    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    query : str like
        Requête à exécuter.
    params : list
        Paramètres à ajouter à la requête.

    Renvoie
    -------
    Le nombre d'enregistrements.
    """
    with connexion.cursor() as cursor:
        try:
            cursor.execute(query, params)
            result = cursor.rowcount
            return result 
        except psycopg.Error as e:
            logger.error(e)
    return None

def get_instances(connexion, nom_table :str) -> list[dict]|None:
    """
    Retourne les instances de la table 'nom_table'.
    
    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    nom_table : str
        Nom de la table.

    Renvoie
    -------
    Les enregistrements de la table 'nom_table'.
    """
    query = sql.SQL('SELECT * FROM {table}').format(table=sql.Identifier(nom_table))
    return execute_select_query(connexion, query)

def count_instances(connexion, nom_table :str) -> int:
    """
    Retourne le nombre d'instances de la table 'nom_table'.
    
    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    nom_table : str
        Nom de la table.

    Renvoie
    -------
    Le nombre d'enregistrements de la table 'nom_table'.
    """
    query = sql.SQL('SELECT COUNT(*) AS nb FROM {table}').format(table=sql.Identifier(nom_table))
    nb = execute_select_query(connexion, query)
    if nb is None: return 0
    return nb[0]['nb']



def get_img_tuile(connexion, id_tuile :int) -> str:
    """
    Retourne l'image associée à la tuile d'identifiant 'id_tuile'

    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    id_tuile : int
        Identifiant de la tuile.

    Renvoie
    -------
    Nom de l'image.
    """
    query = 'SELECT chemin_texture FROM tuile WHERE id_tuile=%s'
    image = execute_select_query(connexion, query, [id_tuile])
    if image is None: return None
    return image[0]['chemin_texture']

def get_nb_element(connexion, id_tuile :int) -> int:
    """
    Retourne le nombre d'éléments présents sur la tuile jeu d'identifiant 'id_tuile'
    
    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    id_tuile : int
        Identifiant de la tuile jeu.

    Renvoie
    -------
    Nombre d'éléments présents sur la tuile.
    """
    query = 'SELECT SUM(nombre) AS nb FROM contient_element WHERE id_tuile=%s '
    nb = execute_select_query(connexion, query, [id_tuile])
    if nb is None: return None
    return nb[0]['nb']

def get_element_simple(connexion, nom_element :str) -> str:
    """
    Retourne l'image de la tuile possédant seulement un élément 'nom_element'
    
    Paramètres
    ----------
    connexion : 
        Connexion à la base de donnée.
    nom_element : str
        Nom de l'élément à afficher.

    Renvoie
    -------
    Nom de l'image correspondant à la tuile souhaitée.
    """
    query = 'SELECT * FROM etape WHERE id_recette=%s ORDER BY numero'
    return execute_select_query(connexion, query, [nom_element])

def is_existing_recipe(connexion, nom_recette):
    """
    retourne True si le nom de la recette n'existe pas dans la BD
    String nom_recette : nom de la recette
    Retourne un booléen
    """
    query = 'SELECT count(*) AS nb FROM recette WHERE nom_recette=%s'
    nb = execute_select_query(connexion, query, [nom_recette])[0]['nb']
    return (nb > 0)

def insert_recipe(connexion, nom_recette, cat_recette):
    """
    Insère une nouvelle recette dans la BD
    String nom_recette : nom de la recette
    String cat_recette : catégorie de la recette
    Retourne le nombre de tuples insérés, ou None
    """
    query = 'INSERT INTO recette (nom_recette, catégorie) VALUES(%s,%s)'
    return execute_other_query(connexion, query, [nom_recette,cat_recette])

def get_table_like(connexion, nom_table, like_pattern):
    """
    Retourne les instances de la table nom_table dont le nom correspond au motif like_pattern
    String nom_table : nom de la table
    String like_pattern : motif pour une requête LIKE
    """
    motif = '%' + like_pattern + '%'
    nom_att = 'nom'  # nom attribut dans ingrédient 
    if nom_table == 'recette':  # à éviter
        nom_att += '_recette'  # nom attribut dans recette 
    query = sql.SQL("SELECT * FROM {} WHERE {} ILIKE {}").format(
        sql.Identifier(nom_table),
        sql.Identifier(nom_att),
        sql.Placeholder())
    #    like_pattern=sql.Placeholder(name=like_pattern))
    return execute_select_query(connexion, query, [motif])
