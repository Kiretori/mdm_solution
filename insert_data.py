import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Database connection
DB_URL = "mysql+pymysql://user:password@localhost/database"
engine = create_engine(DB_URL)

def insert_csv_to_db(csv_file, table_name):
    df = pd.read_csv(csv_file)
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Inserted {len(df)} records into {table_name}.")

def main():
    insert_csv_to_db("fonctionnaires.csv", "Fonctionnaires")
    insert_csv_to_db("services.csv", "Services")
    insert_csv_to_db("etudiants.csv", "Etudiants")
    print("All data inserted successfully!")

if __name__ == "__main__":
    main()
