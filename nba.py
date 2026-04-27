import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playercareerstats

salaries = pd.read_csv('NBA Player Salaries.csv')
print(salaries['2023/2024'][1])
zero = salaries['2023/2024'][1]
print((salaries['2022/2023'] == zero).sum())

SEASON = '2022/2023'

# TEST 
from nba_api.stats.endpoints import leaguedashplayerstats

# Pull all player stats for the 2022-23 Regular Season
# Note: Season format must be 'YYYY-YY'
league_stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season='2022-23',
    per_mode_detailed='PerGame',  # Can also be 'Totals'
    season_type_all_star='Regular Season'
)

# Convert to a DataFrame
df = league_stats.get_data_frames()[0]

# Display the top 10 players by points per game
top_scorers = df[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'REB', 'AST', 'BLK', 'STL', 'FG_PCT', 'FG3_PCT', 'FT_PCT']].sort_values(by='PTS', ascending=False)
print(top_scorers.head(10))

df_merged = df.merge(salaries[['Player Name', '2022/2023']], left_on='PLAYER_NAME', right_on='Player Name', how='left')

print(df_merged)


