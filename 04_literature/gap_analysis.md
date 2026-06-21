# Gap Analysis – Churn Prediction Literature

**Project:** Customer Churn Reproducible Pipeline  
**Author:** Valerio Gomez  
**Date:** June 2026

| Dimension | State of the Art | Gap | How Our Project Addresses It |
|-----------|------------------|-----|------------------------------|
| **Reproducibility** | Most studies lack code, seeds, environment specs. | No standard end-to-end reproducible pipeline. | We provide Docker, DVC, MLflow, pinned dependencies, fixed seed. |
| **Fairness** | 70% of churn papers ignore fairness entirely. | Gender bias in churn models is unmeasured. | We will run AIF360 disparate impact analysis and apply one mitigation. |
| **Documentation** | Rarely includes model cards or datasheets. | Stakeholders cannot assess model limitations. | We create a Model Card (Session 7) and a Datasheet. |
| **Data Leakage** | Many papers scale before splitting or use future info. | Overly optimistic results reported. | We split first, scale only on training data, log the order in MLflow. |
