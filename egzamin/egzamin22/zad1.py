import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

etykiety = ['RMF FM', 'Radio Zet', 'Eska', 'Inne']
wartosci = [24.8, 13, 6.7, 55.5]
kolory = ['red', 'blue', 'green', 'purple']
explode = [0.1, 0, 0, 0]

plt.pie(wartosci, labels=etykiety, colors=kolory, autopct='%1.1f%%', explode=explode,
        shadow=True, startangle=75)
plt.title('Wyniki słuchalności - II-IV 2017')
plt.show()
