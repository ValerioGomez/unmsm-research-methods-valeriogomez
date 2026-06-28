# Research Protocol v0.1: Growth Habit Classification of Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

## 1. Project Title
**Growth Habit Classification of Amazonian Medicinal Plants using Machine Learning**

---

## 2. Problem Statement
Identifying a plant's growth habit (Tree, Shrub, Herb, Liana) in the field requires specialized botanical expertise and significant time, which slows down ecological studies and forestry cataloging. An automated machine learning model capable of predicting the growth habit from taxonomic data, geographic distribution, and traditional etnobotanical uses will accelerate field identification and assist in auditing and curating large biodiversity databases like that of the IIAP.

---

## 3. Research Questions
* **General Question (GQ):** Is it possible to predict the growth habit (Tree, Shrub, Herb, Liana) of Amazonian medicinal plants based on taxonomic, geographic, and etnobotanical features using machine learning?
* **Specific Question 1 (SQ1):** What is the performance (Accuracy, Macro F1-score) of Multinomial Logistic Regression, Random Forest, and XGBoost in classifying plant growth habits?
* **Specific Question 2 (SQ2):** Which features (Family, Genus, Department, or Etnobotanical Uses) contribute the most to the predictions of the models?
* **Specific Question 3 (SQ3):** What feature representation strategy (Taxonomic only, Taxonomic + Geographic, or Full Features with TF-IDF encoded text) yields the highest predictive performance?
* **Specific Question 4 (SQ4):** Are there statistically significant differences in model performance when predicting different growth habits (Tree, Shrub, Herb, Liana)?

---

## 4. Research Objectives
* **General Objective:** Develop and evaluate a reproducible machine learning pipeline to classify the growth habit of Peruvian Amazonian medicinal plants.
* **Specific Objectives:**
  1. Compare the classification performance of Logistic Regression, Random Forest, and XGBoost using cross-validation.
  2. Estimate feature importances to determine the botanical and geographical drivers of growth habits.
  3. Evaluate three feature engineering strategies to determine the value of adding etnobotanical text features.
  4. Perform an error analysis per growth habit category to identify classification boundary weaknesses.

---

## 5. Literature Review Summary
Existing literature on botanical classification using machine learning mostly relies on leaf image recognition, remote sensing, or genomic data, leaving textual and taxonomic database records underutilized. This study addresses this gap by applying natural language processing (TF-IDF) to etnobotanical descriptions (uses) combined with tabular taxonomic metadata to classify growth habits.

---

## 6. Quasi-Experimental Design
This study employs a quasi-experimental, quantitative design using retrospective observational data from the IIAP (~1,028 records). The dataset will be divided into stratified training (70%), validation (15%), and testing (15%) sets using a fixed random seed (`SEED=42`) to simulate experimental controls, comparing parametric (Logistic Regression) and non-parametric ensemble models (Random Forest, XGBoost).

---

## 7. Data Management Plan Outline
The raw dataset will be stored locally and versioned using Data Version Control (DVC) linked to Google Drive storage, preventing raw CSV uploads to GitHub. Cleaned datasets, model metadata, and training metrics will be logged automatically using MLflow to ensure complete data and model lineage.

---

## 8. Ethical Considerations
This research strictly adheres to the Nagoya Protocol on Access and Benefit-sharing by acknowledging the public custody of the IIAP over the dataset. Since the data represents traditional etnobotanical knowledge collected from indigenous and local communities over 18 years, the research maintains academic transparency, does not claim intellectual property over the traditional uses, and attributes all data origin to the original communities and the IIAP.

---

## 9. Project Schedule / Timeline
* **Weeks 1–2:** Paradigm justification, method fit matrix formulation, and initial protocol drafting.
* **Weeks 3–4:** Systematic literature review, gap analysis, and repository restructuring.
* **Weeks 5–6:** Data preparation, pipeline implementation (Git, DVC, MLflow, Docker), and reproducibility audit of published botanical models.
* **Weeks 7–8:** Model training, evaluation, bias/fairness audit across plant classes, Datasheet/Model Card generation, and final report delivery.

---

## 10. Expected Results and Impact
We expect to deliver a fully containerized (Docker), reproducible machine learning pipeline achieving a Macro F1-score of over 0.70. The resulting models and feature importance rankings will provide ecological insights into how plant growth habits relate to taxonomic families and traditional applications in the Peruvian Amazon.
