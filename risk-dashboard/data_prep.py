import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent / "data/raw/german_credit.csv"
OUT = Path(__file__).parent / "data/risk_clean.parquet"

df = (
    pd.read_csv(RAW)
      .assign(risk_score=lambda d: d['Credit amount']/d['Credit amount'].max())
      .pipe(lambda d: d.dropna(subset=['Age', 'Duration']))
)
df.to_parquet(OUT, index=False)
