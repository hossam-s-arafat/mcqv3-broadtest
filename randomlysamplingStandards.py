# Let's first load the CSV file to understand its structure and contents
import pandas as pd

# Load the CSV file
file_path = "./European History Data Model.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Checking the unique values in the 'Domain' column to identify the units
unique_domains = df['Domain'].unique()

# Counting the number of unique domains (units)
num_unique_domains = len(unique_domains)

# Displaying the unique domains and their count
print(unique_domains, num_unique_domains)

# Adjusting the approach based on the new requirement:
# 50 unique rows randomly sampled without the same row being selected twice.
# It's okay if the same L3 Standard appears in different rows. (Unique to AP EU History)
# The sampling should still be evenly distributed across all `num_unique_domains` units.

# Calculate the number of rows to sample from each unit to ensure even distribution
rows_per_unit = 50 // num_unique_domains
print(rows_per_unit)

# Initialize an empty DataFrame for the selected rows
selected_rows_df = pd.DataFrame()

# Loop through each unique domain to select rows
for domain in unique_domains:
    # Filter the dataframe for the current domain
    domain_df = df[df['Domain'] == domain]
    
    # Randomly select rows from this unit
    # If a unit has fewer rows than rows_per_unit, select all rows from that unit
    sampled_rows = domain_df.sample(n=min(rows_per_unit, len(domain_df)), random_state=1, replace=False)
    
    # Append the sampled rows to the selected_rows_df
    selected_rows_df = pd.concat([selected_rows_df, sampled_rows], ignore_index=True)

# If the total selected rows are less than 50 due to rounding, sample additional rows randomly from the entire dataset
additional_rows_needed = 50 - len(selected_rows_df)
print("Additional rows needed", additional_rows_needed)
if additional_rows_needed > 0:
    # Sample additional rows without replacement from the entire dataset
    additional_rows = df.sample(n=additional_rows_needed, random_state=2, replace=False)
    selected_rows_df = pd.concat([selected_rows_df, additional_rows], ignore_index=True)

# Ensuring we have 50 unique rows selected
selected_rows_df = selected_rows_df.sample(n=50, random_state=3).reset_index(drop=True)

# Display the first few rows of the selected data and the total count to confirm
print(selected_rows_df.head(), len(selected_rows_df))


selected_rows_df.to_csv("AP EUHist Standards-BroadTest1.csv")
