DROP SCHEMA IF EXISTS projetbdw CASCADE;
CREATE SCHEMA IF NOT EXISTS projetbdw;
SET search_path TO projetbdw;

create table Classement(
  taille_grille integer, 
  difficulté varchar(32),
  nom varchar(32), 
  date_création date, 
  date_maj date, 
  PRIMARY KEY (taille_grille, difficulté)
);