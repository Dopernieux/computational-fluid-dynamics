# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:05:55 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

nx = 20
ny = 20
nit = 100
dx = 2 / (nx-1)
dy = 1 / (ny-1)

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 1, ny)
X, Y = numpy.meshgrid(x, y)

p = numpy.zeros((nx, ny))

history = [p.copy()]

def laplace(nit):
    
    
    for iit in range(1, nit):
        pd = numpy.copy(p)
        p[1:-1,1:-1] = ((pd[2:,1:-1] + pd[0:-2,1:-1])*dy**2+(pd[1:-1,2:]+pd[1:-1,0:-2])*dx**2) / (2*(dx**2+dy**2))
        
        p[0,:]=0; p[-1, :] = y; p[:, 0] = p[:, 1]; p[:, -1] = p[:, -2]
        
        history.append(p.copy())

laplace(100)

X, Y = numpy.meshgrid(x, y)

fig, ax = pyplot.subplots(figsize=(7, 5), dpi=72)
title = ax.set_title('')

def update(frame):
    ax.cla()
    cf = ax.contourf(X, Y, history[frame].T, cmap='plasma', levels=20)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.text(0.02, 0.02,
            r'$\frac{\partial^2 p}{\partial x^2} + \frac{\partial^2 p}{\partial y^2} = 0$',
            transform=ax.transAxes, fontsize=11)
    ax.set_title(f'iteracja {frame * 10}')
    return cf,

anim = FuncAnimation(fig, update, frames=len(history), interval=100)
anim.save('2d_laplace.gif', writer='pillow', fps=10)
pyplot.show()