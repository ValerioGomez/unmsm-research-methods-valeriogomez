# Reflective Log: Growth Habit Classification of Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

## Unit I Reflection: Research Framing, Method Fit, and Literature Review

### 1. What Happened?
During this unit, the research project underwent a significant restructuring. We shifted the capstone focus from a generic customer churn prediction problem to a specialized botanical classification task: predicting the growth habit (Tree, Shrub, Herb, Liana) of Peruvian Amazonian medicinal plants using data compiled by the Instituto de Investigaciones de la Amazonía Peruana (IIAP). 

To build the foundation of this new project:
- I formulated the **Paradigm Justification**, positioning the research within a realist ontology and a positivist epistemology, arguing that growth habits are objective, physical characteristics.
- I drafted the **Method Fit Matrix** using the EDFCV framework and declared this study as a **quasi-experiment** since we are training models on retrospective observational data rather than a controlled, laboratory-manipulated environment.
- I conducted a **Mini Systematic Review** of 10 relevant peer-reviewed papers and structured a **Research Gap Analysis** focusing on the contextual value of etnobotanical text and the widespread reproducibility gap in botanical ML.

### 2. So What?
This transition highlighted several theoretical and technical friction points when mapping natural biodiversity data into rigid machine learning structures:
* **Taxonomic Redundancy**: A naive approach would include all taxonomic ranks (Group, Class, Order, Family, Genus). However, scientific taxonomy is hierarchical and deterministic; including high-level ranks introduces multicollinearity and causes model overfitting. We resolved this by selecting only Family and Genus as our categorical taxonomic features.
* **Geographical and Textual Representation**: Variables like `DISTRIBUCIÓN` contain multi-department codes (e.g., `"HU, JU, LO"`), which require Multi-Label Binarization rather than standard One-Hot Encoding to preserve spatial relationships. Additionally, etnobotanical text (`USOS`) contains unstructured descriptions of how local communities interact with these plants, which represents valuable implicit ecological data that can be extracted via TF-IDF vectorization.
* **Ethics of Traditional Knowledge**: Since this dataset represents 18 years of etnobotanical knowledge shared by Amazonian communities, we must address scientific integrity. The project must strictly respect the Nagoya Protocol, ensuring that our model serves as a tool for public documentation and conservation rather than bio-piracy.

### 3. Now What?
With the research questions and methodological framework established, the next phase is to build the functional machine learning pipeline (Unit II). To ensure absolute reproducibility and address the methodological gaps identified in our systematic review, I will implement the following steps:
1. **Infrastructure**: Setup a Docker container to freeze python package versions (e.g., `scikit-learn`, `xgboost`, `pandas`, `mlflow`).
2. **Data Versioning**: Initialize Data Version Control (DVC) to track the 1,028 database records using pointer files, storing the raw CSV on a Google Drive remote.
3. **Model Tracking**: Write training scripts that automatically log hyperparameter grid search results (for Logistic Regression, Random Forest, and XGBoost) and evaluation metrics (Accuracy, Macro F1-score) to MLflow.
4. **Consistency**: Freeze all random seeds (`SEED=42`) across the codebase to ensure that data splits and ensemble trees remain identical upon reproduction.
