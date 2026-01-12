
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

print(data.head())

print(data.isnull().any())

print(data.info())

sns.set_style('white')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('dark')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('ticks')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('white')
sns.countplot(x=data['continent'])
sns.despine()
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'])
sns.despine()
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'], palette='winter')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster", font_scale=0.8)
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)
plt.show()

