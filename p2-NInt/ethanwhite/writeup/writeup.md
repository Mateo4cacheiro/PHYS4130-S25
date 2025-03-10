---
   Author: Ethan White
   Topic: Numerical Integration Project
   Course: TN Tech PHYS 4130
   Term: Spring 2025 
---

### Introduction

Numerical integration is a powerful conceptual tool as to understanding how an integral works (specifically with the endpoint methods), but it also has incredible computational ability with methods like the Gauss-Legendre quadrature method. 

For gaussian quadrature, imagine you are a builder and you are measuring the area of the square house you are building. You could get your ruler and measure every single square foot individually, or, you could take a set of optimal points (like the vertices of the house) and calculate the area with just those four point measurements. This is essentially what Gauss-Legendre quadrature does-- it looks at optimal points along a function that provide very good approximations and assigns a weight to them. This process takes place from [-1,+1] and the orthogonal Legendre polynomials describe the weightings and roots of the function approximation.

This program works in three parts to complete each project goal:

1. It uses Simpson's rule to create a table of N, which is the number of subintervals, the value of the integral calculated from N subintervals, and the error of that calculation with the actual value of the integral. 
2. Next, the program calculates the Gaussian quadrature of that same integral by finding our input to f(x) as f(u(x)), where u is the mapping that puts our f(x) integral within [-1,+1]. The du-component is multiplied by the final integration area. 
3. Lastly, the program creates a plot of Legendre polynomials from first order to fourth order. It graphs each individal polynomial (two per plot), and then the resulting function from their multiplication. The integral is unitary along the plot's main diagonal since the Legendre polynomials form an orthogonal set. The off-diagonal terms are zero sometimes because of the coefficients of the resulting multiplication, and other times because the resultant function is odd along symmetric bounds.

<figure>
  <img src=Figure_1.png>
  <figcaption>The 4x4 plot of first - fourth order Legendre polynomials and their corresponding products with eachother. </figcaption>
</figure>
<p>&nbsp;</p> 

### Extensions

The following substitution was made:
$y = 2\sin^2\theta \rightarrow dy = 4\sin\theta\cos\theta d\theta$
$y^2 = 4\sin^4\theta, \sqrt{2-y}=\sqrt{2-2\sin^2\theta}=\sqrt{2}\cos\theta$ 

### Attribution

The main components of this project were created in the homework assignments (up to simpson's rule, at least). Zeke found the first source, [1], helpful so I used it.

1. https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
2. https://en.wikipedia.org/wiki/Gaussian_quadrature
3. https://engcourses-uofa.ca/books/numericalanalysis/numerical-integration/gauss-quadrature/
4. https://en.wikipedia.org/wiki/Legendre_polynomials

### Timekeeping

This project took about 15-20 hours of work. The main struggles were within the extension questions.

### Languages, Libraries, Lessons Learned

1. Python was used for the entirity of this project. 

2. I used numpy and math to.. do math stuff. I used matplotlib.pyplot to create the Legendre plot portion of the project. I used scipy to pull out the weights and roots of the Legendre polynomials. None of these were particularly great, but I found matplotlib.pyplot to be as intuitive as usual (very).
