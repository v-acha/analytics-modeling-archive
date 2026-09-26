# Clinical Disease Genetic Mutations Analysis
![image](https://github.com/user-attachments/assets/19fe066a-852c-47a8-b361-39fe6f948426)

This project involves the analysis of a dataset containing genetic mutations and their clinical significance. The dataset was sourced from ClinVar, a repository of expert-curated genetic disease information. The goal is to identify and analyze harmful mutations, focusing on their genetic positions, mutation values, and associated diseases. This analysis will provide insights into the potential impacts of these mutations on health and their relevance to clinical and therapeutic research.

## Objective
The primary objectives of this project are:

1. To identify and extract harmful mutations from the dataset.
2. To categorize these mutations based on their clinical significance.
3. To analyze the most common mutation values and their associated diseases.
4. To provide strategic insights and recommendations for leveraging this information in a genetic disease data center.

## Data
### Data Source
The data was obtained from the instructor-modified at this link: https://drive.google.com/file/d/1Zps0YssoJbZHrn6iLte2RDLlgruhAX1s/view?usp=sharing 

It contains records of genetic mutations, including information such as `gene name`, `mutation ID number`, `mutation position`, `mutation value`, `clinical significance`, and `implicated disease`.

### Data Extraction Steps
- Load Data: The data was loaded into a pandas DataFrame for analysis.
- Filter Out Header Row: The first row, which contained column headers repeated as data, was removed.
- Group Clinical Significance: Clinical significance values were grouped into broader categories to simplify analysis.

### Clinical Significance Grouping
The clinical significance values were grouped into broader categories as follows:

- **`Uncertain_significance`**: Includes 'Uncertain_significance', 'Conflicting_interpretations_of_pathogenicity', and variations thereof.
- **`Benign/Likely_benign`**: Includes 'Benign', 'Likely_benign', 'Benign/Likely_benign', and variations thereof.
- **`Pathogenic/Likely_pathogenic`**: Includes 'Pathogenic', 'Likely_pathogenic', 'Pathogenic/Likely_pathogenic', and variations thereof.
- **`Other`**: Includes 'risk_factor', 'association', 'drug_response', 'Affects', 'other', and variations thereof.
- **`Not_Given`**: Includes records with 'Not_Given' as the clinical significance.

## Tableau
**Dashboards:** https://public.tableau.com/app/profile/vanellsa.acha/viz/HarmfulMutations/AllGeneticMutations 

In Tableau, three dashboards were created to visualize harmful genetic mutations. The first dashboard displayed a network diagram illustrating the relationships between the top 20 mutation values, their associated diseases, and gene names, with nodes representing genes and diseases, and edges indicating mutation values. The second dashboard showcased the top 15 mutations using a color-coded dot plot, with red representing pathogenic mutations and blue representing likely pathogenic mutations, highlighting the prevalence and clinical significance of each mutation. The third dashboard provided detailed information about each mutation, including mutation values, associated diseases, and gene names, enabling an in-depth exploration of the genetic data. These interactive visualizations allowed for a comprehensive understanding of the genetic mutations and their clinical impacts.

## Results
Total Harmful Mutations Found
- A total of 19,474 harmful mutations were identified in the dataset.
- The most common mutation values and their counts are as follows:
(G->A: 1797 occurrences, C->T: 1504 occurrences, G->T: 573 occurrences, T->C: 475 occurrences, A->G: 470 occurrences, C->A: 458 occurrences, G->C: 383 occurrences, C->G: 351 occurrences, T->G: 227 occurrences, T->A: 223 occurrences, A->T: 221 occurrences, A->C: 216 occurrences, CT->C: 133 occurrences, TG->T: 127 occurrences, TC->T: 115 occurrences)

## Deliverables
- The final result was compiled into a dataframe and saved to a csv file containing Pathogenic/Likely_Pathogenics.
- A summary paper highlighting any notable specifics and the total number of harmful mutations identified within the file.

## Assumptions: 
No prior medical knowledge was assumed; the analysis was based solely on the data and accompanying documentation.
Data Parsing: Customized to handle the unique format of the provided file.
