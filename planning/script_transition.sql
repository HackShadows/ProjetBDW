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





INSERT INTO Element
SELECT E.nom AS nom_élément
FROM donnees_fournies.element E;

INSERT INTO Tuile
SELECT T.id AS id_tuile, T.fichier AS chemin_texture
FROM donnees_fournies.tuile T;

INSERT INTO TuileJeu
SELECT TJ.id AS id_tuile, E.nom AS nom_élément, TJ.nombre_element AS nombre
FROM donnees_fournies.tuile_jeu TJ JOIN donnees_fournies.element E ON donnees_fournies.tuile_jeu.id_element = donnees_fournies.element.id;

INSERT INTO TuileContrainte
SELECT TC.id AS id_tuile, TC.niveau AS difficulté, TC.points AS nb_points
FROM donnees_fournies.tuile_contrainte TC;



INSERT INTO 