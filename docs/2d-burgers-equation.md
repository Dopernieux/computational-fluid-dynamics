# 2D Burgers Equation
## Equation
u_t + u*u_x + v*u_y = ν*(u_xx + u_yy)
v_t + u*v_x + v*v_y = ν*(v_xx + v_yy)

## Scheme
- Forward Euler (time)
- Upwind/Backward difference (convection, x and y)
- Central difference (diffusion, x and y)

## Observations
- the square initial condition diffuses and advects over time — sharp edges smooth out due to viscosity
- increasing nx/ny improves accuracy but slows computation significantly due to nested loops
- for the phenomenon of convection and diffusion to be easily visible, added 4 steps in time
- the velocity field begins restrained by initial conditions, then moves right and up due to convection
- the velocity field becomes blurry with time due to diffusion

## Problems
- CFL stability condition must be satisfied: vis*dt/dx² < 0.5 — violated conditions produce NaN instantly
- boundary conditions must be enforced inside the time loop, not just once before it
- initial condition placement matters — a square near the boundary gets immediately overwritten by boundary values
- parentheses in exponential expressions are easy to misplace and produce silent mathematical errors
- pyplot.show() closes the figure — all annotations and text must be added before calling it