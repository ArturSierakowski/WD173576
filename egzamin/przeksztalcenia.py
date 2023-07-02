import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gastro21.csv', header=None)
new_df = df.transpose()
print(new_df)

etykiety = np.arange(3)
lata = ['2015', '2016', '2017']
width = 0.35
kolory = ['green', 'blue', 'red', 'yellow']
nazwy = ['restauracje', 'bary', 'stołówki', 'punkty gastronomiczne']
for i in etykiety:
    plt.bar(etykiety + i * width, new_df.loc[(new_df[0] == nazwy[i])][2], width=width, color=kolory[i])
plt.xticks(etykiety, lata)
plt.show()
