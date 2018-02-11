# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.style.use('ggplot')

font = FontProperties(fname="simus.ttc", size=18)

ability_size = 6
ability_lable = [u'攻击', u'防守', u'力量', u'耐力', u'速度', u'反应']

ax1 = plt.subplot(221, projection='polar')
ax1 = plt.subplot(221, projection='polar')
ax1 = plt.subplot(221, projection='polar')
ax1 = plt.subplot(221, projection='polar')

player = [
    'M': np.random.randint(size = ability_size, low=60, high=90),
    'H': np.random.randint(size = ability_size, low=60, high=90),
    'P': np.random.randint(size = ability_size, low=60, high=90),
    'Q': np.random.randint(size = ability_size, low=60, high=90)
]
theta = np.linspace(0, 2*np.pi, 6, endpoint=False)

theta = np.append(theta, theta[0])

player['M'] = np.append(planyer['M'], player['M'][0])

ax1.plot[]

