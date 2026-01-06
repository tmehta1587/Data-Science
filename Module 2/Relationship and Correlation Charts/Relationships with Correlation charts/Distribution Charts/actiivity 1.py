
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

print(data.head())

print(data.info())

print(data.isnull().any())

labels = ['population', 'life_exp', 'gdp_cap']

for l in labels: 
    sns.boxplot(y=data[l], palette='winter')
    plt.show()

sns.boxplot(y='gdp_cap', x='continent', data=data, palette='viridis')
plt.show()

sns.boxplot(y='life_exp', x='continent', data=data, palette='viridis')
plt.show()

sns.violinplot(y='gdp_cap', x='continent', data=data, palette='bright')
plt.show()

sns.violinplot(y='life_exp', x='continent', data=data, palette='bright')
plt.show()

for l in labels:
    sns.kdeplot(data[l])
    plt.show()

for l in labels:
    plt.hist(data[l])
    plt.xlabel(l)
    plt.show()

for l in labels:
    sns.distplot(data[l])
    plt.show()
    print("Skewness is:", data[l].skew())
