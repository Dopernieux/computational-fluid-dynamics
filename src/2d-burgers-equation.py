# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:51:03 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 50
ny = 50
nt = 50
dt = 0.001
vis = 0.4
dx = 2 / (nx-1)
dy = 2 / (ny-1)

u = numpy.zeros((nx, ny))
v = numpy.zeros((nx, ny))


for i in range(nx):
    for j in range(ny):
        if i > nx//2 - 5 and i < nx//2 + 5 and j > ny//2 - 5 and j < ny//2 + 5:
            u[i, j] = 2
            v[i, j] = 2
        else:
            u[i, j] = 1
            v[i, j] = 1

fig, axes = pyplot.subplots(2, 2, figsize=(10, 8))
snapshots = []

for it in range(nt):
    un = numpy.copy(u)
    vn = numpy.copy(v)
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u[i,j] = un[i,j] - un[i,j]*(dt/dx)*(un[i,j]-un[i-1,j]) - vn[i,j]*(dt/dy)*(un[i,j]-un[i,j-1]) + vis*(dt/(dx**2))*(un[i-1,j]-2*un[i,j]+un[i+1,j]) + vis*(dt/(dy**2))*(un[i,j-1]-2*un[i,j]+un[i,j+1])
            
            v[i,j] = vn[i,j] - un[i,j]*(dt/dx)*(vn[i,j]-vn[i-1,j]) - vn[i,j]*(dt/dy)*(vn[i,j]-vn[i,j-1]) + vis*(dt/(dx**2))*(vn[i-1,j]-2*vn[i,j]+vn[i+1,j]) + vis*(dt/(dy**2))*(vn[i,j-1]-2*vn[i,j]+vn[i,j+1])
            
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

    if it in [0, nt//3, 2*nt//3, nt-1]:
        snapshots.append((it, numpy.copy(u)))
    
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

for ax, (it, snap) in zip(axes.flat, snapshots):
    cf = ax.contourf(X, Y, snap.T, cmap='magma', levels=20)
    ax.set_title(f't = {it*dt:.3f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    pyplot.colorbar(cf, ax=ax)
    
'''
pyplot.contourf(X, Y, u.T, cmap='viridis')
pyplot.colorbar(label='u')
pyplot.xlabel('x')
pyplot.ylabel('y')
'''

pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} = \nu(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2})$'
            '\n'
            r'$\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x} + v\frac{\partial v}{\partial y} = \nu(\frac{\partial^2 v}{\partial x^2}+\frac{\partial^2 v}{\partial y^2})$',
            transform=pyplot.gca().transAxes,
            fontsize=13)

pyplot.show()