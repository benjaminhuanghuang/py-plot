import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(1, 5)   # create an array

plt.plot(x, x*2)

# plt.grid(True)
plt.grid(color='r', linewidth='2', linestyle='-.')

plt.show()