import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('gastronomia34.csv', header=None, sep=';', thousands='None')
new_df = df.transpose()
print(new_df)

bary = new_df[new_df[0] == 'bary']
restauracje = new_df[new_df[0] == 'restauracje']
x = np.arange(5)

plt.subplot(2, 1, 1)
plt.plot(x, bary[2])
plt.show()
