# Research Protocol v0.1

**Title:** A Reproducible and Fairness-Aware Machine Learning Pipeline for Customer Churn Prediction  
**Author:** Valerio Gomez  
**Date:** June 2026

| Component | Description |
|-----------|-------------|
| **1. Title** | A Reproducible and Fairness-Aware Machine Learning Pipeline for Customer Churn Prediction in a Subscription Service |
| **2. Research Question** | Which classification model maximizes recall for churn prediction, and does it exhibit gender bias? |
| **3. Paradigm** | Positivism – objective measurement of model performance and fairness metrics. |
| **4. Method** | Computational experiment – controlled comparison of Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, and SVM. |
| **5. Data** | Proprietary subscription dataset (n=1,000) with 6 features and binary target (churn). |
| **6. Analysis Plan** | EDA → scaling → train/test split (seed=42) → train 5 models → evaluate via accuracy, recall, F1, confusion matrix → select best recall model → fairness audit with AIF360. |
| **7. Ethics & Bias** | Check for gender-based disparate impact; no PII collected; data is synthetic/anonymized. |
| **8. Reproducibility** | Full stack: Git, DVC, MLflow, Docker, pinned dependencies, seed fixation. |
| **9. Limitations** | Small dataset, single company, binary gender representation limits generalizability and intersectional analysis. |
| **10. Expected Outcomes** | A reproducible pipeline with a best model achieving recall > 0.75, and a bias audit report indicating whether mitigation is necessary. |
