import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
'''
scatter options
    c: color
    s: size
    alpha
    marker
'''
height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 69, 55]
plt.scatter(height, weight, s= 100, c='r', marker='<', alpha=0.5)
plt.show()
