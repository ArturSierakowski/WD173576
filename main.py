import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts, columns=['wartości'])
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)

# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld',
#            rot=0, legend=True, title='Populacja z podziałem na kontynenty')
# plt.legend(['Suma populacji'])
# plt.show()

# wykres = grupa.plot.bar()
# wykres.set_ylabel('mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podziałem na kontynenty')
# plt.xticks(rotation=0)
# plt.show()
