import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

etykiety = np.arange(5)
A = [75, 81, 64, 65, 33]
B = [19, 24, 84, 34, 84]
C = [61, 88, 63, 71, 25]
width = 0.25

plt.bar(etykiety, B, width=width, color='darkblue', label='B')
plt.bar(etykiety+width, C, width=width, color='olive', label='C')
plt.bar(etykiety-width, A, width=width, color='brown', label='A')
plt.legend(loc='upper left')
plt.grid(which='major', axis='y')
plt.title('Wykres')
plt.xlabel('Podpis oxi x')
plt.ylabel('Podpis oxi y')
plt.tight_layout()
plt.show()
