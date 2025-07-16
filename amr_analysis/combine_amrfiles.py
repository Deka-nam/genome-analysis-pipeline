#If you want to see presence/absence patterns across isolates, use this script to combine separate .tsv files generated for each sample.

import pandas as pd
import glob

# Set the path to your TSV files
file_path = "*.tsv"

# Initialize an empty dataframe
merged_df = pd.DataFrame()

# Loop over each TSV file
for file in glob.glob(file_path):
    # Extract sample identifier from file name
    sample_id = file.split('/')[-1].split('.')[0]  # Assuming the sample name is in the file name

    # Read the TSV file into a pandas DataFrame
    df = pd.read_csv(file, sep="\t")

    # Check if the required column exists
    if '% Identity to reference sequence' in df.columns:
        # Select relevant columns
        df = df[['Subclass', 'Gene symbol', 'Sequence name', 'Accession of closest sequence', '% Identity to reference sequence']] #You can select other relevant columns too according to your interest

        # Rename '% Identity to reference sequence' column to reflect the sample identifier
        df = df.rename(columns={'% Identity to reference sequence': sample_id})

        # Merge with the existing dataframe (on common columns)
        if merged_df.empty:
            merged_df = df  # If first file, initialize the merged_df
        else:
            merged_df = pd.merge(merged_df, df, on=['Subclass', 'Gene symbol', 'Sequence name', 'Accession of closest sequence'], how='outer')
    else:
        print(f"Column '% Identity to reference sequence' not found in file: {file}")

# Save the merged dataframe to a new file
merged_df.to_csv("amr_combined.tsv", sep="\t", index=False) #I wanted a .csv file to work in my local computer 

print("AMR files successfully combined.")

