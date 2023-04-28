import pandas as pd

# ZADANIE 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# ZADANIE 2
# print(df[df.Liczba > 1000])

# print(df[df.Imie == 'ARTUR'])

# print(df.groupby(['Rok']).agg({'Liczba': ['sum']}))   # PODZIAL URODZEN NA LATA
# print(df.Liczba.sum())

# print(df.loc[df['Rok'].isin(range(2000, 2006)), 'Liczba'].sum())    # 1 SPOSOB
# print(df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005), 'Liczba'].sum())    # 2 SPOSOB

# print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))

# grouped = df.groupby(['Rok', 'Plec'])
# # print(grouped.agg({'Liczba': ['max']}))
# idx = grouped['Liczba'].idxmax()
# print(df.loc[idx, ['Rok', 'Plec', 'Imie', 'Liczba']])

# TYLKO IMIE
# grouped = df.groupby(['Plec', 'Imie'])
# imiona = grouped.agg({'Liczba': 'sum'})
# print(imiona.loc['M']['Liczba'].idxmax())
# print(imiona.loc['K']['Liczba'].idxmax())

# IMIE I ILOSC
# grouped = df.groupby(['Plec', 'Imie'])
# imiona = grouped.agg({'Liczba': 'sum'})
# idx = imiona.groupby('Plec')['Liczba'].idxmax()
# print(imiona.loc[idx, 'Liczba'])

# ZADANIE 3
df = pd.read_csv('zamowienia.csv', header=0, sep=';')

# sprzedawcy = df['Sprzedawca'].unique()
# print(sprzedawcy)

# najwyzsze = df.sort_values(by='Utarg', ascending=False)
# print(najwyzsze.head(5))

# grouped = df.groupby('Sprzedawca')
# df = grouped['idZamowienia'].count()
# print(df)
# print(df['Sprzedawca'].value_counts())    # ALTERNATYWNY SPOSOB

# print(df['Kraj'].value_counts())

# zamowienia = df[(df['Data zamowienia'].str.contains('2005')) & (df['Kraj'] == 'Polska')]
# print(zamowienia['Utarg'].sum())

# print(round(df.Utarg.mean(), 2))

df_2004 = df[df['Data zamowienia'].str.contains('2004')]
df_2005 = df[df['Data zamowienia'].str.contains('2005')]

df_2004.to_csv('zamowienia_2004.csv', index=False, sep=';', decimal='.')
df_2005.to_csv('zamowienia_2005.csv', index=False, sep=';', decimal='.')
