import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent / "data/raw/KidCreative.csv"
OUT = Path(__file__).parent / "data/risk_clean.parquet"

df = pd.read_csv(RAW)

# --- Adjust these lines based on actual columns in KidCreative.csv ---
# The KidCreative.csv columns are:
# ['Obs No.', 'Buy', 'Income', 'IsFemale', 'IsMarried', 'Has College',
#  'Is Professional', 'Is Retired', 'Unemployed', 'Residence Length',
#  'Dual Income', 'Minors', 'Own', 'House', 'White', 'English',
#  'Prev Child', 'Mag', 'Parent', 'Ment']

# Creating a 'risk_score' based on 'Income' (assuming higher income = lower risk, or vice versa)
# You might want to invert this or use a more complex logic later.
if 'Income' in df.columns:
    # A simple example: higher income, lower risk score (normalized)
    df = df.assign(risk_score=lambda d: 1 - (d['Income'] / d['Income'].max()))
else:
    df = df.assign(risk_score=0.5) # Assign a default score if 'Income' is not found
    print("Warning: 'Income' column not found, assigning default risk_score.")

# Dropping NaNs from relevant columns. 'Income' is a good candidate if it's numerical.
if 'Income' in df.columns:
    df = df.dropna(subset=['Income'])
else:
    print("Warning: 'Income' column not found, skipping dropna on Income.")

df.to_parquet(OUT, index=False)
