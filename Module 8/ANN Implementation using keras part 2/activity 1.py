

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('Churn_Modelling.csv')
print(df.head())

print(df.info)

print(df.describe())

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

print(df)

print(df.info())

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis =1 )

print(df.shape)

y = df.pop('Exited')
X = df

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print(X_train)

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU, PReLU, ELU 

classifier = Sequential()

classifier.add(Dense(units = 6, kernel_initializer = 'he_uniform', activation='relu',input_dim = 10))

classifier.add(Dense(units = 6, kernel_initializer = 'he_uniform', activation='relu'))

classifier.add(Dense(units =1, kernel_initializer = 'glorot_uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'ADamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

model_history = classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

print(classifier.summary())

Y_pred = classifier.predict(X_test)
print(Y_pred)

Y_pred = (Y_pred > 0.5)
print(Y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, Y_pred)
print(cm)

from sklearn.metrics import accuracy_score
score = accuracy_score(Y_pred, y_test)

print(score)