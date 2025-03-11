---
    Author: Zeke Vespie
    Topic: Diffusion Limited Aggregation Project
    Course: TN Tech PHYS4130
    Term: Spring 2025
---

# WRITEUP

## MAIN ASSIGNMENT

This is the first part of my writeup, where I do all the main objectives. I do the first extension to the project later on.

### TRAPEZOIDAL RULE

The first part of the project was using the trapezoidal rule to calculate the integral shown below:

```math
I = \int_0^2 \mathrm{d}x\, \sin^2\left(\sqrt{100x}\right)
```

By doing as told, I found that by multiplying the number of points by 2 repeatedly the integrals solution stabilized with 6 significant figures of accuracy at the point N = 8192.

I also found the error by using an equation I found on Wikipedia [1] that is somehow derived for trapezoidal rule, and it ended up being around 2E-8, which is an order of magnitude off from what I see the difference being on Maple, that being 5E-7.

### SIMPSON'S RULE

By using a ratio of trapezoidal and midpoint rule integration, Simpson's Rule is created. I will not attempt to explain how it is derived from its original, theoretical idea because I do not understand it very well, but this numerical integration method in principle is fitting a parabola to each set of three points along the curve being integrated How does this somehow result in a sum of other weighted rules, and how does this method even work if there isn't a number of points that is evenly divisible by three? I don't really know much, and what I do know I don't really care to explain, but it works.

Using this rule instead of just trapezoidal rule does result in a greater number of function calls (at least for me), but it is a much better approximation, as will be seen later. First, I will employ the variable change outlined below, which doesn't effect the precision of it for this particular calculation but will put it in a more useful state for later.

```math
u=\frac{2x-a-b}{b-a}.
```

This variable change results in the integral changing into the following:

```math
I = \int_{-1}^1 \mathrm{d}u\, \sin^2\left(\sqrt{100{(u+1)}}\right)
```

Approximating this integral with Simpson's Rule gives a value that is precise to 6 significant figures in only 256 points, making it much more efficient.

> To be honest, the entire u-substitution that is done here could have been done later and it would have made a lot more sense to do so, but this is the chronological telling of the events, so that is why it is placed here.

### LEGENDRE POLYNOMIALS AND GAUSSIAN QUADRATURE

The other methods that have been discussed are all well and good, but there is an ever more powerful method called Gaussian Quadrature. It numerically integrates by using Legendre Polynomials, which are famous polynomials that solve a particular differential equation. They can be used to approximate with uncanny precision, but only if the bounds of integration are from -1 to 1, which justifies the change in variables done earlier. 

See below a chart of relevant Legendre Polynomials, with each entry having subplots of $`P_i`$, $`P_j`$, and $`P_i\cdot P_j`$. The first is red, the second is blue, and the third is green. Note that on the diagonal entries there is no red because it overlaps with the blue.

<figure>
  <img src=figures/4x4Grid.png>
    <figcaption>Table of the subplots of ith (red) and jth (blue) Legendre Polynomials and their product (green), where i and j correspond to row and column number</figcaption>
</figure>
<p>&nbsp;</p> 

See here that each of these polynomials has a number of zeros equal to the degree of the polynomial. In order to optimize the Gaussian Quadrature method of numerical integration, "the optimal points for an N order Gaussian Quadrature are the zeros of that order of Legendre polynomial" [2]. The weights and roots of the Legendre Polynomials used in the equation below describe the Gaussian Quadrature method:

```math
\int_{-1}^{1} \mathrm{d}u\, f(u) \approx \sum_{i=1}^N c_{N,i} f\left(u_{N,i}\right)
```

I used this on the integral shown previously in terms of u, and got that for N = 12 the approximation is precise to 7 significant figures, which is nigh on witchcraft.

## EXTENSION

This is the first and only extension to the project, wherein a second integral is approximated in different ways and is commented on.

### FIRST ATTEMPT WITH GAUSSIAN QUADRATURE

I used the Gaussian Quadrature approximation method on the following integral:

```math
\int_0^2\mathrm{d}y\,\frac{y^2}{\sqrt{2-y}}
```

To do this, I had to first do the u-substitution already mentioned, but just as before I notice that the total x covered by this integral is the same as the total x covered by the bounds from -1 to 1. This actually allows for the change of variables to be rather simply interpreted as simply translating the plot by 1 in the -x direction, as shown:

```math
\int_{-1}^1\mathrm{d}u\,\frac{{(u+1)}^2}{\sqrt{1-u}}
```

However, I was generally unable to make it work. I tested up to N = 100000, and this took the program ~4.5 minutes to compute with a precision of only 4 significant figures. I wasn't ever able to figure out what N needed to be for this, but suffice it to say it needs to be ridiculously large.

### VARIABLE CHANGE

I did the variable change recommended, shown below:

```math
y=2\sin^2\theta
```

```math
\mathrm{d}y=4\sin\theta\cos\theta\,\mathrm{d}\theta
```

This changed the integral to the following form, for which I have done all the algebra seperately:

```math
\sqrt{128}\int_0^{\frac{\pi}{2}}\mathrm{d}\theta\,\sin^5\theta
```

### SIMPSON'S RULE

I utilized the Simpson's Rule code from earlier to evaluate this integral now, and after implementing a while loop that stops when the precision to 10 significant figures is met (as checked against by Maple) I found that it can be met with N = 60, which is obviously much better than the Gaussian Quadrature attempt from before. This tells me that the efficiency boost of Gaussian Quadrature can only go so far; having the integral be in a more manageable form helped it out tremendously.

### GAUSSIAN QUADRATURE 2: ELECTRIC BOOGALOO

In order to use Gaussian Quadrature on this, I had to use the u-substitution yet again, but this time I couldn't cheat, so below is the form of the substitution after some manipulation and after plugging in the bounds:

```math
\theta=\frac{\pi}{4}(u+1)
```

```math
\mathrm{d}\theta=\frac{\pi}{4}\mathrm{d}u
```

Using these, the form of the integral becomes the following:

```math
\sqrt{8\pi^2}\int_{-1}^1\mathrm{d}u\,\sin^5[\frac{\pi}{4}(u+1)]
```
With this integral, only N = 10 points were required to get 10 significant figures of precision, which is absolutely absurd. The gods surely smile upon us with calculations the quick.

## CLOSING NOTES

This section is simply to answer any of the questions that I was supposed to answer in this writeup that I have yet to answer.

### ATTRIBUTION
I have 2 references in my writeup, and they are below this text. All other information that I needed was provided. I also learned how to make a 2D array of plots using some website, but I couldn't remember what it was and didn't write it down.

[1] https://en.wikipedia.org/wiki/Trapezoidal_rule, asymptotic error estimate as N goes to infinity

[2] Dr. Mr. MengerSponge, GitHub PHYS4130-S25 branch, p2-NInt writeup

### TIMEKEEPING
I spent less time on this one than the last one, with probably about 10 hours coding and 15 hours total.

### LANGUAGES, LIBRARIES, LESSONS LEARNED:
Coding Language Used: Python
Libraries included: numpy, scipy, matplotlib

The primary thing I learned in this project had to do with generating the 4X4 plot table, and how you can store a bunch of plots in a 2D array in that way. Other than that, everything was straight forward.