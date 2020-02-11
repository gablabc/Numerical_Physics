#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys

savefig = False
if not len(sys.argv) == 1:
    if sys.argv[1] == 'savefig':
        savefig = True
    
# x**2
#def f(x):
#    return x**2
#def fp(x):
#    return 2*x

# 1-2x**2+x**4
def f(x):
    return 1 - 2 * x**2 + x**4
def fp(x):
    return -4 * x + 4 * x**3

def theta(x):
    return np.arctan(fp(x))

# Physical constants
g = 1
m = 1
x = np.linspace(-2, 2, 1000)
y = f(x)
v_norm = 0
pos = [-1.7, f(-1.7)]
v = [0, 0]
direction = -1 * np.sign(fp(pos[0]))
E = m * g * f(pos[0])

# Time
# the maximal time will time_iterations*delta_t
time_iterations = 2000
delta_t = 0.01
t_span = np.arange(time_iterations)


fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_ylim(-0.5, 4)
lines = [0, 0, 0, 0]

# Time loop for the whole simulation
for t in t_span:
    if ((t % 10) == 0):
        # Plot current position
        lines[0], = ax.plot(pos[0], pos[1], "ko")
        lines[1] = ax.text(-1, 2, "Energy = "+ str(np.around(1 / 2 * m * v_norm**2 + m * g * pos[1], decimals = 2)))
        lines[2] = ax.text(-1, 2.2,"K = "+ str(np.around(1/2 * m * v_norm**2, decimals = 2)))
        lines[3] = ax.text(-1, 2.4,"U = "+ str(np.around(m * g * pos[1], decimals = 2)))
        
        if(savefig):
            fig.savefig("./pictures2D/frame" + str(t) + ".jpg")
        else:
            plt.pause(0.01)

        # Remove the plots except the curve
        for i in range(4):
            lines[i].remove()


    # New speed using energy conservation#
    # particule reaches its apex        
    if (2 / m * (E - m * g * f(pos[0])) <= 0):
        direction = -1 * np.sign(fp(pos[0]))
        pos[0] += 0.01 * direction
        pos[1] = f(pos[0])
    else:
        # Calculate new speed
        v_norm = np.sqrt(2 / m * (E - m * g * f(pos[0])))
        v = v_norm * direction * np.array([np.cos(theta(pos[0])), np.sin(theta(pos[0]))])
        pos += delta_t*v
