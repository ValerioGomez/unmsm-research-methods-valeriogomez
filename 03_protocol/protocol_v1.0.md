# Research Protocol v1.0 (Draft)

**Title:** Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning  
**Author:** Valerio Gomez  
**Date:** July 2026  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Project Title
**Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning**

---

## 2. Research Questions & Hypotheses
* **General Question (GQ):** Is it possible to predict the ecological growth habit (Tree, Shrub, Herb, Liana) of Peruvian Amazonian medicinal plants based on taxonomic, geographic, and etnobotanical features using machine learning?
* **Specific Question 1 (SQ1):** What is the performance (Accuracy, Macro F1-score) of Multinomial Logistic Regression, Random Forest, and XGBoost in classifying plant growth habits?
* **Specific Question 2 (SQ2):** Which features (Family, Genus, Department, or Etnobotanical Uses) contribute the most to the predictions of the models?
* **Specific Question 3 (SQ3):** What feature representation strategy (Taxonomic only, Taxonomic + Geographic, or Full Features with TF-IDF encoded text) yields the highest predictive performance?
* **Specific Question 4 (SQ4):** Are there statistically significant differences in model performance when predicting different growth habits (Tree, Shrub, Herb, Liana)?

### Hypotheses
* **H0 (Null Hypothesis):** Machine learning models cannot predict the growth habit of Peruvian Amazonian medicinal plants better than a random baseline classifier.
* **H1 (Alternative Hypothesis):** Machine learning models can predict the growth habit with a Macro F1-score > 0.70.
* **H2 (Alternative Hypothesis):** Non-parametric ensemble methods (XGBoost and Random Forest) will outperform Multinomial Logistic Regression due to the high-dimensional taxonomic and text-derived features.

---

## 3. Quasi-Experimental Design
This study employs a quasi-experimental, quantitative design using retrospective observational data from the IIAP (~1,028 records). The dataset is divided into:
- **Training Set (70%):** Used to fit the models.
- **Validation Set (15%):** Used for model tuning and selecting the best model.
- **Testing Set (15%):** Used for the final evaluation of the selected model.

To prevent data leakage, we partition the dataset *before* fitting any preprocessing transformer (such as TF-IDF or One-Hot encoder). The random seed is locked at `SEED=42` across Python, NumPy, and Scikit-learn.

---

## 4. Preprocessing & Modelling Pipeline
- **Taxonomic Features (Family, Genus):** One-Hot encoded.
- **Geographic Features (Distribution):** Tokenized by department code and binarized using a binary bag-of-words model.
- **Etnobotanical text (Uses):** Tokenized and TF-IDF vectorized with a maximum of 300 features.
- **Target (Habit):** Label encoded (Tree = 0, Shrub = 1, Herb = 2).

### Models Compared
1. **Multinomial Logistic Regression:** baseline parametric model.
2. **Random Forest:** bagging ensemble.
3. **XGBoost:** gradient boosting ensemble.

---

## 5. Preliminary Results (Validation Set)
We evaluated the models on the validation set (15 samples) with the following macro-averaged F1-scores:
- **Multinomial Logistic Regression:** Macro F1 = 0.7648
- **Random Forest:** Macro F1 = 0.8222
- **XGBoost:** Macro F1 = 0.8333

XGBoost and Random Forest outperformed the Logistic Regression baseline, supporting H2. On the test set, the Random Forest model achieved a Test Accuracy of 0.6000 and a Test Macro F1-score of 0.4722, showing signs of overfitting due to the small sample size of the test set (15 samples). Further hyperparameter tuning is required.
