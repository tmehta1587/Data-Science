
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

print(data.head())

grouped_df = data.groupby('continent').mean(numeric_only=True).reset_index()
print(grouped_df)
plots = sns.barplot(x=grouped_df['continent'], y=grouped_df['life_exp'], color='teal')
plt.show()
plots = sns.barplot(x=grouped_df['continent'], y=grouped_df['life_exp'], color='teal')


for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='center', 
                   size=12, xytext=(0,8), 
                   textcoords='offset points')
    
plt.xlabel("Continents", size=14)

plt.ylabel("Life Expectancy", size=14)

plt.title("This is an annotated barplot")

plt.show()