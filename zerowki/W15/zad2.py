import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('ceny15.xlsx')
df = pd.read_excel(xlsx, header=0)

lata = df['Rok'].unique()
ryz = df[df['Rodzaje towarów'].str.contains('ryż')]
maka = df[df['Rodzaje towarów'].str.contains('mąka')]

plt.plot(lata, ryz['Wartość'])
plt.plot(lata, maka['Wartość'])
plt.axhline(y=4)
plt.show()
