from load import load_data
import matplotlib.pyplot as plt
import seaborn as sns

df = load_data()

# Liczba słów w nazwie zespołu i odpowiednie kategorie (to samo co w band_stats.py)
df['Band_word_count'] = df['Band'].apply(lambda x: len(str(x).split()))
def categorize_word_count(n):
    return str(n) if n <= 4 else '5+'
df['Band_word_category'] = df['Band_word_count'].apply(categorize_word_count)

# Wykres słupkowy rozkładu liczby słów w nazwie
plt.figure(figsize=(8,5))
sns.countplot(x='Band_word_category', data=df, order=['1','2','3','4','5+'])
plt.title("Rozkład liczby słów w nazwach zespołów")
plt.xlabel("Liczba słów w nazwie")
plt.ylabel("Liczba zespołów")
plt.show()
