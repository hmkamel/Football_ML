import pandas as pd
import numpy as np

# data = pd.read_csv('shooting_data.csv')

# other_columns = list(data.columns[2:])

# grouped_data = data.groupby('team')

# team_totals = grouped_data[other_columns].mean()

# team_totals = team_totals.reset_index()

# team_totals.to_csv('shooting_data_groupteam.csv',index=False)

# print(team_totals)


# THIS SECTION COMBINES THE DATA FROM STANADRD & SHOOTING TEAM STATS WITH THE MATCH SCHEUDLE
# USING A LEFT JOIN WITH MATCHES MATCHES.HOME_TEAM = STANDARD.TEAM = SHOOTING.TEAM

# Load the "match schedule" data
match_data = pd.read_csv("matches_with_stats.csv")

# Load the "team stats" data
team_data = pd.read_csv("shooting_data_groupteam.csv")

# Define wildcard pattern for team names (adjust as needed)
wildcard_pattern = "%"

# Convert team_data['team'] to a list for string concatenation
team_list = team_data['team'].to_frame()

merged_data = match_data.merge(team_data.copy(), how='left', left_on="home_team", right_on="team", suffixes=("_home_shots", "_away_shots"))
merged_data = merged_data.merge(team_data.copy(), how='left', left_on="away_team", right_on="team", suffixes=("_home_shots", "_away_shots"))

# Rename columns for clarity (optional)
merged_data.rename(columns={"stats": "home_shots"}, inplace=True)
merged_data.rename(columns={"stats_away": "away_shots"}, inplace=True)

# Save the result to a new CSV file (optional)
merged_data.to_csv("matches_with_stats.csv", index=False)

# Print the result (optional)
print(merged_data)