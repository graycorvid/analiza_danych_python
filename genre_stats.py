import pandas as pd
from load import load_data

df = load_data()

# Tworzymy listę gatunków jako lista, usuwając spacje na brzegach
def split_and_clean(genres):
    if pd.isna(genres):
        return []
    return [g.strip() for g in genres.split(',')]

df['Genres_list'] = df['Genres'].apply(split_and_clean)

#Dokładne liczenie, np. "Nu metal"

# sprawdzamy, czy w którymkolwiek gatunku jest "nu metal" w dowolnej formie (nu metal, Nu Metal, Nu-metal itd. - ale bez "nu metalcore")
def has_nu_metal(genres):
    for g in genres:
        g_lower = g.lower()
        if 'nu metal' in g_lower and 'nu metalcore' not in g_lower:
            return True
    return False

nu_metal_count = df['Genres_list'].apply(has_nu_metal).sum()

print(f"Liczba zespołów z gatunkiem 'Nu Metal': {nu_metal_count}")

# ...czy w którymkolwiek gatunku jest "alternative rock"
def has_alternative_rock(genres):
    for g in genres:
        g_lower = g.lower()
        if 'alternative rock' in g_lower:
            return True
    return False

# Liczenie zespołów
alternative_rock_count = df['Genres_list'].apply(has_alternative_rock).sum()

print(f"Liczba zespołów z gatunkiem 'Alternative Rock': {alternative_rock_count}")


