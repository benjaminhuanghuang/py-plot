import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)
y = x*x

plt.plot(x, y)
plt.annotate('This is annotate', xy=(0,1), xytext=(0,20), arrowprops=dict(facecolor='r', frac=0.2, headwidith=30))

plt.show()