import matplotlib.pyplot as plt
import numpy as np

# Dane
x1 = np.linspace(-10, 10, 100)
x2 = np.linspace(-4, 4, 100)
y1 = x1**2
y2 = np.log(np.abs(x2))

# Tworzenie pierwszego wykresu liniowego
fig, ax1 = plt.subplots()
ax1.plot(x1, y1, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel('Y1', color='b')
ax1.tick_params('y', colors='b')

# Tworzenie drugiego wykresu liniowego z ośmi po prawej stronie
ax2 = ax1.twinx()
ax2.plot(x1, y1, 'r-')
ax2.set_ylabel('Y2', color='r')
ax2.tick_params('y', colors='r')

# Tworzenie wykresu logarytmu naturalnego
fig, ax3 = plt.subplots()
ax3.plot(x2, y2, 'g-')
ax3.set_xlabel('X')
ax3.set_ylabel('Y3', color='g')
ax3.tick_params('y', colors='g')

# Wyświetlanie wykresów
plt.show()
