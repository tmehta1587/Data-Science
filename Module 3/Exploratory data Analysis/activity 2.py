
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('Iris_Dataset.csv')

print(data.head(5))

print(data.isnull().sum())

print(data.describe())

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']
for label in labels: 
    print('Distribution of', label)
    sns.boxplot(data[label])
    plt.show()

numeric_data = data.select_dtypes(include='number')

plt.figure(figsize=(10,6))

sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')

plt.show()

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']
for label in labels:
    print('Distribution of', label)
    sns.distplot(data[label])
    plt.show()


labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']
for label in labels :
    print('skewness of', label)
    print(data[label].skew())
