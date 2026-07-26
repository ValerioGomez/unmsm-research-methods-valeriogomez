# Peer Review Report 2: Evaluation of Research Protocol v1.0

**Reviewed Protocol:** [Research Protocol v1.0 (Draft)](../../03_protocol/protocol_v1.0.md)  
**Author of Protocol:** Valerio Gomez  
**Reviewer:** Peer Reviewer 2 (Specialist in Data Science Pipelines & Reproducibility)  
**Date:** July 2026  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Executive Summary

This peer review evaluates **Research Protocol v1.0** from a computational pipeline and data integrity perspective. The study establishes a reproducible pipeline using `ColumnTransformer`, DVC, MLflow, and Docker to classify Peruvian Amazonian medicinal plant growth habits.

The pipeline architecture is well-designed. This review focuses specifically on verifying data partitioning sequencing, preventing data leakage during feature engineering, and ensuring multi-class stratification.

---

## 2. Quantitative Evaluation Criteria

| Evaluation Dimension | Score (1-5) | Assessment Summary |
|---|:---:|---|
| **1. Clarity of Research Questions & Hypotheses** | 4.5/5 | Questions are well-formulated and logically structured across model comparison, feature importance, and representation strategy. |
| **2. Methodological & Computational Rigor** | 4.5/5 | Strong computational controls (`SEED=42`), preprocessor scoping, and stratified 70/15/15 split ratio. |
| **3. Reproducibility & Infrastructure** | 5/5 | Outstanding environment freezing (`Dockerfile`, `requirements.txt`) and remote data versioning (`DVC` + Google Drive). |
| **4. Ethical Compliance & FAIR Data Management** | 4/5 | Well-aligned with FAIR data management principles and institutional data lineage. |
| **5. Feasibility & Expected Impact** | 4.5/5 | High feasibility, clear operational pipeline, and clear execution workflow. |

---

## 3. Key Observations & Critical Feedback

### Major Comment 2: Data Leakage Prevention during Feature Engineering
* **Observation:** In NLP and tabular preprocessing, a common flaw identified in botanical ML literature (e.g., Muflih et al., 2024) is fitting transformers (like TF-IDF vectorizers, One-Hot encoders, or standard scalers) on the full dataset prior to train/test partitioning.
* **Critique:** If `TfidfVectorizer.fit()` or `CountVectorizer.fit()` is called on the entire dataset $X$, document frequency statistics ($\text{IDF}$) leak global information from the validation and test sets into the training phase.
* **Recommendation:**
  1. Explicitly verify in the protocol text and pipeline code that `preprocessor.fit()` is executed *strictly* on `X_train`, while `X_val` and `X_test` are transformed using `preprocessor.transform()`.
  2. Enforce multi-label stratification on `Habit` to ensure minority growth habit classes (such as Lianas or Herbs) maintain identical proportional representation across train, validation, and test sets.

---

## 4. Final Recommendation

**Decision:** **Accept with Minor Revisions**

The protocol methodology is solid. The author should explicitly document the strict fit/transform separation in Protocol v2.0 to highlight leakage prevention as a core methodological strength.
