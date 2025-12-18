import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load import load_data

df = load_data()

# Liczenie zespołów w każdym kraju, "top 9" (ucinamy po 9, bo dalej wszystkie wartości to 1)
country_counts = df['Origin'].value_counts().head(9).reset_index()
country_counts.columns = ['Country', 'Count']

sns.set(style="whitegrid")
plt.figure(figsize=(10,6))

# Wykres słupkowy (9 kolorów)
barplot = sns.barplot(
    x='Country',
    y='Count',
    data=country_counts,
    palette=sns.color_palette("tab10", n_colors=9)
)

# Wartości nad słupkami
for index, row in country_counts.iterrows():
    barplot.text(index, row['Count'] + 0.5, int(row['Count']), color='black', ha="center", fontsize=9)

plt.title("Z jakich krajów pochodzą zespoły:")
plt.xlabel("Kraj")
plt.ylabel("Liczba zespołów")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
