
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")

print("First 10 rows of the dataset:")
print(df.head(10))

print("\nCheck if any column has null values:")
print(df.isnull().any())

print("\nCount of missing values in each column:")
print(df.isnull().sum())

df_all_dropped = df.dropna(how="all")

df_filled = df.fillna(method="bfill")

df_dropped = df.dropna()

print("\nDataset after dropping rows with NaN values:")
print(df_dropped.head())

subset = df.iloc[:5200, :]

plt.figure(figsize =(12,8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()



