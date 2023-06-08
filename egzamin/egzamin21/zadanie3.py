import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# df = pd.read_csv('wynagrodzenia21.csv', header=0, sep=';', decimal=',')
# etykiety = np.arange(4)
# width = 0.4
#
# w_m = df[df['Województwo'] == 'WARMIŃSKO-MAZURSKIE']
# y1 = w_m.values[0, 1:5]
# print(y1)
# plt.bar(etykiety, y1, width, label='warmińsko-mazurskie')
#
# maz = df[df['Województwo'] == 'MAZOWIECKIE']
# y2 = maz.values[0, 1:5]
# print(y2)
# plt.bar(etykiety + 0.4, y2, width, label='mazowieckie')
#
# plt.xlabel('Rok')
# plt.ylabel('Miesięczne wynagrodzenie')
# plt.title('Wynagrodzenia na przestrzeni lat')
# plt.legend()
# plt.xticks(etykiety, ('2010', '2011', '2012', '2013'))
# plt.yticks(np.arange(0, 5000, 1000))
# plt.tight_layout()
# plt.show()

# ALTERNATYWNY SPOSOB
df = pd.read_csv('wynagrodzenia21.csv', header=0, sep=';', decimal=',')
new_df = pd.melt(df, id_vars=["Województwo"], var_name="Rok", value_name="Wynagrodzenie")
lata = ['2010', '2011', '2012', '2013']
etykiety = np.arange(4)
width = 0.35

w_m = new_df.loc[(new_df['Województwo'] == 'WARMIŃSKO-MAZURSKIE') &
                 (new_df['Rok'].isin(lata))]
maz = new_df.loc[(new_df['Województwo'] == 'MAZOWIECKIE') &
                 (new_df['Rok'].isin(lata))]

plt.bar(etykiety, w_m['Wynagrodzenie'], width, label='Warmińsko-mazurskie')
plt.bar(etykiety + width, maz['Wynagrodzenie'], width, label='Mazowieckie')

plt.xlabel('Rok')
plt.ylabel('Wynagrodzenie')
plt.xticks(etykiety, lata)
plt.legend(title='Województwo')
plt.show()
