import random
import json
import pandas as pd
from faker import Faker

# Configuration
num_entries = 5500  # Nombre d'entrées par dataset
fake = Faker()
Faker.seed(42)

# Génération des étudiants (JSON)
etudiants = []
fake.unique.clear()
for _ in range(num_entries):
    etudiants.append({
        "id": fake.unique.random_int(min=1, max=100000),
        "nom": fake.last_name(),
        "prenom": fake.first_name(),
        "email": fake.email() if random.random() > 0.05 else fake.email().replace("@", "@@"),
        "age": fake.random_int(min=18, max=30) if random.random() > 0.05 else fake.word(),
        "date_inscription": fake.date_this_decade().strftime("%Y-%m-%d") if random.random() > 0.1 else fake.date()
    })

with open("data/etudiants.json", "w") as f:
    json.dump(etudiants, f, indent=4)

# Génération des fonctionnaires (CSV)
fake.unique.clear()
fonctionnaires_data = {
    "id": [fake.unique.random_int(min=10000, max=99999) for _ in range(num_entries)],
    "nom": [fake.last_name() for _ in range(num_entries)],
    "prenom": [fake.first_name() for _ in range(num_entries)],
    "email": [fake.email() if random.random() > 0.05 else fake.email().replace("@", "@@") for _ in range(num_entries)],
    "age": [fake.random_int(min=25, max=65) if random.random() > 0.05 else fake.word() for _ in range(num_entries)],
    "date_embauche": [fake.date_this_century().strftime("%Y-%m-%d") if random.random() > 0.1 else fake.date() for _ in range(num_entries)]
}
fonctionnaires_df = pd.DataFrame(fonctionnaires_data)
fonctionnaires_df.to_csv("data/fonctionnaires.csv", index=False)

# Génération des services et produits (CSV)
course_names = [
    "Informatique", "Génie Civil", "Mécanique", "Électronique", 
    "Génie Industriel", "Télécommunications", "Mathématiques Appliquées", 
    "Ingénierie des Systèmes", "Ingénierie Environnementale", "Architecture"
]

course_descriptions = [
    "Formation en développement logiciel et systèmes informatiques", 
    "Formation en conception et gestion de structures civiles", 
    "Formation en conception, fabrication et maintenance de machines", 
    "Formation en conception et gestion des systèmes électroniques",
    "Formation sur la gestion et l'amélioration des processus industriels",
    "Formation en conception, installation et maintenance de réseaux de télécommunication",
    "Formation en résolution de problèmes complexes à l'aide de techniques mathématiques",
    "Formation sur la gestion des systèmes d'information et leur optimisation",
    "Formation en gestion durable des ressources naturelles et en ingénierie environnementale",
    "Formation en conception et gestion d'espaces architecturaux et urbains"
]

course_types = [
    "Cycle ingénieur",
    "Doctorat",
    "Master",
    "License"
]


# Generate services data
services_data = {
    "id": [i for i in range(1, num_entries + 1)],
    "nom": [random.choice(course_names) for _ in range(num_entries)],
    "description": [random.choice(course_descriptions) for _ in range(num_entries)],
    "type": [random.choice(course_types) for _ in range(num_entries)]
}

# Create DataFrame and save to CSV
services_df = pd.DataFrame(services_data)
services_df.to_csv("data/services.csv", index=False)
print("Fichiers générés : etudiants.json, fonctionnaires.csv, services.csv")
