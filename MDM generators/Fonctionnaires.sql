CREATE TABLE Fonctionnaires (
    fonctionnaire_id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    type_fonctionnaire VARCHAR(100) NOT NULL,
    departement_id INT,
    email VARCHAR(255) NOT NULL,
    etudiant_id INT,
    date_embauche DATE,
    FOREIGN KEY (etudiant_id) REFERENCES Etudiants(etudiant_id),
    FOREIGN KEY (departement_id) REFERENCES Departements(departement_id)
);
