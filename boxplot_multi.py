
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


np.random.seed(100)
data = np.random.normal(size=(1000,4), loc=0, scale=1)  # 4 groups
labels= ['A', 'B', 'C', 'D']
plt.boxplot(data, labels=labels)
plt.show()
