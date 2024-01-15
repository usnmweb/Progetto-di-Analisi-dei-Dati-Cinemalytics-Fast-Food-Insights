import pandas as pd
url = 'https://raw.githubusercontent.com/usnmweb/python-AMA/main/csv/filmtv_movies.csv'
df = pd.read_csv(url)
df.columns

# 1) Top 5 

#    Con questo codice abbiamo trovato la top 5 dei film con il voto medio più alto.
#    Per farlo abbiamo filtrato in ordine decrescente la colonna dei voti e
#    ne abbiamo "Tagliato la testa" prendendo il titolo, l'anno e il genere dei primi cinque risultati.


print(len(df.index), len(df.columns))  

df = df.dropna()

top_five = df.sort_values(by='avg_vote', ascending=False).head(5)
list_of_columns = ["title" ,"year", "genre"]
print("la top 5 con il voto medio piu alto sono:",top_five[list_of_columns])

import matplotlib.pyplot as plt
import numpy as np


short_df = top_five

x = short_df["year"]
y = short_df["avg_vote"]

plt.bar(x, y)

plt.ylim(9, 10.1)

plt.show()

# Fine 1 

# 2) Attore che ha fatto più film.

#    Con questo codice abbiamo trovato gli attori che hanno recitato in più film.
#    Per farlo abbiamo ripulito la colonna degli attori dai valori che non ci interessavano (Nan e Attori non professionisti)
#    poi abbiamo ricava


df_filtered = df[df['actors'] != 'Attori non professionisti']


actor_counts = df_filtered['actors'].value_counts()


most_films_actor = actor_counts.idxmax()
number_of_films = actor_counts.loc[most_films_actor]



print(f"{most_films_actor} appeared in {number_of_films} films.")

# Fine 2 


# 3) Regista con più film


director_counts = df['directors'].value_counts()


most_films_director = director_counts.idxmax()
number_of_films = director_counts.loc[most_films_director]



print(f"{most_films_director} directed {number_of_films} films.")

# Fine 3 

# 4) Stato 

movies_for_country = df['country'].value_counts()
# Conto i film per stato

country_with_more_movies = movies_for_country.idxmax()
# trovo stato con la maggiore quantità di film realizzati

print("The state with more movies is:",movies_for_country)

# Fine 4


# 5) Direttore/attore più frequente 

df_filtered_2 = df[df['actors'] != 'Attori non professionisti']


df_filtered_2['directors_actors'] = df_filtered_2['directors'] + ' - ' + df_filtered_2['actors']


director_actor_counts = df_filtered_2['directors_actors'].value_counts()


most_frequent_pair = director_actor_counts.idxmax()
number_of_films = director_actor_counts.loc[most_frequent_pair]


print(f"The most frequent director-actor pair is: {most_frequent_pair}")
print(f"They worked together in {number_of_films} films.")

# fine 5

# 6) Storia vera


true_story_counts = df['description'].str.contains('true story', case=False).sum()


print(f"The number of films with 'true story' in the description is: {true_story_counts}")

# fine 6


# 7) I film più divertenti secondo il voto del pubblico


comedy_films = df[df['genre'].str.contains('Comedy', case=False)]


sorted_comedy_films = comedy_films.sort_values(by='public_vote', ascending=False)


most_humorous_films = sorted_comedy_films.head(5)
print("The most humorous comedy films according to the audience:")
print(most_humorous_films[['title', 'public_vote']])

#fine 7

#Add 2* df
#Abbiamo importato e pulito il secondo df sui report delle vedite dei ristorant 

import pandas as pd
url = 'https://raw.githubusercontent.com/usnmweb/python-AMA/main/csv/Balaji%20Fast%20Food%20Sales.csv'
df_food = pd.read_csv(url)
df_food.columns

df_food = df_food.dropna()

print(len(df_food.index), len(df_food.columns)) #893 10


# mergiato e pulito il nuovo df formato dai due precedenti


df_food['year'] = pd.to_datetime(df_food['date']).dt.year


merged_df = pd.merge(df, df_food, on='year')

print(len(merged_df.index), len(merged_df.columns))

merged_df = merged_df.dropna()

print(len(merged_df.index), len(merged_df.columns))



merged_df.columns

print(len(merged_df.index), len(merged_df.columns))