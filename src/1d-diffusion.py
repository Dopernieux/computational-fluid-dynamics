# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:32:22 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 20
nt = 50
sigma = 0.2
dx = 2 / (nx-1)
vis = 0.1
dt = sigma * dx**2 / vis

u = numpy.ones(nx)

u[int(0.5 / dx):int(1 / dx + 1)] = 2

un = numpy.ones(nx)
        
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] + vis * dt / dx**2 * (un[i+1]-2*un[i]+un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx), u);
        
pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} = \nu\frac{\partial^2 u}{\partial x^2}$',
            transform=pyplot.gca().transAxes,
            fontsize=13)

pyplot.legend()
pyplot.show()