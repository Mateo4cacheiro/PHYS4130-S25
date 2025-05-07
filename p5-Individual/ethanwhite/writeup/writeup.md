# Introduction

The geodesic equation in General Relativity is a tool which can be used towards plotting geodesics (straight lines on a curved space, like spacetime) of particles around a gravitational source with a given metric. The given metric that we will be working with is the spherical polar version of the linearized Schwarzschild weak field limit metric. It can be expressed as the following matrix (but it is a tensor, not a matrix, just to be clear):

$$
g_{\mu\nu}=
\begin{pmatrix}
-1+\frac{2GM}{r} & 0 & 0 & 0 \\
0 & 1+\frac{2GM}{r} & 0 & 0 \\
0 & 0 & 1+\frac{2GM}{r} & 0 \\
0 & 0 & 0 & 1+\frac{2GM}{r}
\end{pmatrix}=
\begin{pmatrix}
-1+\frac{2GM}{r} & 0 & 0 & 0 \\
0 & 1+\frac{2GM}{r} & 0 & 0 \\
0 & 0 & r^2 & 0 \\
0 & 0 & 0 & r^2\sin^2\theta
\end{pmatrix}
$$

Furthermore, the geodesic equation that we will be working with is given by:

$$
\frac{\partial^2 x^{\mu}}{\partial s^2}+\Gamma^{\mu}_{\alpha\beta}\frac{\partial x^\alpha}{\partial s}\frac{\partial x^\beta}{\partial s}=0
$$

It is incredibly important to notice that this is not just one equation (even though it is *the* geodesic equation). Since we are working in 4-dimensional spacetime, $\mu, \alpha, \beta \in \{0, 1, 2, 3\}$

Thus, there are, at first glance, **64 different PDEs**. However, by examining the symmetry of the metric (specifically, that it is diagonal), the equation reduces significantly. You may be asking yourself-- "what is $\Gamma^{\mu}_{\alpha \beta}$?". This symbol, the Christoffel symbol, represents the curvature of spacetime around the 'basis vectors' of space-time itself (coordinates (1, 2, 3) and time (0) and whatnot). This value can be calculated two ways:

$$ 
\Gamma^\mu_{\alpha \beta} = \frac{1}{2} g^{\mu \nu} \left( \partial_\alpha g_{\beta \nu} + \partial_\beta g_{\alpha \nu} - \partial_\nu g_{\alpha \beta} \right) = \frac{\partial^2 x^\gamma}{\partial x^{\alpha} \partial x^{\beta}} \frac{\partial x^{\mu}}{\partial x^\gamma}
$$

It is most useful to look at the first equation with our metric, since everything can be calculated by hand pretty easily-ish.

<figure>
  <img src=starlight-bending.jpg>
  <figcaption> [1] Starlight bending figure.
</figcaption>
</figure>
<p>&nbsp;</p> 

The bending of starlight can be explained by the above cartoon. The 'star light' (light from another star) bends around our sun, such that there is some angle between the initial paths tangent vector and the post-sun-skimming tangent vector (should be precisely 1.75 arcseconds). This phenomenon is also known as gravitational lensing and can be used towards seeing far-away galaxies that may be concealed by other galaxies. 

This phenomenon is particularly interesting because in Newtonian physics, the resulting angle is off by a factor of two compared to the general-relativistic prediction. This gravitational lensing effect was critical towards proving Einstein's theory of general relativity, and once observations made by Sir Arthur Eddington on an expedition in 1919 during a total solar eclipsde were made, Einstein's fame skyrocketed.

# Purpose

The purpose of this project is to combine both general relativity and computational physics by computing the exact angle of starlight bend, and to compare this value with Newtonian predictions. 

# Procedure

> [!IMPORTANT]
> This is the only way that I could figure out a program that would replicate the starlight bend of ~1.75 arcseconds. I've added an additional section titled "Alternative Methods" that discusses the other ways I tried to computationally model the phenomenon, but in the end, this is the code that actually worked. :(

For this program to be efficient, it may be good for us to briefly cover how the Newtonian angle calculation goes, and why it's wrong by a factor of two compared to the GR approach. After this brief calculation, I will explain the code/relevant algorithms.

# Results

# Project Goals (submitted Apr 24th)

The goals of this project are to:

1. Computatinally model the bending of starlight around the sun and compare this resulting angle with observational data (bend angle of 1.75 arcseconds). (18% of final grade in GR course).

This will be done by using the Schwarzchild metric, computing the Christoffel symbols, and using the geodesic equation. The actual computational side of this will be SOLVING this system of coupled PDEs using a higher order sympletic integrator. 

2. If possible, as an extension, model the perihelion advance of Mercury. (2% of final grade in GR course)
