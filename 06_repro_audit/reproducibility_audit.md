# Reproducibility Audit of a Published Churn Prediction Paper

**Paper audited:** Chen, L., & Wang, S. (2022). "A Comparative Study of Ensemble Methods for Subscription Churn." *Journal of Data Science Applications*, 15(3), 210–225.

**Auditor:** Valerio Gomez  
**Date:** June 2026

## 1. Does the paper report random seeds?
No. The paper mentions using train/test split but never specifies a seed. Therefore, results are not deterministically reproducible.

## 2. Does it describe the data split methodology?
Yes, it states "70% training, 30% testing," but does not clarify if stratification was used or if it was a single fixed split.

## 3. Are statistical tests or confidence intervals reported?
No. Only point estimates of accuracy and F1 are given. No confidence intervals or standard deviations across multiple runs.

## 4. Is the code or data publicly available?
No. The paper claims the data is proprietary and no code repository is linked. This makes independent verification impossible.

## 5. Is the compute environment documented?
No. No mention of Python version, library versions, or hardware. The dependency stack is completely unknown.

## 6. Does it avoid data leakage?
Unclear. The paper states features were normalized before training, but does not specify if normalization was computed on the whole dataset or only training data. Potential leakage.

## Overall Reproducibility Score: 2/10
**Justification:** The paper's claims cannot be verified without access to code, data, environment, or even the random seed. The missing information would prevent anyone from obtaining the same numbers. The study is essentially non-reproducible.

## Reflection on My Own Project
- I now enforce **seed fixation** for all libraries.
- I **split before any preprocessing** and log the order in MLflow.
- My **Dockerfile + requirements.txt** freeze the full environment.
- **DVC** tracks the dataset version, so a colleague can run `dvc pull` and get the exact data.
- This audit directly influenced the design of my pipeline.
