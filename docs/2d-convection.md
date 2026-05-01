# 2D Convection

## Equation

u_t + u*u_x + v*u_y = 0
v_t + v*v_x + u*v_y = 0

## Scheme

- Forward Euler (time)
- Backward Euler (space, x)
- Backward Euler (space, y)

## Observations

- Boundary conditions directly affect solution shape. Boundaries of value 1,
    created shapr walls at domain edges. Changin them to 1.5 produced smoother
    transtion from peak (u=2) to boundary.
- Peak remaining smmoth is an effect of numerical diffusion from 1st order
    upwind scheme, not physical diffusion - no viscosity term in this eq.

## Problems

- More dimensions give more complex plots for better result evaluation.
