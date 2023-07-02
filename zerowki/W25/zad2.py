import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('klimat25.xlsx')
df = pd.read_excel(xlsx, header=0)

por = df[df['Nazwa stacji'] == 'PORONIN']
psz = df[df['Nazwa stacji'] == 'PSZCZYNA']
miesiace = df['Miesiac'].unique()

plt.scatter(miesiace, por['Temperatura'])
plt.plot(miesiace, psz['Temperatura'])
plt.ylabel('Temperatura w stopniach')
plt.xlabel('Miesiąc')
plt.title('temperatura na przestrzeni miesiecy')
plt.show()
