# 1D Linear Convection Animation

## Equation

u_t + c*u_x = 0

## Scheme

- Forward Euler (time)
- Backward Euler (space, x)

## Observations

- CFL conditions using sigma can be implemented to prevent blowing up of the 
    calculation.
- Writing program as a function gives us an easier way to call it with
    desirable input.
- Animation in time has great capabilities of displaying results that are easy
    to comprehend.

## Problems

- Animation needs much more code