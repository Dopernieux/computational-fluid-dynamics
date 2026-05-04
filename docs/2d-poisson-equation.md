# 2D Poisson Equation
## Equation
∂²p/∂x² + ∂²p/∂y² = b(x,y)

## Boundary Conditions
- p = 0 at x = 0 and x = 2 (Dirichlet)
- dp/dy = 0 at y = 0 and y = 1 (Neumann)

## Source Term
- b = +100 at (nx//4, ny//4) — positive pressure source
- b = -100 at (3*(nx-1)//4, 3*(ny-1)//4) — negative pressure sink

## Scheme
- Central difference for ∂²p/∂x² and ∂²p/∂y²
- Iterative relaxation (same structure as Laplace)

## Difference from Laplace
- Laplace equation has b = 0 everywhere — no sources, solution is purely
    driven by boundary conditions and finds the smoothest possible distribution
- Poisson equation adds source term b(x,y) — localized forcing that drives
    the solution away from smooth equilibrium toward pressure peaks and valleys
- Physically: Laplace models steady heat conduction with fixed boundary temps,
    Poisson models the same with internal heat generation (e.g. electric current,
    chemical reaction, point charge in electrostatics)

## Observations
- Positive source creates a pressure peak, negative source creates a sink —
    the solution develops a gradient field connecting the two
- Neumann condition dp/dy = 0 acts like a symmetry plane —
    no flux crosses the top and bottom boundaries
- More iterations = smoother field, sharper peak/sink definition
- Parentheses placement in the discretized equation is critical —
    dividing only part of the expression by 2*(dx²+dy²) produces
    completely wrong results that are not obvious to spot visually

## Problems
- Integer division // required for array indexing — Python 3 returns
    float from /, which causes IndexError
- Source term b must be set before the iteration loop —
    resetting inside the loop would overwrite values each iteration
- Bracket error in the scheme caused source term to be scaled incorrectly,
    producing a flat solution with no visible pressure gradient