# EWOD Droplet Solver

Implementation of Young equation for a droplet of water.

## Important Values

Young equation:  γ_SG = γ_SL + γ_LG*cos(θ)
Using value of 0.0728 N/m, for temperature of 20 degrees celsius
Droplet volume V = 1e-9 m^3
Physical assumption - droplet is a spherical cap, which is only true if
Bond number << 1, gravitational force can be ommitted.

## Code

An array of contact angles is defined for iteration.

Function R_from_theta() calculates the value of R (radius of sphere, m) from 
constant volume and angle of triple line of contact theta (θ, radians).
Equation derived using trigonometric dependencies.

Function energy() calculates important values: a (radius of droplet, m),
E_SL (interfacial energy between solid and liquid, J),
E_LG (interfacial energy between liquid and gas, J).

For loop is used to iterate over angles and add multiple curves on same plot, 
theta and difference of interfacial energies is calculated.

R, a, cx (center of sphere in x, m), cy (center of sphere in y, m),
phi_right (right boundary, radians), phi left (left boundary, radians),
angle (curve of droplet, radians), x_arc (x value for plotting the curve),
y_arc (y value for plotting the curve), are all calculated for every iteration 
of angle theta. On every iteration figure is added to the plot.

Matplotlib function for 2d and 3d plotting.

## Observations

When angle of contact grows, from 10° to 170°, shape of droplet changes - from
very flat and broad to more spherical and compact. That is because of constant
volume.

The results are correct with intuition and Young's equation, minimization
of surface energies gives a balance consistent with given theta, which confirms
that energetic model is correct.

The limitations of this model are:
- ideal geometry
- external forces are ommitted
- γ_LG is temperature dependent, value of 0.0728 N/m is valid only at 20°C.
- for V = 1e-9 m^3, Bo = 0.05. So the spherical assumption is really close to
  real case for such a small volume.
- Internal pressure of the droplet is given by Young-Laplace equation
  Δp = 2γ/R, which assumes uniform curvature — valid only for spherical cap
  geometry.

