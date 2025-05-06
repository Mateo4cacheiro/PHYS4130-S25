# P5: Finite Element Analysis

## Introduction
The Finite Element Method (FEM) is a numerical method of solving multi-variable differential equations. It is commonly used in engineering for modeling heat transfer, fluid flow, structural mechanics, etc. The method works by dividing the domain of a given problem into some finite number of sub-domains referred to as finite elements. The collection of elements is called the mesh, which approximates the original domain with arbitrary precision depending on the number of elements. In most cases that FEM is implemented the original equations are partial differential equations (PDEs) which cannot be solved analytically. In each element the PDE is approximated using algebraic equations for steady-state problems, and ordinary differential equations (ODEs) for transient problems. The methods used to solve these problems differ based on the analysis software and the original problem.

## The Original Program

This project is a modification of a pre-existing example problem using scikit-fem, a python FEM library. The original problem in question solves deflection in a clamped steel plate using Kirchhoff-Love plate theory. The equation for the deflection in the plate is given as

```math
\frac{Ed^3}{12(1-\nu^2)} \Delta^2 u = f \quad \text{in $\Omega$},
```
where the domain $\Omega = (0,1)^2 $, $f$ is a force perpendicular to the plate, $d$ is the thickness of the plate, $E$ is Young's modulus, and $\nu$ is Poisson's ratio. The original example produces an analysis of a $1m^2$ steel plate of thickness $0.1m$. The Young's modulus of steel is $E = 200\times10^9$ and Poisson's ration $\nu = 0.3$. The example also utilizes a combination of the boundary conditions for the clamped and free cases, resulting in a plate that is clamped on three sides. Deflection can be visualized using a heatmap (Fig. 1).

![](https://github.com/asgrice/PHYS4130-S25/blob/main/p5-Individual/asgrice/writeup/deflection_square.png)

From this it is clear to see that the unsupported bottom edge deflects under the constant load, while the top, left, and right edges do not.

## The Modification
The purpose of modifying this example code was to better understand how to create and manipulate a mesh, and how to modify the boundary conditions and loading functions. First the original square mesh was changed to be approximately circular mesh with a larger number of elements. The loading function was modified to be sinusoidal. The boundary conditions are those of a plate supported around the entire perimeter. A plot of the solution is shown below 

![](https://github.com/asgrice/PHYS4130-S25/blob/main/p5-Individual/asgrice/writeup/deflection_round.png)