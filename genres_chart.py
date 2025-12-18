from load import load_data
import pandas as pd
import matplotlib.pyplot as plt
import re

df = load_data()

# Czyszczenie - wygenerowałam przy użyciu gpt po prostu różne regexy, bo inaczej powielały mi się te same gatunki przez różnice w pisowni
def clean_genre(g):
    g = g.lower()                  # małe litery
    g = g.replace('-', ' ')        # myślniki -> spacja
    g = re.sub(r'\([^)]*\)', '', g)  # usuwa wszystko w nawiasach
    g = re.sub(r'[^a-z\s]', '', g)   # usuwa kropki i znaki specjalne
    return g.strip()


all_genres = df['Genres'].dropna().str.split(',').explode().apply(clean_genre)

#liczy wystąpienie danego gatunku
genres_count = all_genres.value_counts()

#limit ustawiony na 10
plt.figure(figsize=(8,8))
plt.pie(
    genres_count.head(10),
    labels=genres_count.head(10).index,
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Podział na gatunki")
plt.show()
