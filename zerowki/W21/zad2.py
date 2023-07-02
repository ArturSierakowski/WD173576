import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('ceny21.xlsx')
df = pd.read_excel(xlsx, header=0)

rodzaje = df['Rodzaje produktów'].unique()
lata = df['Rok'].unique()
x = np.arange(len(lata))
style = [':', '--', '-']
kolory = ['r', 'g', 'b']

for i in range(len(rodzaje)):
    prod = df[df['Rodzaje produktów'] == rodzaje[i]]
    plt.plot(x, prod['Wartosc'], label=rodzaje[i], color=kolory[i], linestyle=style[i])
plt.legend(bbox_to_anchor=(1, 0.05), loc='lower right')
plt.annotate('Artur', xy=(5.8, 6.1))
plt.yticks(np.arange(6, 16, 1))
plt.xticks(x, lata)
plt.show()
