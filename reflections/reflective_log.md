# Reflective Log: Growth Habit Classification of Peruvian Amazonian Medicinal Plants

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

---

## Unit II Reflection: Reproducible Pipelines, Model Auditing, and Ethics (Sessions 5-12)

### 1. What Happened?
During this unit, I built and audited the technical and ethical infrastructure of the machine learning pipeline:
- **Reproducible Pipeline (Session 5):** Implemented a modular preprocessing and classification pipeline comparing Multinomial Logistic Regression, Random Forest, and XGBoost. I integrated MLflow for experiment tracking and DVC for data lineage.
- **Reproducibility Audit (Session 6):** Audited an external botanical ML study (Muflih et al., 2024) and evaluated it with a score of 1/10 due to a complete lack of code, data, and environment documentation.
- **Standardized Documentation (Session 7):** Developed a Model Card for our best-performing Random Forest model and a Dataset Datasheet following the frameworks of Mitchell et al. (2019) and Gebru et al. (2021).
- **Ethics & Data Management (Sessions 9-10):** Formulated an ethics protocol applying the Belmont principles to ethnobotanical AI and designed a FAIR-compliant Data Management Plan.
- **Bias Audit (Session 11):** Conducted a geographical bias audit which revealed a significant disparate impact (below the 80% rule) for plant growth classification outside the overrepresented Loreto department.
- **AI Integrity & Policy (Session 12):** Analyzed a retracted botanical machine learning paper to study the impact of fabricated metrics and set up a personal AI use policy to govern generative AI usage.

### 2. So What?
This unit bridged the gap between theoretical research framing and concrete computational engineering:
- **The Reality of the Replication Crisis:** The reproducibility audit showed that botanical machine learning literature is largely non-reproducible. This validated the effort spent setting up Docker, pinned requirements, and DVC.
- **Systemic Biases in Scientific Data:** The bias audit proved that geographic representation imbalances in collection databases translate directly into performance inequalities in AI models. A model trained on skewed collections behaves unfairly towards underrepresented ecological regions.
- **Ethical Open Science:** Complying with the Nagoya Protocol means recognizing that open science cannot be absolute when dealing with traditional indigenous knowledge. We must protect data from commercial exploitation while sharing code and modeling parameters openly.

### 3. Now What?
As we move into the final stage of the course:
1. **Regularization:** I will apply regularization and feature selection to the pipeline to address the significant overfitting observed on the test set (F1-score drop from 0.82 to 0.47).
2. **Database Scale:** Scale the training pipeline from the 100-sample clean subset to the full 1,028-sample IIAP dataset once data pre-cleaning is approved.
3. **Synthesis:** Compile the complete research protocols (v1.0 and v2.0) and gather classmate peer reviews to finalize the capstone project.
