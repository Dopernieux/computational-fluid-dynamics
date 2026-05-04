# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

nx = 31
ny = 31
nt = 17
sigma = 0.25
vis = 0.05
dx = 2 / (nx-1)
dy = 2 / (ny-1)
dt = sigma * dx * dy /vis

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((nx, ny))

history = [u.copy()]

def diffusion(nt):

    u[int(.5 / dx): int(1 / dx + 1), int(.5/ dy): int(1.5 / dy + 1)] = 2
              
    for it in range(nt + 1):
        un = u.copy()
        u[1:-1,1:-1] = un[1:-1,1:-1] + (vis*(dt/(dx**2))*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[:-2,1:-1])) + (vis*(dt/(dy**2))*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,:-2]))
         
        u[0, :] = 1; u[-1, :] = 1; u[:, 0] = 1; u[:, -1] = 1
        
        history.append(u.copy())
    
diffusion(17)

X, Y = numpy.meshgrid(x, y)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')
surf = [ax.plot_surface(X, Y, history[0].T, cmap='plasma', linewidth=0, antialiased=False)]
fig.colorbar(surf[0], ax=ax, label='u')
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(1, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
title = ax.set_title('')

def update(frame):
    surf[0].remove()
    surf[0] = ax.plot_surface(X, Y, history[frame].T, cmap='plasma', linewidth=0, antialiased=False)
    title.set_text(f't = {frame * dt:.4f} (krok {frame})')
    return surf[0], title

anim = FuncAnimation(fig, update, frames=len(history), interval=100)
ax.text2D(0.02, 0.02,
            r'$\frac{\partial u}{\partial t} = \nu\frac{\partial^2 u}{\partial x^2} + \nu\frac{\partial^2 u}{\partial y^2}$',
            transform=ax.transAxes,
            fontsize=11)
anim.save('2d_diffusion.gif', writer='pillow', fps=10)

pyplot.show()