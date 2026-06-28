# Paradigm Justification: Growth Habit Classification of Amazonian Medicinal Plants

**UNMSM – Doctoral Program in Deep Technologies**  
**Course:** Research Methods & Scientific Integrity in AI  
**Author:** Valerio Gomez  
**Instructor:** Dr. Loveleen Gaur  

---

## 1. Ontological Stance: Realism
Ontology addresses the nature of reality. In this research, we adopt a **realist ontology**, which asserts that an objective reality exists independent of human cognition, language, or social construction. 

In the botanical domain of this study, the **growth habit** of a medicinal plant—classified as a Tree, Shrub, Herb, or Liana—is a physical, morphological, and ecological fact. A plant’s growth habit is determined by genetic characteristics, cellular structures (such as woodiness), and environmental adaptations. Whether an observer labels a plant or not, its physical stature, growth rate, and biological features remain constant. The data collected by the Instituto de Investigaciones de la Amazonía Peruana (IIAP) represents empirical measurements and classifications of these real-world objects. Therefore, the reality under study is objective, structured, and external to the researcher.

## 2. Epistemological Stance: Positivism
Epistemology concerns how knowledge is acquired and validated. This study resides firmly within a **positivist epistemology**. Positivism argues that valid knowledge can only be obtained through empirical observation, measurement, and the search for regularities or causal relationships.

In this project, we seek to discover patterns linking a plant's taxonomic taxonomy (Family, Genus), geographic distribution (Departments), and traditional uses to its growth habit. By representing these variables as discrete numeric vectors, we assume that the relationship between taxonomy and growth habit can be modeled mathematically. The researcher remains detached from the object of study, avoiding subjective interpretation. The validity of the predictive models is verified using standardized, objective statistical metrics, specifically **Accuracy** and **Macro F1-score**, ensuring that the findings are replicable by any independent investigator using the same dataset and code.

## 3. Methodological Stance: Hypothetical-Deductive & Quantitative
Consistent with realism and positivism, the methodology of this study is **hypothetical-deductive** and strictly quantitative. 

We begin with the theoretical premise that botanical taxonomy and geographic distribution are statistically correlated with growth habits due to evolutionary adaptations. We formulate a hypothesis: *A machine learning model can predict the growth habit of an Amazonian medicinal plant with statistically significant accuracy based on its taxonomic classification, geographic distribution, and traditional etnobotanical uses.* To test this, we design a quantitative comparison of three supervised classification algorithms:
1. **Multinomial Logistic Regression** (as a parametric baseline)
2. **Random Forest** (as a non-parametric bagging ensemble)
3. **XGBoost** (as a non-parametric boosting ensemble)

By comparing their performance, we deductively determine which algorithm best captures the underlying patterns of the data, using mathematical criteria (such as hyperparameters optimized via grid search and validated through cross-validation).

## 4. Rejection of Alternative Paradigms
To confirm the suitability of positivism, alternative paradigms were evaluated and rejected:
* **Constructivism/Interpretivism**: This paradigm assumes that reality is multiple, subjective, and socially constructed. Since growth habit is a biological and physical property of the flora, it cannot be redefined by social consensus or subjective views. An interpretivist framework would fail to produce a reproducible predictive model.
* **Critical Theory**: This paradigm focuses on exposing power structures and driving social emancipation. While the preservation of traditional Amazonian knowledge has social and ethical value, the primary research objective of this capstone is technical and predictive.
* **Pragmatismo**: Although pragmatism allows mixing qualitative and quantitative methods to solve practical problems, this study is entirely quantitative in its data structures, modeling, and evaluation metrics, making a pure positivist framework more academically rigorous.
