import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv (r'pubg-match-deaths/aggregate/agg_match_stats_4_proj_2.csv')
df = pd.DataFrame(data, columns= ['player_dmg', 'placement'])
stats_fixed = df.groupby('placement')[['player_dmg']].mean()
stats_fixed.sort_values('player_dmg').reset_index()
stats_fixed.columns=['Damage Delt']
stats_fixed.plot()
plt.show()
