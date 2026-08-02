"""
Full Model Optimization Script with GridSearchCV
Baseline + Optimized comparison for all 3 models.
"""
import os, random, warnings, json
import numpy as np
import pandas as pd
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

SEED = 42
os.environ['PYTHONHASHSEED'] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)

# ---- Load ----
df = pd.read_csv('data/dataset.csv', sep=';', encoding='latin-1')
df.columns = ['N','Family','Scientific_Name','Distribution','Common_Name',
              'Uses','Habit','Group','Class','Order','Genus','References']
df['Habit'] = df['Habit'].astype(str).str.strip()
for col in ['Family','Genus','Distribution','Uses']:
    df[col] = df[col].fillna('Unknown')

X = df[['Family','Genus','Distribution','Uses']]
y = df['Habit']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, stratify=y, random_state=SEED)
X_val,   X_test, y_val,   y_test = train_test_split(X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=SEED)

le = LabelEncoder()
y_train_enc = le.fit_transform(y_train)
y_val_enc   = le.transform(y_val)
y_test_enc  = le.transform(y_test)

preprocessor = ColumnTransformer([
    ('taxonomic',     OneHotEncoder(handle_unknown='ignore'),
                      ['Family','Genus']),
    ('geographic',    CountVectorizer(
                          tokenizer=lambda x: [t.strip() for t in x.split(',') if t.strip()]),
                      'Distribution'),
    ('etnobotanical', TfidfVectorizer(max_features=300), 'Uses')
])
X_train_proc = preprocessor.fit_transform(X_train)
X_val_proc   = preprocessor.transform(X_val)
X_test_proc  = preprocessor.transform(X_test)

print(f"Feature matrix (train): {X_train_proc.shape}")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)


def eval_model(model, label):
    yv = model.predict(X_val_proc)
    yt = model.predict(X_test_proc)
    return {
        'label':    label,
        'val_acc':  round(float(accuracy_score(y_val_enc, yv)),  4),
        'val_f1':   round(float(f1_score(y_val_enc,  yv, average='macro')), 4),
        'test_acc': round(float(accuracy_score(y_test_enc, yt)), 4),
        'test_f1':  round(float(f1_score(y_test_enc, yt, average='macro')), 4),
    }


# =============================================
# BASELINE
# =============================================
print("\n=== BASELINE ===")
bl = {
    'LR':  LogisticRegression(multi_class='multinomial', max_iter=1000, random_state=SEED),
    'RF':  RandomForestClassifier(n_estimators=100, random_state=SEED),
    'XGB': XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=SEED,
                         eval_metric='mlogloss', verbosity=0)
}
baseline_results = {}
for name, model in bl.items():
    model.fit(X_train_proc, y_train_enc)
    r = eval_model(model, name)
    baseline_results[name] = r
    print(f"  {name}: ValF1={r['val_f1']}  TestF1={r['test_f1']}")


# =============================================
# GRIDSEARCH: Logistic Regression
# =============================================
print("\n=== GridSearchCV: Logistic Regression ===")
lr_gs = GridSearchCV(
    LogisticRegression(multi_class='multinomial', max_iter=2000, random_state=SEED),
    {'C': [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]},
    cv=cv, scoring='f1_macro', n_jobs=-1
)
lr_gs.fit(X_train_proc, y_train_enc)
best_lr = lr_gs.best_estimator_
lr_r = eval_model(best_lr, 'LR_opt')
lr_r['best_C']  = lr_gs.best_params_['C']
lr_r['cv_f1']   = round(float(lr_gs.best_score_), 4)
print(f"  Best C={lr_r['best_C']}  CV_F1={lr_r['cv_f1']}  ValF1={lr_r['val_f1']}  TestF1={lr_r['test_f1']}")


# =============================================
# GRIDSEARCH: Random Forest
# =============================================
print("\n=== GridSearchCV: Random Forest ===")
rf_gs = GridSearchCV(
    RandomForestClassifier(random_state=SEED),
    {'n_estimators': [100, 200, 300],
     'max_depth':    [None, 10, 20],
     'min_samples_split': [2, 5]},
    cv=cv, scoring='f1_macro', n_jobs=-1
)
rf_gs.fit(X_train_proc, y_train_enc)
best_rf = rf_gs.best_estimator_
rf_r = eval_model(best_rf, 'RF_opt')
rf_r['best_params'] = rf_gs.best_params_
rf_r['cv_f1']       = round(float(rf_gs.best_score_), 4)
print(f"  Best={rf_r['best_params']}  CV_F1={rf_r['cv_f1']}  ValF1={rf_r['val_f1']}  TestF1={rf_r['test_f1']}")


# =============================================
# GRIDSEARCH: XGBoost
# =============================================
print("\n=== GridSearchCV: XGBoost ===")
xgb_gs = GridSearchCV(
    XGBClassifier(random_state=SEED, eval_metric='mlogloss', verbosity=0),
    {'max_depth':    [3, 5, 7],
     'learning_rate': [0.01, 0.05, 0.1],
     'n_estimators': [100, 200],
     'subsample':    [0.8, 1.0],
     'reg_lambda':   [1, 5]},
    cv=cv, scoring='f1_macro', n_jobs=-1
)
xgb_gs.fit(X_train_proc, y_train_enc)
best_xgb = xgb_gs.best_estimator_
xgb_r = eval_model(best_xgb, 'XGB_opt')
xgb_r['best_params'] = xgb_gs.best_params_
xgb_r['cv_f1']       = round(float(xgb_gs.best_score_), 4)
print(f"  Best={xgb_r['best_params']}  CV_F1={xgb_r['cv_f1']}  ValF1={xgb_r['val_f1']}  TestF1={xgb_r['test_f1']}")


# =============================================
# BEST MODEL REPORT
# =============================================
candidates = {'LR_opt': lr_r, 'RF_opt': rf_r, 'XGB_opt': xgb_r}
best_name = max(candidates, key=lambda k: candidates[k]['test_f1'])
print(f"\n=== BEST OPTIMIZED MODEL: {best_name} ===")
best_model_map = {'LR_opt': best_lr, 'RF_opt': best_rf, 'XGB_opt': best_xgb}
best_pred = best_model_map[best_name].predict(X_test_proc)
print(classification_report(y_test_enc, best_pred, target_names=le.classes_))


# =============================================
# SAVE
# =============================================
output = {
    'baseline':   baseline_results,
    'optimized':  {'LR_opt': lr_r, 'RF_opt': rf_r, 'XGB_opt': xgb_r},
    'best_model': best_name,
    'classes':    list(le.classes_)
}
os.makedirs('outputs', exist_ok=True)
with open('outputs/optimized_results.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("\nSaved -> outputs/optimized_results.json")
print("COMPLETE")
