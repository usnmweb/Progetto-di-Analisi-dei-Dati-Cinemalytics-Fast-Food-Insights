import pandas as pd
url = 'https://raw.githubusercontent.com/usnmweb/python-AMA/main/csv/filmtv_movies.csv'
df = pd.read_csv(url)
df.columns


avg_vote_title = df['avg_vote'].idxmax()
avg_title_max = df.loc[avg_vote_title, "title"]
print("il voto medio piu alto di un film è di:",avg_title_max )