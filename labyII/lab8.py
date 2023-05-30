import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# plt.plot([1, 3, 5, 7])
# plt.show()

# x = np.array([1, 2, 3, 4])
# y = x**2
#
# plt.plot(x, y, 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot(x, y, 'r')
# plt.plot(x, y, 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

# WYKRESY WIELOMIANIOWE
# x = np.arange(0, 5, 0.2)
# plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()
#
# # plt.plot(x, x, 'r--', label='liniowa')
# # plt.plot(x, x**2, 'bo', label='kwadratowa')
# # plt.plot(x, x**3, 'g^', label='sześcienna')
# # plt.legend()
# # plt.show()

# WYKRES SINUSA
# x = np.arange(0, 10.1, 0.1)
# plt.plot(x, np.sin(x), 'co', label='sin(x)')
# plt.xlabel('wartosci x')
# plt.ylabel('wartosci y')
# plt.legend()
# plt.title('wykres funkcji sin(x)')
# plt.show()

# JAKIES LOSOWE WARTOSCI
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

# SIATKI WYKRESOW
x1 = np.arange(0, 2.02, 0.02)
x2 = np.arange(0, 2.02, 0.02)

y1 = np.sin(x1 * np.pi * 2)
y2 = np.cos(x2 * np.pi * 2)

# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2, 'r')
# plt.title('wykres cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplots_adjust(hspace=0.5)
#
# plt.show()

# WYKRES 3x2
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1)
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
#
# axs[1, 1].plot(x2, y2)
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
#
# axs[2, 0].plot(x1, y1, 'r')
# axs[2, 0].set_title('wykres sin(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('sin(x)')
#
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[2, 1])
#
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# plt.show()

# WYKRESY SLUPKOWE
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)

# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
#
# plt.bar(x=etykiety, height=wartosci, color=['yellow', 'red', 'green'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja')
# plt.show()

grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
print(grupa)

# METODA 1
# grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja', legend=True, rot=0, title='Populacja na kontynentach')

# METODA 2 (nie ma none'ow)
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Populacja')
# wykres.set_xlabel('Kontynenty')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kontynentach')

# plt.savefig('wykres.png')
# plt.show()

# SERIA DANYCH
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# WYKRES KOLOWY Z PANDASA
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': [sum]})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20,
#            figsize=(6, 6), colors=['red', 'green'])
# plt.legend(loc='lower right')
# plt.title('Procent zamówienia dla sprzedawcy')
# plt.show()

# WYKRES KOLOWY Z MATPLOTLIBA
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: "{:.1f}%".format(pct),
#                                   textprops=dict(color="black"), colors=['red', 'green'])
# print(autotext)
# plt.title('Suma zamówień dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()

# SREDNIA KROCZACA Z PANDASA
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# HISTOGRAM Z MATPLOTLIBA
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('wartosci')
# plt.ylabel('prawdopodobienstwo')
# plt.title('histogram')
# plt.grid()
# plt.show()
