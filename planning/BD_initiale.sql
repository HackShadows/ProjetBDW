DROP SCHEMA IF EXISTS projetbdw CASCADE;
CREATE SCHEMA IF NOT EXISTS projetbdw;
SET search_path TO projetbdw;

/*Création des tables*/

create table Classement (
  taille_grille integer, 
  difficulté varchar(10),
  nom varchar(64), 
  date_création date, 
  date_maj date, 
  PRIMARY KEY (taille_grille, difficulté)
);

create table Joueur (
  id_joueur integer, 
  nom varchar(64),
  prénom varchar(64), 
  pseudo varchar(64), 
  année_naiss integer, 
  PRIMARY KEY (id_joueur)
);

create table Grille (
  id_grille integer, 
  taille integer,
  difficulté varchar(10), 
  PRIMARY KEY (id_joueur)
);

create table Pioche (
  id_pioche integer, 
  nb_tuiles_découvertes integer,
  PRIMARY KEY (id_pioche)
);

create table Tour (
  id_tour integer, 
  id_partie integer,
  pos_x integer,
  pos_y integer,
  id_tuile integer,
  PRIMARY KEY (id_tour, id_partie)
);

create table Element (
  nom_élément varchar(32), 
  PRIMARY KEY (nom_élément)
);

create table Tuile (
  id_tuile integer,
  chemin_texture varchar(128), 
  PRIMARY KEY (id_tuile)
);

create table TuileContrainte (
  id_tuile integer,
  difficulté varchar(16),
  chemin_texture varchar(128), 
  PRIMARY KEY (id_tuile)
);

create table Partie (
  id_partie integer, 
  date_création datetime,
  en_cours boolean, 
  score integer,
  id_joueur integer,
  id_grille integer,
  id_pioche integer,
  PRIMARY KEY (id_partie)
);