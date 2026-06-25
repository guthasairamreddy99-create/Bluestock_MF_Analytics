import os
import pandas as pd

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

# Process all CSV files in raw folder
for filename in os.listdir(RAW_FOLDER):
    if filename.endswith(".csv"):
        print(f"Processing {filename}...")

        file_path = os.path.join(RAW_FOLDER, filename)

        df = pd.read_csv(file_path)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Save cleaned file
        output_path = os.path.join(PROCESSED_FOLDER, filename)
        df.to_csv(output_path, index=False)

        print(f"Saved: {output_path}")

print("\n✅ All datasets cleaned successfully!")