
"""
Created on Fri Feb 24 23:09:10 2023

@author: saransh.s
"""



 
import os
import pandas as pd
pd.set_option("display.max_columns", None)

#from urllib.request import urlopen

import soccerdata as sd

stats = ['shooting','passing','passing_types','goal_shot_creation','defense','possession','misc','keeper_adv']
#Directory
os.chdir(r"D:\Personal\Football Analysis\Event Data\Team Analysis\Arsenal\Arsenal_stats\data")

fbref = sd.FBref(leagues="ENG-Premier League", seasons=2022)

#team_season_stats = fbref.read_team_season_stats(stat_type="passing")

for i in stats:
    player_season_stats = fbref.read_player_season_stats(stat_type=i)
    player_season_stats.to_csv(f"player_{i}.csv")    

