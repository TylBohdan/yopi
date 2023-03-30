from math import sin, cos

import numpy as np
from matplotlib import pyplot as plt, animation
from numpy import linspace


def initpict():
    plt.title('Animation')
    plt.xlabel('X')
    plt.ylabel('Y')


fig = plt.figure(figsize=(7, 7), facecolor='white')
ax = plt.axes(xlim=(-15, 15), ylim=(-15, 15))
ax.grid = (True)
line, = ax.plot([], [], '*', lw=5)


def redraw(i):
    t = np.linspace(-20, 20, 1)
    if i >= 100:
        y = 9 * np.sin(t - i / 10) - np.sin(t - i / 10)
        x = 9 * np.cos(t - i / 10) + np.cos(9 * (t - i / 10))
    else:
        y = 9 * np.sin(t - 20 + i / 10) - np.sin(t - 20 + i / 10)
        x = 9 * np.cos(t - 20 + i / 10) + np.cos(9 * (t - 20 + i / 10))

    line.set_data(x, y)


t = np.linspace(-20, 20, 1000)
y1 = 9 * np.sin(t) - np.sin(9 * t)
x1 = 9 * np.cos(t) + np.cos(9 * t)
plt.plot(x1, y1, lw=1, c='maroon')
anim = animation.FuncAnimation(fig, redraw, frames=200, init_func=initpict, interval=10, repeat=True)
plt.show()
anim.save(filename='PM-EXAM.gif')

