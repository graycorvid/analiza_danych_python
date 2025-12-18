import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load import load_data

# Wczytanie danych
df = load_data()

# Liczba gatunków
df['Genres_count'] = df['Genres'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)

# Zliczenie ile zespołów ma ile gatunków
count_genres = df['Genres_count'].value_counts().sort_index()

# Wykres słupkowy
plt.figure(figsize=(10,6))
sns.barplot(x=count_genres.index, y=count_genres.values, palette='viridis')

# Dodanie etykiet nad słupkami
for i, val in enumerate(count_genres.values):
    plt.text(i, val + 0.5, str(val), ha='center', va='bottom', fontsize=10)

plt.title("Liczba zespołów według ilości wykonywanych gatunków")
plt.xlabel("Liczba gatunków")
plt.ylabel("Liczba zespołów")
plt.show()

