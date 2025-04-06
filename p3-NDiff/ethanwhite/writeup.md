---
    Name: Ethan White
    Topic: Project 3, Numerical Differentiation
    Class: PHYS 4130
---

### Introduction

In this module, we learned about numerical differentiation through the methods of forward, backward, and central difference formulae. Three point and five point stencils were also explored. The method of solving n-point stencils is to Taylor expand a function f(x) and its difference counterparts like f(x+-h), f(x+-2h), f(x+-3h)... etc and then solve for the coefficients such that only the first derivative remains. The error is then proportional to whatever term is first leftover once you solve for the coefficients (if that makes sense). N-order central difference stencils have error proportional to h^(N-1), and this is explored in this writeup.

> [!NOTE]
> This writeup only contains information regarding the explanation types of questions for the P3 notebook.

### Solutions

Exercise 1) As h -> 0, with h going down to $10^{-12}$, the log-log plot freaks out because you are basically taking the natural logarithm of zero (which isn't defined). 

3.2a) 

3.2b) The error is proportional to $h^4$ since the line is.. relatively straight. Solving for the slope of the line yields m = 0.89, which is pretty close. After h goes lower than 0.001, the error looks atrocious (since the log of 1/h^4 would be so close to 0 the log would mess up). But otherwise it is pretty close.

3.3) The derivative should be something like:
