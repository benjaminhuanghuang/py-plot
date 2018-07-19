import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)
y = x*x

plt.plot(x, y)
plt.text(0, 40, 'This is text', family="serif", color='r', style='italic', weight=10)
plt.text(-2, 20, 'This is text 2', family="fantasy", size=20, weight='light', bbox=dict(facecolor='r', alpha=0.2))

plt.show()