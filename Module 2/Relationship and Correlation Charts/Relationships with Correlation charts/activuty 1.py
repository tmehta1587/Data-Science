
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('gapminder(2007).csv')

data.head()

data.info()

data.isnull().any()

sns.scatterplot(data=data, x='gdp_cap', y='life_exp')
plt.show()

sns.scatterplot(data=data, x='gdp_cap', y='life_exp', hue='continent')
plt.show()

fig, ax = plt.subplots(figsize=(8,8))
sns.scatterplot(data=data, x="gdp_cap", y="life_exp", size="population", alpha=0.7, hue="continent", sizes=(20,1000), palette='bright')
plt.show()

sns.heatmap(data.corr(numeric_only=True))
plt.show()

sns.relplot(data=data, y='life_exp', x='gdp_cap', col='continent', col_wrap=3, height=3)
plt.show()

sns.pairplot(data, hue='continent')
plt.show()

