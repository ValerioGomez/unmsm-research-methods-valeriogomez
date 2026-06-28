# Growth Habit Classification of Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur

## Project Title
**"Growth Habit Classification of Amazonian Medicinal Plants using Machine Learning Ensembles"**

## Project Description
This repository contains a reproducible machine learning pipeline designed to predict the growth habit (Tree, Shrub, Herb, Liana) of medicinal plants in the Peruvian Amazon using the database compiled by the Instituto de Investigaciones de la Amazonía Peruana (IIAP). The project compares three classifiers (Multinomial Logistic Regression, Random Forest, and XGBoost) and incorporates etnobotanical text features (uses) via TF-IDF vectorization alongside taxonomic and geographic metadata. The stack utilizes Git, DVC, MLflow, and Docker to ensure full transparency and reproducibility, in compliance with the Nagoya Protocol.

## Quick Start (Stranger Test)
```bash
git clone https://github.com/ValerioGomez/unmsm-research-methods-valeriogomez.git
cd unmsm-research-methods-valeriogomez
docker build -t research-project .
docker run -it --rm -p 8888:8888 -v $(pwd):/project research-project jupyter lab --ip=0.0.0.0 --allow-root
```
*Note: Once the data preparation code is finalized, data pulling will be handled via DVC using `dvc pull`.*

---

## Repository Index

| Session | Document | Status |
|---------|----------|--------|
| 01 | [Paradigm Justification](01_paradigm/paradigm_justification.md) | ✅ Active |
| 02 | [Method Fit Matrix](02_method/method_fit_matrix.md) | ✅ Active |
| 03 | [Protocol v0.1](03_protocol/protocol_v0.1.md) | ✅ Active |
| 03 | [Protocol v1.0](03_protocol/protocol_v1.0.md) | ⏳ Pending |
| 03 | [Protocol v2.0](03_protocol/protocol_v2.0.md) | ⏳ Pending |
| 04 | [Systematic Review](04_literature/systematic_review.md) | ✅ Active |
| 04 | [Gap Analysis](04_literature/gap_analysis.md) | ✅ Active |
| 04 | [PRISMA Diagram](04_literature/prisma_diagram.png) | ✅ Active |
| 05 | [Pipeline Notebook](05_pipeline/notebook.ipynb) | ⏳ Pending |
| 06 | [Reproducibility Audit](06_repro_audit/reproducibility_audit.md) | ⏳ Pending |
| 07 | [Model Card](07_model_card/model_card.md) | ⏳ Pending |
| 07 | [Datasheet](07_model_card/datasheet.md) | ⏳ Pending |
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
*Which supervised classification algorithm (Multinomial Logistic Regression, Random Forest, or XGBoost) maximizes the macro F1-score for predicting the growth habit (Tree, Shrub, Herb, Liana) of Amazonian medicinal plants, and to what extent does the integration of unstructured etnobotanical text features (uses) improve performance compared to taxonomic and geographic baselines?*
