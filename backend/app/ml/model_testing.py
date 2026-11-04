
from pathlib import Path
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("SAFETRIP AI - ROAD RISK MODEL TESTING STARTED", flush=True)

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATASET_PATH = (
    PROJECT_ROOT
    / "Dataset"
    / "Indian Road Accident Dataset (2022–2025)"
    / "indian_roads_dataset.csv"
)

OUTPUT_DIR = Path(__file__).resolve().parent / "results"
MODEL_DIR = Path(__file__).resolve().parent / "saved_models"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def main():

    print("\nLoading dataset...", flush=True)

    df = pd.read_csv(DATASET_PATH)

    print("Dataset shape:", df.shape)
    print("Columns:", df.columns.tolist())

    target = "risk_score"

    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found.")

    # Remove identifiers and direct outcome/leakage columns.
    drop_columns = [
        "accident_id",
        "risk_score",
        "accident_severity",
        "casualties",
        "vehicles_involved",
        "cause"
    ]

    X = df.drop(columns=drop_columns, errors="ignore")
    y = pd.to_numeric(df[target], errors="coerce")

    # Remove missing target rows
    valid = y.notna()
    X = X.loc[valid].copy()
    y = y.loc[valid].copy()

    # Remove columns that are entirely empty
    X = X.dropna(axis=1, how="all")

    numeric_features = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    transformers = []

    if numeric_features:
        transformers.append(
            ("numeric", numeric_pipeline, numeric_features)
        )

    if categorical_features:
        transformers.append(
            ("categorical", categorical_pipeline, categorical_features)
        )

    preprocessor = ColumnTransformer(transformers)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    models = {
        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        ),

        "Decision Tree": DecisionTreeRegressor(
            max_depth=10,
            random_state=42
        )
    }

    results = []
    best_model = None
    best_name = None
    best_mae = float("inf")

    for name, model in models.items():

        print(f"\nTraining {name}...", flush=True)

        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)

        print(f"{name} Results:")
        print(f"MAE: {mae:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"R2 Score: {r2:.4f}")

        results.append({
            "Model": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2 Score": r2
        })

        if mae < best_mae:
            best_mae = mae
            best_model = pipeline
            best_name = name

    # Logistic Regression is a classifier, not a regressor.
    # Test it separately only if risk_score is converted into
    # meaningful Low / Medium / High classes.

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        OUTPUT_DIR / "road_risk_model_comparison.csv",
        index=False
    )

    joblib.dump(
        best_model,
        MODEL_DIR / "best_road_risk_model.pkl"
    )

    print("\nMODEL COMPARISON")
    print(results_df.to_string(index=False))

    print("\nBest model:", best_name)
    print("Saved model:", MODEL_DIR / "best_road_risk_model.pkl")
    print("Saved results:", OUTPUT_DIR / "road_risk_model_comparison.csv")

    print("\nROAD RISK MODEL TESTING COMPLETED", flush=True)


if __name__ == "__main__":
    main()
#python -u model_testing.py