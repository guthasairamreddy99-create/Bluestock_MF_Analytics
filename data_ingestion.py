import pandas as pd
import os

# Folder containing raw CSV files
data_folder = "data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

print("=" * 70)
print(" MUTUAL FUND DATA INGESTION ")
print("=" * 70)

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    print("\n" + "=" * 70)
    print(f"File Name : {file}")
    print("=" * 70)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\n" + "=" * 70)
print("All datasets loaded successfully.")
print("=" * 70)