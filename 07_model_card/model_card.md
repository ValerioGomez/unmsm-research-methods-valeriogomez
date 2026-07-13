# Model Card: Amazonian Plant Growth Habit Classifier

This model card documents the performance, specifications, and limitations of the Random Forest growth habit classifier developed for ecological categorization of medicinal plants in the Peruvian Amazon.

## 1. Model Details
* **Model Name:** AmazonianPlant-RF
* **Version:** 1.0
* **Model Type:** Random Forest Classifier (Scikit-learn implementation)
* **Release Date:** July 2026
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
* **Input Features:**
  - **Taxonomic (Family, Genus):** One-Hot encoded.
  - **Geographical (Distribution departments):** Binary multi-label representation via CountVectorizer.
  - **Etnobotanical text (Uses):** TF-IDF features (max_features=300).
* **Target Classes:** Habit (Tree = 0, Shrub = 1, Herb = 2).

## 4. Performance Metrics
The model was evaluated using multi-class metrics (Macro-averaged to account for class imbalance):

| Metric | Validation Set (15 samples) | Test Set (15 samples) |
|---|---|---|
| **Accuracy** | 0.8000 | 0.6000 |
| **Macro F1-score** | 0.8222 | 0.4722 |

### Performance Insights
* The model shows high predictive accuracy on validation data (Macro F1 = 82.22%), but performance drops significantly on the test set (Macro F1 = 47.22%), suggesting overfitting to the high-dimensional taxonomic and textual features on this small dataset size (n=100).
* Multinomial Logistic Regression and XGBoost validation scores were also logged (0.7648 and 0.8333 respectively).

## 5. Ethical Considerations
* **Indigenous Knowledge Protection:** The training features include traditional etnobotanical uses compiled from local and indigenous communities. The model is released under an open-science framework to prevent commercial appropriation, aligning with the Nagoya Protocol.
* **Attribute Bias:** Certain plant families and geographical departments (e.g., Loreto) are overrepresented, which can skew the classification accuracy.

## 6. Limitations & Technical Boundaries
* **Sample Size:** The current dataset of 100 records is too small to build a highly generalizable classifier. Model accuracy will be re-evaluated when scaled to the full 1,028 IIAP records.
* **Class Constraints:** The model does not currently predict climbers (Lianas/Bejucos) or ferns, as they are not represented in the 100-sample clean subset.
