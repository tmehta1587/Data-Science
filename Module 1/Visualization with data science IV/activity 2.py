
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

np.random.seed(23685752)
N_points = 10000
n_bins = 20

x = np.random.randn(N_points)
y = 8 ** x + np.random.randn(10000) + 25

fig, axs = plt.subplots(1,1, figsize = (10,7), tight_layout = True)

axs.hist(x, bins = n_bins)

plt.show()
