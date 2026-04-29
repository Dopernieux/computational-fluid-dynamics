# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:25:30 2026

@author: szczv
"""

import numpy
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

def convection_animation(nx):
    dx = 2 / (nx-1)
    nt = 20
    dt = .01
    
    u = numpy.ones(nx)
    
    u[int(.5 / dx) : int(1 / dx + 1)] = 2
    
    history = [u.copy()]
    
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            
            u[i] = un[i] - un[i]*(dt/dx)*(un[i]-un[i-1])
            
        history.append(u.copy())
        
    fig, ax = pyplot.subplots()
    ax.set_xlim(0, 2)
    ax.set_ylim(0.5, 2.5)
    ax.set_xlabel('x')
    ax.set_ylabel('u')
    line, = ax.plot([], [])
    title = ax.set_title('')
    x = numpy.linspace(0, 2, nx);   
    
    def update(frame):
        line.set_data(x, history[frame])
        title.set_text(f't = {frame * dt:.3f} (krok {frame})')
        return line, title
    
    animation = FuncAnimation(fig, update, frames=len(history), interval=100, blit=True)

    animation.save('1d-convection.gif', writer='pillow', fps=10)
    pyplot.show()
    
convection_animation(41)    