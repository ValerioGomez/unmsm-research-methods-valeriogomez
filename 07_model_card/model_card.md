# Model Card: Amazonian Plant Growth Habit Classifier

This model card documents the performance, specifications, and limitations of the machine learning classifiers developed for ecological categorization of medicinal plants in the Peruvian Amazon (IIAP Dataset).

## 1. Model Details
* **Model Name:** AmazonianPlant-XGB (Optimized) / AmazonianPlant-RF (Baseline)
* **Version:** 2.0 (Post-GridSearchCV Optimization)
* **Model Type:** Extreme Gradient Boosting (XGBoost Classifier) & Random Forest Classifier
* **Release Date:** August 2026
* **Developer:** Valerio Gomez (UNMSM Doctoral Program in Deep Technologies)
* **License:** MIT License (for source code)

## 2. Intended Use
* **Primary Intended Use:** Automated classification of ecological growth habits (Tree, Shrub, Herb) for Peruvian Amazonian medicinal plants. The model aims to assist botanists and researchers at IIAP in cataloging flora records and auditing database entry errors.
* **Intended Users:** Botanical researchers, ecologists, conservationists, database curators.
* **Out-of-Scope Uses:** The model is not trained on non-medicinal flora, non-Amazonian species, or plants outside the Madre de Dios, Loreto, and Ucayali departments. It should not be used for commercial bioprospecting or automated decision-making regarding land conservation policies without human verification.

## 3. Training & Evaluation Data
* **Training Dataset:** 70 samples (from `data/dataset.csv` compiled by IIAP).
* **Validation Dataset:** 15 samples.
* **Test Dataset:** 15 samples.
* **Input Features (312 total features):**
  - **Taxonomic (Family, Genus):** One-Hot encoded (8 families, 54 genera).
  - **Geographical (Distribution departments):** Binary multi-label representation via CountVectorizer.
  - **Etnobotanical text (Uses):** TF-IDF features (max_features=300).
* **Target Classes:** Habit (Herb = 47%, Tree = 30%, Shrub = 23%).

## 4. Performance Metrics: Baseline vs. Systematic Optimization (GridSearchCV)

| Model & Version | Hyperparameter Configuration | Val Accuracy | Val Macro F1 | Test Accuracy | Test Macro F1 | Key Result / Improvement |
|---|---|---|---|---|---|---|
| **Random Forest (Baseline v1.0)** | Default (`n_est=100`, `max_depth=None`) | 0.8667 | 0.8222 | 0.6000 | 0.4722 | Overfitted; 0.00 recall on Arbusto class |
| **Logistic Regression (Baseline v1.0)** | Default (`L2`, `max_iter=1000`) | 0.8000 | 0.7648 | 0.6000 | 0.6238 | Linear baseline |
| **XGBoost (Baseline v1.0)** | Default (`lr=0.1`, `n_est=100`) | 0.8667 | 0.8333 | 0.7333 | 0.7746 | Strong initial performance |
| **Logistic Regression (Optimized v2.0)** | GridSearch (`C=5.0`) | 0.8000 | 0.7648 | 0.6000 | 0.6238 | Regularization tuned |
| **XGBoost (Optimized v2.0 ★ BEST)** | GridSearch (`lr=0.01`, `depth=7`, `n_est=200`, `reg_lambda=1`) | 0.7333 | 0.7091 | **0.7333** | **0.6984** | **Restored Arbusto recall (F1=0.57); Best generalization** |

### Per-Class Test Breakdown (Optimized XGBoost)
* **Hierba (Herb):** Precision = 0.86 | Recall = 0.86 | **F1 = 0.86**
* **Árbol (Tree):** Precision = 0.60 | Recall = 0.75 | **F1 = 0.67**
* **Arbusto (Shrub):** Precision = 0.67 | Recall = 0.50 | **F1 = 0.57** *(Fixed zero-recall artifact from baseline RF)*

## 5. Ethical Considerations
* **Indigenous Knowledge Protection:** The training features include traditional etnobotanical uses compiled from local and indigenous communities. The model is released under an open-science framework to prevent commercial appropriation, aligning with the Nagoya Protocol.
* **Attribute Bias:** Certain plant families and geographical departments (e.g., Loreto) are overrepresented, which can skew the classification accuracy.

## 6. Limitations & Technical Boundaries
* **Sample Size:** The current clean subset of 100 records is too small to build a highly generalizable classifier. Model accuracy will be re-evaluated when scaled to the full 1,028 IIAP records.
* **Class Constraints:** The model does not currently predict climbers (Lianas/Bejucos) or ferns, as they are not represented in the 100-sample clean subset.
