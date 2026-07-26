"""
Model Training & MLflow Logging Module.
Trains Logistic Regression, Random Forest, and XGBoost models.
"""

import os
import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score
import mlflow
import mlflow.sklearn

from data_loader import load_data
from preprocess import build_preprocessor, encode_target

SEED = 42

def set_seed(seed=SEED):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

def run_training_pipeline(data_path="../data/dataset.csv"):
    set_seed(SEED)
    df = load_data(data_path)
    
    X = df[['Family', 'Genus', 'Distribution', 'Uses']]
    y = df['Habit']
    
    # Partition data
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, stratify=y, random_state=SEED
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=SEED
    )
    
    y_train_enc, y_val_enc, y_test_enc, le = encode_target(y_train, y_val, y_test)
    
    # Preprocess
    preprocessor = build_preprocessor()
    X_train_proc = preprocessor.fit_transform(X_train)
    X_val_proc = preprocessor.transform(X_val)
    X_test_proc = preprocessor.transform(X_test)
    
    # MLflow Setup
    mlflow.set_experiment("Medicinal_Plants_Growth_Habit")
    
    models = {
        'Multinomial_Logistic_Regression': LogisticRegression(multi_class='multinomial', max_iter=1000, random_state=SEED),
        'Random_Forest': RandomForestClassifier(n_estimators=100, random_state=SEED),
        'XGBoost': XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=SEED, eval_metric='mlogloss')
    }
    
    results = {}
    for name, model in models.items():
        with mlflow.start_run(run_name=name):
            model.fit(X_train_proc, y_train_enc)
            val_preds = model.predict(X_val_proc)
            val_acc = accuracy_score(y_val_enc, val_preds)
            val_f1 = f1_score(y_val_enc, val_preds, average='macro')
            
            mlflow.log_param("seed", SEED)
            mlflow.log_metric("val_accuracy", val_acc)
            mlflow.log_metric("val_macro_f1", val_f1)
            mlflow.sklearn.log_model(model, artifact_path=name)
            
            results[name] = {"val_accuracy": val_acc, "val_macro_f1": val_f1}
            print(f"Model: {name} | Val Acc: {val_acc:.4f} | Val Macro F1: {val_f1:.4f}")
            
    return results

if __name__ == "__main__":
    run_training_pipeline()
