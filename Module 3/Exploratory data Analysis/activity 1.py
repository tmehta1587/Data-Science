
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('Titanic_Dataset.csv')

print(data.head(5))

sns.countplot(x='Pclass', hue='Survived', data=data)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.distplot(data['Age'], kde=False,bins=40)
plt.show()

sns.countplot(data['Gender'])
plt.show()

sns.countplot(x='Survived', hue='SibSp', data=data, palette='mako')
plt.show()

sns.countplot(x='Survived', hue='Parch', data=data, palette='mako')
plt.show()

sns.distplot(data['Fare'])
plt.show()

sns.boxplot(x='Pclass', y='Age', data=data, palette='winter')
plt.show()


numeric_data = data.select_dtypes(include='number')

plt.figure(figsize=(10,6))

sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')

plt.show()