# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:16:34 2026

@author: szczv
"""

import numpy
import timeit
from matplotlib import pyplot

nx = 60
ny = 60
nt = 50
dt = 0.01
c = 1
dx = 2 / (nx-1)
dy = 2 / (ny-1)

u = numpy.ones((nx, ny))

def b_table():
    u[int(.5 / dx): int(1 / dx + 1), int(.5 / dy): int(1 / dy + 1)] = 2

def b_loop():
    for i in range(nx):
        for j in range(ny):
            if i > 5 and i < 10 and j > 5 and j < 10:
                u[i, j] = 2 
                
def c_array():     
    for it in range(nt):
        un = u.copy()
        u[1:, 1:] = un[1:,1:] - c*(dt/dx)*(un[1:,1:]-un[0:-1,1:]) - c*(dt/dy)*(un[1:,1:]-un[1:,0:-1])
        
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1
        
def c_raw():
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u[i,j] = un[i,j] - c*(dt/dx)*(un[i,j]-un[i-1,j]) - c*(dt/dy)*(un[i,j]-un[i,j-1])    
                
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1
if __name__ == '__main__':
    setup = "from __main__ import b_table, b_loop, c_raw, c_array, u"
    
    t_b_table_c_raw = timeit.timeit("b_table(); c_raw()", setup=setup, number=10)
    t_b_table_c_array = timeit.timeit("b_table(); c_array()", setup=setup, number=10)
    t_b_loop_c_raw = timeit.timeit("b_loop(); c_raw()", setup=setup, number=10)
    t_b_loop_c_array = timeit.timeit("b_loop(); c_array()", setup=setup, number=10)
    
    print(f"BC table, calculation loops: {t_b_table_c_raw:.4f} s")
    print(f"BC table, calculation array: {t_b_table_c_array:.4f} s")
    print(f"BC loop, calculation loops: {t_b_loop_c_raw:.4f} s")
    print(f"BC loop, calculation array: {t_b_loop_c_array:.4f} s")

u = numpy.ones((nx, ny))
b_table()
c_array()

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u.T, cmap='plasma')
fig.colorbar(surf, ax=ax, label='u')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylabel('u')
ax.set_title('2D Linear Convection')
ax.text2D(0.02, 0.05,
            r'$\frac{\partial u}{\partial t} + c\frac{\partial u}{\partial x} + c\frac{\partial u}{\partial y}= 0$',
            transform=ax.transAxes,
            fontsize=11)
pyplot.show()
