import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x ** 2 
plt.plot(x, y)
plt.show()
