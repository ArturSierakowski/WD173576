import matplotlib.pyplot as plt
from PIL import Image

plt.subplot(2, 2, 1)
wartosci = [15.7, 25.58, 16.86, 21.51, 12.79, 7.56]
etykiety = ['A', 'B', 'C', 'D', 'E', 'F']
kolory = ['brown', 'pink', 'beige', 'lime', 'brown', 'blue']
plt.pie(wartosci, labels=etykiety, colors=kolory, autopct='%.2f%%',
        startangle=45, explode=[0, 0.1, 0, 0, 0, 0])
plt.title("Lewo Góra")

plt.subplot(2, 2, 4)
wartosci = [20.37, 17.59, 9.72, 19.91, 15.74, 16.67]
etykiety = ['A', 'B', 'C', 'D', 'E', 'F']
kolory = ['brown', 'pink', 'beige', 'lime', 'brown', 'blue']
plt.pie(wartosci, labels=etykiety, colors=kolory, autopct='%.2f%%',
        startangle=45, explode=[0, 0.1, 0, 0, 0, 0])
plt.title("Prawo Dół")
plt.savefig('b21.jpg')
plt.show()
