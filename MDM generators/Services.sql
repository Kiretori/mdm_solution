CREATE TABLE Services (
    service_id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    type TEXT NOT NULL,
    university_id INT,
    date_creation DATE NOT NULL,
    FOREIGN KEY (university_id) REFERENCES Universites(universite_id)
);
