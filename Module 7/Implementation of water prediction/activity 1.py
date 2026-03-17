import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('water_potability.csv')

print("First 5 rows of dataset:")
print(df.head(), "\n")

print("Shape of dataset:", df.shape, "\n")

print("Missing values in each column:")
print(df.isnull().sum(), "\n")

print("Dataset info:")
print(df.info(), "\n")

print("Descriptive statistics:")
print(df.describe(), "\n")

df.fillna(df.mean(), inplace=True)
print("Missing values after filling with mean:")
print(df.isnull().sum(), "\n")

print("Potability value counts:")
print(df['Potability'].value_counts(), "\n")

sns.countplot(df['Potability'])
plt.title("Potability Count")
plt.show()

sns.histplot(df['ph'], kde=True)
plt.title("PH Distribution")
plt.show()

df.hist(figsize=(14,14))
plt.show()

plt.figure(figsize=(13,8))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.title("Correlation Heatmap")
plt.show()

df.boxplot(figsize=(14,7))
plt.title("Boxplot of Features")
plt.show()

X = df.drop('Potability', axis=1)
Y = df['Potability']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101, shuffle=True)
print("Data split into training and testing sets.\n")

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dt = DecisionTreeClassifier(criterion='gini', min_samples_split=10, splitter='best')
dt.fit(X_train, Y_train)
prediction_dt = dt.predict(X_test)

print("Decision Tree Classifier Results:")
print("Accuracy Score:", round(accuracy_score(Y_test, prediction_dt)*100, 2))
print("Confusion Matrix:\n", confusion_matrix(Y_test, prediction_dt))
print("Classification Report:\n", classification_report(Y_test, prediction_dt))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, Y_train)
prediction_knn = knn.predict(X_test)

print("\nK-Nearest Neighbors Results:")
print("Accuracy Score:", round(accuracy_score(Y_test, prediction_knn)*100, 2))
print("Confusion Matrix:\n", confusion_matrix(Y_test, prediction_knn))
print("Classification Report:\n", classification_report(Y_test, prediction_knn))

from sklearn.linear_model import LogisticRegression
log = LogisticRegression(max_iter=1000, random_state=0)
log.fit(X_train, Y_train)
prediction_log = log.predict(X_test)

print("\nLogistic Regression Results:")
print("Accuracy Score:", round(accuracy_score(Y_test, prediction_log)*100, 2))
print("Confusion Matrix:\n", confusion_matrix(Y_test, prediction_log))
print("Classification Report:\n", classification_report(Y_test, prediction_log))