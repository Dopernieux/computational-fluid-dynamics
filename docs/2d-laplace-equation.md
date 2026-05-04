# 2D Laplace Equation
## Equation
∂²p/∂x² + ∂²p/∂y² = 0

## Boundary Conditions
- p = 0 at x = 0
- p = y at x = 2
- dp/dy = 0 at y = 0 and y = 1 (Neumann condition)

## Scheme
- Central difference for both ∂²p/∂x² and ∂²p/∂y² (iterative solver)
- No time stepping — iterative relaxation until convergence

## Observations
- Unlike previous equations, Laplace has no time derivative —
    the solution is found by iterating toward a steady state, not by marching in time.
    Each iteration brings p closer to the equilibrium distribution.
- Boundary condition p = y at x = 2 drives the solution —
    pressure increases linearly with y on the right wall and
    this gradient propagates through the domain toward x = 0.
- Neumann condition dp/dy = 0 is implemented by setting the boundary
    node equal to its neighbor — this enforces zero gradient at y = 0 and y = 1
    and acts like a symmetry or insulation condition.
- Convergence is visible in the animation — early iterations show
    sharp transitions near boundaries, later iterations smooth out
    into the final elliptic distribution.
- 1000 iterations with nx = ny = 20 is sufficient for visual convergence
    t this resolution. Finer grids require more iterations.

## Performance
- contourf renders ~10x faster than plot_surface for 2D fields
- numpy array operations used throughout — no raw Python loops

## Problems
- text2D annotation disappears each frame when using ax.cla() —
    must be redrawn inside update() function
- projection='3d' conflicts with contourf — must use standard 2D axes
- Neumann boundary conditions must be updated inside the iteration loop,
    not just once before it, otherwise gradients accumulate incorrectly