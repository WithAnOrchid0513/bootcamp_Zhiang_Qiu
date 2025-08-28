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