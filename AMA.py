import pandas as pd
url = 'https://raw.githubusercontent.com/usnmweb/python-AMA/main/csv/filmtv_movies.csv'
df = pd.read_csv(url)
df.columns

print(len(df.index), len(df.columns))  

df = df.dropna()
print(df.shape)


top_five = df.sort_values(by='avg_vote', ascending=False).head(5)
list_of_columns = ["title" ,"year", "genre"]
print("la top 5 con il voto medio piu alto sono:",top_five[list_of_columns])