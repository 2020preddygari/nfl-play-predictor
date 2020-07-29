import numpy as np
import pandas as pd

rushing_offense_rankings = ['SEA', 'BAL', 'LA', 'CAR', 'NE', 'NO', 'TEN', 'HOU', 'BUF', 'DAL', 'CHI', 'DEN', 'SF', 'CLE', 'LAC', 'KC', 'WAS', 'MIA', 'JAX', 'IND', 'CIN', 'GB', 'DET', 'NYG', 'OAK', 'NYJ', 'ATL', 'PHI', 'TB', 'MIN', 'PIT', 'ARI']
passing_offense_rankings = ['TB', 'PIT', 'KC', 'ATL', 'LA', 'IND', 'PHI', 'NE', 'GB', 'LAC', 'NYG', 'NO', 'MIN', 'CLE', 'SF', 'CAR', 'HOU', 'OAK', 'DEN', 'DET', 'CHI', 'BAL', 'DAL', 'CIN', 'NYJ', 'JAX', 'SEA', 'WAS', 'TEN', 'MIA', 'BUF', 'ARI']
rushing_defense_rankings = ['CHI', 'NO', 'HOU', 'BAL', 'DAL', 'PIT', 'PHI', 'IND', 'LAC', 'DET', 'NE', 'CAR', 'SEA', 'SF', 'MIN', 'BUF', 'WAS', 'TEN', 'JAX', 'NYG', 'DEN', 'GB', 'LA', 'TB', 'ATL', 'NYJ', 'KC', 'CLE', 'CIN', 'OAK', 'MIA', 'ARI']
passing_defense_rankings = ['BUF', 'JAX', 'MIN', 'ARI', 'BAL', 'TEN', 'CHI', 'DET', 'LAC', 'PIT', 'SF', 'GB', 'DAL', 'LA', 'WAS', 'IND', 'SEA', 'CAR', 'OAK', 'DEN', 'MIA', 'NE', 'NYG', 'NYJ', 'CLE', 'TB', 'ATL', 'HOU', 'NO', 'PHI', 'KC', 'CIN']


dataset = pd.read_csv("pbp-2018.csv")
dataset.sort_values(by=["GameId", "Quarter", "Minute", "Second"], inplace=True, ascending=False)
dataset["id"] = [x for x in range(0, dataset.shape[0])]
dataset.set_index("id", inplace=True)
dataset.columns = [c.lower() for c in dataset]
dataset_test = dataset.drop(["unnamed: 10", "unnamed: 12", "unnamed: 16", "unnamed: 17", "challenger", "ismeasurement", "nextscore", "description", "teamwin", "seasonyear", "isrush", "ispass", "isincomplete", "istouchdown", "passtype", "issack", "ischallenge", "ischallengereversed", "isfumble", "ispenalty", "istwopointconversionsuccessful", "rushdirection", "isinterception", "yardlinefixed", "yardlinedirection", "ispenaltyaccepted", "penaltyteam", "isnoplay", "penaltytype", "penaltyyards", "yards"], axis=1)


