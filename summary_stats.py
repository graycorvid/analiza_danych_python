from load import load_data
import pandas as pd
import numpy as np


# Wczytanie danych za pomocą funkcji z load.py
df = load_data()

# Zamiana wszystkich stringów 'Nan', 'nan', 'NaN' w całym df na prawdziwe NaN
df = df.replace(['Nan', 'nan', 'NaN'], np.nan)

# Liczba unikalnych wartości w każdej kolumnie
print("Liczba unikalnych wartości w każdej kolumnie:")
print(df.nunique()) 
# Najczęstsze wartości w każdej kolumnie (bez NaN)
print("\nNajczęstsze wartości w każdej kolumnie:")
for col in df.columns:
    print(f"\n{col}:")
    print(df[col].value_counts(dropna=True).head(5))

#Nietstey powyższe zestawienia unikalnych i najczęstszych wartości traktują każdą komórkę jako pojedynczą wartość tekstową.
#Nie uwzględniają przypadków, gdy w kolumnie 'Genres' występuje kilka gatunków w jednej komórce, więc nie pokazująfaktycznej liczby zespołów w poszczególnych gatunkach.")
#Bardziej szczegółowe wyszukiwanie w pliku "genre_stats.py"



# Dodatkowo dla kolumny Genres: liczba gatunków (do dwóch miejsc po przecinku)
df['Genres_count'] = df['Genres'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)
print("\nStatystyki dotyczące liczby gatunków w kolumnie 'Genres':")
print(df['Genres_count'].describe().round(2))

#count - liczba wierszy (czyli też liczba zespołów i ich gatunków)
#mean - średnia liczba gatunków na jeden zespół
#std - odchylenie (jak bardzo liczba gatunków różni się od średniej)
#min - minimalna wartość (niektóre zespoły nie mają wpisanego gatunku)
#25% - jedna czwarta (pierwszy kwartyl) zespołów ma podanych 2 lub niej gatunków
#50% - połowa zespołów ma 3 lub mniej gatunków
#75% - jedna czwarta (3 kwartyl) ma 4 lub więcej gatunków
#max - maksymalna liczba gatunków przypisana do jednego zespołu
