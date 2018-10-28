#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 00:38:34 2018

@author: gabriel
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(X,Y):
    return X**2 + Y**2;
def N(x,y):
    return np.array([-2 * x, -2 * y, 1]) / np.sqrt(4 * x**2 + 4 * y**2 + 1);


#surface
X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 500),np.linspace(-1.5, 1.5, 500))
Z = f(X, Y)

#physical constants
g = 9.8
m = 1
pos = np.array([1, 0, f(1, 0)], dtype = 'double')
v = np.array([2, 2, 0], dtype = 'double')

#remove normal component of speed
v -= np.dot(v, N(pos[0], pos[1])) * N(pos[0], pos[1])

time_iterations = 8000
t_span = np.arange(time_iterations)
delta_t = 0.001
G = m * g * np.array([0, 0, -1])

fig = plt.figure(1)
ax = Axes3D(fig)

#top view
ax.view_init(elev=90., azim=0)
#side view
#ax.view_init(elev=10., azim=0)
#top-side view
#ax.view_init(elev=45., azim=35)


line = np.array(pos)
for t in t_span:
    #compute accelerationn
    A = (G - np.dot(G, N(pos[0], pos[1])) * N(pos[0], pos[1])) / m
    #compute new speed
    v += delta_t * A
    #remove normal composant
    v -= np.dot(v, N(pos[0], pos[1])) * N(pos[0], pos[1])
    #compute new position
    pos += v * delta_t
    
    #add new position to line
    line = np.vstack((line, pos))
    ##plot
    if (t % 100 == 0):
        ax.clear()
        ax.plot_surface(X, Y, Z, alpha = 0.5, cmap = 'viridis')
        ax.scatter3D(pos[0], pos[1], pos[2], c = "k")
        ax.plot3D(line[:,0], line[:,1], line[:,2], c = 'k')
        ax.set_aspect(1)
        #plt.pause(0.01)
        fig.savefig("./pictures3D/frame" + str(t) + ".jpg")
