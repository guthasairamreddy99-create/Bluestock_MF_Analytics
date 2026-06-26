import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("../reports", exist_ok=True)

# Load cleaned NAV history dataset
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "HDFC_Top_100_NAV.csv"
)

df = pd.read_csv(file_path)

print("\nColumns in dataset:")
print(df.columns.tolist())
print("Dataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Plot 1 - NAV Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["nav"], bins=30)
plt.title("Distribution of NAV")
plt.xlabel("NAV")
plt.ylabel("Frequency")
plt.savefig(os.path.join(BASE_DIR, "reports", "nav_distribution.png"))
plt.close()

# -----------------------------
# Plot 2 - NAV Trend Over Time
# -----------------------------

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12,6))
plt.plot(df["date"], df["nav"])
plt.title("NAV Trend Over Time")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "reports", "nav_trend.png"))
plt.close()

print("\nEDA completed successfully.")