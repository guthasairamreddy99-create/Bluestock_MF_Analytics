import os
import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

processed_folder = "data/processed"

# Load every cleaned CSV into SQLite
for filename in os.listdir(processed_folder):

    if filename.endswith(".csv"):

        table_name = filename.replace(".csv", "")

        file_path = os.path.join(processed_folder, filename)

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {table_name} into database")

print("\n✅ SQLite database created successfully!")