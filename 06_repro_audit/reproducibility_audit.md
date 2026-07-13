# Reproducibility Audit of a Published Botanical Machine Learning Study

**Audited Paper:** Muflih, M. A., et al. (2024). "Comparison of SVM, Naive Bayes, and ELM Models in Plant Growth Classification." *INTI Journal*, Vol. 2024, No. 1.

**Auditor:** Valerio Gomez  
**Date:** July 2026  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Audit Checklist & Verification Questions

| Verification Question | Audit Result / Finding | Status |
|---|---|---|
| **1. Are random seeds reported?** | No. The paper mentions splitting the dataset into training and testing partitions, but does not provide the random seeds or state whether the partitions are fixed. | ❌ **Failed** |
| **2. Is the data split methodology detailed?** | Partially. It states an 80/20 split ratio was used, but does not specify if the partition was stratified by target classes to maintain balanced proportions. | ⚠️ **Partial** |
| **3. Are confidence intervals or statistical tests reported?** | No. Only single point estimates of classification accuracy are reported. No cross-validation variance, standard deviations, or statistical tests (such as McNemar's test) are included. | ❌ **Failed** |
| **4. Is the code or dataset publicly available?** | No. The paper does not provide a link to a GitHub repository, Zenodo archive, or any open-source database containing the code or Excel sheets used. | ❌ **Failed** |
| **5. Is the compute environment documented?** | No. The paper does not specify the versions of libraries (e.g., Scikit-learn, Python version) or hardware configurations used to execute the Extreme Learning Machine (ELM). | ❌ **Failed** |
| **6. Does it avoid data leakage?** | Unclear. The paper mentions normalizing input variables (temperature, sunlight hours) but does not clarify whether the scaling parameters (mean/variance) were computed only on the training set or on the entire dataset before splitting. | ❌ **Failed** |

---

## 2. Overall Reproducibility Score: 1/10
**Justification:** The paper fails to meet basic scientific reproducibility standards in machine learning. Without access to the raw dataset, seed variables, library versions, or source code, independent replication of the classification results (SVM: 58.97%, Naïve Bayes: 51.28%, ELM: 43.85%) is impossible. The study is a "black box" computational exercise.

---

## 3. Reflections and Mitigations in My Project
This reproducibility audit directly informs and reinforces the strict computational controls implemented in my own capstone project:
* **Fixed Seeds:** In `05_pipeline/notebook.ipynb`, `SEED=42` is locked for Python, NumPy, and Scikit-learn, ensuring deterministic train/test splits and model initializations.
* **Leakage Prevention:** Splitting (70% training, 15% validation, 15% testing) is performed strictly *before* any preprocessing or text TF-IDF vectorization.
* **Environment Freezing:** Pinned dependencies in `requirements.txt` and a containerized environment via `Dockerfile` ensure identical execution regardless of the host machine.
* **Data Lineage:** Raw and processed files are tracked using DVC pointer files, linking them to versioned storage on Google Drive.
