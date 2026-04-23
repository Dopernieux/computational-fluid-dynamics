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
dt = 0.01
dx = 2 / (nx-1)
dy = 2 / (ny-1)

u = numpy.zeros((nx, ny))
v = numpy.zeros((nx, ny))

for i in range(nx):
    for j in range(ny):
        if i > 5 and i < 10 and j > 5 and j < 10:
            u[i, j] = 2
            v[i, j] = 2
        else:
            u[i, j] = 1
            v[i, j] = 1
'''       
u[0, 0] = 1
u[-1, -1] = 1
v[0, 0] = 1
v[-1, -1] = 1
'''
un = numpy.array([nx, ny])
vn = numpy.array([nx, ny])
        
for it in range(nt):
    un = u.copy()
    vn = v.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = un[i,j] - un[i,j]*(dt/dx)*(un[i,j]-un[i-1,j]) - vn[i,j]*(dt/dy)*(un[i,j]-un[i,j-1])
            
            v[i,j] = vn[i,j] - vn[i,j]*(dt/dx)*(vn[i,j]-vn[i-1,j]) - un[i,j]*(dt/dy)*(vn[i,j]-vn[i,j-1])

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

pyplot.contourf(X, Y, u, cmap='viridis')
pyplot.colorbar(label='u')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y}= 0$'
            '\n'
            r'$\frac{\partial v}{\partial t} + v\frac{\partial v}{\partial x} + u\frac{\partial v}{\partial y}= 0$',
            transform=pyplot.gca().transAxes,
            fontsize=11)
pyplot.show()