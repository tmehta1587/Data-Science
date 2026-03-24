
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import warnings
warnings.filterwarnings('ignore')

data = '/kaggle/input/facebook-live-sellers-in-thailand-uci-ml-repo/live.csv'
df = pd.read_csv(data)

print(df.shape)

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.drop(['column1', 'column3', 'column4'], axis=1, inplace=True))

print(df.info())

print(df.describe())

print(df['status_id'].unique())

print(len(df['status_id'].unique()))

print(df['status_published'].unique())

print(len(df['status_published'].unique()))

print(df['status_type'].unique())

print(df.drop(['status_id', 'status_published'], axis=1, inplace=True))

print(df.info())

print(df.head())

X = df
y = df['status_type']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['status_type'] = le.fit_transform(X['status_type'])
y = le.transform(y)

X.info()

X.head()

cols = X.columns
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X = ms.fit_transform(X)
x = pd.DataFrame(X, columns=[cols])

print(X.head())

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

kmeans.cluster_centers_

labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d sample were correctly labeled." %(correct_labels, y.size))
print('Accuracy score: {0:0.2f}' - format(correct_labels/float(y.size)))

from sklearn.cluster import KMeans 
cs = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter=300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    cs.append(kmeans.inertia_)

plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('NUmber of clusters')
plt.ylabel('')
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=7, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
