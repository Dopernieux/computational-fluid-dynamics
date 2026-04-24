# 1D Linear Convection — Multiple Schemes
## Equation
u_t + c*u_x = 0

## Schemes
- 1st order Backward Difference (BD) — explicit
- 1st order Central Difference (CD) — explicit  
- 2nd order Backward Difference (2BD) — explicit
- 2nd order Backward Difference (2BD) — implicit

## Stability Conditions
- BD 1st order: σ = c*dt/dx <= 1.0
- CD 1st order: unconditionally unstable for pure convection
- 2BD explicit:  σ = c*dt/dx <= 0.1
- 2BD implicit: unconditionally stable — no CFL restriction

## Observations
- The first-order BD is stable but introduces significant numerical diffusion—the peak
    of the triangular wave flattens and broadens over time, even though the equation does not contain
    a diffusion term. This demonstrates a purely mathematical consequence of first-order truncation.
- The first-order CD is unconditionally unstable for convection; it samples information symmetrically
    from both sides, whereas convection depends on one specific side. The result of the
    truncation error is growing oscillations that eventually explode regardless of dt.
    The 1st-order CD was included to demonstrate the need for upwind schemes.
- 2BD explicit preserves the shape of the triangle much better than BD 1st, exhibiting less
    numerical diffusion. However, it requires σ <= 0.1, which is a value 10 times more
    restrictive than in the case of BD 1st.
- 2BD implicit is the most complex and yields the most reliable results; it is
    stable for any dt, preserves shape best, and exhibits no oscillations. All of this
    comes at the cost of computational complexity.

## Key Tradeoff
- Higher order of accuracy - better shape preservation, but stricter stability conditions
    Implicit schemes do not require stability conditions but rely on solving
    matrices, which increases the computational cost.
- The central difference fails not due to an inappropriate order of magnitude, but due to
    incorrect physical assumptions—convection is a one-sided phenomenon, and the numerical scheme
    must take this into account.

## Problems
- The 2BD explicit scheme fails when σ > 0.1 — much stricter conditions than one might expect
    based on CFL alone.
- CD instability cannot be remedied by reducing dt.
- The implicit scheme requires careful matrix assembly—boundary rows must be
    determined before starting the calculations.
- All schemes were tested on a triangular boundary condition between x=0.9 and x=1.1,
    which ensures sharp gradients and serves as a good stress test for numerical diffusion. 