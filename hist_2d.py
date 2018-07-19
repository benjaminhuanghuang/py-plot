import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.random.randn(1000) + 2
y = np.random.randn(1000) + 3
plt.hist2d(x, y, bins=10)
plt.show()
