# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:05:55 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 20
ny = 20
nit = 1000
dx = 2 / (nx-1)
dy = 1 / (ny-1)

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 1, ny)
X, Y = numpy.meshgrid(x, y)

p = numpy.zeros((nx, ny))
p[nx-1, :] = y
pn = 0

fig, axes = pyplot.subplots(2, 1, figsize=(5, 8))
snapshots = []

for iit in range(1, nit):
    pd = numpy.copy(p)
    for i in range(2, nx-1):
        for j in range(2, ny-1):
            p[i,j] = (pd[i+1,j] + pd[i-1,j])*dy**2+(pd[i,j+1]+pd[i,j-1])*dx**2/(dx**2+dy**2)/2
    p[2:nx-2,1]=p[2:nx-2,2]
    p[2:nx-2,ny-1]=p[2:nx-2,ny-2]
    
    if iit in [0, nit//3, 2*nit//3, nit-1]:
        snapshots.append((iit, numpy.copy(p)))

for ax, (iit, snap) in zip(axes.flat, snapshots):
    cf = ax.contourf(X, Y, snap.T, cmap='magma', levels=20)
    ax.set_title('')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    pyplot.colorbar(cf, ax=ax)
