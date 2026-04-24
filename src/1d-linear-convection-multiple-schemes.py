# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:11:37 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 41
nt = 6
sigma = 0.8
c = 1
dx = 0.05
dt = sigma * dx / c

ubd = numpy.zeros(nx)   # BD in x
ucd = numpy.zeros(nx)   # CD in x
u2bde = numpy.zeros(nx) # 2nd order BD in x (explicit)
u2bdi = numpy.zeros(nx) # 2nd order BD in x (implicit)
# ulw = numpy.zeros(nx)   # Lax-Wendroff - 2n order BD in x and in t

unbd = numpy.zeros(nx)   # BD in x
uncd = numpy.zeros(nx)   # CD in x
un2bde = numpy.zeros(nx)   # 2nd order BD in x (explicit)
un2bdi = numpy.zeros(nx)   # 2nd order BD in x (implicit)
# unlw = numpy.zeros(nx)   # Lax-Wendroff - 2n order BD in x and in t

uzero = numpy.zeros(nx)
x = numpy.linspace(0, 2, nx)

for i in range(nx):
    if 0.9 <= x[i] and x[i] <= 1:
        ubd[i] = 10*(x[i]-0.9)
        ucd[i] = 10*(x[i]-0.9)
        u2bde[i] = 10*(x[i]-0.9)
        u2bdi[i] = 10*(x[i]-0.9)
        # ulw[i] = 10*(x[i]-0.9)
    if 1.0 <= x[i] and x[i] <= 1.1:
        ubd[i] = 10*(1.1-x[i])
        ucd[i] = 10*(1.1-x[i])
        u2bde[i] = 10*(1.1-x[i])
        u2bdi[i] = 10*(1.1-x[i])
        # ulw[i] = 10*(1.1-x[i])
        
uzero[:] = ubd[:]
        
A = numpy.zeros((nx, nx))
r = c * dt / (2 * dx)
A[0, 0] = 1
A[1, 1] = 1
A[-1, -1] = 1

for i in range(2, nx-1):
    A[i, i] = 1 + 3*r
    A[i, i-1] = -4*r
    A[i, i-2] = r
    
for it in range(nt):
    unbd = ubd.copy()
    uncd = ucd.copy()
    un2bde = u2bde.copy()
    un2bdi = u2bdi.copy()
    # unlw = ulw.copy()
    for i in range(1, nx-1):
        
        # BD in x:
        ubd[i] = unbd[i] - c*dt/dx*( unbd[i]-unbd[i-1] )
        
        # CD in x:
        ucd[i] = uncd[i] - c*dt/2/dx*( uncd[i+1] - uncd[i-1] )
        
        # 2nd order BD in x (explicit)
        u2bde[i] = un2bde[i] - c*dt/2/dx*( 3*un2bde[i] - 4*un2bde[i-1] + un2bde[i-2])
    
    # 2nd order BD in x (implicit)
    b = un2bdi.copy()
    u2bdi = numpy.linalg.solve(A, b)
    
pyplot.plot(numpy.linspace(0, 2, nx), ubd, label='BD in x');
pyplot.plot(numpy.linspace(0, 2, nx), ucd, label='CD in x');
pyplot.plot(numpy.linspace(0, 2, nx), u2bde, label='2nd order BD in x (explicit)');
pyplot.plot(numpy.linspace(0, 2, nx), u2bdi, label='2nd order BD in x (implicit)');

pyplot.legend()