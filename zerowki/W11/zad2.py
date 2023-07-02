import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('szkolysrednie11.xlsx')
df = pd.read_excel(xlsx, header=0)

lata = df['Rok'].unique()
ucz = df[df['Wykaz'] == 'uczniowie']
ab = df[df['Wykaz'] == 'absolwenci']

plt.plot(lata, ucz['Wartość'], label='uczniowie')
plt.plot(lata, ab['Wartość'], label='absolwenci')
plt.legend()
plt.title("stosunek uczniow do absolwentow")
plt.show()
