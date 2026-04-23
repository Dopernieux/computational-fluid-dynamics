# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
import time, sys

nx = 20
ny = 20
nt = 50
dt = 0.01
c = 1
dx = 2 / (nx-1)
dy = 2 / (ny-1)

u = numpy.zeros((nx, ny))

for i in range(nx):
    for j in range(ny):
        if i > 5 and i < 10 and j > 5 and j < 10:
            u[i, j] = 2
        else:
            u[i, j] = 1
        
u[0, 0] = 1
u[-1, -1] = 1

un = numpy.array([nx, ny])
        
for it in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = un[i,j] - c*(dt/dx)*(un[i,j]-un[i-1,j]) - c*(dt/dy)*(un[i,j]-un[i,j-1])
        

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

pyplot.contourf(X, Y, u, cmap='viridis')
pyplot.colorbar(label='u')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show
      
'''  
pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} + \c\frac{\partial u}{\partial x} + \c\frac{\partial u}{\partial y}= \0$',
            transform=pyplot.gca().transAxes,
            fontsize=13)
'''
pyplot.legend()
pyplot.show()