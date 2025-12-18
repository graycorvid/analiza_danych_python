# Analiza zbioru danych 'Alternative Metal Bands'

['Alternative Metal Bands' kaggle dataset](https://www.kaggle.com/datasets/aslawant/alternative-metal-bands?resource=download)

## Opis datasetu

Plik `alternative_metal_bands.csv` zawiera informacje o zespołach grających w gatunkach metalowych, głównie alternative metal i pokrewne. Kolumny w dataset to:

- **Band** – nazwa zespołu
- **Origin** – kraj pochodzenia
- **Active** – status zespołu (Yes / No / On hiatus / brak danych)
- **Genres** – gatunki muzyczne zespołu (mogą być oddzielone przecinkami)

Dataset zawiera kilkaset wierszy z zespołami z różnych krajów i różnymi zestawami gatunków muzycznych. Wszystkie analizy są wykonywane na kopii danych, oryginalny plik CSV pozostaje niezmieniony.

### `load.py` – wczytywanie danych

Plik odpowiedzialny za **ładowanie datasetu** do dalszej analizy. Zawiera funkcję `load_data()`, która:

- Wczytuje CSV z danymi o zespołach alternative metal do Pandas DataFrame.
- Przy uruchomieniu bezpośrednim wyświetla: pierwsze 5 wierszy, info o kolumnach i wymiary datasetu.

### `summary_stats.py` – podstawowe statystyki

Plik generuje ogólne statystyki datasetu:

- Zamienia wszystkie `'Nan'`, `'nan'`, `'NaN'` na prawdziwe `NaN`.
- Pokazuje liczbę unikalnych wartości i najczęstsze wartości w kolumnach (bez NaN).
- Dla kolumny `'Genres'` liczy liczbę gatunków na zespół i pokazuje podstawowe statystyki (`mean`, `std`, `min`, `max`, kwartyle).

### `null_stats.py` – analiza braków danych

- Sprawdza brakujące wartości (`NaN`) w każdej kolumnie.
- Wyświetla liczbę i procent braków (zaokrąglone do 2 miejsc).
- Pokazuje wartości w kolumnie `Active` przed i po uzupełnieniu braków etykietą `"Unknown"`.

### `bands_stats.py` – analiza nazw zespołów

- Liczy słowa w nazwach zespołów i przypisuje je do kategorii:
  - 1, 2, 3, 4 słowa lub 5+ słów.
- Wyświetla liczbę zespołów w każdej kategorii.
- Pokazuje listę zespołów trójczłonowych.
- Pokazuje listę zespołów czteroczłonowych w kolejności odwrotnej alfabetycznie.

### `genre_stats.py` – analiza gatunków muzycznych

- Tworzy listę gatunków dla każdej komórki kolumny `Genres`.
- Liczy zespoły zawierające konkretny gatunek, np.:
  - "Nu Metal".
  - "Alternative Rock".
- Wyświetla liczbę zespołów przypisanych do tych gatunków.

### Wykresy

Pliki `genres_chart.py`, `countries_chart.py`, `bands_chart.py`, `activity_chart.py` oraz `describe_genres_chart.py` odpowiadają za wizualizacje danych.

- **`genres_chart.py`** – wykres kołowy pokazujący rozkład liczby zespołów w poszczególnych gatunkach (jeden zespół może być liczony w kilku gatunkach).
- **`countries_chart.py`** – wykres słupkowy pokazujący liczbę zespołów według krajów
- **`bands_chart.py`** – wykres słupkowy pokazujący liczbę zespołów według długości nazwy zespołu (1, 2, 3, 4, 5+ słów).
- **`describe_genres_chart.py`** – wykres słupkowy pokazujący liczbę zespołów w zależności od liczby gatunków przypisanych do jednego zespołu.
- **`activity_chart.py`** – wykres kołowy pokazujący podział zespołów według statusu aktywności (Yes, No, On hiatus, Unknown).

## Narzędzia

- Python 3.x
- Pandas – do manipulacji danymi
- NumPy – pomocniczo przy brakach danych
- Seaborn i Matplotlib – do wizualizacji

Instalacja wszystkich pakietów może być wykonana jednym poleceniem:

```bash
pip install pandas numpy matplotlib seaborn
```
