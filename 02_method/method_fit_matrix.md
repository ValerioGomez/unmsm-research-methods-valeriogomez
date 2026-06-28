# Method Fit Matrix: Growth Habit Classification of Peruvian Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

## 1. Methodological Declaration: Quasi-Experimental Design
This study is explicitly classified as a **quasi-experiment** rather than a true experiment. 
* In a **true experiment**, the researcher has full control over the independent variables, actively manipulates the treatments, and randomly assigns subjects to experimental and control groups.
* In this study, we utilize **observational data** collected by the Instituto de Investigaciones de la Amazonía Peruana (IIAP) over 18 years. We cannot manipulate the taxonomy, geographic origin, or growth habits of these plants. 
* However, we apply a **quasi-experimental framework** by using computational controls: we divide the dataset into independent training, validation, and testing subsets, stratifying by the target variable (`HÁBITO`) to prevent distribution shifts. We freeze random seeds (`SEED=42`) to ensure that the experimental partition is perfectly reproducible. This approach simulates the rigor of experimental controls on static, retrospective observational data, which provides transparency and scientific credibility.

---

## 2. EDFCV Fit Matrix

The Method Fit is evaluated across five dimensions (EDFCV): Epistemological Fit, Data Fit, Feasibility, Contribution, and Venue Fit.

| Criterion | Evaluation & Justification | Alignment Status |
| :--- | :--- | :--- |
| **E - Epistemological Fit** | The research question asks if growth habit can be predicted from taxonomic, geographic, and textual features. This aligned with the **positivist paradigm**. Machine learning models act as mathematical mapping functions ($f(X) \rightarrow Y$). By using objective, quantitative performance metrics (Accuracy, Macro F1-score) and cross-validation, the epistemological assumption of objective, measurable truth is fully satisfied. | **Highly Aligned** |
| **D - Data Fit** | The IIAP database contains approximately **1,028 records** of Amazonian medicinal plants. The variables include high-quality taxonomy (Family, Genus), geographic distribution (Department codes), and unstructured text (uses). This size is sufficient for training medium-complexity classifiers (Logistic Regression, Random Forest, XGBoost) without deep neural networks, which would overfit. The target variable `HÁBITO` has four classes (Tree, Shrub, Herb, Liana), representing a classic multi-class classification problem. | **Highly Aligned** |
| **F - Feasibility** | The project is highly feasible. It relies on standard, open-source Python libraries (`pandas`, `scikit-learn`, `xgboost`, `mlflow`). The dataset size is small enough to run training processes in seconds on consumer-grade hardware (or within a Docker container). Data is already collected by IIAP, eliminating the risk of field collection delays. | **Highly Feasible** |
| **C - Contribution** | **Practical Contribution**: Provides IIAP with an automated tool to classify newly discovered or cataloged specimens and identify potential recording errors in their database.<br>**Theoretical Contribution**: Investigates the correlation strength between traditional medicinal uses (etnobotanical text) and the plant's ecological growth habit, a relationship rarely explored quantitatively. | **High Value** |
| **V - Venue Fit** | The methodology (reproducible machine learning pipeline, Docker environment, DVC tracking, and fairness/bias checks) aligns with high-impact journals in **Biodiversity Informatics**, **Ecological Informatics**, and **Applied Artificial Intelligence** (e.g., *Ecological Informatics*, *Springer Nature Applied Sciences*). | **Aligned** |

---

## 3. Methodological Rigor and Limitations
* **Confounding Variables**: Sampling bias in geographical collection (some departments like Loreto are heavily overrepresented) could lead to spatial autocorrelation, where the model predicts growth habit based on regional bias rather than true botanical features. This will be mitigated and documented in the Datasheet.
* **Feature Engineering**: To prevent data leakage and overfitting, we will evaluate three distinct feature strategies: taxonomic features only, taxonomic + geographic features, and the full set including etnobotanical text encoded via TF-IDF.
