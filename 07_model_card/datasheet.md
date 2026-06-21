# Datasheet for Subscription Churn Dataset

## Motivation
- **Purpose:** To support predictive modeling research on customer churn.
- **Creator:** Synthetic dataset provided for the UNMSM course (based on realistic patterns).

## Composition
- **Instances:** 1,000
- **Features:** 6 (Age, Gender, Monthly Spend, Subscription Duration, Support Interactions, Churn label)
- **Missing data:** None
- **Sensitive attributes:** Gender (binary)

## Collection Process
- Data was generated synthetically or sampled from historical records (exact provenance not specified but assumed to be from a subscription business).
- No direct human subjects were involved in the creation of this dataset.

## Preprocessing
- No cleaning necessary; ready to model after scaling.
- Train/test split stratified by target to preserve class balance.

## Uses
- This dataset is suitable for classification tasks and fairness auditing.
- Not suitable for making real-world decisions about individuals without additional context.

## Distribution
- Available via DVC remote (Google Drive) with the repository.
- License: For academic use only, as per course guidelines.

## Maintenance
- The dataset will not be updated. Version controlled with DVC; any changes would produce a new commit and a new `.dvc` pointer.
