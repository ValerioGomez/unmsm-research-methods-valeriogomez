# Method-Fit Matrix

**Project:** Customer Churn Prediction – Reproducible Pipeline  
**Author:** Valerio Gomez  
**Date:** June 2026

## Refined Research Question
*Which supervised classification algorithm maximizes recall for churn prediction on the subscription dataset, and does the best model exhibit gender-based performance disparities?*

## Candidate Methods

| Method | Description |
|--------|-------------|
| **Experiment (Computational)** | Controlled comparison of multiple ML models using identical data splits, seeds, and evaluation protocol. |
| **Case Study** | In-depth investigation of churn within this single company, using mixed quantitative and qualitative data. |
| **Design Science** | Creation and evaluation of an artifact (e.g., a churn prediction dashboard with fairness constraints). |

## Evaluation Criteria (1 = weak, 5 = strong)

| Criterion | Experiment | Case Study | Design Science |
|-----------|------------|------------|----------------|
| Control over variables | 5 | 2 | 3 |
| Generalizability of findings | 3 | 2 | 3 |
| Feasibility (time/data) | 5 | 3 | 2 |
| Ethical compliance & fairness integration | 4 | 4 | 5 |
| Alignment with positivist paradigm | 5 | 3 | 2 |
| **Total** | **22** | **14** | **15** |

## Justification of Selection
**Experiment** scores highest because:
- The dataset is ready-made; no qualitative data collection is needed.
- The research question is comparative and quantitative, ideally suited to a controlled experiment with fixed seeds and preprocessing.
- Reproducibility is built into the experimental design: Docker, DVC, MLflow.
- Fairness can be examined as a post-hoc analysis, which I will add using AIF360 in Session 11.

Case Study was rejected because it would require access to customer interviews or internal documents not available. Design Science would demand building a full artifact beyond the scope of this mini-study.

**Chosen method:** Computational Experiment.
