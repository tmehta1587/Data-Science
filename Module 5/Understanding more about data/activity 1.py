
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("\nLoading Titanic Dataset...")
Titanic = pd.read_csv("titanic.csv")

print("\nFirst 5 rows of dataset:")
print(Titanic.head())

print("nColumns in Dataset: ")
print(Titanic.columns)

print("\nShape of Dataset (Rows, Columns):")
print(Titanic.shape)

print("\nMissing Values in Each Column:")
print(Titanic.isnull().sum())

print("\nDisplaying Heatmap of Missing Values...")

plt.figure(figsize=(12,6))
sns.heatmap(Titanic.isnull(), cmap="spring", yticklabels=False)

plt.title("Missing Values Before Cleaning")
plt.xlabel("Columns")
plt.ylabel("Passengers")
plt.xticks(rotation=45)

plt.show()

print("\nDropping 'deck' or 'Cabin' column if present ...")

Titanic.drop(["deck", "Cabin"], axis=1, inplace=True, errors="ignore")

print("\nDataset After Dropping Deck/Cabin:")
print(Titanic.head())

print("\nRemoving Remaining Rows with Missing Values...")
print(Titanic.dropna(inplace=True))


print("\nHeatmap After Removing Missing Values ...")

plt.figure(figsize=(12,6))
sns.heatmap(Titanic.isnull(), cmap="spring", yticklabels=False, cbar=False)

