import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

x = np.linspace(0, 5*np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.plot(x, y1)
# plt.plot(x, y2)

# fill range between x axis and curve
plt.fill(x, y1, 'b', alpha=0.3)
plt.fill(x, y2, 'r', alpha=0.3)

plt.show()