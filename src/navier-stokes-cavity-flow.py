# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:27:32 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

nx = 41
ny = 41
sigma = 0.015
nu = 0.05
rho = 1
F = 1

dx = 2 / (nx-1)
dy = 2 / (ny-1)
dt = 0.005 #sigma * dx * dy / nu

x = numpy.linspace(0 , 2, nx)
y = numpy.linspace(0 , 2, ny)
X, Y = numpy.meshgrid(x, y)

u = numpy.zeros((nx, ny))
v = numpy.zeros((nx, ny))
p = numpy.zeros((nx, ny))
c = numpy.ones((nx, ny))

#history = [u.copy()]

def cavity(nt):
    
    u[int(.5 / dx): int(1 / dx + 1), int(.5 / dy): int(1 / dy + 1)] = 2
    v[int(.5 / dx): int(1 / dx + 1), int(.5 / dy): int(1 / dy + 1)] = 2
    p[int(.5 / dx): int(1 / dx + 1), int(.5 / dy): int(1 / dy + 1)] = 2
    
    pn = numpy.empty_like(p)
    pn = p.copy()
    
    for n in range(nt):
        un = u.copy()
        vn = v.copy()
        pn = p.copy()
        
        u[1:-1,1:-1] = (un[1:-1,1:-1]) 
        - (un[1:-1,1:-1]*(dt/dx)*(un[1:-1,1:-1]-un[0:-2,1:-1])) 
        - (vn[1:-1,1:-1]*(dt/dy)*(un[1:-1,1:-1]-un[1:-1,0:-2])) 
        - ((1/rho)*(dt/(2*dx))*(pn[2:,1:-1]-pn[0:-2,1:-1])) 
        + (nu*(dt/(dx**2))*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])) 
        + (nu*(dt/(dy**2))*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2]))
        + F*dt
        
        v[1:-1,1:-1] = (vn[1:-1,1:-1]) 
        - (un[1:-1,1:-1]*(dt/dx)*(vn[1:-1,1:-1]-vn[0:-2,1:-1])) 
        - (vn[1:-1,1:-1]*(dt/dy)*(vn[1:-1,1:-1]-vn[1:-1,0:-2])) 
        - ((1/rho)*(dt/(2*dx))*(pn[2:,1:-1]-pn[1:-1,0:-2])) 
        + (nu*(dt/(dx**2))*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[0:-2,1:-1])) 
        + (nu*(dt/(dy**2))*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2]))
        
        p[1:-1,1:-1] = ((pn[2:,1:-1]+pn[0:-2,1:-1])*(dy**2) 
        + (pn[1:-1,2:]+pn[1:-1,0:-2])*(dx**2)) / (2*((dx**2)+(dy**2))) 
        - (((rho*(dx**2)*(dy**2))/(2*((dx**2)+(dy**2))))
        * (((1/dt)*(((un[2:,1:-1]-un[0:-2,1:-1])/(2*dx))
        + ((vn[1:-1,2:]-vn[1:-1,0:-2])/(2*dy)))) 
        - (((un[2:,1:-1]-un[0:-2,1:-1])/(2*dx))**2) 
        - (2*((vn[2:,1:-1]-vn[0:-2,1:-1])/(2*dx))
        * ((un[1:-1,2:]-un[1:-1,0:-2])/(2*dy))) 
        - (((vn[1:-1,2:]-vn[1:-1,0:-2])/(2*dy))**2)))
        
        u[0, :] = 0; u[-1, :] = 0; # u[:, 0] = 1; u[:, -1] = 0
        v[0, :] = 0; v[-1, :] = 0; # v[:, 0] = 0; v[:, -1] = 0
        p[0, :] = p[1, :]; p[-1, :] = p[-2, : ]; p[:, 0] = p[:, 2]; p[:, -1] = p[:, -2]; p[0, 0] = 0
        
        #history.append(u.copy())
        
cavity(100)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.contourf(X, Y, p, alpha=0.5, cmap='viridis')
pyplot.colorbar()
pyplot.contour(X, Y, p, cmap='viridis')
pyplot.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])
pyplot.xlabel('X')
pyplot.ylabel('Y')
        
        