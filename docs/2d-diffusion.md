# 2D Diffusion

## Equation

u_t = nu*( (u_x)^2 + (u_y)^2 ) 

## Scheme

- Forward Euler (time)
- Central Euler (space, x)
- Central Euler (space, y)

## Observations

- diffusion always smooths out the result
- stability is dependent on relation dt/dx^2

## Problems

- usage of minus sign instead of plus sign gave non physical results
- lack of boundary conditions led to errors on boundaries
- orientation of the grid makes the result harder to comprehend