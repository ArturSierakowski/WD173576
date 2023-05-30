import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ZADANIE 1
# sns.set()
# x = np.arange(0, 30.1, 0.1)
# sns.lineplot(x=x, y=np.sin(x), label='sin(x)', linestyle='--')
# sns.lineplot(x=x, y=np.cos(x), label='cos(x)', linestyle='-')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres sin(x) i cos(x)')
# plt.legend(loc='upper right')
# plt.show()

# ZADANIE 2
# sns.set()
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa = df.groupby('Plec').agg({'Liczba': 'sum'})
# wykres = sns.barplot(x=grupa.index, y='Liczba', data=grupa)
# plt.title('Liczba narodzin chłopców i dziewczynek')
# plt.xlabel('Płeć')
# plt.ylabel('Liczba dzieci w milionach')
# # argument do legendy poza wykresem - bbox_to_anchor=(1, 0.5)
# plt.legend(loc='lower left')
# plt.show()
#
# grupa = df.groupby('Rok').agg({'Liczba': 'mean'})
# sns.barplot(x=grupa.index, y='Liczba', data=grupa)
# plt.title('Średnia liczba narodzonych dzieci w każdym roku')
# plt.xlabel('Rok')
# plt.ylabel('Średnia liczba narodzonych dzieci')
# plt.xticks(rotation=45)
# plt.show()

# ZADANIE 3
# df = pd.read_csv('zamowienia.csv', delimiter=';')
# grupa = df.groupby('Sprzedawca').size()
# sns.barplot(x=grupa.index, y=grupa.values)
# plt.xticks(rotation=20)
# plt.show()

# ZADANIE 4
df = pd.read_csv('iris.data', header=0, decimal='.', sep=',')
x = df['petal length']
y = df['petal width']
sns.scatterplot(x=x, y=y, data=df, hue='class')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
