import pandas as pd
from load import load_data 

df = load_data()

# Liczenie słów w nazwie zespołu
df['Bands_name_word_count'] = df['Band'].apply(lambda x: len(str(x).split()))

# Kategorie: 1 słowo, 2 słowa, 3 słowa, 4 słowa ,5+ słów
def categorize_word_count(n):
    return str(n) if n <= 4 else '5+'


df['Bands_word_category'] = df['Bands_name_word_count'].apply(categorize_word_count)
df[df['Bands_name_word_count'] == 5]['Band']

# Liczba zespołów w każdej kategorii
count_by_words = df['Bands_word_category'].value_counts().sort_index()
print("Liczba zespołów według liczby słów w nazwie:")
print(count_by_words)

# Przykładowa lista zespołów trójczłonowych
bands_3_bands = df[df['Bands_name_word_count'] == 3]['Band']
print("\nZespoły trójczłonowe:")
print(bands_3_bands.to_list())

# Przykładowa lista zespołów  czteroczłonowych w kolejności odwrotnej alfabetycznie
bands_4_words = df[df['Bands_word_category'] == '4']['Band'].sort_values(ascending=False)
print("\nZespoły czteroczłonowe:")
print(bands_4_words.to_list())