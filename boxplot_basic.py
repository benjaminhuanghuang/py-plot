
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


np.random.seed(100)
data = np.random.normal(size=10000, loc=0, scale=1)

plt.boxplot(data, sym="o", whis=1.5)
plt.show()
