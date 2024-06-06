import soccerdata as sd
import pandas as pd

# Retrieve the data for the big 5 european leagues in the last 5 years - from Fbref webiste
fbref = sd.FBref(leagues=['Big 5 European Leagues Combined'], seasons=[ '2223'])

read_team_matchups = fbref.read_schedule()

read_team_matchups.to_csv('match_schedule_2223.csv')
