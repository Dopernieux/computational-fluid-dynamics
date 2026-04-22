# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:32:22 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
import time, sys

nx = 20
nt = 50
dt = 0.1
vis = 0.1
dx = 2 / (nx-1)

u = numpy.ones(nx)

for i in range(nx):
    if i > 5 and i < 10:
        u[i] = 2
    else:
        u[i] = 1
        
u[0] = 1
u[-1] = 1

un = numpy.ones(nx)
        
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - vis * dt / dx / dx * (un[i+1]-2*un[i]+un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx), u);
        
pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} = \nu\frac{\partial^2 u}{\partial x^2}$',
            transform=pyplot.gca().transAxes,
            fontsize=13)

pyplot.legend()
pyplot.show()