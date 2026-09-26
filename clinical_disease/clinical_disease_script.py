# Load the data
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Define a function to parse the INFO field into a dictionary
def parse_info(info_string):
    info_dict = {}
    for part in info_string.split(';'):
        if '=' in part:
            key, value = part.split('=', 2)
            info_dict[key] = value
        else:
            info_dict[part] = 'Not_Given'
    return info_dict

# Placeholder for the extracted data
data = []

# Read the file line by line
with open('clinvar_final.txt', 'r') as file:
    for line in file:
        if not line.startswith('#'):
            parts = line.strip().split('\t')
            if len(parts) < 8:
                continue  # Skip incomplete lines

            chrom, pos, mutation_id, ref, alt, info_string = parts[0], parts[1], parts[2], parts[3], parts[4], parts[7]
            
            # Parsing the INFO field using function
            info = parse_info(info_string)
            
            # Extracting necessary fields
            gene_name = info.get('GENEINFO', 'Not_Given').split(':')[1] if 'GENEINFO' in info else 'Not_Given'
            clnsig = info.get('CLNSIG', 'Not_Given')
            disease = info.get('CLNDN', 'Not_Given').replace('_', ' ').replace('|', ', ')
            mutation_value = f"{ref}->{alt}"
            mutation_position = f"{chrom}:{pos}"
            
            # Append the data
            data.append([
                gene_name,
                mutation_id,
                mutation_position,
                mutation_value,
                clnsig,
                disease
            ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Gene Name',
    'Mutation ID Number',
    'Mutation Position',
    'Mutation Value',
    'Clinical Significance',
    'Disease Implicated'
])
# Remove the first row containing headers
df = df.iloc[1:]

#GROUPING MUTATIONS 
from collections import defaultdict

# Define the mapping dictionary
mapping_groups = {
    'Uncertain_significance': [
        'Uncertain_significance',
        'Uncertain_significance,_risk_factor'
    ],
    'Benign/Likely_benign': [
        'Likely_benign',
        'Benign',
        'Benign/Likely_benign',
        'Benign/Likely_benign,_risk_factor',
        'Benign/Likely_benign,_protective',
        'Benign/Likely_benign,_other',
        'Benign/Likely_benign,_association',
        'Benign,_drug_response',
        'Benign,_other'
    ],
    'Pathogenic': [
        'Pathogenic',
        'Pathogenic,_risk_factor',
        'Pathogenic,_other',
        'Pathogenic,_Affects',
        'Pathogenic,_association,_protective',
        'Pathogenic,_protective'
    ],
    'Likely_pathogenic': [
        'Likely_pathogenic',
        'Pathogenic/Likely_pathogenic',
        'Pathogenic/Likely_pathogenic,_other',
        'Pathogenic/Likely_pathogenic,_risk_factor',
        'Likely_pathogenic,_risk_factor',
        'Likely_pathogenic,_other',
        'Likely_pathogenic,_association'
    ],

    'Conflicting_interpretations_of_pathogenicity': ['Conflicting_interpretations_of_pathogenicity',
        'Conflicting_interpretations_of_pathogenicity,_risk_factor',
        'Conflicting_interpretations_of_pathogenicity,_other',
        'Conflicting_interpretations_of_pathogenicity,_Affects,_other',
        'Conflicting_interpretations_of_pathogenicity,_protective',
        'Conflicting_interpretations_of_pathogenicity,_Affects',
        'Conflicting_interpretations_of_pathogenicity,_association',
        'Conflicting_interpretations_of_pathogenicity,_Affects,_association,_drug_response,_other',
        'Conflicting_interpretations_of_pathogenicity,_other,_risk_factor',],
    'Other': [
        'risk_factor',
        'association',
        'drug_response',
        'Affects',
        'other',
        'Affects,_risk_factor'
    ],
    'Not_Given': [
        'Not_Given'
    ]
}

# Reverse the mapping dictionary to create a direct mapping
direct_mapping = defaultdict(lambda: 'Other')
for key, values in mapping_groups.items():
    for value in values:
        direct_mapping[value] = key

# Apply the mapping to the DataFrame
df['Clinical Significance Grouped'] = df['Clinical Significance'].map(direct_mapping)

# Reorder the columns to place 'Clinical Significance Grouped' next to 'Clinical Significance'
column_order = [
    'Gene Name', 'Mutation ID Number', 'Mutation Position', 'Mutation Value', 
    'Clinical Significance', 'Clinical Significance Grouped', 'Disease Implicated'
]
df = df[column_order]