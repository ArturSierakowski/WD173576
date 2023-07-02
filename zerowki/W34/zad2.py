import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('sprzedaz34.xlsx')
df = pd.read_excel(xlsx, header=0)

grupa = df.groupby('Rok')
etykiety = ['2015', '2016', '2017']
jab = grupa[grupa['Produkt'] == 'Jabłka']
gru = grupa[grupa['Produkt'] == 'Gruszki']
mor = grupa[grupa['Produkt'] == 'Morele']
plt.bar(etykiety, jab)
