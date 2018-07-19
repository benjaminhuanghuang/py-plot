import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
'''
    linestyle
    color
    marker
'''
x = np.linspace(-10, 10, 100)
y = x ** 2 
plt.plot(x, y, linestyle='--', c='r', marker='o')
plt.show()
