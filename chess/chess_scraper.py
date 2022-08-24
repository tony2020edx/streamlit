import pandas as pd

url = 'https://ratings.fide.com/top.phtml?list=men'

df_list = pd.read_html(url)

chess = df_list[4]

print(chess)

chess.to_csv('chess.csv')


#a function to devide the input ny half

def devide(a):
    b = a / 2

    return a