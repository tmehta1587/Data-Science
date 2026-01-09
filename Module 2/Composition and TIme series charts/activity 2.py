
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Weather_Dataset.csv')

print(df.head())

print(df_group = df.groupby('month').mean())
print(df_group = df_group.reset_index())

print(df_group.plot.area(x='month', y='Humidity', alpha=0.6))

plt.plot(df['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading Number Over Time')
plt.show()


