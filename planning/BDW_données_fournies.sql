DROP SCHEMA IF EXISTS données_fournies;
CREATE SCHEMA données_fournies;
SET search_path TO données_fournies;

CREATE TABLE element(
    id integer PRIMARY KEY,
    nom varchar(50),
    symbole varchar(80)
);

INSERT INTO element(id, nom, symbole) VALUES (1,'Kraken','kraken.png');
INSERT INTO element(id, nom, symbole) VALUES (2,'Dragon','dragon.png'); 
INSERT INTO element(id, nom, symbole) VALUES (3,'Maelstrom','maelstrom.png'); 
INSERT INTO element(id, nom, symbole) VALUES (4,'Epave','epave.png'); 
INSERT INTO element(id, nom, symbole) VALUES (5,'Sable','sable.png');
INSERT INTO element(id, nom, symbole) VALUES (6,'Rocher','rocher.png'); 


-- TUILES JEU
CREATE TABLE tuile(
    id integer PRIMARY KEY,
    typeT varchar(50),
    fichier varchar(80)
);

CREATE TABLE tuile_jeu(
    id integer,
    id_element integer,
    nombre_element integer,
    PRIMARY KEY( id, id_element )
);

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (1,1,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (1,'jeu','tj01.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (2,2,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (2,'jeu','tj02.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (3,3,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (3,'jeu','tj03.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (4,4,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (4,'jeu','tj04.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (5,5,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (5,'jeu','tj05.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (6,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (6,'jeu','tj06.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (7,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (7,'jeu','tj07.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (8,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (8,'jeu','tj08.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (9,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (9,'jeu','tj09.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (10,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (10,'jeu','tj10.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (11,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (11,'jeu','tj11.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (12,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (12,'jeu','tj12.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (13,1,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (13,'jeu','tj13.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (14,2,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (14,'jeu','tj14.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (15,3,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (15,'jeu','tj15.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (16,4,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (16,'jeu','tj16.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (17,5,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (17,'jeu','tj17.png');
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (18,6,3);
INSERT INTO tuile (id, typeT, fichier) VALUES (18,'jeu','tj18.png');


INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (19,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (19,2,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (19,'jeu','tj19.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (20,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (20,3,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (20,'jeu','tj20.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (21,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (21,4,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (21,'jeu','tj21.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (22,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (22,5,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (22,'jeu','tj22.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (23,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (23,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (23,'jeu','tj23.png');


INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (24,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (24,3,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (24,'jeu','tj24.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (25,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (25,4,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (25,'jeu','tj25.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (26,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (26,5,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (26,'jeu','tj26.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (27,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (27,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (27,'jeu','tj27.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (28,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (26,4,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (28,'jeu','tj28.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (29,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (29,5,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (29,'jeu','tj29.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (30,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (30,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (30,'jeu','tj30.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (31,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (31,5,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (31,'jeu','tj31.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (32,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (32,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (32,'jeu','tj32.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (33,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (33,6,1);
INSERT INTO tuile (id, typeT, fichier) VALUES (33,'jeu','tj33.png');



INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (34,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (34,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (34,'jeu','tj34.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (35,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (35,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (35,'jeu','tj35.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (36,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (36,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (36,'jeu','tj36.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (37,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (37,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (37,'jeu','tj37.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (38,1,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (38,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (38,'jeu','tj38.png');


INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (39,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (39,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (39,'jeu','tj39.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (40,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (40,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (40,'jeu','tj40.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (41,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (41,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (41,'jeu','tj41.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (42,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (42,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (42,'jeu','tj42.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (43,2,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (43,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (43,'jeu','tj43.png');



INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (44,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (44,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (44,'jeu','tj44.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (45,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (45,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (45,'jeu','tj45.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (46,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (46,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (46,'jeu','tj46.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (47,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (47,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (47,'jeu','tj47.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (48,3,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (48,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (48,'jeu','tj48.png');


INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (49,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (49,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (49,'jeu','tj49.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (50,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (50,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (50,'jeu','tj50.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (51,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (51,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (51,'jeu','tj51.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (52,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (52,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (52,'jeu','tj52.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (53,4,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (53,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (53,'jeu','tj53.png');



INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (54,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (54,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (54,'jeu','tj54.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (55,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (55,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (55,'jeu','tj55.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (56,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (56,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (56,'jeu','tj56.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (57,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (57,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (57,'jeu','tj57.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (58,5,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (58,6,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (58,'jeu','tj58.png');



INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (59,6,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (59,1,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (59,'jeu','tj59.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (60,6,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (60,2,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (60,'jeu','tj60.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (61,6,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (61,3,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (61,'jeu','tj61.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (62,6,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (62,4,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (62,'jeu','tj62.png');

INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (63,6,1);
INSERT INTO tuile_jeu (id, id_element, nombre_element) VALUES (63,5,2);
INSERT INTO tuile (id, typeT, fichier) VALUES (63,'jeu','tj63.png');





-- TUILES CONTRAINTES

CREATE TABLE tuile_contrainte (
        id integer PRIMARY KEY,
        niveau varchar(50),
        points integer
);

CREATE TABLE a_pour_contrainte (
        id_tuile integer,
        id_contrainte integer,
        typeC varchar(10),
        PRIMARY KEY( id_tuile, id_contrainte )
);


-- Pas de kraken
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (101,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (101,1,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (101,'contrainte','tc101.png');

-- Pas de dragon
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (102,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (102,2,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (102,'contrainte','tc102.png');

-- Pas de maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (103,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (103,3,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (103,'contrainte','tc103.png');

-- Pas d'épave
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (104,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (104,4,'elt');  
INSERT INTO tuile (id, typeT, fichier) VALUES (104,'contrainte','tc104.png');

-- Pas de sable
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (105,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (105,5,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (105,'contrainte','tc105.png');

-- Pas de rocher
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (106,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (106,6,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (106,'contrainte','tc106.png');


-- Pas de Kraken, pas de dragon
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (107,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (107,1,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (107,2,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (107,'contrainte','tc107.png');

-- Pas de Maelstrom, pas d'épave
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (108,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (108,3,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (108,4,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (108,'contrainte','tc108.png');

-- Pas de sable, pas de rocher
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (109,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (109,5,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (109,6,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (109,'contrainte','tc109.png');

-- Pas de Kraken, pas de rocher
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (110,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (110,1,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (110,6,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (110,'contrainte','tc110.png');

-- Pas de Dragon, pas de sable
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (111,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (111,2,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (111,5,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (111,'contrainte','tc111.png');

-- Pas de Maelstrom, pas d'épave
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (112,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (112,3,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (112,4,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (112,'contrainte','tc112.png');

-- Pas de Kraken, pas de Maelstrom, pas de sable
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (113,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (113,1,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (113,3,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (113,5,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (113,'contrainte','tc113.png');

-- Pas de Dragon, pas d'épave, pas de rocher
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (114,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (114,2,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (114,4,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (114,6,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (114,'contrainte','tc114.png');

-- Pas de Kraken, pas de Dragon, pas de maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (115,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (115,1,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (115,2,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (115,3,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (115,'contrainte','tc115.png');

-- Pas d'épave, pas de sable, pas de rocher
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (116,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (116,4,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (116,5,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (116,6,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (116,'contrainte','tc116.png');


-- 3 krakens
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (117,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (117,19,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (117,'contrainte','tc117.png');

-- 3 dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (118,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (118,20,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (118,'contrainte','tc118.png');

-- 3 maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (119,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (119,21,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (119,'contrainte','tc119.png');

-- 3 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (120,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (120,22,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (120,'contrainte','tc120.png');

-- 3 sable
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (121,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (121,23,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (121,'contrainte','tc121.png');

-- 3 rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (122,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (122,24,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (122,'contrainte','tc122.png');


--  1 kraken et 2 dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (123,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (123,7,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (123,14,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (123,'contrainte','tc123.png');


--  1 maelstrom  et 2 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (124,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (124,9,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (124,16,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (124,'contrainte','tc124.png');


--  1 sable et 2 rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (125,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (125,11,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (125,18,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (125,'contrainte','tc125.png');


-- 4 Krakens
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (126,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (126,25,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (126,'contrainte','tc126.png');

-- 4 Dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (127,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (127,26,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (127,'contrainte','tc127.png');

-- 4 Maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (128,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (128,27,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (128,'contrainte','tc128.png');

-- 4 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (129,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (129,28,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (129,'contrainte','tc129.png');

-- 4 sables
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (130,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (130,29,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (130,'contrainte','tc130.png');

-- 4 Rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (131,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (131,30,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (131,'contrainte','tc131.png');

--  2 kraken et 2 dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (132,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (132,13,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (132,14,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (132,'contrainte','tc132.png');

--  2 maelstrom  et 2 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (133,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (133,15,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (133,16,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (133,'contrainte','tc133.png');

--  2 sable maelstrom  et 2 rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (134,'Facile',6);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (134,17,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (134,18,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (134,'contrainte','tc134.png');


-- 5 krakens
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (135,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (135,31,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (135,'contrainte','tc135.png');

-- 5 dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (136,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (136,32,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (136,'contrainte','tc136.png');

-- 5 maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (137,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (137,33,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (137,'contrainte','tc137.png');

-- 5 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (138,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (138,34,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (138,'contrainte','tc138.png');

-- 5 sables
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (139,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (139,35,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (139,'contrainte','tc139.png');

-- 5 rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (140,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (140,36,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (140,'contrainte','tc140.png');

--  3 kraken et 2 maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (141,'Difficile',7);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (141,19,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (141,15,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (141,'contrainte','tc141.png');

--  3 dragons  et 2 épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (142,'Difficile',7);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (142,20,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (142,16,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (142,'contrainte','tc142.png');

--  3 maelstrom  et 2 sables
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (143,'Difficile',7);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (143,21,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (143,17,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (143,'contrainte','tc143.png');

--  3 épaves  et 2 rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (144,'Difficile',7);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (144,22,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (144,18,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (144,'contrainte','tc144.png');


-- Majoritaire kraken
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (145,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (145,37,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (145,'contrainte','tc145.png');

-- Majoritaire dragon
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (146,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (146,38,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (146,'contrainte','tc146.png');

-- Majoritaire maelstrom
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (147,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (147,39,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (147,'contrainte','tc147.png');

-- Majoritaire épaves
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (148,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (148,40,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (148,'contrainte','tc148.png');

-- Majoritaire sable
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (149,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (149,41,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (149,'contrainte','tc149.png');

-- Majoritaire rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (150,'Facile',4);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (150,42,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (150,'contrainte','tc150.png');


--  3 Kraken et 3 Rochers
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (151,'Difficile',8);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (151,19,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (151,24,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (151,'contrainte','tc151.png');

-- 4 épaves et 4 dragons
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (152,'Difficile',10);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (152,26,'elt');
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (152,28,'elt');
INSERT INTO tuile (id, typeT, fichier) VALUES (152,'contrainte','tc152.png');




-- 5 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (153,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (153,43,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (153,'contrainte','tc153.png');

-- 6 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (154,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (154,44,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (154,'contrainte','tc154.png');

-- 7 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (155,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (155,45,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (155,'contrainte','tc155.png');

-- 8 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (156,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (156,46,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (156,'contrainte','tc156.png');

-- 9 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (157,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (157,47,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (157,'contrainte','tc157.png');

-- 10 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (158,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (158,48,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (158,'contrainte','tc158.png');

-- 11 éléments sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (159,'Difficile',11);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (159,49,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (159,'contrainte','tc159.png');


-- 5 éléments différents sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (160,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (160,50,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (160,'contrainte','tc160.png');

-- 6 éléments différents sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (161,'Facile',5);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (161,51,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (161,'contrainte','tc161.png');


-- 5 fois un élément au choix sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (162,'Difficile',12);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (162,52,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (162,'contrainte','tc162.png');

-- 6 fois un élément au choix sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (163,'Difficile',13);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (163,53,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (163,'contrainte','tc163.png');

-- 7 fois un élément au choix sur la ligne/colonne
INSERT INTO tuile_contrainte (id, niveau, points) VALUES (164,'Difficile',14);
INSERT INTO a_pour_contrainte( id_tuile, id_contrainte, typeC) VALUES (164,54,'nb');
INSERT INTO tuile (id, typeT, fichier) VALUES (164,'contrainte','tc164.png');

-- -----------------------
-- Les contraintes
CREATE TABLE contrainte_element (
    id integer PRIMARY KEY,
    id_element integer,
    nb_elements integer
    );

CREATE TABLE contrainte_nombre (
    id integer PRIMARY KEY,
    typeC varchar(50),
    libellé varchar(250),
    nb_elements integer
    );

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (1,1,0);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (2,2,0);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (3,3,0);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (4,4,0); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (5,5,0);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (6,6,0);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (7,1,1);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (8,2,1);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (9,3,1);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (10,4,1); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (11,5,1);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (12,6,1);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (13,1,2);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (14,2,2);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (15,3,2);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (16,4,2); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (17,5,2);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (18,6,2);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (19,1,3);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (20,2,3);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (21,3,3);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (22,4,3); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (23,5,3);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (24,6,3);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (25,1,4);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (26,2,4);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (27,3,4);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (28,4,4); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (29,5,4);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (30,6,4);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (31,1,5);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (32,2,5);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (33,3,5);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (34,4,5); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (35,5,5);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (36,6,5);

INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (37,1,null);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (38,2,null);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (39,3,null);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (40,4,null); 
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (41,5,null);
INSERT INTO contrainte_element (id, id_element, nb_elements)  VALUES (42,6,null);

INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (43,'NB_Elts_Exact', 'Nombre exact d''éléments sur la ligne/colonne',5);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (44,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',6);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (45,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',7);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (46,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',8);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (47,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',9);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (48,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',10);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (49,'NB_Elts_Exact','Nombre exact d''éléments sur la ligne/colonne',11);

INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (50,'NB_Diff_Elts','Nombre exact d''éléments différents sur la ligne/colonne',5);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (51,'NB_Diff_Elts','Nombre exact d''éléments différents sur la ligne/colonne',6);

INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (52,'NB_Elt_Fix_Exact','Nombre exact pour 1 élément au choix sur la ligne/colonne',5);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (53,'NB_Elt_Fix_Exact','Nombre exact pour 1 élément au choix sur la ligne/colonne',6);
INSERT INTO contrainte_nombre (id, typeC, libellé, nb_elements)  VALUES (54,'NB_Elt_Fix_Exact','Nombre exact pour 1 élément au choix sur la ligne/colonne',7);


-- ***********************************************************************

CREATE TABLE grille (
    id integer,
    num_ligne integer,
    num_colonne integer,
    id_tuile integer,
    PRIMARY KEY (id, num_ligne, num_colonne)
);

INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,0,1,102);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,0,2,112);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,0,3,122);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,0,4,132);

INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,1,0,101);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,2,0,111);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,3,0,121);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,4,0,131);


INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,1,1,10);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,1,2,20);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,1,3,30);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,1,4,40);

INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,2,1,1);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,2,2,21);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,2,3,31);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,2,4,41);

INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,3,1,4);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,3,2,24);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,3,3,34);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,3,4,44);

INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,4,1,6);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,4,2,26);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,4,3,36);
INSERT INTO grille (id, num_ligne, num_colonne, id_tuile) VALUES (1,4,4,46);

CREATE TABLE pioche (
    id_grille integer,
    rang integer,
    id_tuile integer,
    PRIMARY KEY (id_grille, rang)
);

INSERT INTO pioche (id_grille, rang, id_tuile) VALUES (1, 0, 1);
INSERT INTO pioche (id_grille, rang, id_tuile) VALUES (1, 1, 12);
INSERT INTO pioche (id_grille, rang, id_tuile) VALUES (1, 2, 23);
INSERT INTO pioche (id_grille, rang, id_tuile) VALUES (1, 3, 34);
INSERT INTO pioche (id_grille, rang, id_tuile) VALUES (1, 4, 45);



CREATE TABLE joueur (
    idJ integer Primary key,
    nom varchar(80),
    prénom varchar(80),
    année_naiss integer,
    pseudo varchar(50)
);
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (11, 'BONO','Jean',1998,'BJ1998');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (12, 'HETTE','Rose',1999,'HR1999');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (13, 'ONETTE','Camille',1998,'OC1998');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (14, 'ONETTE','Marie',1988,'OM1988');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (15, 'TARTINE','Kimberley',1988,'TK1988');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (16, 'DABITUDE','Côme',2010,'DC2010');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (17, 'INE','Ruth',1991,'IR1991');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (18, 'FERRAND','Teddy',1990,'FT1990');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (19, 'LAIZOTRES','Pâcome',1983,'LP1983');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (20, 'TOP','Théo',2000,'TT2000');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (21, 'ACOOL','Meg',1985,'AM1985');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (22, 'HERE','Axel',1984,'HA1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (23, 'PELLE','Sarah',1991,'PS1991');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (24, 'SURE','Sarah',1999,'SS1999');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (25, 'LEFRIGO','Steve, Eudes, Hubert, Yann, Adam',1983,'LS1983');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (26, 'FELAMOTO','Abraham',1984,'FA1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (27, 'AIGRE-DENLASAUCE','Melvyn',1988,'AM1988');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (28, 'APOURTOUCE','Yann',1987,'AY1987');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (29, 'FACTURE','Manu',2009,'FM2009');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (30, 'OCHON','Paul',2003,'OP2003');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (31, 'FASSOL','Rémi',1990,'FR1990');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (32, 'NAUH','Pia',1997,'NP1997');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (33, 'TARE','Guy',1998,'TG1998');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (34, 'CAS','Harmony',2003,'CH2003');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (35, 'RIE','Brad',1988,'RB1988');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (36, 'DIE','Sam',2010,'DS2010');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (37, 'HOL','Ethan',1981,'HE1981');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (38, 'PABIEN','Eva',1993,'PE1993');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (39, 'MALADE','Yles',2004,'MY2004');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (40, 'MALOPIET','Ella',2010,'ME2010');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (41, 'VA-AREUCULON','Ellie',1984,'VE1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (42, 'CAMAIS','Léon',1995,'CL1995');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (43, 'CROC','Odile',1989,'CO1989');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (44, 'LANGLAIS','Elodie',1981,'LE1981');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (45, 'CATTE','Suri',1998,'CS1998');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (46, 'GAROU','Lou',2003,'GL2003');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (47, 'ABBET','Oscar',2009,'AO2009');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (48, 'LOUPE','Macha',2008,'LM2008');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (49, 'ME','Sarah',1984,'MS1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (50, 'PELET-TAMERE','Tara',1997,'PT1997');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (51, 'FROINICHO','Jenny',1994,'FJ1994');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (52, 'AIHAIRE','Line',1986,'AL1986');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (53, 'OMIALE','Pauline',2004,'OP2004');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (54, 'PERET','Ines',2005,'PI2005');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (55, 'PLURIEN','Jonathan',2006,'PJ2006');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (56, 'FRUIT','Jude',1989,'FJ1989');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (57, 'VERRE','Justin',1982,'VJ1982');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (58, 'TINE','Clément',2008,'TC2008');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (59, 'ANASSE','Anne',2000,'AA2000');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (60, 'BANNE','Anne',1998,'BA1998');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (61, 'VERSAIRE','Annie',1980,'VA1980');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (62, 'FETE','Célia',1989,'FC1989');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (63, 'FEUILLE-CIZO','Pierre',1984,'FP1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (64, 'HAINE','Hervé',1984,'HH1984');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (65, 'ROHIDE','Paula',2000,'RP2000');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (66, 'FAIBIEN-LAICHOSE','Lazard',2004,'FL2004');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (67, 'RIVE-DOUBLIER','Sama',2003,'RS2003');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (68, 'FAIRELA','Kate',1991,'FK1991');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (69, 'HIET','Mendy',1980,'HM1980');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (70, 'HUSSE','Angèle',2005,'HA2005');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (71, 'HION','Carry',1993,'HC1993');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (72, 'AUL','Jenny, Diane, Beth, Nicole, Esther',1985,'AJ1985');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (73, 'DENTS','Malo',1994,'DM1994');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (74, 'JAIDAIS','Carry',2008,'JC2008');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (75, 'GAULET','Henri',1990,'GH1990');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (76, 'PLEURET','Louan',1980,'PL1980');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (77, 'LIGUILY','Guy',1982,'LG1982');
INSERT INTO joueur (idJ, nom, prénom, année_naiss,  pseudo) VALUES (78, 'PAHENPLEURER','Eva',1992,'PE1992');
