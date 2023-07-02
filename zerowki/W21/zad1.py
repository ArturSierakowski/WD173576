import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from PIL import Image

x = [0.38, 0.47, 0.48, 0.67, 0.68, 0.84, 0.85]
y = [-0.4, -0.72, -0.09, -0.31, -0.69, -0.13, -0.73]
z = [0, 20, 0, 0, 20, 20, 20]

norm = Normalize(vmin=0, vmax=20)
cmap = plt.cm.spring

plt.scatter(x, y, c=z, cmap=cmap, norm=norm)
plt.colorbar()
plt.xlabel('Rozkład')
plt.ylabel('Wartość')
plt.title('Wyniki doświadczenia (7 próbek)')
plt.show()
