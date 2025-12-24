
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as plt

Penguins_df = pd.read_csv('Penguins_Data.csv')

sns.histplot (Penguins_df['Culmen length(mm)' ], bins=10, kde=True) 

plt.show()

