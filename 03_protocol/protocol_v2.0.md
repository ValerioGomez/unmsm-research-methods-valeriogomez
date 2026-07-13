# Research Protocol v2.0 (Final)

**Title:** Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning  
**Author:** Valerio Gomez  
**Date:** July 2026  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Project Title
**Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning**

---

## 2. Final Pipeline Architecture
The final machine learning pipeline is designed with strict modularity and computational controls to prevent data leakage and ensure reproducibility:

1. **Ingestion & Versioning:** Raw and processed datasets are locked and versioned via DVC (linked to Google Drive storage).
2. **Train-Validation-Test Partitioning:** The dataset is split into 70% training, 15% validation, and 15% testing, stratified by the `Habit` target variable using a fixed random seed (`SEED=42`).
3. **Preprocessing Pipeline (ColumnTransformer):**
   - **Taxonomic categorical data (Family, Genus):** Encoded using `OneHotEncoder(handle_unknown='ignore')`.
   - **Geographic department codes (Distribution):** Cleaned, split by commas, and binarized using `CountVectorizer`.
   - **Traditional etnobotanical text descriptions (Uses):** Tokenized and TF-IDF vectorized (`TfidfVectorizer`) with a limit of 300 features.
4. **Models & Hyperparameters:**
   - **Multinomial Logistic Regression:** baseline parametric model (max_iter=1000, multi_class='multinomial').
   - **Random Forest Classifier:** n_estimators=100, random_state=42.
   - **XGBoost Classifier:** n_estimators=100, learning_rate=0.1, random_state=42, eval_metric='mlogloss'.

---

## 3. Performance Summary
| Model | Validation Accuracy | Validation Macro F1 | Test Accuracy | Test Macro F1 |
|---|---|---|---|---|
| Multinomial Logistic Regression | 0.7333 | 0.7648 | - | - |
| Random Forest | 0.8000 | 0.8222 | 0.6000 | 0.4722 |
| XGBoost | 0.8000 | 0.8333 | - | - |

*Note: Models perform well on validation data but show overfitting on the test set due to high-dimensional feature representations on a small sample size. Future work will investigate regularized representations.*

---

## 4. Ethical & Integrity Compliance
- **Nagoya Protocol Alignment:** This study acknowledges the public custody of the IIAP over the Amazonian plant dataset. The etnobotanical uses belong to the indigenous and local communities. The code is shared under an open-source license, but the data remains restricted to academic replication to prevent commercial biopiracy.
- **Fairness & Bias Check:** Evaluated performance disparities across taxonomic families and regions to ensure the model does not disproportionately misclassify growth habits of plants from less-sampled departments.

---

## 5. Peer Review Response Table
Below is the response table addressing the major comments raised by peer reviewers during the course:

| # | Reviewer Comment | Action Taken in Protocol v2.0 |
|---|---|---|
| 1 | The sample size is small for XGBoost; it may overfit. | Acknowledged in Section 3 and the Model Card. Added Logistic Regression as a simpler baseline. |
| 2 | Data leakage might occur if TF-IDF is fit on the whole dataset. | Added a strict data splitting pipeline that performs split *before* fitting the preprocessor. |
| 3 | Need to explicitly mention Nagoya Protocol compliance. | Expanded the ethical protocol (Session 9) to document traditional knowledge rights. |
