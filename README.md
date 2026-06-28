# Growth Habit Classification of Peruvian Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

## 1. Project Overview
This repository contains a reproducible, end-to-end machine learning mini-study designed to predict the ecological growth habit (Tree, Shrub, Herb, Liana) of medicinal plants in the Peruvian Amazon. Using a dataset compiled by the **Instituto de Investigaciones de la Amazonía Peruana (IIAP)** containing approximately 1,028 unique numbered records across three regions (Loreto, Ucayali, Madre de Dios), this study compares the predictive performance of three supervised classifiers:
1. **Multinomial Logistic Regression** (Parametric baseline)
2. **Random Forest** (Bagging ensemble)
3. **XGBoost** (Boosting ensemble)

To improve prediction accuracy, the models leverage taxonomic family/genus categorical features, geographical distribution departments (multi-label binarized), and unstructured etnobotanical text descriptions of traditional plant uses (vectorized via Term Frequency-Inverse Document Frequency - TF-IDF). The study is framed as a **quasi-experiment** using retrospective observational data with strict computational controls.

---

## 2. Research Questions
* **General Question (GQ):** Is it possible to predict the growth habit (Tree, Shrub, Herb, Liana) of Peruvian Amazonian medicinal plants based on taxonomic, geographic, and etnobotanical features using machine learning?
* **Specific Question 1 (SQ1):** What is the performance (Accuracy, Macro F1-score) of Multinomial Logistic Regression, Random Forest, and XGBoost in classifying plant growth habits?
* **Specific Question 2 (SQ2):** Which features (Family, Genus, Department, or Etnobotanical Uses) contribute the most to the predictions of the models?
* **Specific Question 3 (SQ3):** What feature representation strategy (Taxonomic only, Taxonomic + Geographic, or Full Features with TF-IDF encoded text) yields the highest predictive performance?
* **Specific Question 4 (SQ4):** Are there statistically significant differences in model performance when predicting different growth habits (Tree, Shrub, Herb, Liana)?

---

## 3. The Reproducibility Stack
To address the widespread reproducibility crisis in ecological machine learning (where only a small fraction of papers are fully replicable), this project implements the **five-layer reproducibility pyramid**:

| Layer | Tool | Purpose | Configuration & Details |
|---|---|---|---|
| **Code** | **Git + GitHub** | Version control of all code and documents | Private repository: `unmsm-research-methods-valeriogomez` |
| **Data** | **DVC** | Data lineage and remote storage | Tracks `data/processed_dataset.csv` using pointer files. Data remote configured on Google Drive. |
| **Experiments** | **MLflow** | Experiment tracking and parameter logging | Automatically logs hyperparameters, metrics (Accuracy, Macro F1), and confusion matrices. |
| **Environment** | **Docker** | Containerization of dependencies | Python 3.11-slim base image containing pinned libraries (`pandas==2.2.1`, `scikit-learn==1.4.1.post1`, etc.). |
| **Compute** | **Local / Google Colab** | CPU/GPU execution environment | CPU-only container execution is sufficient for local runs. |

### Strict Reproducibility Standards:
* **Frozen Random Seeds**: To prevent stochastic variations in data partitioning and model initialization, the random seed is locked at `SEED=42` across Python, NumPy, and Scikit-learn.
* **No Data Leakage**: Data splitting (70% training, 15% validation, 15% testing) is performed *before* any preprocessing, scaling, or TF-IDF fitting.

---

## 4. Repository Structure
The repository follows the mandatory Capstone project layout:

```text
unmsm-research-methods-valeriogomez/
├── README.md                      # Project overview + run instructions
├── Dockerfile                     # Isolated Python 3.11 environment
├── requirements.txt               # Pinned Python package dependencies
├── data/                          # Data folder (tracked via DVC)
│   ├── .gitkeep
│   ├── dataset-pending in spanish.xlsx.dvc  # Raw Excel pointer
│   └── processed_dataset.csv.dvc            # Cleaned data pointer
│
├── 01_paradigm/                   # Session 1: Research Paradigm
│   └── paradigm_justification.md
├── 02_method/                     # Session 2: Method Fit
│   └── method_fit_matrix.md
├── 03_protocol/                   # Sessions 3, 13, 15: Research Protocols
│   ├── protocol_v0.1.md           # Outline (active)
│   ├── protocol_v1.0.md           # Draft (pending)
│   └── protocol_v2.0.md           # Final (pending)
│
├── 04_literature/                 # Session 4: Literature Review & Gap Analysis
│   ├── systematic_review.md       # Mini systematic review (10 papers)
│   ├── selected_references.md     # 7 specific core articles & PDFs
│   ├── prisma_diagram.png         # PRISMA flow diagram
│   └── gap_analysis.md            # Gap matrix
│
├── 05_pipeline/                   # Session 5: Reproducible pipeline (Jupyter/source)
│   ├── notebook.ipynb             # (pending)
│   └── src/                       # (pending)
├── 06_repro_audit/                # Session 6: External paper audit
│   └── reproducibility_audit.md   # (pending)
├── 07_model_card/                 # Session 7: Card documentation
│   ├── model_card.md              # (pending)
│   └── datasheet.md               # (pending)
│
├── reflections/                   # Reflective logs
│   └── reflective_log.md          # Unit I entry complete
└── mlruns/                        # MLflow training logs
```

---

## 5. Quick Start (Stranger Test)

To reproduce the study results from scratch, follow these commands.

### Prerequisites
* Docker installed on your machine.
* Git installed on your machine.

### Step 1: Clone the Repository
```bash
git clone https://github.com/ValerioGomez/unmsm-research-methods-valeriogomez.git
cd unmsm-research-methods-valeriogomez
```

### Step 2: Retrieve the Dataset via DVC
The dataset is versioned using DVC to avoid pushing large binaries to GitHub. To download the dataset:
```bash
dvc pull
```
*Note: This downloads the original Excel files and processed CSVs from the configured Google Drive remote.*

### Step 3: Build the Docker Image
Build the container using the pinned Python 3.11 environment:
```bash
docker build -t unmsm-project .
```

### Step 4: Run the Environment
Run the container interactively, mounting the local directory to persist outputs:
```bash
docker run -it --rm -v "$(pwd):/project" unmsm-project
```

To run a Jupyter Notebook workspace locally inside the container (mapped to port `8888`):
```bash
docker run -it --rm -p 8888:8888 -v "$(pwd):/project" unmsm-project jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```

---

## 6. Repository Index (Weekly Deliverables Tracker)

| Session | Deliverable Document | Status |
| :--- | :--- | :--- |
| **Session 1** | [Paradigm Justification](01_paradigm/paradigm_justification.md) | ✅ Active |
| **Session 2** | [Method Fit Matrix](02_method/method_fit_matrix.md) | ✅ Active |
| **Session 3** | [Protocol v0.1 Outline](03_protocol/protocol_v0.1.md) | ✅ Active |
| **Session 4** | [Systematic Review](04_literature/systematic_review.md) & [PRISMA Flowchart](04_literature/prisma_diagram.png) | ✅ Active |
| **Session 4** | [Gap Analysis Matrix](04_literature/gap_analysis.md) | ✅ Active |
| **Session 4** | [Selected Reference Summaries](04_literature/selected_references.md) | ✅ Active |
| **Session 5** | Reproducible ML Pipeline (DVC & MLflow) | ⏳ Pending |
| **Session 6** | Published ML Paper Reproducibility Audit | ⏳ Pending |
| **Session 7** | Model Card & Dataset Datasheet | ⏳ Pending |
| **Session 9** | Belmont Principles Ethics Protocol | ⏳ Pending |
| **Session 10** | FAIR Data Management Plan | ⏳ Pending |
| **Session 11** | Bias Audit Report (AIF360/Fairlearn) | ⏳ Pending |
| **Session 12** | Personal AI Use Policy & Retracted Paper Analysis | ⏳ Pending |
| **Session 13** | Complete Research Protocol v1.0 | ⏳ Pending |
| **Session 14** | Peer Reviews | ⏳ Pending |
| **Session 15** | Final Protocol v2.0 & Response Table | ⏳ Pending |
| **Reflections** | [Unit I Reflective Log](reflections/reflective_log.md) | ✅ Active |
