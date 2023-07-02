import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('nieruchomosci12.csv', header=None, sep=';', decimal=',', thousands=' ')
df = df.transpose()
df[4] = df[4].str.replace(' ', '')

labels = df[1].unique()
rp = df[df[0] == 'rynek pierwotny']
rw = df[df[0] == 'rynek wtórny']

plt.subplot(1, 2, 1)
plt.pie(rp[4], autopct='%1.2f%%')
plt.title('rynek pierwotny')
plt.subplot(1, 2, 2)
plt.pie(rw[4], autopct='%1.2f%%')
plt.title('rynek wtorny')
plt.legend(bbox_to_anchor=(0, 0), labels=labels)
# plt.savefig('nieruchomosci.jpg', format='jpg')
plt.show()
