import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mieszkania16.csv', header=0, sep=';')
grouped = df.groupby('Formy budownictwa')
print(grouped)
height = 0.3

for name, group in grouped:
    plt.barh(group['Rok'], group['Wartość'], height=height, label=name)
plt.xlabel('Wartość')
plt.ylabel('Rok')
plt.title('Wykres słupkowy poziomy')
plt.legend()
plt.show()
