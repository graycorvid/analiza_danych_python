from load import load_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = load_data()

# Lista gatunków dla każdego zespołu
def split_and_clean(genres):
    if pd.isna(genres):
        return []
    return [g.strip() for g in genres.split(',')]

df['Genres_list'] = df['Genres'].apply(split_and_clean)

# Rozszerzenie danych: każdy gatunek osobno
df_expanded = df.explode('Genres_list')

# Wybór top 10 gatunków
top_genres = df_expanded['Genres_list'].value_counts().head(10).index
df_expanded = df_expanded[df_expanded['Genres_list'].isin(top_genres)]

# Wybór top 10 krajów (najwięcej zespołów)
top_countries = df_expanded['Origin'].value_counts().head(10).index
df_expanded = df_expanded[df_expanded['Origin'].isin(top_countries)]

# Grupowanie: liczba zespołów dla każdego kraju i gatunku
heatmap_data = df_expanded.groupby(['Origin', 'Genres_list']).size().unstack(fill_value=0)

# Heatmapa: wizualizacja
plt.figure(figsize=(12,8))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Liczba zespołów'})
plt.title("Liczba zespołów w top krajach według top gatunków")
plt.xlabel("Gatunki")
plt.ylabel("Kraj")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
