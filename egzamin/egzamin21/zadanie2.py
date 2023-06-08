import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('ceny21.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

data_pszenna = df[df['Rodzaje towarów'] == 'mąka pszenna - za 1kg']
plt.scatter(data_pszenna['Rok'], data_pszenna['Wartość'], marker='^', c='red')

data_jeczmienna = df[df['Rodzaje towarów'] == 'kasza jęczmienna - za 0,5kg']
plt.scatter(data_jeczmienna['Rok'], data_jeczmienna['Wartość'], marker='o', c='blue')
plt.title('Wykres punktowy cen produktów zbożowych na przestrzeni lat')
plt.legend(['Mąka pszenna za 1kg', 'Kasza jęczmienna za 0,5kg'])
plt.xlabel('Rok')
plt.ylabel('Cena (zł)')
plt.savefig("ceny21.png")
plt.show()
