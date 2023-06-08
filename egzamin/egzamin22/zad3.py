import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('stacjepaliw.xlsx')
df = pd.read_excel(xlsx, header=0)

fig, ax = plt.subplots()
w_m = df[df['Nazwa'] == 'WARMIŃSKO-MAZURSKIE']
print(w_m)
x1 = w_m.columns[1:]
y1 = w_m.values[0][1:]
ax.plot(x1, y1, label='WARMIŃSKO-MAZURSKIE', color='blue')

maz = df[df['Nazwa'] == 'MAZOWIECKIE']
print(maz)
x2 = maz.columns[1:]
y2 = maz.values[0][1:]
ax.plot(x2, y2, label='MAZOWIECKIE', color='orange')

ax.legend(title='Województwo')
ax.set_xlabel('Rok')
ax.set_ylabel('Stacje paliw')
ax.set_title('Stacje paliw na przestrzeni lat')
plt.show()
