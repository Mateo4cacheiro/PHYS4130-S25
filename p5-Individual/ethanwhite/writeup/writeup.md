# Introduction

The geodesic equation in General Relativity is a tool which can be used towards plotting geodesics (straight lines on a curved space, like spacetime) of particles around a gravitational source with a given metric. The given metric that we will be working with is the spherical polar version of the linearized Schwarzschild weak field limit metric. It can be expressed as the following matrix (but it is a tensor, not a matrix, just to be clear):

$$
g_{\mu\nu}=
\begin{pmatrix}
-1+\frac{2GM}{r} & 0 & 0 & 0 \\
0 & 1+\frac{2GM}{r} & 0 & 0 \\
0 & 0 & 1+\frac{2GM}{r} & 0 \\
0 & 0 & 0 & 1+\frac{2GM}{r}
\end{pmatrix}
$$

Furthermore, the geodesic equation that we will be working with is given by:

$$
\frac{\partial^2 x^{\mu}}{\partial s^2}+\Gamma^{\mu}_{\alpha\beta}\frac{\partial x^\alpha}{\partial s}\frac{\partial x^\beta}{\partial s}=0
$$

It is incredibly important to notice that this is not just one equation (even though it is *the* geodesic equation). Since we are working in 4-dimensional spacetime, $\mu, \alpha, \beta \in \{0, 1, 2, 3\}$

Thus, there are, at first glance, **64 different PDEs**. However, by examining the symmetry of the metric (specifically, that it is diagonal), the equation reduces significantly. You may be asking yourself-- "what is $\Gamma^{\mu}_{\alpha \beta}$?". This symbol, the Christoffel symbol, represents the curvature of spacetime around the 'basis vectors' of space-time itself (coordinates (1, 2, 3) and time (0) and whatnot). This value can be calculated two ways:

$$ 
\Gamma^\mu_{\alpha \beta} = \frac{1}{2} g^{\mu \nu} \left( \partial_\alpha g_{\beta \nu} + \partial_\beta g_{\alpha \nu} - \partial_\nu g_{\alpha \beta} \right) = \Gamma^{\mu}_{\alpha \beta} = \frac{\partial^2 x^\gamma}{\partial x^{\alpha} \partial x^{\beta}} \frac{\partial x^{\mu}}{\partial x^\gamma}
$$



<figure>
  <img src=starlight-bending.jpg>
  <figcaption> [1] Starlight bending figure.
</figcaption>
</figure>
<p>&nbsp;</p> 

The bending of starlight can be explained by the above cartoon. The 'star light' (light from another star) bends around our sun, such that there is some angle between the initial paths tangent vector and the post-sun-skimming tangent vector (should be precisely 1.75 arcseconds). 

# Purpose

The purpose of this project is to combine both general relativity and computational physics by computing the exact angle of starlight bend.

# Project Goals

The goals of this project are to:

1. Computatinally model the bending of starlight around the sun and compare this resulting angle with observational data (bend angle of 1.75 arcseconds).

This will be done by using the Schwarzchild metric, computing the Christoffel symbols, and using the geodesic equation. The actual computational side of this will be SOLVING this system of coupled PDEs using a higher order sympletic integrator.

2. If possible, as an extension, model the perihelion advance of Mercury.
