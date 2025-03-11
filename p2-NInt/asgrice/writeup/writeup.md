# Project 2: Numeric Integration with Gauss-Legendre Quadrature

## Background
Gauss-Legendre Quadrature is a numeric integration method which approximates the definite 
integral of a function $f(x)$ as a sum from 1 to N of $c_{N,i}*f(x_i)$ where $x_i$ are the roots of the Nth 
Legendre polynomial, and $c_{N,i}$ are the weights associated with each polynomial. The domain
of integration must be mapped to [-1, 1] for this method to work. A simple u-substitution
can be used to map an interval [a, b] to [-1, 1].

## The Program
The code for this project is very brief. A function is defined, in this case given as 
$f(x) = sin^2(\sqrt{100x})$ with a domain of integration [0, 2]. A u-substitution is also
provided as 

```math
u=\frac{2x-a-b}{b-a}.
```

which with a bit of rearranging gives 

```math
x=\frac{1}{2}(u(b - a) + a + b).
```

and 

```math
\frac{du}{dx} = \frac{2}{b - a}
```

The function definition is shown below:

```
def func(u,a,b):
    k = 0.5*(u*(b-a) + a + b)
    val = (np.sin(np.sqrt(100*k)))**2
    return val
```