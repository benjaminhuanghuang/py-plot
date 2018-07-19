import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

x = np.arange(1,11,1)

plt.plot(x,x)

# Method 1
plt.locator_params('x',nbins=5)

# Method 2, using axis object
ax = plt.gca()   # get current axis

ax.locator_params(nbins=5)
ax.locator_params('x',nbins=5)

plt.show()