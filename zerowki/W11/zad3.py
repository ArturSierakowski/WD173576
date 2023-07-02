import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('samochodyosobowe11.csv', sep=';', header=None)
new_df = df.transpose()
print(new_df)

plt.subplot(1, 2, 1)
df18 = new_df[new_df[1] == '2018']
labels = df18[0]
plt.pie(df18[3])
plt.title("b,cfmdnsmds")

plt.subplot(1, 2, 2)
df19 = new_df[new_df[1] == '2019']
plt.pie(df19[3])
plt.title("fscds;cdks")
# plt.subplots_adjust(wspace=0.2)
plt.legend(bbox_to_anchor=(0, 0), labels=labels, )
plt.show()
