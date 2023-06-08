import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile('turcja.xlsx')
df = pd.read_excel(xlsx, header=0)
df_ankara = df[df['city'] == 'Ankara']

lata = [2005, 2006, 2007, 2008, 2009, 2010]
ankara_lata = df_ankara[df_ankara['years'].isin(lata)]
print(ankara_lata)

plt.bar(lata, ankara_lata['pop'])
plt.annotate('najwieksza populacja', xy=(2010, 4000000), xytext=(2008.2, 4800000),
             arrowprops=dict(facecolor='red'),
             fontsize=11, color='red', fontweight='bold')
plt.xlabel('Lata')
plt.ylabel('Ludność w milionach')
plt.title('Populacja Ankary na przestrzeni lat')
plt.show()
