import numpy as np
import pandas as pd


def fetch_venue_wins(df,toss, venue):
    if toss == 'Overall' and venue == 'Overall':
        temp_df = df
    if toss == 'Overall' and venue != 'Overall':
        temp_df = df[df['venue'] == venue]
    if toss != 'Overall' and venue == 'Overall':
        temp_df = df[df['toss_decision'] == toss]
    if toss != 'Overall' and venue != 'Overall':
        temp_df = df[(df['toss_decision'] == toss) & (df['venue'] == venue)]

    x = temp_df.groupby('venue').sum()[['Royal Challengers Bangalore', 'Kings XI Punjab',
                                        'Delhi Daredevils', 'Mumbai Indians', 'Kolkata Knight Riders',
                                        'Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
                                        'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
                                        'Gujarat Lions', 'Rising Pune Supergiants',
                                        'Rising Pune Supergiant', 'Delhi Capitals']]

    x['Total'] = x['Royal Challengers Bangalore'] + x['Kings XI Punjab'] + x['Delhi Daredevils'] + x['Mumbai Indians'] + \
                 x['Kolkata Knight Riders'] + x['Rajasthan Royals'] + x['Deccan Chargers'] + x['Chennai Super Kings'] + \
                 x['Kochi Tuskers Kerala'] + x['Pune Warriors'] + x['Sunrisers Hyderabad'] + x['Gujarat Lions'] + x[
                     'Rising Pune Supergiants'] + x['Rising Pune Supergiant'] + x['Delhi Capitals']

    return x


def venue_wins(df1):
    df2 = df1.groupby('venue').sum()[['Royal Challengers Bangalore', 'Kings XI Punjab',
                                'Delhi Daredevils', 'Mumbai Indians', 'Kolkata Knight Riders',
                                'Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
                                'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
                                'Gujarat Lions', 'Rising Pune Supergiants',
                                'Rising Pune Supergiant', 'Delhi Capitals']]

    df2['Total'] = df2['Royal Challengers Bangalore'] + df2['Kings XI Punjab'] + df2['Delhi Daredevils'] + df2[
        'Mumbai Indians'] + df2['Kolkata Knight Riders'] + df2['Rajasthan Royals'] + df2['Deccan Chargers'] + df2[
                       'Chennai Super Kings'] + df2['Kochi Tuskers Kerala'] + df2['Pune Warriors'] + df2[
                       'Sunrisers Hyderabad'] + df2['Gujarat Lions'] + df2['Rising Pune Supergiants'] + df2[
                       'Rising Pune Supergiant'] + df2['Delhi Capitals']

    df21 = df2.sort_values('Total', ascending=False)

    return df21

def venue_toss_list(df):
    toss = df['toss_decision'].unique().tolist()
    toss.insert(0, 'Overall')

    venue = df['venue'].unique().tolist()
    venue.sort()
    venue.insert(0, 'Overall')

    return toss,venue

def team_wins(df):
    # Drop any rows where winner is NaN
    df_wins = df['winner'].dropna().value_counts().reset_index()
    df_wins.columns = ['team', 'wins']
    return df_wins

def city_matches(df):
    city_matches = df['city'].value_counts().reset_index()
    city_matches1 = city_matches.rename(columns={'index': 'Cities', 'city': 'No  of  Matches'})
    return city_matches1

def man_of_match(df):
    man_of_match = df['player_of_match'].value_counts().reset_index()
    man_of_match1 = man_of_match.rename(columns={'index': 'Player Name', 'player_of_match': 'Frequency'})
    return man_of_match1

def tos_decision(df):
    toss_decision = df['toss_decision'].value_counts().reset_index()
    toss_decision1 = toss_decision.rename(columns={'index': 'Decision', 'toss_decision': 'Frequency'})
    return toss_decision1


def teams_list(df):
    team1 = df['team1'].unique().tolist()
    team1.insert(0, 'Overall')

    team2 = df['team2'].unique().tolist()
    team2.insert(0, 'Overall')

    return team1,team2


def fetch_team_matches(df,team1, team2):
    if team1 == 'Overall' and team2 == 'Overall':
        temp_df1 = df
    if team1 == 'Overall' and team2 != 'Overall':
        temp_df1 = df[df['team2'] == team2]
    if team1 != 'Overall' and team2 == 'Overall':
        temp_df1 = df[df['team1'] == team1]
    if team1 != 'Overall' and team2 != 'Overall':
        temp_df1 = df[(df['team1'] == team1) & (df['team2'] == team2)]

    x1 = temp_df1.drop(['id', 'neutral_venue', 'eliminator', 'method'], axis=1)
    return x1
