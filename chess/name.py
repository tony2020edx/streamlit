import pandas as pd


path = '/Users/tony/PycharmProjects/streamlit/chess/chess.csv'

df = pd.read_csv(path, index_col=0)

Average_rating = df['Rating'].mean()
Average_Age = df['Age'].mean()

most_aged_player = df['Age'].max()
least_aged_player = df['Age'].min()

#name of player with most age
player_with_most_age = df['Name'][df['Age'] == most_aged_player]
player_with_least_age = df['Name'][df['Age'] == least_aged_player]


#number of players born in on or after year 2000
players_born_after_2000 = df['B-Year'][df['B-Year'] >= 2000].count()
print(players_born_after_2000)