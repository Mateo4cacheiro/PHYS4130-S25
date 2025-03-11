# Project 2: Numeric Integration with Gauss-Legendre Quadrature

## Background
Gauss-Legendre Quadrature is a numeric integration method which approximates the definite 
integral of a function $f(x)$ as a sum from 1 to N of $c_{N,i}*f(x_i)$ where $x_i$ are the roots of the Nth 
Legendre polynomial, and $c_{N,i}$ are the weights associated with each polynomial. The domain
of integration must be mapped to [-1, 1] for this method to work. A simple u-substitution
can be used to map an interval [a, b] to [-1, 1].

## The Program
The code for this project is very brief. A function is defined, in this case given as 
$f(x) = sin^2(\sqrt{100x})$
