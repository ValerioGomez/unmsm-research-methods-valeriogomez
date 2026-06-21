# Model Card – Churn Prediction Classifier

## Model Details
- **Name:** ChurnPred-GB (Gradient Boosting selected via recall)
- **Version:** 1.0
- **Type:** Gradient Boosting Classifier (scikit-learn)
- **Date:** June 2026
- **Owners:** Valerio Gomez, UNMSM Research Methods project

## Intended Use
- **Primary use:** Predict customer churn probability for a subscription service to prioritize retention actions.
- **Out-of-scope uses:** Not for individual credit scoring, hiring, or medical diagnosis. Not for automated decisions without human review.

## Training Data
- **Dataset:** Subscription churn dataset (n=1,000)
- **Features:** Age, Gender, Monthly Spending, Subscription Duration, Support Interactions
- **Target:** Churn (0/1)
- **Preprocessing:** Train/test split (80/20, stratified), StandardScaler fitted on training data only.

## Evaluation
- **Metrics:** Accuracy, Recall, F1 (to be filled after training)
- **Test set:** 200 samples, same distribution as training.
- **Fairness:** Disparate impact by gender to be evaluated in Session 11 using AIF360.

## Ethical Considerations
- **Bias:** Gender is a protected attribute; the model might learn historical biases. Mitigation will be explored.
- **Privacy:** The dataset contains no personally identifiable information (PII). The client ID is removed before modeling.

## Limitations
- Small, single-source dataset; may not generalize.
- Binary gender representation excludes non-binary individuals.
- Does not capture contextual reasons for churn (e.g., economic factors).

## Citation & Reproducibility
- Full pipeline: https://github.com/ValerioGomez/unmsm-research-methods-valeriogomez
- Run: `git clone … && dvc pull && docker build -t churn-pred . && docker run …`
