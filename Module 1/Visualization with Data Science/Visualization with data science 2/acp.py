
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1, 2, 3, 4])
y=x*2

plt.plot(x,y)

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]

plt.plot(x1, y1, '-.')

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()