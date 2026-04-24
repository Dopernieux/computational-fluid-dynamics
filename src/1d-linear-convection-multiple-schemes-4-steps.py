# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:11:37 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot

nx = 41
nt = 25
sigma = 0.1
c = 1
dx = 0.05
dt = sigma * dx / c

ubd = numpy.zeros(nx)
ucd = numpy.zeros(nx)
u2bde = numpy.zeros(nx)
u2bdi = numpy.zeros(nx)

x = numpy.linspace(0, 2, nx)
for i in range(nx):
    if 0.9 <= x[i] <= 1.0:
        ubd[i] = ucd[i] = u2bde[i] = u2bdi[i] = 10*(x[i]-0.9)
    if 1.0 <= x[i] <= 1.1:
        ubd[i] = ucd[i] = u2bde[i] = u2bdi[i] = 10*(1.1-x[i])

uzero = ubd.copy()

A = numpy.zeros((nx, nx))
r = c * dt / (2 * dx)
A[0, 0] = 1
A[1, 1] = 1
A[-1, -1] = 1
for i in range(2, nx-1):
    A[i, i]   = 1 + 3*r
    A[i, i-1] = -4*r
    A[i, i-2] = r

snap_steps = [0, nt//3, 2*nt//3, nt-1]
snapshots = {s: None for s in snap_steps}

for it in range(nt):
    unbd  = ubd.copy()
    uncd  = ucd.copy()
    un2bde = u2bde.copy()
    un2bdi = u2bdi.copy()

    for i in range(1, nx-1):
        ubd[i]   = unbd[i]   - c*dt/dx*(unbd[i] - unbd[i-1])
        ucd[i]   = uncd[i]   - c*dt/2/dx*(uncd[i+1] - uncd[i-1])
        u2bde[i] = un2bde[i] - c*dt/2/dx*(3*un2bde[i] - 4*un2bde[i-1] + un2bde[i-2])

    b = un2bdi.copy()
    u2bdi = numpy.linalg.solve(A, b)

    if it in snap_steps:
        snapshots[it] = {
            'ubd':   ubd.copy(),
            'ucd':   ucd.copy(),
            'u2bde': u2bde.copy(),
            'u2bdi': u2bdi.copy(),
        }

fig, axes = pyplot.subplots(2, 2, figsize=(12, 8))
fig.suptitle('1D Linear Convection — porównanie schematów', fontsize=13)

for ax, step in zip(axes.flat, snap_steps):
    snap = snapshots[step]
    t_val = step * dt
    ax.plot(x, uzero,        color='gray', linestyle='--', linewidth=1, label='t=0')
    ax.plot(x, snap['ubd'],   label='BD (1st order)')
    ax.plot(x, snap['ucd'],   label='CD (1st order)')
    ax.plot(x, snap['u2bde'], label='2nd order BD explicit')
    ax.plot(x, snap['u2bdi'], label='2nd order BD implicit')
    ax.set_title(f't = {t_val:.3f}  (krok {step})')
    ax.set_xlabel('x')
    ax.set_ylabel('u')
    ax.set_ylim(-0.3, 1.2)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

pyplot.tight_layout()
pyplot.show()