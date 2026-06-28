# Research Gap Analysis: Botanical Growth Habit Classification

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

This document presents the research gap analysis for classifying growth habits of Amazonian medicinal plants. We identify knowledge, methodological, contextual, and theoretical gaps in the existing literature and explain how this project addresses them.

## 1. Gap Analysis Table

| Gap Category | Identified Limitation in Literature | Project Mitigation / Contribution | Academic Rigor Level |
| :--- | :--- | :--- | :--- |
| **Knowledge Gap** | Most machine learning studies in botany focus on commercial timber species, North American/European temperate forests, or crop classification. There is a lack of automated, predictive analysis applied directly to hyper-diverse tropical databases, such as the Peruvian Amazonian database compiled by the IIAP. | We apply ML classifiers (Logistic Regression, Random Forest, XGBoost) directly to a specialized database of over 1,000 Amazonian medicinal plant species. | **High** (Addresses neglected tropical biodiversity) |
| **Methodological Gap** | Ecological and botanical ML models rarely document random seeds, software dependency versions, or data pipeline states, resulting in a reproducibility crisis (as noted by Evans & Green, 2023). | We implement a strict **Reproducibility Stack** using Git, Data Version Control (DVC) for data lineage, MLflow for metric tracking, and Docker for environment freezing. | **Critical** (Ensures full replication of experimental results) |
| **Contextual Gap** | Existing growth form models rely purely on taxonomic categories or climate variables. They ignore the rich, unstructured etnobotanical texts (traditional uses descriptions) that contain implicit ecological cues. | We integrate unstructured etnobotanical text (`USOS`) via **TF-IDF vectorization** to evaluate if local human knowledge adds predictive value to taxonomic models. | **High** (Innovates by blending NLP with tabular data) |
| **Theoretical Gap** | Standard classification models treat plant growth habits as mutually exclusive, static categories (Tree, Shrub, Herb, Liana). They fail to account for biological transitions (e.g., plants that behave as shrubs or lianas depending on canopy light). | We perform an **error analysis per class** (Macro F1-score comparison) to analyze where the boundaries between classes break down, revealing transitional species. | **Moderate** (Exposes boundary limitations of classification models) |

---

## 2. Detailed Explanation of the Gaps

### 2.1 The Contextual Gap: Integrating Etnobotanical Text (`USOS`)
Traditional etnobotanical descriptions detail how and where communities harvest plants. For example, text like *"harvested in high tree branches"* or *"collected in the forest understory"* implicitly encodes whether a plant is a Liana/Epiphyte (high branch) or a Shrub/Herb (understory). By applying TF-IDF vectorization to the `USOS` field, we capture these linguistic patterns and convert them into numerical features. This project directly tests whether adding these textual features (Feature Set C) improves the classifier's performance compared to purely taxonomic baseline models (Feature Set A).

### 2.2 The Methodological Gap: The "Reproducibility Pyramid"
In botany, models are often published as static results with no sharing of exact dataset splits or package versions, making it impossible for other researchers to verify findings. By using:
1. **DVC**: We track the 1,028 database records using `.dvc` files, hosting the actual CSV in Google Drive.
2. **MLflow**: We log hyperparameter configurations and macro F1 scores dynamically, creating an automated registry.
3. **Docker**: We package the training environment so that anyone can replicate the exact predictions, addressing the reproducibility gap.
