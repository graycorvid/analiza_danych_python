import pandas as pd
import matplotlib.pyplot as plt
from load import load_data

df = load_data()

# Zamiana pustych pól i NaNów na 'Unknown'
df['Active'] = df['Active'].fillna('Unknown')

status_counts = df['Active'].value_counts()

plt.figure()
plt.pie(
    status_counts.values,
    autopct='%1.1f%%',  
    startangle=90
)

plt.legend(
    status_counts.index,
    title="Czy aktywnie działa",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

plt.title("Status aktywności zespołów")
plt.tight_layout()
plt.show()
