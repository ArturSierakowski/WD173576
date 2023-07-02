import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('praca14.xlsx')
df = pd.read_excel(xlsx, header=0)

etykiety = df['Rok'].unique()
nmp = df[df['Miejsca pracy'].str.contains('nowo')]
zmp = df[df['Miejsca pracy'].str.contains('zlikwidowanych')]

plt.bar(etykiety, nmp['Wartosc'], label='nowo utworzone')
plt.bar(etykiety, zmp['Wartosc'], label='zlikwidowane')
plt.title('miejsca pracy na przestrzeni lat')
plt.xlabel('Rok')
plt.ylabel('Miejsca pracy w tysiacach')
plt.legend()
plt.tight_layout()
plt.show()
