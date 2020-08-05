import pandas as pd
from data_conversion import convert_data

# NFL team rankings for 2018 season
RUSHING_OFFENSE_RANKINGS_2018 = ['SEA', 'BAL', 'LA', 'CAR', 'NE', 'NO', 'TEN', 'HOU', 'BUF', 'DAL', 'CHI', 'DEN', 'SF', 'CLE', 'LAC', 'KC', 'WAS', 'MIA', 'JAX', 'IND', 'CIN', 'GB', 'DET', 'NYG', 'OAK', 'NYJ', 'ATL', 'PHI', 'TB', 'MIN', 'PIT', 'ARI']
PASSING_OFFENSE_RANKINGS_2018 = ['TB', 'PIT', 'KC', 'ATL', 'LA', 'IND', 'PHI', 'NE', 'GB', 'LAC', 'NYG', 'NO', 'MIN', 'CLE', 'SF', 'CAR', 'HOU', 'OAK', 'DEN', 'DET', 'CHI', 'BAL', 'DAL', 'CIN', 'NYJ', 'JAX', 'SEA', 'WAS', 'TEN', 'MIA', 'BUF', 'ARI']
RUSHING_DEFENSE_RANKINGS_2018 = ['CHI', 'NO', 'HOU', 'BAL', 'DAL', 'PIT', 'PHI', 'IND', 'LAC', 'DET', 'NE', 'CAR', 'SEA', 'SF', 'MIN', 'BUF', 'WAS', 'TEN', 'JAX', 'NYG', 'DEN', 'GB', 'LA', 'TB', 'ATL', 'NYJ', 'KC', 'CLE', 'CIN', 'OAK', 'MIA', 'ARI']
PASSING_DEFENSE_RANKINGS_2018 = ['BUF', 'JAX', 'MIN', 'ARI', 'BAL', 'TEN', 'CHI', 'DET', 'LAC', 'PIT', 'SF', 'GB', 'DAL', 'LA', 'WAS', 'IND', 'SEA', 'CAR', 'OAK', 'DEN', 'MIA', 'NE', 'NYG', 'NYJ', 'CLE', 'TB', 'ATL', 'HOU', 'NO', 'PHI', 'KC', 'CIN']

RUSHING_OFFENSE_RANKINGS_2019 = ["BAL", "SF", "TEN", "SEA", "DAL", "MIN", "IND", "BUF", "HOU", "ARI", "PHI", "CLE", "OAK", "CAR", "GB", "NO", "JAX", "NE", "NYG", "DEN", "DET", "WAS", "KC", "TB", "CIN", "LA", "CHI", "LAC", "PIT", "ATL", "NYJ", "MIA"]
PASSING_OFFENSE_RANKINGS_2019 = ["TB", "DAL", "ATL", "LA", "KC", "LAC", "NO", "NE", "OAK", "DET", "PHI", "MIA", "SF", "SEA", "HOU", "JAX", "GB", "NYG", "CIN", "CAR", "TEN", "CLE", "MIN", "ARI", "CHI", "BUF", "BAL", "DEN", "NYJ", "IND", "PIT", "WAS"]
RUSHING_DEFENSE_RANKINGS_2019 = ["TB", "NYJ", "PHI", "NO", "BAL", "NE", "IND", "OAK", "CHI", "BUF", "DAL", "TEN", "MIN", "PIT", "ATL", "DEN", "SF", "LAC", "LA", "NYG", "DET", "SEA", "GB", "ARI", "HOU", "KC", "MIA", "JAX", "CAR", "CLE", "WAS", "CIN"]
PASSING_DEFENSE_RANKINGS_2019 = ["SF", "NE", "PIT", "BUF", "LAC", "BAL", "CLE", "KC", "CHI", "DAL", "DEN", "LA", "CAR", "GB", "MIN", "JAX", "NYJ", "WAS", "PHI", "NO", "CIN", "ATL", "IND", "TEN", "OAK", "MIA", "SEA", "NYG", "HOU", "TB", "ARI", "DET"]

train_data = convert_data(PASSING_OFFENSE_RANKINGS_2018, PASSING_DEFENSE_RANKINGS_2018, RUSHING_OFFENSE_RANKINGS_2018, RUSHING_DEFENSE_RANKINGS_2018, "pbp-2018.csv")
test_data = convert_data(PASSING_OFFENSE_RANKINGS_2019, PASSING_DEFENSE_RANKINGS_2019, RUSHING_OFFENSE_RANKINGS_2019, RUSHING_DEFENSE_RANKINGS_2019, "pbp-2019.csv")
