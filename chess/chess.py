
import pandas as pd


path = "/Users/tony/PycharmProjects/streamlit/chess/players_by_year_born.csv"


df = pd.read_csv(path, index_col=0)

print(df)