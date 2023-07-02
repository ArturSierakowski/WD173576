import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

etykiety = ['A', 'B', 'C', 'D', 'E']
lewy = [35, 48, 15, 40, 39]
prawy = [-30, -32, - 38, -34, -31]

plt.subplot(1, 2, 1)
plt.barh(etykiety, lewy)
plt.xticks(np.arange(0, 50, 10))

plt.subplot(1, 2, 2)
plt.barh(etykiety, prawy)
plt.show()
