import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('sport25.csv', header=None, sep=';')
df = df.transpose()
df[2] = df[2].astype(int)

lata = df[1].unique()
etykiety = np.arange(len(lata))
sporty = df[0].unique()
width = 0.20
colors = ['red', 'blue', 'green', 'orange']

for i in range(len(sporty)):
    sport = df[df[0] == sporty[i]]
    plt.bar(etykiety + i*width, sport[2], width=width, color=colors[i])
plt.xticks(etykiety, lata)
plt.show()
