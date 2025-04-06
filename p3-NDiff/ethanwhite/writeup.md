---
    Name: Ethan White
    Topic: Project 3, Numerical Differentiation
    Class: PHYS 4130
---

### Introduction

In this module, we learned about numerical differentiation through the methods of forward, backward, and central difference formulae. Three point and five point stencils were also explored. The method of solving n-point stencils is to Taylor expand a function $f(x)$ and its difference counterparts like $f(x\pmh)$, $f(x\pm2h)$, $f(x\pm3h)$... etc and then solve for the coefficients such that only the first derivative remains. The error is then proportional to whatever term is first leftover once you solve for the coefficients (if that makes sense). N-order central difference stencils have error proportional to $h^{N-1}$, and this is explored in this writeup.

> [!NOTE]
> This writeup only contains information regarding the explanation types of questions for the P3 notebook.

### Solutions
> [!IMPORTANT]

> To view the plots, please use code.py by commenting in/out the five functions at the bottom of the code. If you enabled all five functions at the same time, only one plot would spawn and everything would overlap and be super ugly.
Exercise 1) As h $\rightarrow$ 0, with h going down to $10^{-12}$, the log-log plot freaks out because you are basically taking the natural logarithm of zero (which isn't defined). 

3.2a) We know the following qualities:

$f(x-2h)=f(x)-2f'(x)h+2f''(x)h^2-\frac{4}{3}f^{(3)}(x)h^3+\frac{2}{3}f^{(4)}(x)h^4-O(5)$
$f(x-h)=f(x)-f'(x)h+\frac{1}{2}f''(x)h^2-\frac{1}{6}f^{(3)}(x)h^3+\frac{1}{24}f^{(4)}(x)h^4-O(5)$
$f(x+h)=f(x)+f'(x)h+\frac{1}{2}f''(x)h^2+\frac{1}{6}f^{(3)}(x)h^3+\frac{1}{24}f^{(4)}(x)h^4+O(5)$
$f(x+2h)=f(x)+2f'(x)h+2f''(x)h^2+\frac{4}{3}f^{(3)}(x)h^3+\frac{2}{3}f^{(4)}(x)h^4+O(5)$

$af(x-2h)+bf(x-h)+cf(x)+df(x+h)+ef(x+2h)=(a+b+c+d+e)f(x)+(-2a-b+d+2e)hf'(x)+(2a+\frac{b}{2}+\frac{d}{2}+2e)h^2f''(x)+(-\frac{4a}{3}-\frac{b}{6}+\frac{d}{6}+\frac{4e}{3})h^3f^{(3)}(x)+(\frac{2a}{3}\frac{b}{24}+\frac{d}{24}+\frac{2e}{3})h^4f^{(4)}(x)+O(5)$

Then, we need to solve the system of equations: \\

$a+b+c+d+e = 0$ \\
$-2a-b+d+2e = 1$ \\
$2a + b/2 + d/2 + 2e = 0$ \\ 
$-4a/3-b/6+d/6+4e/3 = 0$ \\
$2a/3+b/24+d/24+2e/3 = 0$ \\

3.2b) The error is proportional to $h^4$ since the line is.. relatively straight. Solving for the slope of the line yields $m \approx 0.89$, which is pretty close. After h goes lower than 0.001, the error looks atrocious (since the log of 1/$h^4$ would be so close to 0 the log would mess up). But otherwise it is pretty close.

3.3) This graph makes sense because it is, firstly, exactly the same as if it were plotted on Desmos. Next, since as the limit goes to infinity for $f(x)=\frac{\ln{x}}{\cosh{x}}, $f(\infty)=0$. Thus, since $f(\infty)=0$, $f''(\infty)=0$ as well. Also, as $x\rightarrow0$, $ln(x)$ becomes more and more negative (approaching infinity), and the second derivative sees this affect as well but it's amplifed significantly more (since goes like $1/x^2$ instead of $\ln{x}$). The $\cosh{x}$ function doesn't really do much lol.
