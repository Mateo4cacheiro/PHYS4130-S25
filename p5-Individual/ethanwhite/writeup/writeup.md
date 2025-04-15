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
\frac{d^2x^{\mu}}{ds^2}+\Gamma^{\mu}_{\alpha\beta}\frac{dx^\alpha}{ds}\frac{dx^\beta}{ds}=0
$$

It is incredibly important to notice that this is not just one equation (even though it is the geodesic equation). Since we are working in 4-dimensional space-time, 
$$ \mu $$ 
can be a value of 0, 1, 2, and 3, as can 
$$ \alpha $$
and 
$$ \beta $$
. Thus, there are, at first glance, **64 different PDEs**. After looking at the symmetry of the 

<figure>
  <img src=starlight-bending.jpg>
  <figcaption> Starlight bending figure.
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
