import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

A = [-36, -25, -20, -34]
B = [-22, -17, -12, -22]
etykiety = ['2000', '2002', '2004', '2006']
width = 0.35

plt.barh(etykiety, A, width)
plt.barh(etykiety, B, width, left=A)
plt.show()
