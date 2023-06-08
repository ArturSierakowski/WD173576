import pandas as pd

data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Country', 'Population', 'Capital'])
print(df)

print(df.iloc[[0], [0]])
print("--")
print(df.loc[[0], ['Country']])
print("--")
print(df.loc[2])
print("--")
print(df.loc[:, 'Capital'])
print("--")
print(df.loc[1, 'Capital'])