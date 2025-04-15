# Introduction

The geodesic equation in General Relativity is a tool which can be used towards plotting geodesics (straight lines on a curved space, like spacetime) of particles around a gravitational source with a given metric. The given metric that we will be working with is the spherical polar version of the linearized Schwarzchild weak field limit metric. It can be expressed as the following matrix (but it is a tensor, not a matrix, just to be clear):

\begin{center}
g_{\mu\nu}=\begin{pmatrix}
-1+\frac{2GM}{r} & 0 & 0 & 0 \\
0 & 1+\frac{2GM}{r} & 0 & 0 \\
0 & 0 & 1+\frac{2GM}{r} & 0 \\
0 & 0 & 0 & 1+\frac{2GM}{r} \\
\end{pmatrix}
\end{center}

Furthermore, the geodesic equation that we will be working with is given by: \begin{center}\frac{d^2x^{\mu}}{ds^2}+\Gamma^{\mu}_{\alpha\beta}\frac{dx^\alpha}{ds}\frac{dx^\beta}{ds}=0\end{center}

# Purpose

The purpose of this project is to combine both general relativity and computational physics.

# Project Goals

The goals of this project are to:

1. Computatinally model the bending of starlight around the sun and compare this resulting angle with observational data (bend angle of 1.75 arcseconds).

This will be done by using the Schwarzchild metric, computing the Christoffel symbols, and using the geodesic equation. The actual computational side of this will be SOLVING this system of coupled PDEs using a higher order sympletic integrator.

2. If possible, as an extension, model the perihelion advance of Mercury.
