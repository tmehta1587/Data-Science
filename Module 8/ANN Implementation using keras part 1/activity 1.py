
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('Churn_Modelling.csv')
print(df.head())

print(df.info())

print(df.describe())

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

print(df)

print(df.info())

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

print(df.shape)

y = df.pop('Exited')
x = df

print(x.shape)

print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print(X_test)
print(X_train)