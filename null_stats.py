import pandas as pd
from load import load_data  

df = load_data()

# kopia datasetu
df_temp = df.copy()

# Liczenie braków danych (puste komórki, Null, NaN)
print("Liczba braków danych w każdej kolumnie:")
print(df_temp.isnull().sum())

print("\nProcent braków w każdej kolumnie:")
print(df_temp.isnull().mean() * 100)

print("\nProcent braków w każdej kolumnie (zaokrąglone do 2 miejsc):")
print((df_temp.isnull().mean() * 100).round(2))

# Pokazanie jakie wartości są w kolumnie 'Active' 
print("\nWartości w kolumnie 'Active' przed modyfikacją wartości null & NaN:")
print(df_temp['Active'].value_counts(dropna=False))  #dropna, żeby zobaczyć wartości NaN/puste pola w datasetcie

# Zamiana braków/NaN na czytelny label, np. Unknown/Brak danych
df_temp['Active'] = df_temp['Active'].fillna('Unknown')

# Sprawdzenie wartości w Active po użyciu 'fillna' (na kopii, nie zmieniamy orygnalnego pliku .csv)
print("\nPo uzupełnieniu braków w kolumnie 'Active' (na kopii danych):")
print(df_temp['Active'].value_counts())


