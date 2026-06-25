import pandas as pd
import requests
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_data = pd.DataFrame(data["data"])

        file_name = f"data/raw/{fund_name}_NAV.csv"

        nav_data.to_csv(file_name, index=False)

        print(f"Saved {file_name}")

    else:
        print(f"Failed to fetch {fund_name}")