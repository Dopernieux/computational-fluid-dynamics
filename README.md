# Computational Fluid Dynamics - From Scratch

Implementation of basic CFD equations in 1D and 2D from scratch.

Implementacje równań CFD w 1D i 2D napisane od podstaw.

## Models

- 1D and 2D Linear Convection
- 1D and 2D Diffusion
- 1D and 2D Nonlinear Convection
- 1D and 2D Burgers' Equation

## Results

![1dLinearConvection](results/1d-linear-convection-multiple-schemes-4-steps-lw.png)
![2dBurgers](results/2d-burgers-equation-steps.png)
![1dBurgers](results/1d-burgers-equation.png)
![2dDiffusion](results/2d-diffusion-low-dt.png)
![Diffusion](results/1d-diffusion-low-vis.png)
![2dConvection](2d-linear-convection.png)

## Run

pip install -r requirements.txt
python src/1d-burgers-equation.py
