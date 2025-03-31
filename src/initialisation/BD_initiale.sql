DROP SCHEMA IF EXISTS projetbdw CASCADE;
CREATE SCHEMA projetbdw;
SET search_path TO projetbdw;

/* Création des tables */

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

create table Partie (
  id_partie integer, 
  date_création TIMESTAMP,
  en_cours boolean, 
  score integer,
  id_joueur integer,
  taille_grille INTEGER,
  difficulté VARCHAR(10),
  id_grille integer,
  id_pioche integer,
  PRIMARY KEY (id_partie)
);

create table Grille (
  id_grille integer, 
  taille integer,
  difficulté varchar(10), 
  PRIMARY KEY (id_grille)
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

create table TuileJeu (
  id_tuile integer,
  PRIMARY KEY (id_tuile)
);

create table TuileContrainte (
  id_tuile integer,
  difficulté varchar(16),
  nb_points integer,
  PRIMARY KEY (id_tuile)
);

create table Contrainte (
  id_contrainte integer,
  PRIMARY KEY (id_contrainte)
);

create table ContrainteElement (
  id_contrainte integer,
  nombre integer,
  nom_élément varchar(32),
  PRIMARY KEY (id_contrainte)
);

create table ContrainteNombre (
  id_contrainte integer,
  nombre integer,
  type_contrainte varchar(32),
  PRIMARY KEY (id_contrainte)
);

create table associe_contrainte (
  id_tuile integer,
  id_contrainte integer,
  PRIMARY KEY (id_tuile, id_contrainte)
);

create table contient_element (
  id_tuile integer,
  nom_élément varchar(32),
  nombre INTEGER,
  PRIMARY KEY (id_tuile, nom_élément)
);

create table contient_tuile_contrainte (
  id_tuile integer,
  id_grille INTEGER,
  ligne boolean,
  position INTEGER,
  PRIMARY KEY (id_tuile, id_grille)
);

ALTER TABLE Partie ADD FOREIGN KEY (id_joueur) REFERENCES Joueur (id_joueur);
ALTER TABLE Partie ADD FOREIGN KEY (taille_grille, difficulté) REFERENCES Classement (taille_grille, difficulté);
ALTER TABLE Partie ADD FOREIGN KEY (id_grille) REFERENCES Grille (id_grille);
ALTER TABLE Partie ADD FOREIGN KEY (id_pioche) REFERENCES Pioche (id_pioche);
ALTER TABLE Tour ADD FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);
ALTER TABLE Tour ADD FOREIGN KEY (id_tuile) REFERENCES TuileJeu (id_tuile);
ALTER TABLE TuileJeu ADD FOREIGN KEY (id_tuile) REFERENCES Tuile (id_tuile);
ALTER TABLE TuileContrainte ADD FOREIGN KEY (id_tuile) REFERENCES Tuile (id_tuile);
ALTER TABLE ContrainteElement ADD FOREIGN KEY (id_contrainte) REFERENCES Contrainte (id_contrainte);
ALTER TABLE ContrainteElement ADD FOREIGN KEY (nom_élément) REFERENCES Element (nom_élément);
ALTER TABLE ContrainteNombre ADD FOREIGN KEY (id_contrainte) REFERENCES Contrainte (id_contrainte);
ALTER TABLE associe_contrainte ADD FOREIGN KEY (id_tuile) REFERENCES TuileContrainte (id_tuile);
ALTER TABLE associe_contrainte ADD FOREIGN KEY (id_contrainte) REFERENCES Contrainte (id_contrainte);
ALTER TABLE contient_element ADD FOREIGN KEY (id_tuile) REFERENCES TuileJeu (id_tuile);
ALTER TABLE contient_element ADD FOREIGN KEY (nom_élément) REFERENCES Element (nom_élément);
ALTER TABLE contient_tuile_contrainte ADD FOREIGN KEY (id_tuile) REFERENCES TuileContrainte (id_tuile);
ALTER TABLE contient_tuile_contrainte ADD FOREIGN KEY (id_grille) REFERENCES Grille (id_grille);