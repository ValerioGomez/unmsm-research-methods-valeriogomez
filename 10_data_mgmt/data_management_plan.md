# Data Management Plan (DMP): FAIR Principles Application

**Project:** Growth Habit Classification of Peruvian Amazonian Medicinal Plants using Machine Learning  
**Author:** Valerio Gomez  
**Course:** Research Methods & Scientific Integrity in AI (UNMSM)

---

## 1. FAIR Principles Implementation

This DMP details the policies and technical controls applied to ensure that the dataset and model artifacts adhere to the **FAIR Data Principles**:

### Findable
* **DVC Versioning:** Every dataset state is captured as a unique hash value inside `.dvc` tracking files (e.g., `data/processed_dataset.csv.dvc`). These metadata files are checked into Git, providing a complete, historical lineage of data versions.
* **Rich Metadata:** We document the dataset attributes, provenance, and collection methodology in a standardized **Datasheet** (Session 7), ensuring that future researchers can understand what the dataset represents.

### Accessible
* **DVC Remotes:** The actual binary dataset (CSV/XLSX) is stored in a secure Google Drive DVC remote. Anyone with access to the repository can retrieve the exact files using standard command-line tools (`dvc pull`), avoiding the need for manual file transfers.
* **Open Formats:** Raw data is stored in standard spreadsheet format (.xlsx), and processed data is saved as plain text comma-separated values (.csv), which can be opened on any platform without proprietary software.

### Interoperable
* **Standard Schemas:** The processed data uses standardized botanical and taxonomic schemas: Family, Genus, and Scientific Name follow the standard APG IV (Angiosperm Phylogeny Group) nomenclature.
* **Geographic Encoding:** Geographical distribution departments use the official ISO 3166-2:PE two-letter administrative codes (e.g., LOR, MAD, UCA, or standard AM, AY, HU, LO, MD, PU, SM, UC).

### Reusable
* **Clear Documentation:** The dataset's preprocessing and modeling pipeline is detailed in a Jupyter Notebook (`05_pipeline/notebook.ipynb`), demonstrating how to load, clean, and use the data.
* **Licensing:** Code is licensed under the MIT License. The dataset remains under the academic custody of IIAP and is restricted to non-commercial replication uses.

---

## 2. Long-term Preservation & Storage Plan

* **DVC Google Drive Remote:** Holds the raw and intermediate dataset hashes.
* **GitHub Repository:** Acts as the primary preservation registry for code, pipeline configs, and `.dvc` metadata pointers.
* **Local Backups:** Master copies of the original IIAP datasets are maintained in physical offline storage by IIAP researchers to prevent data loss.
