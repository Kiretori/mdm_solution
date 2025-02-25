CREATE TABLE Etudiants (
    etudiant_id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    universite_id INT,
    programme_etude VARCHAR(100) NOT NULL,
    date_inscription DATE NOT NULL,
    date_diplome DATE,
    fonctionnaire_id INT NULL,
    email VARCHAR(255) NOT NULL,
    FOREIGN KEY (universite_id) REFERENCES Universites(universite_id),
    FOREIGN KEY (fonctionnaire_id) REFERENCES Fonctionnaires(fonctionnaire_id)
);
