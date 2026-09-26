## VCF file description

VCF is a text file format which contains meta-information lines, a header line, and then data lines each containing information about a position in the genome. The format also can contain genotype information on samples for each position.

### **The VCF specification:**

Description summarized from (4.1) document here: https://drive.google.com/file/d/1lx9yHdlcqmU_OlHiTUXKC_LQDqYBypH_/view 

- Instructor-modified "clinvar_final.txt" at this link: https://drive.google.com/file/d/1Zps0YssoJbZHrn6iLte2RDLlgruhAX1s/view?usp=sharing 

- This file was modified to be not exactly the same as 'standard' .vcf file to test your data parsing skills. This is a large file so do NOT upload it into your github repo!

### Fixed Fields:

There are 8 fixed fields per record. All data lines are **tab-delimited**. In all cases, missing values are specified with a dot (‘.’). 

1. `CHROM` - chromosome number
2. `POS` - position DNA nuceleotide count (bases) along the chromosome
3. `ID` - The unique identifier for each mutation
4. `REF` - reference base(s)
5. `ALT` - alternate base(s)
6. `FILTER` - filter status
7. `QUAL` - quality
8. `INFO` - a semicolon-separated series of keys with values in the format: <key>=<data>

### Applicable INFO field specifications

- `GENEINFO` = <Gene name>
- `CLNSIG` =  <Clinical significance>
- `CLNDN` = <Disease name>


### Sample ClinVar data (vcf file format - not exactly the same as the file to download!)

- `##fileformat=VCFv4.1`
- `##fileDate=2019-03-19`
- `##source=ClinVar`
- `##reference=GRCh38`

#CHROM | POS    | ID          | REF | ALT | QUAL | FILTER | INFO
-------|--------|-------------|-----|-----|------|--------|-----------------------------------------
1      | 949523 | rs786201005 | C   | T   | .    | .      | GENEINFO=ISG15;CLNSIG=5
1      | 949696 | rs672601345 | C   | CG  | .    | .      | GENEINFO=ISG15;CLNSIG=5;CLNDN=Cancer
1      | 949739 | rs672601312 | G   | T   | .    | .      | GENEINFO=ISG15;CLNDBN=Cancer
1      | 955597 | rs115173026 | G   | T   | .    | .      | GENEINFO=AGRN;CLNSIG=2;CLNDN=Cancer
1      | 955619 | rs201073369 | G   | C   | .    | .      | GENEINFO=AGG;CLNDN=Heart_dis
1      | 957640 | rs6657048   | C   | T   | .    | .      | GENEINFO=AGG;CLNSIG=3;CLNDN=Heart_dis
1      | 976059 | rs544749044 | C   | T   | .    | .      | GENEINFO=AGG;CLNSIG=0;CLNDN=Heart_dis

## Parsing Strategy

- **Parsing Strategy:** Given the modifications to the standard VCF format, a customized data parsing approach was implemented. Each line was printed and examined to ensure the correct recovery of the fields of interest.
- **Filtering Criteria:** Focus was placed on extracting lines that contained mutation data relevant to our needs, specifically those classified as harmful.
- **Handling Missing Data:** Missing values in the dataset were replaced with 'Not_Given'. The frequency of 'Not_Given' entries in the CLNSIG column was calculated using the value_counts() function from the pandas library.
- **Definition of Harmful Mutations:** For the purposes of this analysis, harmful mutations were defined based on their clinical significance as indicated in the dataset documentation and associated metadata.