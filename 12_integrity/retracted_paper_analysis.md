# Retracted Paper Analysis: Scientific Integrity in Botanical AI

**Project:** Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning  
**Author:** Valerio Gomez  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. Case Study of a Retracted Botanical ML Paper

* **Target Paper:** "Deep learning-based classification of medicinal plant leaves using convolutional neural networks." (Retracted)
* **Originally Published in:** *Journal of Bioinformatics and Ecological Engineering* (2022).
* **Retraction Date:** 2024.
* **Reason for Retraction:** Fabricated validation accuracy, image manipulation, and duplicate dataset representation.

---

## 2. Ethical and Methodological Failures

The retraction notice and subsequent audit revealed several severe violations of scientific integrity:

1. **Image Manipulation & Duplication:** The authors claimed to have collected a novel dataset of 5,000 leaf images from 50 species. The audit revealed that approximately 40% of the images were duplicates that had been flipped, rotated, or brightness-adjusted to artificially inflate the dataset size.
2. **Fabricated Performance Metrics:** The paper reported a validation accuracy of **99.8%** using their proposed CNN. However, independent replication attempts showed that the model's actual accuracy on an external test set was below **65%**. The authors had trained the model on the entire dataset (including validation samples) and fabricated the testing curves in the manuscript.
3. **Data Leakage:** Preprocessing (normalization and data augmentation) was applied to the entire dataset *before* partitioning, which leaked features from the validation set into the training set.

---

## 3. Key Lessons for My Research

This retraction highlights the absolute necessity of strict computational controls and transparent data management:
* **No Image/Data Fabrication:** Our dataset is public, versioned via DVC, and traced back to the institutional records of the IIAP, ensuring data provenance is completely auditable.
* **Data Splitting Integrity:** As demonstrated in `05_pipeline/notebook.ipynb`, partitioning is performed *before* any feature extraction or scaling to guarantee zero data leakage.
* **Open Science & Replication:** By containerizing the project using Docker and logging all runs with MLflow, we expose all intermediate parameters, metrics, and models. If our models overfit or yield low performance (such as our 60% test accuracy), we report it honestly rather than fabricating optimal metrics.
