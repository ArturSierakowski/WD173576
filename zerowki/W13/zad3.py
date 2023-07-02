import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('malzenstwa13.csv', header=0, sep=';')
new_df = pd.melt(df, id_vars=["Województwo"], var_name="Rok", value_name="Liczba")

etykiety = new_df['Rok'].unique()
sl = new_df[new_df['Województwo'] == 'ŚLĄSKIE']
print(sl)
op = new_df[new_df['Województwo'] == 'OPOLSKIE']
print(op)
mp = new_df[new_df['Województwo'] == 'MAŁOPOLSKIE']
print(mp)

plt.plot(etykiety, sl['Liczba'], label='slaskie')
plt.plot(etykiety, op['Liczba'], label='opolskie')
plt.plot(etykiety, mp['Liczba'], label='malopolskie')
plt.legend()
plt.title('malzenstwa z podzialem na wojewodztwa')
plt.ylabel('Liczba malzesntw')
plt.xlabel('Rok')
plt.show()
