-- Transitionne les données des tables créées par BDW_données_fournies.sql dans nos tables à nous.



-- DONNEES FOURNIES :
-- ==================
-- element            (id        integer PKEY, nom           varchar(50)     , symbole        varchar(80)      ,                    ,                   );
-- tuile              (id        integer PKEY, typeT         varchar(50)     , fichier        varchar(80)      ,                    ,                   );
-- tuile_jeu          (id        integer PKEY, id_element    integer     PKEY, nombre_element integer          ,                    ,                   );
-- tuile_contrainte   (id        integer PKEY, niveau        varchar(50)     , points         integer          ,                    ,                   );
-- a_pour_contrainte  (id_tuile  integer PKEY, id_contrainte integer     PKEY, typeC          varchar(10)      ,                    ,                   );
-- contrainte_element (id        integer PKEY, id_element    integer         , nb_elements    integer          ,                    ,                   );
-- contrainte_nombre  (id        integer PKEY, typeC         varchar(50)     , libellé        varchar(250)     , nb_elements integer,                   );
-- grille             (id        integer PKEY, num_ligne     integer     PKEY, num_colonne    integer      PKEY, id_tuile    integer,                   );
-- pioche             (id_grille integer PKEY, rang          integer     PKEY, id_tuile       integer          ,                    ,                   );
-- joueur             (idJ       integer PKEY, nom           varchar(80)     , prénom         varchar(80)      , année_naiss integer, pseudo varchar(50));




-- Rien pour Classement


INSERT INTO Joueur
SELECT J.idJ AS id_joueur, J.nom AS nom, J.prénom AS prénom, J.pseudo AS pseudo, J.année_naiss AS année_naiss
FROM données_fournies.joueur J;


-- Rien pour Partie


INSERT INTO Grille
SELECT G.id AS id_grille, MAX(G.num_ligne) AS taille, NULL AS difficulté
FROM données_fournies.grille G
GROUP BY G.id;


INSERT INTO Pioche
SELECT P.id_grille AS id_pioche, COUNT(P.rang) AS nb_tuiles_découvertes
FROM données_fournies.pioche P
GROUP BY P.id_grille;


-- Rien pour Tour


INSERT INTO Element
SELECT E.nom AS nom_élément
FROM données_fournies.element E;


INSERT INTO Tuile
SELECT T.id AS id_tuile, T.fichier AS chemin_texture
FROM données_fournies.tuile T;


INSERT INTO TuileJeu
SELECT DISTINCT TJ.id AS id_tuile
FROM données_fournies.tuile_jeu TJ;


INSERT INTO TuileContrainte
SELECT TC.id AS id_tuile, FALSE, TC.points AS nb_points
FROM données_fournies.tuile_contrainte TC
WHERE TC.niveau = 'Facile';
INSERT INTO TuileContrainte
SELECT TC.id AS id_tuile, TRUE, TC.points AS nb_points
FROM données_fournies.tuile_contrainte TC
WHERE TC.niveau = 'Difficile';
-- INSERT INTO TuileContrainte
-- SELECT TC.id AS id_tuile, NULL, TC.points AS nb_points
-- FROM données_fournies.tuile_contrainte TC
-- WHERE TC.niveau NOT IN ('Facile', 'Difficile');


INSERT INTO Contrainte
SELECT CE.id AS id_contrainte
FROM données_fournies.contrainte_element CE;
INSERT INTO Contrainte
SELECT CN.id AS id_contrainte
FROM données_fournies.contrainte_nombre CN;


INSERT INTO ContrainteElement
SELECT CE.id AS id_contrainte, CE.nb_elements AS nombre, E.nom AS nom_élément
FROM données_fournies.contrainte_element CE JOIN données_fournies.element E ON CE.id_element = E.id;


INSERT INTO ContrainteNombre
SELECT CN.id AS id_contrainte, CN.nb_elements AS nombre, CN.typeC AS type_contrainte
FROM données_fournies.contrainte_nombre CN;



INSERT INTO associe_contrainte
SELECT APC.id_tuile AS id_tuile, APC.id_contrainte AS id_contrainte
FROM données_fournies.a_pour_contrainte APC;


INSERT INTO contient_element
SELECT TJ.id AS id_tuile, E.nom AS nom_élément, TJ.nombre_element AS nombre
FROM données_fournies.tuile_jeu TJ JOIN données_fournies.element E ON TJ.id_element = E.id;


INSERT INTO contient_tuile_contrainte
SELECT G.id_tuile AS id_tuile, G.id AS id_grille, TRUE, G.num_colonne
FROM données_fournies.grille G
WHERE G.num_ligne=0;
INSERT INTO contient_tuile_contrainte
SELECT G.id_tuile AS id_tuile, G.id AS id_grille, FALSE, G.num_ligne
FROM données_fournies.grille G
WHERE G.num_colonne=0;


INSERT INTO contient_tuile_jeu
SELECT P.id_tuile AS id_tuile, P.id_grille AS id_pioche, P.rang AS rang
FROM données_fournies.pioche P;

DROP SCHEMA IF EXISTS données_fournies CASCADE;
