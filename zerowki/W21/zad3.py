import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('sprzedaz21.csv', header=None, sep='@')
df = df.transpose()
df[2] = df[2].astype(int)
print(df)

owoce = df[0].unique()
lata = df[1].unique()
etykiety = np.arange(len(lata))
kolory = ['red', 'yellowgreen', 'indigo']
wysokosc = 0.25

for i in range(len(owoce)):
    owoc = df[df[0] == owoce[i]]
    plt.barh(etykiety + i*wysokosc, owoc[2], height=wysokosc, color=kolory[i], label=owoce[i])
plt.yticks(etykiety, lata)
plt.legend()
plt.title('Sprzedaz owocow na przestrzeni lat')
plt.ylabel('Rok')
plt.xlabel('Liczba owoców')
plt.tight_layout()
plt.show()
