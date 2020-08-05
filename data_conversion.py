import pandas as pd


def convert_data(pass_offense_rankings, pass_defense_rankings, rush_offense_rankings, rush_defense_rankings, filename):
    # Inputs data and trims unnecessary data
    dataset = pd.read_csv(filename)
    dataset.columns = [c.lower() for c in dataset]
    dataset_test = dataset.drop(["seriesfirstdown", "unnamed: 10", "unnamed: 12", "unnamed: 16", "unnamed: 17", "challenger", "ismeasurement", "nextscore", "description", "teamwin", "seasonyear", "isrush", "ispass", "isincomplete", "istouchdown", "passtype", "issack", "ischallenge", "ischallengereversed", "isfumble", "ispenalty", "istwopointconversionsuccessful", "rushdirection", "isinterception", "yardlinefixed", "yardlinedirection", "ispenaltyaccepted", "penaltyteam", "isnoplay", "penaltytype", "penaltyyards", "yards"], axis=1)

    pass_offense = []
    pass_defense = []
    rush_offense = []
    rush_defense = []
    null_set = dataset_test.notnull()
    for i in range(0, dataset_test.shape[0]):
        # converts the quarter, minute, and second time measurements into half and seconds passed in half
        seconds = 900 - (dataset_test.loc[i, "minute"] * 60 + dataset_test.loc[i, "second"])
        if dataset_test.loc[i, "quarter"] % 2 == 0:
            seconds += 900
        dataset_test.loc[i, "second"] = seconds
        dataset_test.loc[i, "quarter"] = (dataset_test.loc[i, "quarter"] + 1) // 2

        # Delets kickoffs and dead plays.  Makes playtypes more general
        if dataset_test.loc[i, "playtype"] == "NO PLAY" or dataset_test.loc[i, "playtype"] == "KICK OFF":
            dataset_test = dataset_test.drop([i])
            continue
        if dataset_test.loc[i, "playtype"] == "SCRAMBLE" or dataset_test.loc[i, "playtype"] == "SACK":
            dataset_test.loc[i, "playtype"] = "PASS"

        # Checks whether the play is not time stoppage and creates columns for the offense and defense team rankings
        if null_set.loc[i, "offenseteam"] and null_set.loc[i, "formation"] and null_set.loc[i, "playtype"]:
            pass_offense.append(pass_offense_rankings.index(dataset_test.loc[i, "offenseteam"]) + 1)
            pass_defense.append(pass_defense_rankings.index(dataset_test.loc[i, "defenseteam"]) + 1)
            rush_offense.append(rush_offense_rankings.index(dataset_test.loc[i, "offenseteam"]) + 1)
            rush_defense.append(rush_defense_rankings.index(dataset_test.loc[i, "defenseteam"]) + 1)

    # Adds rankings columns to DataFrame and touches up time section of DataFrame
    dataset_test = dataset_test.dropna()
    dataset_test["passoffense"] = pass_offense
    dataset_test["passdefense"] = pass_defense
    dataset_test["rushoffense"] = rush_offense
    dataset_test["rushdefense"] = rush_defense
    dataset_test = dataset_test.drop(["minute"], axis=1)
    dataset_test = dataset_test.rename(columns={"quarter": "half"})

    # Drops duplicates and time stops (timeouts, quarter endings, etc.)
    # Sorts the data chronologically
    dataset_test = dataset_test.drop_duplicates(keep="last")
    dataset_test = dataset_test.sort_values(["gameid", "half", "second"])
    dataset_test = dataset_test.reset_index(drop=True)
    return dataset_test




