import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# r = np.arange(1, 6, 1)
r = np.empty(5)
r.fill(5)

theta = [0,
         np.pi/2,
         np.pi,
         np.pi/2 * 3,
         2*np.pi]

ax = plt.subplot(111, projection='polar')   # polar cooridate
ax.plot(theta, r, color='r', linewidth=2)
ax.grid(True)


plt.show()