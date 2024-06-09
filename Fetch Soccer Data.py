import soccerdata as sd
import pandas as pd

# Retrieve the data for the big 5 european leagues in the last 5 years - from Fbref webiste
fbref = sd.FBref(leagues=['Big 5 European Leagues Combined'], seasons=['1920', '2021', '2122'])

read_team_leagues = fbref.read_team_season_stats(stat_type='standard')
read_team_stats = fbref.read_team_season_stats(stat_type='shooting')

read_team_leagues.to_csv('stand_data.csv', index=False)
read_team_stats.to_csv('shooting_data.csv', index=False)

