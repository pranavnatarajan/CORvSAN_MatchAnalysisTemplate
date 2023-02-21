  """
  This contains the code for the Match Analysis Template
  As in main_analysis.ipynb, bar sanity checks.
  Opta data obtained from FootballReference.com
  using the ScraperFC module on python.

  Author: Pranav Natarajan
  email: pn12@uw.edu
  """

# installing ScraperFC to get match report data from FBref
# if not installed on working instance
try:
  import ScraperFC as sfc
except:
  # running CLI command to install module
  %pip install ScraperFC
  # import module
  import ScraperFC as sfc

# loading required packages
import numpy as np
import pandas as pd
import traceback


if __name__ == "__main__":

  # getting Brasileirao Serié A match data between Corinthians (H)
  # vs Santos (A)
  # on June 25 2022.
  match_link=\
    r"https://fbref.com/en/matches/4bf12498/Corinthians-Santos-June-25-2022-Serie-A"

  # Initialize the FBRef scraper
  scraper = sfc.FBRef()
  try:
      match = scraper.scrape_match(link=match_link)
  except:
      # Catch and print any exceptions.
      traceback.print_exc()
  finally:
      # Again, make sure to close the scraper when you're done
      scraper.close()

  # getting home player stats
  cor_stats = match["Home Player Stats"].values[0][0]
  # getting away player stats
  san_stats = match["Away Player Stats"].values[0][0]

  ### GETTING MATCH STATISTICS BY TYPE

  ## 1. SUMMARY STATISTICS

  # getting the summary data
  # for the home team
  cor_stats_summary = cor_stats["Summary"]
  # ONLY HERE: get the number of players
  num_players_cor = cor_stats_summary.shape[0]
  # remove last row of dataframe
  cor_stats_summary = cor_stats_summary.iloc[0:num_players_cor-1, :]
  # create Team column
  cor_stats_summary["Team"] = "COR"

  # for the away team
  san_stats_summary = san_stats["Summary"]
  # ONLY HERE: get the number of players
  num_players_san = san_stats_summary.shape[0]
  # remove last row of dataframe
  san_stats_summary = san_stats_summary.iloc[0:num_players_san-1, :]
  # create Team column
  san_stats_summary["Team"] = "SAN"

  # concatenating the two dataframes, ignoring index so that it resets
  stats_summary = pd.concat([cor_stats_summary, san_stats_summary],
                            ignore_index=True)

  # removing multi_indexing in columns
  stats_summary.columns = ["-".join(cname) for cname in stats_summary.columns]
  # saving to csv
  stats_summary.to_csv("stats_summary.csv", index=None)

  ## 2. PASSING

  # for the home team
  cor_stats_passing = cor_stats["Passing"]
  # removing final row
  cor_stats_passing = cor_stats_passing.iloc[0:num_players_cor-1, :]
  # creating Team column
  cor_stats_passing["Team"] = "COR"

  # for the away team
  san_stats_passing = san_stats["Passing"]
  # removing final row
  san_stats_passing = san_stats_passing.iloc[0:num_players_san-1, :]
  # creating Team column
  san_stats_passing["Team"] = "SAN"

  # concatenating dataframes
  stats_passing = pd.concat([cor_stats_passing, san_stats_passing],
                            ignore_index=True)

  # removing multi-indexing in columns
  stats_passing.columns = ["-".join(cname) for cname in stats_passing.columns]
  # saving to csv
  stats_passing.to_csv("stats_passing.csv", index=None)

  ## 3. PASS TYPES

  # Getting the Pass Types data
  # for the home team
  cor_stats_pass_types = cor_stats["Pass Types"]
  # removing final row
  cor_stats_pass_types = cor_stats_pass_types.iloc[0:num_players_cor-1, :]
  # creating Team column
  cor_stats_pass_types["Team"] = "COR"

  # for the away team
  san_stats_pass_types = san_stats["Pass Types"]
  # removing final row
  san_stats_pass_types = san_stats_pass_types.iloc[0:num_players_san-1, :]
  # creating Team column
  san_stats_pass_types["Team"] = "SAN"


  # concatenating dataframes
  stats_pass_types = pd.concat([cor_stats_pass_types, san_stats_pass_types],
                            ignore_index=True)

  # removing multi-indexing in columns
  stats_pass_types.columns =\
     ["-".join(cname) for cname in stats_pass_types.columns]

  # saving to csv
  stats_pass_types.to_csv("stats_pass_types.csv", index=None)

  ## 4. DEFENSE

  # Getting the Defense data
  # for the home team
  cor_stats_defense = cor_stats["Defense"]
  # removing final row
  cor_stats_defense = cor_stats_defense.iloc[0:num_players_cor-1, :]
  # creating Team column
  cor_stats_defense["Team"] = "COR"

  # for the away team
  san_stats_defense = san_stats["Defense"]
  # removing final row
  san_stats_defense = san_stats_defense.iloc[0:num_players_san-1, :]
  # creating Team column
  san_stats_defense["Team"] = "SAN"

  # concatenating dataframes
  stats_defense = pd.concat([cor_stats_defense, san_stats_defense],
                            ignore_index=True)

  # removing multi-indexing in columns
  stats_defense.columns = ["-".join(cname) for cname in stats_defense.columns]

  # saving to csv
  stats_defense.to_csv("stats_defense.csv", index=None)

  ## 5. POSSESSION

  # Getting the Possession data
  # for the home team
  cor_stats_pos = cor_stats["Possession"]
  # removing final row
  cor_stats_pos = cor_stats_pos.iloc[0:num_players_cor-1, :]
  # creating Team column
  cor_stats_pos["Team"] = "COR"

  # for the away team
  san_stats_pos = san_stats["Possession"]
  # removing final row
  san_stats_pos = san_stats_pos.iloc[0:num_players_san-1, :]
  # creating Team column
  san_stats_pos["Team"] = "SAN"

  # concatenating dataframes
  stats_pos = pd.concat([cor_stats_pos, san_stats_pos],
                            ignore_index=True)

  # removing multi-indexing in columns
  stats_pos.columns = ["-".join(cname) for cname in stats_pos.columns]

  # saving to csv
  stats_pos.to_csv("stats_pos.csv", index="None")

  ## 6. MISCELLANEOUS

  # Getting the Miscellaneous data
  # for the home team
  cor_stats_misc = cor_stats["Misc"]
  # removing final row
  cor_stats_misc = cor_stats_misc.iloc[0:num_players_cor-1, :]
  # creating Team column
  cor_stats_misc["Team"] = "COR"

  # for the away team
  san_stats_misc = san_stats["Misc"]
  # removing final row
  san_stats_misc = san_stats_misc.iloc[0:num_players_san-1, :]
  # creating Team column
  san_stats_misc["Team"] = "SAN"


  # concatenating dataframes
  stats_misc = pd.concat([cor_stats_misc, san_stats_misc],
                            ignore_index=True)

  # removing multi-indexing in columns
  stats_misc.columns = ["-".join(cname) for cname in stats_misc.columns]

  # saving to csv
  stats_misc.to_csv("stats_misc.csv", index=None)

  ## 7. GOALKEEPERS

  # loading the goalkeeper dataframes
  cor_stats_GK = cor_stats["GK"]
  san_stats_GK = san_stats["GK"]

  # adding the team columns to each dataframe
  cor_stats_GK["Team"] = "COR"
  san_stats_GK["Team"] = "SAN"

  # concatenating the dataframes
  stats_GK = pd.concat([cor_stats_GK, san_stats_GK],
                        ignore_index=True)

  # removing multi-indexing in columns
  stats_GK.columns = ["-".join(cname) for cname in stats_GK.columns]

  # saving to csv
  stats_GK.to_csv("stats_GK.csv", index=None)

  ## 8. TEAM SHEETS

  # getting teamsheets
  cor_teamsheet = cor_stats["Team Sheet"]
  san_teamsheet = san_stats["Team Sheet"]
  # adding the team column to maintain data uniformity
  cor_teamsheet["Team"] = "COR"
  san_teamsheet["Team"] = "SAN"
  # getting the starting 11
  cor_teamsheet_s11 = cor_teamsheet.iloc[0:11, :]
  san_teamsheet_s11 = san_teamsheet.iloc[0:11, :]
  # getting the bench
  cor_teamsheet_bench = cor_teamsheet.iloc[12:, :]
  san_teamsheet_bench = san_teamsheet.iloc[12:, :]

  # removing multi-indexing in columns
  cor_teamsheet_s11.columns =\
     ["-".join(cname) for cname in cor_teamsheet_s11.columns]
  cor_teamsheet_bench.columns =\
     ["-".join(cname) for cname in cor_teamsheet_bench.columns]
  san_teamsheet_s11.columns =\
     ["-".join(cname) for cname in san_teamsheet_s11.columns]
  san_teamsheet_bench.columns =\
     ["-".join(cname) for cname in san_teamsheet_bench.columns]

  # saving to csvs
  cor_teamsheet_s11.to_csv("cor_teamsheet_s11.csv", index=None)
  san_teamsheet_s11.to_csv("san_teamsheet_s11.csv", index=None)
  cor_teamsheet_bench.to_csv("cor_teamsheet_bench.csv", index=None)
  san_teamsheet_bench.to_csv("san_teamsheet_bench.csv", index=None)

  ### GETTING SHOT DATA

  shots = match["Shots"].values[0][0].copy()

  # renaming Team names
  shots[('Unnamed: 2_level_0','Squad')].replace({"Santos":"SAN",
                                            "Corinthians":"COR"},
                                        inplace=True)

  # changing column names to remove indexing
  shots.columns = ["_".join(cname) for cname in shots.columns]

  # replacing half and full time added times to numeric values
  shots["Unnamed: 0_level_0_Minute"] = shots["Unnamed: 0_level_0_Minute"].\
  replace(["45+1", "90+5"], ["46", "95"])

  # creating initial and final state of game row tuples
  xg_SAN_to_append = {"Unnamed: 0_level_0_Minute":[0, 97],
  "Unnamed: 1_level_0_Player":[None, None],
  "Unnamed: 2_level_0_Squad":["SAN", "SAN"],
  "Unnamed: 3_level_0_xG":[0, 0],
  "Unnamed: 4_level_0_PSxG":[0, 0],
  "Unnamed: 5_level_0_Outcome":[None, None],
  "Unnamed: 6_level_0_Distance":[None, None],
  "Unnamed: 7_level_0_Body Part": [None, None],
  "Unnamed: 8_level_0_Notes": ["Start First Half", "End of Game"],
  "SCA 1_Player": [None, None],
  "SCA 1_Event": [None, None],
  "SCA 2_Player": [None, None],
  "SCA 2_Event": [None, None]}

  xg_COR_to_append = {"Unnamed: 0_level_0_Minute":[0, 97],
  "Unnamed: 1_level_0_Player":[None, None],
  "Unnamed: 2_level_0_Squad":["COR", "COR"],
  "Unnamed: 3_level_0_xG":[0, 0],
  "Unnamed: 4_level_0_PSxG":[0, 0],
  "Unnamed: 5_level_0_Outcome":[None, None],
  "Unnamed: 6_level_0_Distance":[None, None],
  "Unnamed: 7_level_0_Body Part": [None, None],
  "Unnamed: 8_level_0_Notes": ["Start First Half", "End of Game"],
  "SCA 1_Player": [None, None],
  "SCA 1_Event": [None, None],
  "SCA 2_Player": [None, None],
  "SCA 2_Event": [None, None]}

  # coercing these dictionaries to dataframes to concatenate later
  xg_SAN_to_append = pd.DataFrame.from_dict(xg_SAN_to_append)
  xg_COR_to_append = pd.DataFrame.from_dict(xg_COR_to_append)

  # adding the initial and final xG states to the table
  shots1 = pd.concat([xg_SAN_to_append, xg_COR_to_append, shots]).copy()
  # making minutes as an integer column
  shots1["Unnamed: 0_level_0_Minute"] = shots1["Unnamed: 0_level_0_Minute"].\
                                                            astype(np.int8)
  # sorting by time ASC
  shots1 = shots1.sort_values(by="Unnamed: 0_level_0_Minute")
  # saving to CSV for use in Tableau
  shots1.to_csv("shots.csv")

  ### GETTING SCOUTING REPORTS

  # For Angelo Borges
  player_link = r"https://fbref.com/en/players/737945d9/Angelo-Borges"
  # Initialize the FBRef scraper
  scraper = sfc.FBRef()
  try:
      player_borges = scraper.\
        complete_report_from_player_link(player_link=player_link)
  except:
      # Catch and print any exceptions.
      traceback.print_exc()
  finally:
      # Again, make sure to close the scraper when you're done
      scraper.close()

  # For Adson
  player_link = r"https://fbref.com/en/players/eda38706/Adson"
  # Initialize the FBRef scraper
  scraper = sfc.FBRef()
  try:
      player_adson = scraper.\
        complete_report_from_player_link(player_link=player_link)
  except:
      # Catch and print any exceptions.
      traceback.print_exc()
  finally:
      # Again, make sure to close the scraper when you're done
      scraper.close()

  # getting the dataframes
  angelo_borges = player_borges[0].copy()
  adson = player_adson[0].copy()

  # adding the index as columns, splitting into Category and Statistic
  angelo_borges.\
    reset_index([0, 1], names=["Category", "Statistic"], inplace=True)
  adson.\
    reset_index([0, 1], names=["Category", "Statistic"], inplace=True)

  ## adding columns for the bio

  # for Angelo Borges
  angelo_borges["Name"] = "Ângelo Borges"
  angelo_borges["Position"] = "FW/RW/MF"
  angelo_borges["Age(Y-D)"] = "18-009"
  angelo_borges["Country"] = "BRA"
  angelo_borges["Team"] = "SAN"
  angelo_borges["Height (cm)"] = "173"
  angelo_borges["Weight (kg)"] = "67"
  angelo_borges["Foot"] = "Left"

  # for Adson
  adson["Name"] = "Adson"
  adson["Position"] = "FW"
  adson["Age(Y-D)"] = "22-085"
  adson["Country"] = "BRA"
  adson["Team"] = "COR"
  adson["Height (cm)"] = "171"
  adson["Weight (kg)"] = "71"
  adson["Foot"] = "Left"

  # concatenating into one dataframe
  scouting = pd.concat([angelo_borges, adson], axis=0)

  # saving to CSV for use on Tableau Later
  scouting.to_csv("scouting.csv", index=None)