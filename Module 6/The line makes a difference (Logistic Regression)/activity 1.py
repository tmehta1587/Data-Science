

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arrange(10).reshape(-1,1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='linlinear', C=10.0, random_state=0)
model.fit(x, y)

