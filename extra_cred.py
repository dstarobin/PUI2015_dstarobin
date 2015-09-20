import os
import sys

import numpy as np
np.random.seed(1)

first_set = np.random.randn(100,2)

np.random.seed(1)
second_set = 1.5 * np.random.randn(50,2) + (2, 2) 

import matplotlib.pyplot as plt
# can use x,y = zip(*first_set) and x1,y1 = zip(*second_set), 
# but wanted to use zip below

x,y = zip(*first_set)
x1,y1 = zip(*second_set)
fig = plt.figure(facecolor = "w")
#plt.scatter(*zip(*first_set), c = 'r')
#plt.scatter(*zip(*second_set), c = 'b')


default = plt.scatter(x,y, color = "r")
altered = plt.scatter(x1,y1, color = "b")

ax = plt.subplot2grid((1,2),(0, 0))
#ax = fig.add_subplot(121)
plt.scatter(x,y)
plt.scatter(x1,y1)
plt.title('Single Distribution Scatter', fontsize = 44)
plt.xlabel('NumPy Random #s')
plt.ylabel('NumPy Random #s')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()
ax.xaxis.grid(True)
ax.yaxis.grid(True)

ax1 = plt.subplot2grid((1,2),(0, 1))
#ax1 = fig.add_subplot(122)
plt.scatter(x,y, c = 'r')
plt.scatter(x1,y1, c = 'b')
plt.title('Unaltered vs. Altered Scatter', fontsize = 44)
plt.xlabel('NumPy Random #s')
plt.ylabel('NumPy Random #s')
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.get_xaxis().tick_bottom()  
ax1.get_yaxis().tick_left()
ax1.xaxis.grid(True)
ax1.yaxis.grid(True)
plt.legend((default, altered),
			('(unaltered) mu x = .226, mu y = -.013', 
			'(altered) mu x and y= 2, sigma = 2.25'),
			loc = 'upper right')

plt.show()

