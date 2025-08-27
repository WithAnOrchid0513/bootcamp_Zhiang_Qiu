import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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


def train_random_forest(df, feature_cols, target_col, n_estimators, test_size=0.25, random_state=7):
    X = df[feature_cols]
    y = df[target_col]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Model
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    return model, X_test, y_test, y_pred
