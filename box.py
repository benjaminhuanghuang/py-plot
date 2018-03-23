
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.random.randn(1000)  # normal distribution
D = pd.DataFrame([x, x+1]).T   # 
D.plot(kind = 'box')
plt.show()