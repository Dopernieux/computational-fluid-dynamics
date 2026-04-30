# 2D Linear Convection

## Equation

u_t + c*u_x + c*u_y = 0

## Scheme

- Forward Euler (time)
- Backward Euler (space, x)
- Backward Euler (space, y)

## Performance Comparison (nx=ny=200, nt=50)
| Initialization | Calculations | Czas    |
|----------------|--------------|---------|
| table          | array        | 0.005 s |
| table          | raw loops    | 0.150 s |
| loop           | array        | 0.007 s |
| loop           | raw loops    | 0.155 s |

Array operations ~30x faster than raw Python loops.

## Observations

- dt needs to be carefully chosen to give comprehendable results

## Problems

- more dimensions need more complex plotting
- need to learn matrixes for better understanding