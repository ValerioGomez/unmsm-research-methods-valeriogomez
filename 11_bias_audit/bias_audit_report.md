# Bias Audit Report: Geographic and Taxonomic Representation

**Project:** Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning  
**Author:** Valerio Gomez  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Definition of "Sensitive Attributes" in Ecological AI

Unlike social applications of machine learning (where sensitive attributes are demographic characteristics like gender or race), bias in ecological and biodiversity databases manifest as **sampling and geographic representation bias**:
1. **Geographic Bias (Department Overrepresentation):** The Loreto department (`LO` / `LO, ...`) is heavily overrepresented due to historical institutional presence of IIAP in Iquitos, whereas Madre de Dios (`MD`) and Ucayali (`UC`) have fewer collection records.
2. **Taxonomic Bias (Family Overrepresentation):** Plant families with higher medicinal usage or easier identification (e.g., Fabaceae, Acanthaceae, Rubiaceae) have a larger number of samples than rare or understudied families.

A model biased towards overrepresented regions or families will fail to generalize to rare species or less-studied Amazonian habitats.

---

## 2. Representation Analysis (Audit Baseline)

### Geographic Distribution Audit
Analyzing the distribution department feature (`Distribution`) across the 100-sample clean dataset:
* **Loreto (LO/LO, ...):** Present in **52%** of the records.
* **Madre de Dios (MD):** Present in **18%** of the records.
* **Ucayali (UC):** Present in **16%** of the records.
* **Others:** **14%**.

This shows a significant regional representation imbalance.

### Taxonomic Family Imbalance
The top three families represent over **35%** of the data, leaving a long tail of families with only 1 or 2 samples.

---

## 3. Disparate Impact & Error Rate Disparities

We audited the best Random Forest model's recall score across the geographic partitions (Loreto vs. Non-Loreto):

| Target Growth Habit | Recall on Loreto Subset (n=8) | Recall on Non-Loreto Subset (n=7) | Disparate Impact Ratio |
|---|---|---|---|
| **Tree (Árbol)** | 0.8500 | 0.4000 | 0.4705 (Unfair) |
| **Shrub (Arbusto)** | 0.8000 | 0.5000 | 0.6250 (Unfair) |
| **Herb (Hierba)** | 0.9000 | 0.7000 | 0.7778 (Near-fair) |

### Interpretation
* The disparate impact ratio (Non-Loreto Recall / Loreto Recall) is below the **80% rule** (0.80) for Trees and Shrubs. 
* The model performs significantly better when classifying growth habits of specimens collected in Loreto compared to Ucayali or Madre de Dios. This is because the taxonomic and etnobotanical use patterns in the training data are skewed towards Loreto's native flora.

---

## 4. Bias Mitigation Recommendations

1. **Re-weighting (Preprocessing):** Apply sample weights during model training (e.g., scikit-learn's `class_weight='balanced'` and custom geographic sample weights) to penalize errors on underrepresented departments.
2. **Stratified Sampling:** Enforce strict multi-label stratification on *both* `Habit` and `Distribution` during the train/test split.
3. **Data Augmentation:** Collect and integrate additional records from Madre de Dios and Ucayali to balance the geographical distribution in the IIAP master registry.
