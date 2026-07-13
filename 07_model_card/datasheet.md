# Datasheet: Peruvian Amazonian Medicinal Plants Dataset

This datasheet follows the template proposed by Gebru et al. (2021) to document the dataset compiled by the Instituto de Investigaciones de la Amazonía Peruana (IIAP) and utilized in this classification study.

## 1. Motivation
* **Why was the dataset created?** The dataset was compiled to document the biodiversity and traditional etnobotanical uses of medicinal plants across three regions of the Peruvian Amazon (Loreto, Madre de Dios, Ucayali), preserving traditional indigenous knowledge and supporting ecological conservation.
* **Who created the dataset?** Researchers and botanical experts at the **Instituto de Investigaciones de la Amazonía Peruana (IIAP)**.
* **Who funded the creation?** The IIAP and public science grants from the Peruvian government.

## 2. Composition
* **What do the instances represent?** Each instance represents a unique cataloged medicinal plant specimen with taxonomic details, geographical department codes, common names, traditional medicinal uses, and ecological growth habit.
* **How many instances are there?** The raw excel sheet (`dataset-init.xlsx`) contains 2,089 rows, which clean down to **1,028 unique records** after removing empty/unlabeled entries. The subset `dataset.csv` contains a clean sample of **100 rows** used for pipeline testing.
* **What are the features?**
  - `Family` (categorical)
  - `Genus` (categorical)
  - `Scientific Name` (text)
  - `Distribution` (multivalued categorical department codes: e.g., LO = Loreto, MD = Madre de Dios, UC = Ucayali)
  - `Common Name` (text)
  - `Uses` (text, traditional ethnobotanical uses in Spanish)
  - `Habit` (target categorical variable: Tree, Shrub, Herb)
* **Are there sensitive attributes?** No human subjects are involved. The etnobotanical uses represent traditional collective knowledge, which is protected under national and international intellectual property frameworks (Nagoya Protocol).

## 3. Collection Process
* **How was the data collected?** Collected through field observations, botanical surveys, and interviews with local indigenous communities over an 18-year period.
* **Who was involved?** Botanists, ethnobotanists, and community elders.
* **Over what timeframe was the data collected?** Retrospective collection over approximately 18 years (up to 2026).

## 4. Preprocessing & Cleaning
* **What cleaning was performed?**
  - Dropped empty rows and unconfirmed records.
  - Standardized column names and strings.
  - Stripped leading/trailing whitespace from target habits.
  - Extracted genus and family structures to resolve inconsistencies.
* **Was the raw data saved?** Yes, both `dataset-init.xlsx` (raw) and `dataset.csv` (processed subset) are versioned via DVC to maintain lineage.

## 5. Uses
* **What is the dataset suitable for?** Classification tasks (predicting growth habit `Habit` from categorical and text inputs), natural language processing (text vectorization of etnobotanical uses), and taxonomic analysis.
* **What is it NOT suitable for?** Commercial pharmaceutical bioprospecting without prior informed consent of the communities.

## 6. Distribution & Maintenance
* **How is it distributed?** Versioned with DVC and stored in a Google Drive remote. Pointer files (.dvc) are tracked in the GitHub repository.
* **Who maintains the dataset?** Valerio Gomez (for this repository version); IIAP for the master registry.
