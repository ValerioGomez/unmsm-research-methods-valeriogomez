# Establishing a Reproducible Predictive Architecture for Customer Churn in Subscription Services

## Overview
This repository contains the complete research and implementation for the project **"Establishing a Reproducible Predictive Architecture for Customer Churn in Subscription Services"**, developed for the Research Methods and Scientific Integrity course at UNMSM.

**Author:** Valerio Gomez  
**Affiliation:** Universidad Nacional Mayor de San Marcos (UNMSM)  

---

## Repository Index and Status (Up to Session 07)

This directory structure indexes the active research components. Clicking on each link will navigate to the corresponding document or code asset.

### 🔬 Session 01: Paradigm
* [Paradigm Justification](01_paradigm/paradigm_justification.md) - Theoretical and philosophical justification of the research paradigm (Ontology, Epistemology, and Methodology).

### 📊 Session 02: Method
* [Method Fit Matrix](02_method/method_fit_matrix.md) - Analysis of methodological alignment with research questions and objective.

### 📋 Sessions 03, 13, 15: Protocol
* [Protocol v0.1 (Initial)](03_protocol/protocol_v0.1.md) - Initial draft of the research protocol.
* [Protocol v1.0 (Mid-term)](03_protocol/protocol_v1.0.md) - Refined protocol incorporating design and data collection strategies.
* [Protocol v2.0 (Final)](03_protocol/protocol_v2.0.md) - Finalized protocol with analytical plan and scheduling.

### 📚 Session 04: Literature
* [Systematic Review](04_literature/systematic_review.md) - Systematic search strategy and preliminary literature mapping.
* [PRISMA Flow Diagram](04_literature/prisma_diagram.png) - Visual representation of search exclusions.
* [Gap Analysis](04_literature/gap_analysis.md) - Identification of research gaps in current customer churn models.

### ⚙️ Session 05: Pipeline
* [Reproducible Training Notebook](05_pipeline/notebook.ipynb) - Jupyter Notebook executing data preprocessing and model evaluation.

### 🔍 Session 06: Reproducibility Audit
* [Reproducibility Audit](06_repro_audit/reproducibility_audit.md) - Technical audit evaluating the reproducibility of an external ML paper.

### 🏷️ Session 07: Documentation Standards
* [Model Card](07_model_card/model_card.md) - Standardized reporting on the trained classification model (Mitchell et al., 2019).
* [Datasheet](07_model_card/datasheet.md) - Detailed documentation of dataset metadata, collection, and bias checks (Gebru et al., 2021).

### ⚖️ Session 09: Ethics
* [Ethics Protocol](09_ethics/ethics_protocol.md) - *(Pending / Empty)*

### 🗄️ Session 10: Data Management
* [Data Management Plan](10_data_mgmt/data_management_plan.md) - *(Pending / Empty)*

### 🛡️ Session 11: Bias Audit
* [Bias Audit Report](11_bias_audit/bias_audit_report.md) - *(Pending / Empty)*

### 🏛️ Session 12: Integrity
* [Retracted Paper Analysis](12_integrity/retracted_paper_analysis.md) - *(Pending / Empty)*
* [AI Use Policy](12_integrity/ai_use_policy.md) - *(Pending / Empty)*

### 📝 Reflections
* [Reflective Log](reflections/reflective_log.md) - Course journal structured using Rolfe's *What? So What? Now What?* framework.

---

## Environment & Replication Instructions

To replicate the environment and ensure reproducibility, refer to the following instructions:

### Prerequisites
- Install [Docker](https://docs.docker.com/) on your local machine.

### Environment Setup
1. Build the Docker container:
   ```bash
   docker build -t unmsm-research-env .
   ```
2. Run the environment interactively:
   ```bash
   docker run -it --rm -v "$(pwd):/app" unmsm-research-env
   ```
