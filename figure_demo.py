import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

# create 50 linear space from -1 to 1
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1

y2 = x ** 2
plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(8,5))
plt.plot(x, y2)
plt.plot(x, y1, color='r', linewidth=3.0, linestyle='-')

plt.show()