import soccerdata as sd
import pandas as pd

fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=[1819,1920,2021,2122,2223,2324])


season_stats = fbref.read_team_season_stats(stat_type='standard')

print(season_stats)


