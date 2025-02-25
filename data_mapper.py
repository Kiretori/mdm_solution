import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine, Table, MetaData

# Load mapping.json
def load_mapping(mapping_file):
    with open(mapping_file, "r", encoding="utf-8") as file:
        return json.load(file)

# Load data (CSV or JSON)
def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

# Transform data using mappings
def transform_data(data, mappings):
    transformed = {}
    for table, columns in mappings.items():
        transformed[table] = data.rename(columns=columns)
        transformed[table] = transformed[table].replace("", None)  # Convert empty strings to NULL
    return transformed

# Insert data into database
def insert_data(transformed_data, db_url="mysql+pymysql://user:password@localhost/database"):
    engine = create_engine(db_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    with engine.connect() as conn:
        for table_name, df in transformed_data.items():
            if table_name in metadata.tables:
                df.to_sql(table_name, conn, if_exists="append", index=False)
            else:
                print(f"Table {table_name} does not exist in the database.")

# Main execution
def main(data_file, mapping_file="data/mapping.json"):
    mappings = load_mapping(mapping_file)
    data = load_data(data_file)
    transformed_data = transform_data(data, mappings)
    insert_data(transformed_data)
    print("Data successfully inserted!")

# Example usage
if __name__ == "__main__":
    main("data/etudiants.json")  # Change to your actual file
    main("data/fonctionnaires.csv")
    main("data/services.csv")