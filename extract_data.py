import pandas as pd

# Read the CSV file
data = pd.read_csv('my_data.csv')  # Replace 'your_data.csv' with your actual filename

# Define a function to extract year and team
def extract_info(url):
  # Check if url is a string (assuming only URLs or numbers are present)
  if isinstance(url, str):
    parts = url.split('-')
    # Ensure at least 3 parts for valid URL format
    if len(parts) >= 3:
      # Extract year (assuming format YYYY-YYYY)
      year = parts[1]
      # Extract team (part before "-Stats")
      team = parts[-2]
      return year, team
    else:
      # Handle invalid URLs with less than 3 parts (return None for both)
      return None, None
  else:
    # Handle non-string URLs (return None for both)
    return None, None

# Apply the function with error handling
data['year'], data['team'] = zip(*data['url'].apply(extract_info))  # Using unpacking

# Save the modified DataFrame to a new CSV (optional)
data.to_csv('data_with_year_team.csv', index=False)  # Replace filename if needed

print("Year and Team information extracted!")
