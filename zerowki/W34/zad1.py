import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

labels = ['e', 'a', 'b', 'c', 'd']
colors = ['blue', 'brown', 'olive', 'turquoise', 'beige']

plt.subplot(2, 1, 1)
wartosci = [8.93, 19.64, 21.43, 36.61, 13.39]
explode = [0, 0, 0, 0.2, 0]
plt.pie(wartosci, labels=labels, explode=explode, colors=colors, autopct='%1.2f%%')

plt.subplot(2, 1, 2)
wartosci = [29.2, 16.2, 19.5, 24, 11]
explode = [0.1, 0, 0, 0.2, 0]
plt.pie(wartosci, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', startangle=-80)
plt.savefig('w34.svg', format='svg')
plt.show()
