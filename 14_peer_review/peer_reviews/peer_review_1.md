# Peer Review Report 1: Evaluation of Research Protocol v1.0

**Reviewed Protocol:** [Research Protocol v1.0 (Draft)](../../03_protocol/protocol_v1.0.md)  
**Author of Protocol:** Valerio Gomez  
**Reviewer:** Peer Reviewer 1 (Specialist in Machine Learning & Ecological Modeling)  
**Date:** July 2026  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Executive Summary

This peer review evaluates **Research Protocol v1.0**, titled *"Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning"*. The protocol presents a quasi-experimental machine learning study comparing Multinomial Logistic Regression, Random Forest, and XGBoost to predict plant growth habits (Tree, Shrub, Herb) from taxonomic, geographic, and etnobotanical features.

Overall, the protocol is well-structured, methodologically sound, and strongly committed to computational reproducibility. However, there are key methodological risks related to sample size, model complexity, and overfitting that require addressing before final protocol approval.

---

## 2. Quantitative Evaluation Criteria

| Evaluation Dimension | Score (1-5) | Assessment Summary |
|---|:---:|---|
| **1. Clarity of Research Questions & Hypotheses** | 5/5 | Research questions (GQ, SQ1-SQ4) and null/alternative hypotheses ($H_0, H_1, H_2$) are explicitly stated, testable, and aligned with positivist epistemology. |
| **2. Methodological & Computational Rigor** | 3.5/5 | The train/val/test split and random seed controls are rigorous, but sample size constraints ($n=100$) pose a severe overfitting risk for non-parametric ensemble models. |
| **3. Reproducibility & Infrastructure** | 5/5 | Excellent reproducibility architecture utilizing Docker containerization, DVC data versioning, MLflow tracking, and locked random seeds (`SEED=42`). |
| **4. Ethical Compliance & FAIR Data Management** | 4/5 | Addresses indigenous knowledge custody and FAIR principles well, though explicit mention of Nagoya Protocol compliance should be strengthened. |
| **5. Feasibility & Expected Impact** | 4.5/5 | Highly feasible using lightweight open-source Python tooling (`scikit-learn`, `xgboost`, `pandas`), providing high utility for IIAP botanical cataloging. |

---

## 3. Key Observations & Critical Feedback

### Major Comment 1: High Dimensionality vs. Small Sample Size Overfitting
* **Observation:** Protocol v1.0 reports strong validation performance for XGBoost (Macro F1 = 0.8333) and Random Forest (Macro F1 = 0.8222), but notes a steep degradation on the test set (Test Accuracy = 0.6000, Test Macro F1 = 0.4722).
* **Critique:** Combining 300 TF-IDF features for `USOS` with One-Hot encoded taxonomic features creates a feature matrix with $>350$ dimensions on a dataset of only 100 total samples (70 training samples). Non-parametric gradient boosting models (XGBoost) will inevitably memorize noise on 70 training samples.
* **Recommendation:** 
  1. Include Multinomial Logistic Regression as an essential parametric baseline with $L_2$ regularization.
  2. Implement feature selection or reduce `max_features` in `TfidfVectorizer` to prevent extreme variance.
  3. Re-evaluate models on the full master dataset of 1,028 IIAP records once data cleaning is finalized.

---

## 4. Final Recommendation

**Decision:** **Accept with Minor Revisions**

The author must address the sample size and overfitting concerns in Protocol v2.0 by acknowledging high-dimensional regularization strategies and updating performance tables accordingly.
