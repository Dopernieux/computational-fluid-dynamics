# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 101
ny = 101
nt = 80
sigma = 0.2
dx = 2 / (nx-1)
dy = 2 / (ny-1)
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.zeros((nx, ny))
v = numpy.zeros((nx, ny))

def bc():
    u[int(.5/ dx): int(1.5 / dx + 1), int(.5/ dy): int(1.5 / dy + 1)] = 2
    v[int(.5/ dx): int(1.5 / dx + 1), int(.5/ dy): int(1.5 / dy + 1)] = 2

'''
for i in range(nx):
    for j in range(ny):
        if i > 5 and i < 10 and j > 5 and j < 10:
            u[i, j] = 2
            v[i, j] = 2
        else:
            u[i, j] = 1
            v[i, j] = 1
'''
'''       
u[0, 0] = 1
u[-1, -1] = 1
v[0, 0] = 1
v[-1, -1] = 1
'''

def computation():
    for it in range(nt):
        un = u.copy()
        vn = v.copy()
        u[1:,1:] = un[1:,1:] - un[1:,1:]*(dt/dx)*(un[1:,1:]-un[:-1,1:]) - vn[1:,1:]*(dt/dy)*(un[1:,1:]-un[1:,:-1])
        v[1:,1:] = vn[1:,1:] - vn[1:,1:]*(dt/dx)*(vn[1:,1:]-vn[:-1,1:]) - un[1:,1:]*(dt/dy)*(vn[1:,1:]-vn[1:,:-1])
        
        u[0, :] = 0; u[-1, :] = 0; u[:, 0] = 0; u[:, -1] = 0
        v[0, :] = 0; v[-1, :] = 0; v[:, 0] = 0; v[:, -1] = 0
'''
for it in range(nt):
    un = u.copy()
    vn = v.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = un[i,j] - un[i,j]*(dt/dx)*(un[i,j]-un[i-1,j]) - vn[i,j]*(dt/dy)*(un[i,j]-un[i,j-1])
            
            v[i,j] = vn[i,j] - vn[i,j]*(dt/dx)*(vn[i,j]-vn[i-1,j]) - un[i,j]*(dt/dy)*(vn[i,j]-vn[i,j-1])
'''

bc()
computation()

X, Y = numpy.meshgrid(x, y)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u.T, cmap='plasma')
fig.colorbar(surf, ax=ax, label='u')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
ax.set_title('2D Convection')
ax.text2D(0.02, 0.02,
            r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y}= 0$'
            '\n'
            r'$\frac{\partial v}{\partial t} + v\frac{\partial v}{\partial x} + u\frac{\partial v}{\partial y}= 0$',
            transform=ax.transAxes,
            fontsize=11)
pyplot.show()
