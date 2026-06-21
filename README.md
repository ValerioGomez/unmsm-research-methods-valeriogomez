# Customer Churn Prediction – Reproducible ML Pipeline & Fairness Audit

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur

## Project Title
**"A Reproducible and Fairness-Aware Machine Learning Pipeline for Customer Churn Prediction in a Subscription Service"**

## Project Description
This repository contains a fully reproducible machine learning pipeline for predicting customer churn in a subscription service. It compares five classifiers (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, and SVM), selects the best by recall, and includes a fairness audit for gender bias. The stack includes Git, DVC, MLflow, and Docker to ensure anyone can reproduce the results with a single command.

## Quick Start (Stranger Test)
```bash
git clone https://github.com/ValerioGomez/unmsm-research-methods-valeriogomez.git
cd unmsm-research-methods-valeriogomez
dvc pull
docker build -t churn-project .
docker run -it --rm -p 8888:8888 -v $(pwd):/project churn-project jupyter lab --ip=0.0.0.0 --allow-root
```
Then open the notebook in `05_pipeline/notebook.ipynb` and run all cells.

---

## Repository Index

| Session | Document | Status |
|---------|----------|--------|
| 01 | [Paradigm Justification](01_paradigm/paradigm_justification.md) | ✅ Active |
| 02 | [Method Fit Matrix](02_method/method_fit_matrix.md) | ✅ Active |
| 03 | [Protocol v0.1](03_protocol/protocol_v0.1.md) | ✅ Active |
| 03 | [Protocol v1.0](03_protocol/protocol_v1.0.md) | ✅ Active |
| 03 | [Protocol v2.0](03_protocol/protocol_v2.0.md) | ✅ Active |
| 04 | [Systematic Review](04_literature/systematic_review.md) | ✅ Active |
| 04 | [Gap Analysis](04_literature/gap_analysis.md) | ✅ Active |
| 04 | [PRISMA Diagram](04_literature/prisma_diagram.png) | ✅ Placeholder |
| 05 | [Pipeline Notebook](05_pipeline/notebook.ipynb) | ✅ Active |
| 06 | [Reproducibility Audit](06_repro_audit/reproducibility_audit.md) | ✅ Active |
| 07 | [Model Card](07_model_card/model_card.md) | ✅ Active |
| 07 | [Datasheet](07_model_card/datasheet.md) | ✅ Active |
| 09 | [Ethics Protocol](09_ethics/ethics_protocol.md) | ⏳ Pending |
| 10 | [Data Management Plan](10_data_mgmt/data_management_plan.md) | ⏳ Pending |
| 11 | [Bias Audit Report](11_bias_audit/bias_audit_report.md) | ⏳ Pending |
| 12 | [Retracted Paper Analysis](12_integrity/retracted_paper_analysis.md) | ⏳ Pending |
| 12 | [AI Use Policy](12_integrity/ai_use_policy.md) | ⏳ Pending |
| – | [Reflective Log](reflections/reflective_log.md) | ✅ Active |

---

## Reproducibility Stack

| Tool | Purpose |
|------|---------|
| **Git** | Full version history of code and documents |
| **DVC** | Dataset version control and remote storage |
| **MLflow** | Experiment tracking (metrics, parameters, models) |
| **Docker** | Containerized, frozen environment |
| **`requirements.txt`** | Pinned Python dependencies |
| **`SEED=42`** | Fixed random seed for all libraries |

---

## Research Question
*Which supervised classification algorithm maximizes recall for churn prediction on the subscription dataset, and does the best model exhibit gender-based performance disparities?*
