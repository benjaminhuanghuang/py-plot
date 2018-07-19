import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

n = 1024
# create 1024 numbers, mean is 0 , sd is 1
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # color

plt.scatter(X, Y, s = 75, c= T, alpha = 0.5)
plt.scatter(np.arange(5), np.arange(5), c= 'r')
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
# hide all ticks
plt.xticks(())  
plt.xticks(())   
plt.show()
