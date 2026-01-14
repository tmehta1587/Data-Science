
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic_Dataset.csv')

print(data.head())

mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ", mean_age)

mean_fare = np.mean(data['Fare'])
print("Mean Fare is -", mean_fare)
