# Paradigm Justification Statement

**Project:** A Reproducible and Fairness-Aware Machine Learning Pipeline for Customer Churn Prediction  
**Author:** Valerio Gomez  
**Date:** June 2026

## 1. Topic & Context
Customer churn is a critical business problem for subscription-based services. The provided dataset contains 1,000 records with demographic and behavioral attributes, and the goal is to predict which customers will cancel. The dominant approach in industry is to apply supervised classification models to identify at-risk customers and trigger retention actions.

## 2. Preliminary Research Question
*Which classification model yields the highest recall for churn prediction while maintaining reproducibility and fairness across gender groups?*

## 3. Chosen Paradigm: Positivism
I adopt a **positivist** research paradigm. Positivism assumes that reality exists objectively and can be measured. In this study, customer churn is an observable event (0/1), and the relationships between predictors (age, spending, support interactions) and churn can be quantified, tested, and generalized through statistical and machine learning models. The evaluation metrics (accuracy, recall, F1) provide objective evidence of model performance.

## 4. Justification
- The research question is empirical: it asks which model performs best under a defined metric.
- The data is structured, numerical, and collected independently of the researcher.
- The analysis relies on hypothesis testing (e.g., "Random Forest outperforms Logistic Regression in recall") and replicable computational experiments.
- Reproducibility – a core requirement of the course – is naturally aligned with positivist assumptions: fixed environments, versioned data, and deterministic seeds enable anyone to obtain the same results.

## 5. Implications
- **Methodology:** I will conduct a controlled computational experiment comparing multiple classifiers using the same train/test split and random seed.
- **Bias audit:** While the paradigm is positivist, I will later integrate a fairness audit (Session 11) to measure disparate impact across gender, acknowledging that "objective" models can still produce ethically unequal outcomes.
- **Generalizability:** The findings will be tied to this specific dataset; I will not overclaim external validity, but the reproducibility pipeline ensures the internal validity is verifiable.

## 6. One Doubt / Tension
Although I chose positivism, the reasons *why* a customer churns (e.g., poor service experience, perceived value) are inherently interpretivist. The dataset only captures behavioral traces, not the customer's lived experience. This tension will remain unresolved in the project, and I will acknowledge it in the ethics protocol.
