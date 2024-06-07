import pandas as pd

# Define the input and output filenames
input_file = 'stand_data_mod.csv'
output_file = 'stand_data_mod_clean.csv'  # Replace with your desired output filename

# Read the data from the CSV file
df = pd.read_csv(input_file)

# Remove the last 6 characters from the 'team' column (assuming text strings)
df['team'] = df['team'].str[:-6]

# Save the DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Data saved to: {output_file}")
