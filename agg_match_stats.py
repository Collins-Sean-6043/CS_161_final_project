"""
Display the distance traveled compared to placement of PUBG combatants.

This program will look at the placement of players relative to
their total travel distance. This should show a corolation of
longer distances traveled aligning with higher placing players.

Sean Collins
"""


import pandas as pd # pd.command instead of pandas.command
import matplotlib.pyplot as plt

def main():
    """
    Display the distance traveled compared to placement of PUBG combatants.

    This program will look at the placement of players relative to
    their total travel distance. This should show a corolation of
    longer distances traveled aligning with higher placing players.

    Parameters
    ----------
    arg1 : DataFrame
        This is a collection of data from PUBG matches played, it shows
        the placement of the player and their distance traveled in
        different ways.

    Returns
    ----------
    plt.show()
        Display a linegraph with final placement along the
        x axis and distance traveled along the y axis.

    """
    data = pd.read_csv (r'pubg-match-deaths/aggregate/agg_match_stats_4_clean.csv')
    df = pd.DataFrame(data, columns= ['dist_ride', 'dist_walk', 'placement'])
    df['travel_distance'] = df['dist_ride'] + df['dist_walk']
    stats_fixed = df.groupby('placement')[['travel_distance']].mean()
    stats_fixed.sort_values('travel_distance').reset_index()
    stats_fixed.columns=['Distance Traveled']
    stats_fixed.plot()
    plt.show()
