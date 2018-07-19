import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

mu = 100   # mean of distribution
sigma = 20  # standard deviation of distribution
data = mu + sigma * np.random.randn(20000)


plt.hist(data, bins=100, color='r', normed=True)

plt.show() 