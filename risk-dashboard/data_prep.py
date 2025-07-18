import pandas as pd
from pathlib import Path

# CORRECTED: Changed 'file' to '__file__'
RAW = Path(__file__).parent / "data/raw/KidCreative.csv"
OUT = Path(__file__).parent / "data/risk_clean.parquet"

df = (
    pd.read_csv(RAW)
      # You might need to adjust these lines based on the actual columns in KidCreative.csv
      # The 'Credit amount' column might not exist, or 'Age'/'Duration' for dropna.
      # For now, let's keep them but be aware you might get KeyError if columns don't exist.
      .assign(risk_score=lambda d: d.get('Credit amount', 0)/d.get('Credit amount', 1).max()) # Use .get() to avoid KeyError if column is missing
      .pipe(lambda d: d.dropna(subset=['Age', 'Duration'], errors='ignore')) # Use errors='ignore' to not fail if columns are missing
)
df.to_parquet(OUT, index=False)
