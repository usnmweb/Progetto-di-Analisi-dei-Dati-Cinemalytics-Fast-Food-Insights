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

top_countries = movies_for_country.head(10)

country_with_more_movies = top_countries.idxmax()
print("The country with the most movies is:", country_with_more_movies)

top_countries.plot(kind='bar', figsize=(12, 6), color='skyblue')
plt.title('Top 10 Countries with the Most Movies')
plt.xlabel('Country')
plt.ylabel('Number of Movies')
plt.show()

# Fine 4


# 5) Direttore/attore più frequente 

import seaborn as sns


# Filtra i film con attori professionisti
df_filtered_2 = df[df['actors'] != 'Attori non professionisti']

# Combina le colonne 'directors' e 'actors'
df_filtered_2['directors_actors'] = df_filtered_2['directors'] + ' - ' + df_filtered_2['actors']

# Calcola le frequenze
director_actor_counts = df_filtered_2['directors_actors'].value_counts()

# Seleziona le prime 10 coppie più frequenti per rendere il grafico più leggibile
top_pairs = director_actor_counts.head(10)

# Crea un grafico a barre
plt.figure(figsize=(12, 6))
sns.barplot(x=top_pairs.values, y=top_pairs.index, palette="viridis")
plt.title('Top 10 Director-Actor Pairs in Films')
plt.xlabel('Number of Films')
plt.ylabel('Director-Actor Pair')
plt.show()

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


# 8)  Film più popolare, giorno di picco e prodotto maggiormente ordinato

df_food['year'] = pd.to_datetime(df_food['date']).dt.year


merged_df = pd.merge(df, df_food, on='year')


top_films_by_year = merged_df.groupby(['year', 'title']).size().groupby('year').nlargest(2).reset_index(level=0, drop=True)


top_dates_by_year = merged_df.groupby(['year', 'date']).size().groupby('year').nlargest(2).reset_index(level=0, drop=True)


top_items_by_year = merged_df.groupby(['year', 'item_name']).size().groupby('year').nlargest(2).reset_index(level=0, drop=True)


fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Top 4 Most Popular in Each Category')


axes[0].pie(top_films_by_year, labels=top_films_by_year.index, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Top 4 Films')


axes[1].pie(top_dates_by_year, labels=top_dates_by_year.index, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Top 4 Dates')


axes[2].pie(top_items_by_year, labels=top_items_by_year.index, autopct='%1.1f%%', startangle=90)
axes[2].set_title('Top 4Item Names')

plt.show()

# 9) Lo stato in cui sono state fatte più transazioni, metodo di pagamento, genere operatore che ha ricevuto l'ordine

df_food['year'] = pd.to_datetime(df_food['date']).dt.year


merged_df = pd.merge(df, df_food, on='year')


most_transaction_info = merged_df.groupby(['country', 'transaction_type', 'received_by'])['transaction_amount'].sum().idxmax()

most_transaction_country = most_transaction_info[0]
most_transaction_type = most_transaction_info[1]
most_received_by = most_transaction_info[2]

print("Country with the most transaction amount:", most_transaction_country)
print("Transaction type with the most transaction amount:", most_transaction_type)
print("Received by with the most transaction amount:", most_received_by)