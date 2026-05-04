# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

nx = 41
ny = 41
nt = 50
sigma = 0.0015
nu = 0.01
dx = 2 / (nx-1)
dy = 2 / (ny-1)
dt = sigma * dx * dy / nu

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

u = numpy.ones((nx, ny))
v = numpy.ones((nx, ny))

history = [u.copy()]

def diffusion(nt):

    u[int(.1 / dx): int(.4 / dx + 1), int(.1/ dy): int(.4 / dy + 1)] = 2
    v[int(.1 / dx): int(.4 / dx + 1), int(.1/ dy): int(.4 / dy + 1)] = 2
              
    for it in range(nt + 1):
        un = u.copy()
        vn = v.copy()
        
        u[1:-1,1:-1] = un[1:-1,1:-1] - dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) - dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) + nu * dt / dx**2 * (un[1:-1,2:] - 2 * un[1:-1,1:-1] + un[1:-1, 0:-2]) + nu * dt / dy**2 * (un[2:,1:-1] - 2 * un[1:-1,1:-1] + un[0:-2, 1:-1])
        v[1:-1,1:-1] = vn[1:-1,1:-1] - dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) - dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) + nu * dt / dx**2 * (vn[1:-1,2:] - 2 * vn[1:-1,1:-1] + vn[1:-1, 0:-2]) + nu * dt / dy**2 * (vn[2:,1:-1] - 2 * vn[1:-1,1:-1] + vn[0:-2, 1:-1])             
        
        u[0, :] = 1; u[-1, :] = 1; u[:, 0] = 1; u[:, -1] = 1
        v[0, :] = 1; v[-1, :] = 1; v[:, 0] = 1; v[:, -1] = 1
        
        history.append(u.copy())
    
diffusion(100)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')
surf = [ax.plot_surface(X, Y, history[0].T, cmap='plasma',
                        linewidth=0, antialiased=False)]
fig.colorbar(surf[0], ax=ax, label='u')
ax.set_xlim(0, 2); ax.set_ylim(0, 2); ax.set_zlim(1, 2)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('u')
ax.text2D(0.02, 0.02,
          r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} = \nu\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)$',
          transform=ax.transAxes, fontsize=9)
title = ax.set_title('')

def update(frame):
    surf[0].remove()
    surf[0] = ax.plot_surface(X, Y, history[frame].T, cmap='plasma',
                              linewidth=0, antialiased=False)
    title.set_text(f't = {frame * dt:.4f}  (krok {frame})')
    return surf[0], title

anim = FuncAnimation(fig, update, frames=len(history), interval=100)
anim.save('2d_burgers.gif', writer='pillow', fps=10)
pyplot.show()