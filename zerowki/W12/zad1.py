import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

etykiety = np.arange(5)
wartosci = [24, 96, 17, 66, 23]

plt.barh(etykiety, wartosci)
for i in etykiety:
    plt.annotate(wartosci[i], xy=(wartosci[i], etykiety[i]))
plt.title("Wykres Słupki")
plt.yticks(etykiety, ['A', 'B', 'C', 'D', 'E'], rotation=45)
plt.show()
