import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('kurs14.csv', header=0, sep=';', decimal=',')
p = df[df['Dzień'] % 2 == 0]
etykiety = np.arange(len(p))

plt.plot(etykiety, p['Kurs CZK'])
plt.xticks(etykiety, p['Dzień'])
plt.show()
