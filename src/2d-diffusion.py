# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 20
ny = 20
nt = 50
dt = 0.025
vis = 0.1
dx = 2 / (nx-1)
dy = 2 / (ny-1)

u = numpy.zeros((nx, ny))

for i in range(nx):
    for j in range(ny):
        if i > 5 and i < 10 and j > 5 and j < 10:
            u[i, j] = 2
        else:
            u[i, j] = 1
    
u[0, :] = 1
u[-1, :] = 1
u[:, 0] = 1
u[:, -1] = 1
        
for it in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = un[i,j] + (vis*(dt/(dx**2))*(un[i-1,j]-2*un[i,j]+un[i+1,j])) + (vis*(dt/(dy**2))*(un[i,j-1]-2*un[i,j]+un[i,j+1]))
            

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

pyplot.contourf(X, Y, u.T, cmap='viridis')
pyplot.colorbar(label='u')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} = \nu(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2})$',
            transform=pyplot.gca().transAxes,
            fontsize=11)
pyplot.show()