# -*- coding: utf-8 -*-
"""
Created on Thu May  7 06:02:29 2026

@author: szczv
"""

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

gamma_LG = 0.072
nx = 101
ny = 101
nt = 9

na = np.linspace(10, 170, nt)

steps = np.linspace(0, 0, nt)

def R_from_theta(theta, V):
    return (3*V / (np.pi * (1 - np.cos(theta))**2 * (2 + np.cos(theta))))**(1/3)

def energy(theta):
    R = R_from_theta(theta, V)
    a = R * np.sin(theta)
    E_SL = - gamma_diff * np.pi * a**2
    E_LG = gamma_LG * 2 * np.pi * R**2 * (1 - np.cos(theta))
    return E_SL + E_LG

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.axis('equal')
ax1.set_title('Cross section of droplet for different contact angles')

for nti in range(nt):
    theta_eq = np.radians(na[nti])
    gamma_diff = gamma_LG * np.cos(theta_eq)    # γ_SG - γ_SL
    
    V = 1e-9   # objętosc kropli w m^3
    
    result = minimize_scalar(energy, bounds=(0.01, np.pi - 0.01), method='bounded')

    R = R_from_theta(theta_eq, V)
    a = R * np.sin(theta_eq)
    cx = 0
    cy = -R*np.cos(theta_eq)
    
    phi_right = np.arctan2(0 - cy, a - cx)
    phi_left  = np.arctan2(0 - cy, -a - cx)
    if phi_left < phi_right:
        phi_left += 2*np.pi
    angle = np.linspace(phi_right, phi_left, nx)
    
    x_arc = cx + R * np.cos(angle)
    y_arc = cy + R * np.sin(angle)
    
    ax1.plot(x_arc, y_arc, label=f'{na[nti]:.0f}°')
    ax1.plot([-a, a], [0, 0], color='gray', linewidth=0.5)
    
######

ax1.axhline(y=0, color='black', linewidth=1)
ax1.legend()
plt.show()

phi_3d = np.linspace(0, 2*np.pi, 101)
X = np.outer(x_arc, np.cos(phi_3d))
Y = np.outer(x_arc, np.sin(phi_3d))
Z = np.outer(y_arc, np.ones_like(phi_3d))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zlim(0, R*1.1)
ax2.view_init(elev=20, azim=45)
ax2.axis('equal')
ax2.set_title(f'3D Droplet, θ = {np.degrees(theta_eq):.0f}°')

print(f'theta: {np.degrees(result.x):.4f} ')
print(f'srodek kropli: {cy:.4f} ')
print(f'promien kropli: {R:.4f} ')




