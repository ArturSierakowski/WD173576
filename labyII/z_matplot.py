import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = np.arange(1, 21, 1.0)
# y = x**(-1)
# ZADANIE 1
# plt.plot(x, y, 'r-')
# plt.axis([1, 21, 0, 1])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(['f(x) = 1/x'])
# plt.show()

# ZADANIE 2
# plt.plot(x, y, 'g>', linestyle='dotted')
# plt.axis([0, 20, 0, 1])
# plt.title('Wykres funkcji dla f(x) dla x [1, 20]')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(['f(x) = 1/x'])
# plt.show()

# ZADANIE 3
# x = np.arange(0, 30.1, 0.1)
# plt.subplot(2, 1, 1)
# plt.plot(x, np.sin(x), 'r-')
# plt.ylabel('sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x), 'b-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()

# ZADANIE 4
# iris_data = pd.read_csv('iris.data', decimal='.', sep=',')
# x = iris_data.iloc[:, 0]
# y = iris_data.iloc[:, 1]
#
# plt.scatter(x, y, c=np.random.randint(0, 149, 149), s=np.abs(x - y))
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.title('Wykres punktowy Iris')
# plt.show()

# ZADANIE 5
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# DLACZEGO NIE DZIALA
# grupa = df.groupby('Plec').agg({'Liczba': 'sum'})
# grupa.plot(kind='bar', xlabel='Płeć dziecka', ylabel='Liczba dzieci w milionach', rot=0, color=['pink', 'cyan'])
# plt.title('Podzial dzieci na plec w okresie 2000-2017')
# plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

grupa = df.groupby('Plec')
etykiety = list(grupa.groups.keys())
wartosci = grupa['Liczba'].sum()
ax1.bar(x=etykiety, height=wartosci, color=['pink', 'cyan'])
ax1.set_xlabel('Płeć')
ax1.set_ylabel('Urodzenia w milionach')

df_mez = df[df['Plec'] == 'M']
suma_mez = df_mez.groupby('Rok')['Liczba'].sum()
ax2.plot(suma_mez.index, suma_mez.values, label='Mężczyźni')
df_kob = df[df['Plec'] == 'K']
suma_kob = df_kob.groupby('Rok')['Liczba'].sum()
ax2.plot(suma_kob.index, suma_kob.values, label='Kobiety')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Urodzenia')
ax2.legend()

grupa = df.groupby('Rok')
etykiety = list(grupa.groups.keys())
wartosci = grupa['Liczba'].sum()
ax3.bar(x=etykiety, height=wartosci, color=['C2', 'C3', 'C9'])
ax3.set_xlabel('Rok')
ax3.set_ylabel('Urodzenia')

plt.suptitle('Dane narodzin w okresie 2000-2017')
plt.subplots_adjust(wspace=1)
plt.show()
