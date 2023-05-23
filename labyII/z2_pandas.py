import pandas as pd
import matplotlib.pyplot as plt

# ZADANIE 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# grupa = df.groupby('Rok')
# x = list(grupa.groups.keys())
# y = list(grupa.agg('Liczba').sum())
# plt.plot(x, y, 'r')
# plt.xlabel('Rok')
# plt.ylabel('Liczba urodzeń')
# plt.title('Liczba urodzeń na przestrzeni lat')
# plt.xticks(x[::2])
# plt.show()

# ZADANIE 2
# grupa = df.groupby('Plec')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['pink', 'cyan'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba dzieci w milionach')
# plt.title('Liczba narodzin chłopców i dziewczynek w okresie 2000-2017')
# plt.show()

# ZADANIE 3
# df_sorted = df.sort_values('Rok', ascending=False)
# lata = df_sorted['Rok'].unique()[:5]
# df_filtered = df_sorted[df_sorted['Rok'].isin(lata)]
#
# grupa = df_filtered.groupby('Plec').agg({'Liczba': 'sum'})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6),
#            colors=['pink', 'cyan'], ylabel='Płeć procentowo')
# plt.legend(loc='lower left')
# plt.title('Procent narodzin chłopców i dziewczynek w okresie 2013-2017')
# plt.show()

# ZADANIE 4
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa = df.groupby('Sprzedawca').size()
grupa.plot(kind='bar', xlabel='Sprzedawca', ylabel='Ilość zamówień', rot=20, color=['C2', 'C3', 'C9'])
plt.subplots_adjust(bottom=0.15)
plt.title('Ilość zamówień w zależności od sprzedawcy')
plt.show()
