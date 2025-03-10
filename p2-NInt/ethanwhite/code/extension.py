import functions
import numpy as np
import scipy as sp
import math

def f(x,c): # Adjusts integrand based on user choice.
	if c == "Y": f = math.sqrt(128)*(math.sin(x))**5
	else: f = (x**2)/(math.sqrt(2-x))
	return f

def quadrature(a,b,N,c): # Quadrature method!
        roots, weights = sp.special.roots_legendre(N) # Provided on writeup.
        sum = 0
        for i in range(0,N):
                sum += weights[i] * f(((b-a)*roots[i]+a+b)/2,c) # Multiplies the weight by the function evaluated at opti>
                if i == N-1: sum *= (b-a)/2 # Our du-component that we must use from our initial mapping.

        return sum

a, b, N = 0, 2, int(input("\nN = "))
choice = input("Apply change of variables? Y/N: ") # Asking user.

if choice == "Y": b = math.pi/2 # Just changes b, since a doesn't change w/ change of variables.

print("\nWith Gaussian quadrature, the integral is: ",quadrature(a,b,N,choice))
if choice == "Y": print("With Simpson's method, the integral is: ",functions.simpson(a,b,N,choice))
print("\nNotice that the correct integral value is 6.03397786613")

# Pre-variable-change, N = 100,000 did not even get to 5 significant digit for quadrature method.

# N = 9 produces accuracy of 10 significant digits after the change of variables for quadrature method.
# N = 87 produces accuracy of 10 significant digits after the change of variables for Simpson's method.
