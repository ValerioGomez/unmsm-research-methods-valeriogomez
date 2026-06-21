# Reproducible Machine Learning Study on Customer Churn Prediction

## UNMSM — Doctoral Program in Deep Technologies
**Course:** Research Methods & Scientific Integrity in AI  
**Instructor:** Dr. Loveleen Gaur  
**Author:** Valerio Gómez  
**Project Title:** Establishing a Reproducible Predictive Architecture for Customer Churn in Subscription Services  

---

## 1. Project Description
This study implements a robust, reproducible machine learning pipeline to predict customer churn in a subscription-based service. Utilizing a dataset containing behavioral and demographic metrics from 1,000 customers (such as age, monthly spending, subscription length, and support interactions), we train multiple classification models to identify customers at risk of cancellation.

Crucially, the project is structured to demonstrate adherence to the **Reproducibility Pyramid** across its five distinct dimensions:
1. **Code:** Full history versioned in Git.
2. **Data:** Dataset versioned with DVC.
3. **Environment:** Containerized using Docker (`python:3.11-slim` base image) and locked with pinned `requirements.txt`.
4. **Experiments:** Automated logging of runs, hyperparameter configurations, metrics, and models using MLflow.
5. **Compute:** CPU-bound pipeline designed to execute identically locally or in a cloud workbench.

---

## 2. Directory Structure
The repository is organized following the course Capstone Project Brief:

```text
unmsm-research-methods-valeriogomez/
├── README.md                      # Project overview & replication guide
├── Dockerfile                     # Environment containerization recipe
├── requirements.txt               # Pinned dependencies
├── .gitignore                     # Git ignore rules
├── .dvc/                          # DVC internal configuration
├── data/                          # Data files (tracked by DVC, ignored by Git)
│   ├── .gitkeep
│   └── customer_churn.csv.dvc     # DVC data pointer file
│
├── 01_paradigm/                   # Session 1: Research paradigm justification
│   └── paradigm_justification.md
├── 02_method/                     # Session 2: Methodology fit matrix
│   └── method_fit_matrix.md
├── 03_protocol/                   # Session 3: Initial and final research protocols
│   └── protocol_v0.1.md
├── 04_literature/                 # Session 4: Systematic review & PRISMA
│   ├── systematic_review.md
│   ├── prisma_diagram.png         # PRISMA flow diagram
│   └── gap_analysis.md            # Identified gaps in current literature
│
├── 05_pipeline/                   # Session 5: Reproducible training notebook
│   ├── notebook.ipynb             # Execution notebook
│   └── src/
│       └── .gitkeep
├── 06_repro_audit/                # Session 6: Reproducibility audit on external papers
│   └── reproducibility_audit.md
├── 07_model_card/                 # Session 7: Documentation standards
│   ├── model_card.md              # Model card (Mitchell et al., 2019)
│   └── datasheet.md               # Dataset datasheet (Gebru et al., 2021)
│
├── reflections/                   # Course reflective logs
│   └── reflective_log.md          # Reflective journal (What -> So What -> Now What)
└── mlruns/                        # Local MLflow experiments store (Git ignored)
```

---

## 3. Reproduction Instructions

To reproduce the study results exactly as presented:

### Prerequisites
Make sure you have [Docker](https://docs.docker.com/get-docker/) installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/ValerioGomez/unmsm-research-methods-valeriogomez.git
cd unmsm-research-methods-valeriogomez
```

### Step 2: Set Up Data Version Control (DVC)
Since the dataset is stored in a DVC remote (or mock local remote storage), run:
```bash
dvc pull
```
This fetches the raw data `data/customer_churn.csv` from storage using the pointer `data/customer_churn.csv.dvc`.

### Step 3: Build the Docker Container
Create the locked runtime environment:
```bash
docker build -t unmsm-project .
```

### Step 4: Run the Environment
Launch the container and access its bash shell, mounting your working directory to preserve output files:
```bash
docker run -it --rm -v "$(pwd):/project" -p 8888:8888 -p 5000:5000 unmsm-project
```

### Step 5: Execute the Pipeline
Inside the Docker container shell:
- **To run JupyterLab:**
  ```bash
  jupyter lab --ip=0.0.0.0 --no-browser --allow-root
  ```
- **To view logged MLflow experiments:**
  ```bash
  mlflow server --host 0.0.0.0 --port 5000
  ```
- Open `05_pipeline/notebook.ipynb` and execute all cells. This notebook sets random seeds, splits data before scaling, trains classification models, and records outputs to MLflow.
