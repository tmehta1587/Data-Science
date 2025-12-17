
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Penguins_Data.csv")

print("\nCheck if any column has null values:")
print(df.isnull().any())

print("\nCount of missing values in cloumn:")
print(df.isnull().sum())

print("Bar Plot")
print(df.isnull().sum().plot(kind='bar'))
