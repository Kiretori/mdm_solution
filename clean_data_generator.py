from faker import Faker
import random
import csv

fake = Faker()


# Generate fake data
def generate_fonctionnaires(n=5000):
    fonctionnaires = []
    for _ in range(n):
        fonctionnaires.append(
            [
                _,  # Auto-increment ID
                fake.last_name(),
                fake.first_name(),
                random.choice(["Professeur", "Administratif", "Technicien"]),
                fake.email(),
                random.choice(
                    [None, random.randint(1, n)]
                ),  # Some Fonctionnaires were students
                fake.date_between(start_date="-30y", end_date="today"),
            ]
        )
    return fonctionnaires

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
def generate_services(n=5000):
    services = []
    for _ in range(n):
        services.append(
            [
                _,  # Auto-increment ID
                random.choice(course_names),
                random.choice(course_descriptions),
                random.choice(["Cycle ingénieur", "Doctorat", "Master", "License"]),
                random.randint(1, 100),  # Assuming 100 universities exist
                fake.date_between(start_date="-50y", end_date="today"),
            ]
        )
    return services


def generate_etudiants(n=5000):
    etudiants = []
    for _ in range(n):
        etudiants.append(
            [
                _,  # Auto-increment ID
                fake.last_name(),
                fake.first_name(),
                fake.date_of_birth(minimum_age=18, maximum_age=30),
                random.randint(1, 100),  # Assuming 100 universities exist
                random.choice(course_names + [""]),
                fake.date_between(start_date="-10y", end_date="today"),
                fake.date_between(start_date="-5y", end_date="today")
                if random.random() > 0.5
                else None,
                random.choice(
                    [None, random.randint(1, n)]
                ),  # Some students become employees
                fake.email(),
            ]
        )
    return etudiants


# Save to CSV
def save_to_csv(filename, data, headers):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)


# Generate and save
save_to_csv(
    "clean_data/fonctionnaires.csv",
    generate_fonctionnaires(),
    [
        "fonctionnaire_id",
        "nom",
        "prenom",
        "type_fonctionnaire",
        "email",
        "etudiant_id",
        "date_embauche",
    ],
)
save_to_csv(
    "clean_data/services.csv",
    generate_services(),
    ["service_id", "nom", "description", "type", "university_id", "date_creation"],
)
save_to_csv(
    "clean_data/etudiants.csv",
    generate_etudiants(),
    [
        "etudiant_id",
        "nom",
        "prenom",
        "date_naissance",
        "universite_id",
        "programme_etude",
        "date_inscription",
        "date_diplome",
        "fonctionnaire_id",
        "email",
    ],
)
