import pandas as pd
import os

# Wczytuje dataset alternative_metal_bands.csv i zwraca DataFrame jako 'df'
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "alternative_metal_bands.csv")
    df = pd.read_csv(file_path)
    return df

# jeśli uruchamiamy load.py (wstępne dane, aby przetestować dataset)
if __name__ == "__main__":
    df = load_data()
    print("Pierwsze 5 wierszy:")
    print(df.head())

    print("\nInformacje o kolumnach i typach danych:")
    print(df.info())

    print("\nWymiary datasetu:", df.shape)
