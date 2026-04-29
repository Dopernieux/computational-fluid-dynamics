# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:32:22 2026

@author: szczv

Twierdzenie Burgersa, rozwiązanie numeryczne (u) i analityczne (un)
"""

import numpy
import sympy
from matplotlib import pyplot
from sympy import init_printing
init_printing(use_latex=True)
from sympy.utilities.lambdify import lambdify

x, nu, t = sympy.symbols('x nu t')

phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) + sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))

phiprime = phi.diff(x)

u = -2 * nu * (phiprime / phi) + 4

ufunc = lambdify((t, x, nu), u)
print(ufunc(1, 4, 3))


'''
nx = 50
nt = 50
dt = 0.01
vis = 0.1
dx = 2 * numpy.pi / (nx-1)

u = numpy.ones(nx)
ua = numpy.ones(nx)
ip1 = numpy.ones(nx, dtype=int)
im1 = numpy.ones(nx, dtype=int)
x = numpy.copy(u)


for i in range(nx):
    ip1[i] = i+1
    im1[i] = i-1
    x[i] = (i-1)*dx
    
ip1[nx-1] = 0
im1[0] = nx-1

for i in range(nx):
    phi = numpy.exp(-(x[i]**2)/(4*vis)) + numpy.exp((-(x[i]-2*(numpy.pi))**2/(4*vis)))
    
    dphi = (-(1/2)*(x[i]/vis))*numpy.exp(-(x[i]**2)/(4*vis))+((-(x[i]-2*(numpy.pi)))/(2*vis))*numpy.exp((-(x[i]-2*(numpy.pi))**2/(4*vis)))
    
    u[i] = (-2)*vis*(dphi/phi)+4


for it in range(nt):
    t = it*dt
    
    un = numpy.copy(u)
    
    for i in range(nx):
        u[i] = un[i]-un[i]*(dt/dx)*( un[i] - un[im1[i]]) + vis * (dt/(dx**2)) * (un[ip1[i]]-2*un[i]+un[im1[i]])
        
    for i in range(nx):
        phi = numpy.exp( -(x[i]-4*t)**2 / (4*vis*(t+1))) + numpy.exp(-(x[i]-4*t-2*numpy.pi)**2/(4*vis*(t+1)))
        
        dphi = ((-1/(2*vis*(t+1)))*(x[i]-4*t) * numpy.exp(-(x[i]-4*t)**2 / (4*vis*(t+1))) + ((-1/(2*vis*(t+1)))*(x[i]-4*t-2*numpy.pi)*numpy.exp(-(x[i]-4*t-2*numpy.pi)**2/(4*vis*(t+1)))))
        
        ua[i] = -2*vis*(dphi/phi)+4

pyplot.plot(numpy.linspace(0, 2*(numpy.pi), nx), u, label='numeryczne')
pyplot.plot(numpy.linspace(0, 2*(numpy.pi), nx), ua, label='analityczne')

pyplot.text(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \nu\frac{\partial^2 u}{\partial x^2}$',
            transform=pyplot.gca().transAxes,
            fontsize=13)

pyplot.legend()
pyplot.show()
'''

    
    