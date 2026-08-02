"""
Evaluation Module: Best Model Evaluation on the Test Set.
Generates classification report, confusion matrix, and logs final metrics to MLflow.
"""

import os
import random
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
import mlflow
import mlflow.sklearn

from data_loader import load_data
from preprocess import build_preprocessor, encode_target

SEED = 42


def set_seed(seed: int = SEED):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)


def evaluate_best_model(data_path: str = "../data/dataset.csv",
                        output_dir: str = "../outputs"):
    """
    Trains the best model (Random Forest) and evaluates it on the held-out test set.
    Saves confusion matrix and classification report. Logs metrics to MLflow.

    Args:
        data_path (str): Path to the processed dataset CSV.
        output_dir (str): Directory where output plots will be saved.
    """
    set_seed(SEED)
    os.makedirs(output_dir, exist_ok=True)

    # --- Data Loading & Partitioning ---
    df = load_data(data_path)
    X = df[['Family', 'Genus', 'Distribution', 'Uses']]
    y = df['Habit']

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, stratify=y, random_state=SEED
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=SEED
    )

    # --- Preprocessing (fit only on train) ---
    y_train_enc, y_val_enc, y_test_enc, le = encode_target(y_train, y_val, y_test)
    preprocessor = build_preprocessor()
    X_train_proc = preprocessor.fit_transform(X_train)
    X_val_proc   = preprocessor.transform(X_val)
    X_test_proc  = preprocessor.transform(X_test)

    # --- Best Model: Random Forest ---
    best_model = RandomForestClassifier(n_estimators=100, random_state=SEED)
    best_model.fit(X_train_proc, y_train_enc)

    # --- Test Set Predictions ---
    y_test_pred = best_model.predict(X_test_proc)

    test_acc = accuracy_score(y_test_enc, y_test_pred)
    test_f1  = f1_score(y_test_enc, y_test_pred, average='macro')

    print("\n" + "="*55)
    print("  BEST MODEL (Random Forest) — TEST SET PERFORMANCE")
    print("="*55)
    print(f"  Test Accuracy   : {test_acc:.4f}")
    print(f"  Test Macro F1   : {test_f1:.4f}")
    print("="*55)
    print("\nClassification Report:")
    print(classification_report(y_test_enc, y_test_pred, target_names=le.classes_))

    # --- Confusion Matrix Plot ---
    cm = confusion_matrix(y_test_enc, y_test_pred)
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=le.classes_, yticklabels=le.classes_, ax=ax
    )
    ax.set_title('Confusion Matrix — Random Forest (Test Set)', fontsize=13, pad=12)
    ax.set_xlabel('Predicted Growth Habit', fontsize=11)
    ax.set_ylabel('True Growth Habit', fontsize=11)
    fig.tight_layout()

    cm_path = os.path.join(output_dir, "confusion_matrix_test.png")
    fig.savefig(cm_path, dpi=150)
    plt.close(fig)
    print(f"\nConfusion matrix saved → {cm_path}")

    # --- MLflow Logging ---
    mlflow.set_experiment("Medicinal_Plants_Growth_Habit")
    with mlflow.start_run(run_name="Random_Forest_FINAL_TEST"):
        mlflow.log_param("model",       "RandomForestClassifier")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("seed",         SEED)
        mlflow.log_metric("test_accuracy",  test_acc)
        mlflow.log_metric("test_macro_f1",  test_f1)
        mlflow.log_artifact(cm_path)
        mlflow.sklearn.log_model(best_model, artifact_path="Random_Forest_FINAL")

    print("MLflow run logged successfully.")
    return {"test_accuracy": test_acc, "test_macro_f1": test_f1}


if __name__ == "__main__":
    evaluate_best_model()
