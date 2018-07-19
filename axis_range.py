import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)

plt.plot(x, x*x)

print(plt.axis())
plt.axis([-5, 5, 20, 60])   # x_min, x_max, y_min, y_max

print(plt.xlim())
plt.xlim([0, 60])     # change x_min, x_max
plt.xlim(xmin=-20)    # change x_min


plt.show()
