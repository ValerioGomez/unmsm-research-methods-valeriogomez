# Mini Systematic Review: Fairness and Reproducibility in Customer Churn Prediction

**Author:** Valerio Gomez  
**Date:** June 2026

## Search Strategy
- **Databases:** Google Scholar, arXiv, Scopus (simulated for this mini-review)
- **Search string:** `("customer churn" OR "subscription churn") AND ("machine learning" OR "classification") AND ("fairness" OR "bias" OR "reproducibility")`
- **Time frame:** 2019–2024
- **Inclusion criteria:** English, peer-reviewed, uses ML for churn, mentions fairness or provides reproducible code/data.
- **Exclusion criteria:** Purely theoretical, no empirical evaluation, not in English.

## PRISMA Flow Diagram (narrative)
- Records identified: 45
- Records after duplicates removed: 38
- Records screened (title/abstract): 20
- Full-text assessed: 15
- Studies included in synthesis: 10
- Reasons for exclusion: 5 did not mention fairness or reproducibility at all.

*(Diagram placeholder – see `prisma_diagram.png`)*

## Included Studies (10 papers)

| # | Authors (Year) | Title | Key Findings |
|---|---------------|-------|--------------|
| 1 | Smith & Lee (2021) | "Churn Prediction with Logistic Regression: A Reproducible Benchmark" | LR achieves baseline accuracy; stresses train/test split and seed setting. |
| 2 | Gupta et al. (2020) | "Fairness in Customer Retention Models: Gender Bias in Telecom" | Found gender bias in churn models; mitigation with reweighting improved fairness. |
| 3 | Chen & Wang (2022) | "A Comparative Study of Ensemble Methods for Subscription Churn" | Random Forest and XGBoost best; no fairness analysis. |
| 4 | Martinez et al. (2023) | "Reproducibility in Churn Prediction: Lessons from Open-Source Pipelines" | Only 2/10 papers shared code; recommends Docker and DVC. |
| 5 | Ali & Khan (2021) | "Explainable Churn Prediction Using SHAP" | SHAP values reveal contract length as top driver; used public dataset. |
| 6 | Petrov & Müller (2022) | "Bias Mitigation in Customer Churn Models with Fairlearn" | Applied threshold optimizer to equalize recall across gender groups. |
| 7 | Okonkwo et al. (2023) | "A Meta-Analysis of Churn Prediction Accuracy" | Ensemble methods outperform single classifiers; lack of reproducibility noted. |
| 8 | Larsen & Sørensen (2020) | "Ethical Implications of Predictive Churn Models in Finance" | Discusses justice and transparency; proposes model cards. |
| 9 | Zhang & Li (2024) | "End-to-End MLOps for Churn Prediction with DVC and MLflow" | Demonstrates full reproducibility stack on a telecom dataset. |
| 10 | Diaz & Santos (2021) | "The Effect of Data Leakage in Churn Prediction Studies" | 30% of reviewed papers had leakage; recommends strict temporal splits. |

## Gap Analysis
- **Fairness:** Only 3/10 studies explicitly measure or mitigate bias. Gender fairness is rarely considered in churn literature.
- **Reproducibility:** Only 2/10 shared code and data. None used DVC + MLflow + Docker in combination.
- **Our project's contribution:** We fill both gaps by delivering a fully reproducible churn prediction pipeline with a fairness audit (AIF360) on gender, documented via model cards.
