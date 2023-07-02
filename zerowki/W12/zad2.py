import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('ceny12.xlsx')
df = pd.read_excel(xlsx, header=0)

marg15 = df[(df['Rodzaje towarów i usług'].str.contains('margaryna')) & (df['Rok'] == 2015)]
x = df['Miesiące'].unique()
y = marg15['Wartosc']
plt.plot(x, y)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
