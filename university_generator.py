from faker import Faker
import pandas as pd
# Initialize Faker instance
fake = Faker()

# Number of entries to generate
num_entries = 40

# Generate fake data
data = {
    "university_id": [i for i in range(1, num_entries + 1)],
    "university_name": [fake.company() + " University" for _ in range(num_entries)],
    "location": [fake.city() for _ in range(num_entries)],
}

# Create the DataFrame
university_df = pd.DataFrame(data)

# Display the generated table
university_df.to_csv("clean_data/university.csv", index=False)