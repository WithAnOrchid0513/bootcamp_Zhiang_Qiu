import pandas as pd
import numpy as np

def clean_dataframe(df, date_cols=None, rename=None):
    if rename:
        df = df.rename(columns=rename)

    if date_cols:
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def mae(y_true, y_pred):
    return float(np.mean(np.abs(y_true - y_pred)))
