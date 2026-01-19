
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic_Dataset.csv')

print(data.head(5))

sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.countplot(x='Survived', data=data, palette='winter')
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')
plt.show()

sns.countplot(x='Embarked', data=data)
plt.show()

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()
