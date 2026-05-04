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
b = numpy.zeros((nx, ny))

history = [p.copy()]

def poisson(nit):
    b[nx//4, ny//4] = 100
    b[3*(nx-1)//4, 3*(ny-1)//4] = -100
    
    for iit in range(nit):
        pd = p.copy()
        p[1:-1,1:-1] = (((pd[2:,1:-1] + pd[0:-2,1:-1])*dy**2 + (pd[1:-1,2:] + pd[1:-1,0:-2])*dx**2) - b[1:-1,1:-1]*dx**2*dy**2) / (2*(dx**2+dy**2))
        
        p[0,:]=0; p[-1,:]=0; p[:,0]=p[:,1]; p[:,-1]=p[:,-2]
        
        history.append(p.copy())

poisson(100)

X, Y = numpy.meshgrid(x, y)

fig, ax = pyplot.subplots(figsize=(7, 5), dpi=72)
title = ax.set_title('')

def update(frame):
    ax.cla()
    cf = ax.contourf(X, Y, history[frame].T, cmap='plasma', levels=20)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.text(0.02, 0.02,
            r'$\frac{\partial^2 p}{\partial x^2} + \frac{\partial^2 p}{\partial y^2} = b$',
            transform=ax.transAxes, fontsize=11)
    ax.set_title(f'iteracja {frame * 10}')
    return cf,

anim = FuncAnimation(fig, update, frames=len(history), interval=100)
anim.save('2d_poisson.gif', writer='pillow', fps=10)
pyplot.show()