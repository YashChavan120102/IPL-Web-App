import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px

df = pd.read_csv('IPL Matches 2008-2020.csv')

df = preprocessor.preprocess(df)

st.set_page_config(layout="wide")

st.sidebar.image('https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Official_Logo.svg/1200px-Indian_Premier_League_Official_Logo.svg.png')
st.sidebar.text("     ")
st.sidebar.text("     ")

st.sidebar.title("IPL Information (2008 - 2020)")

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Venue wise wins','Team Wise Data','Overall Analysis','Wins'),index=2
)

if user_menu == 'Venue wise wins':
    #st.header("Venue wise wins by each team")

    toss,venue = helper.venue_toss_list(df)
    selected_stadium = st.sidebar.selectbox("Select Stadium", venue)
    selected_toss_decision = st.sidebar.selectbox("Select Toss Decision",toss)

    venue_wins = helper.fetch_venue_wins(df,selected_toss_decision,selected_stadium)
    if selected_toss_decision == 'Overall' and selected_stadium == 'Overall':
        st.title("Overall Wins by each team")
    if selected_toss_decision != 'Overall' and selected_stadium == 'Overall':
        st.title("Number of wins by each team when the toss decision was to "+selected_toss_decision)
    if selected_toss_decision == 'Overall' and selected_stadium != 'Overall':
        st.title("Number of wins by each team at "+selected_stadium)
    if selected_toss_decision != 'Overall' and selected_stadium != 'Overall':
        st.title("Number of wins by each team at "+selected_stadium+" when toss decision was to "+selected_toss_decision)
    st.table(venue_wins)

if user_menu == 'Overall Analysis':
    teams = df['team1'].nunique()
    stadiums = df['venue'].nunique()
    player_of_match = df['player_of_match'].mode()
    result_margin = df['result_margin'].max()
    matches = df['id'].shape[0]
    cities = df['city'].nunique()

    st.title("Top Statistics (2008 - 2020)")
    col1,col2,col3 = st.columns(3)
    col1.metric("Teams", teams)
    col2.metric("Stadiums", stadiums)
    col3.metric("Top Result Margin", result_margin)

    col1, col2,col3 = st.columns(3)
    col1.metric("Matches", matches)
    col2.metric("Cities", cities)


    st.text("     ")
    st.text("     ")
    team_wins = helper.team_wins(df)

# Debug line to check the DataFrame
st.write("DEBUG: team_wins DataFrame")
st.dataframe(team_wins)

# Safely plot only if data is valid
if team_wins is not None and not team_wins.empty:
    st.title("Team Wins")
    fig = px.bar(team_wins, x="team", y="wins", width=1000, height=500, color="team", pattern_shape="team")
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig)
else:
    st.warning("No team win data available to display.")

    st.text("     ")
    city_matches = helper.city_matches(df)
    fig1 = px.line(city_matches, x="Cities", y="No  of  Matches",width=1000,height=500)
    st.title("Number of Matches in each city")
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig1)

    st.text("     ")
    man_of_match = helper.man_of_match(df)
    fig2 = px.line(man_of_match, x="Player Name", y="Frequency",width=1000,height=500)
    fig2.update_traces(marker_size=10)
    st.title("Man of the Match award winners")
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig2)

    st.text("     ")
    toss_decision = helper.tos_decision(df)
    fig3 = px.pie(toss_decision, values='Frequency', names='Decision')
    st.title("Overall Toss Decisions")
    st.plotly_chart(fig3)

df1 = pd.read_csv('IPL Matches 2008-2020.csv')
if user_menu == 'Team Wise Data':
    team1,team2 = helper.teams_list(df1)
    selected_team1 = st.sidebar.selectbox("Select Team 1", team1)
    selected_team2 = st.sidebar.selectbox("Select Team 2", team2)

    team_matches = helper.fetch_team_matches(df1, selected_team1, selected_team2)
    if team1 == 'Overall' and team2 == 'Overall':
        st.title("Overall Matches")
    if team1 == 'Overall' and team2 != 'Overall':
        st.title("Overall teams vs "+selected_team2)
    if team1 != 'Overall' and team2 == 'Overall':
        st.title(selected_team1+" vs ovearll teams")
    if team1 != 'Overall' and team2 != 'Overall':
        st.title(selected_team1 + " vs "+selected_team2)

    st.table(team_matches)


if user_menu == 'Wins':
    st.header("Total matches won by each team from year 2008 - 2020")


    col1, col2, col3 = st.columns(3)
    col1.metric("Mumbai Indians", "120")
    col2.metric("Chennai Super Kings", "106")
    col3.metric("Kolkata Knight Riders", "99")

    col1, col2, col3 = st.columns(3)
    col1.metric("Royal Challengers Bangalore", "91")
    col2.metric("Kings XI Punjab", "88")
    col3.metric("Rajasthan Royals", "81")

    col1, col2, col3 = st.columns(3)
    col1.metric("Delhi Daredevils", "67")
    col2.metric("Sunrisers Hyderabad", "66")
    col3.metric("Deccan Chargers", "29")

    col1, col2, col3 = st.columns(3)
    col1.metric("Delhi Capitals", "19")
    col2.metric("Rising Pune Supergiants", "15")
    col3.metric("Gujarat Lions", "13")

    col1, col2, col3 = st.columns(3)
    col1.metric("Pune Warriors", "12")
    col2.metric("Kochi Tuskers Kerala", "6")

