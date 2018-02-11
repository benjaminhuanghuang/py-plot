# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.style.use('ggplot')

font = FontProperties(fname="simus.ttc", size=12)

ability_size = 6
ability_label = [u'攻击', u'防守', u'力量', u'耐力', u'速度', u'反应']

# create subplot with 2 row3, 2 cols, index 1, 2, 3, 4
ax1 = plt.subplot(221, projection='polar')
ax2 = plt.subplot(222, projection='polar')
ax3 = plt.subplot(223, projection='polar')
ax4 = plt.subplot(224, projection='polar')

players = {
    'M': np.random.randint(size = ability_size, low=60, high=90),
    'H': np.random.randint(size = ability_size, low=60, high=90),
    'P': np.random.randint(size = ability_size, low=60, high=90),
    'Q': np.random.randint(size = ability_size, low=60, high=90)
}
theta = np.linspace(0, 2*np.pi, 6, endpoint=False)

theta = np.append(theta, theta[0])

def setPlot(plot, playerName, color, title):
    player = players[playerName]
    player = np.append(player, player[0])
    plot.plot(theta, player, color)
    plot.fill(theta, player, color, alpha=0.3)
    plot.set_xticks(theta)
    # ax1.set_xticklabels(ability_label, y=0.5, fontproperties = font)  # for chinese
    plot.set_xticklabels(ability_label, y=0.1)
    plot.set_title (title, color=color, size=14)

setPlot(ax1, 'M', 'r', 'Player1')
setPlot(ax2, 'H', 'g', 'Player2')
setPlot(ax3, 'P', 'b', 'Player3')
setPlot(ax4, 'Q', 'y', 'Player4')


plt.show()

