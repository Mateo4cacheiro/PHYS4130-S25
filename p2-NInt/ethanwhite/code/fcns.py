import numpy as np
import math
import scipy as sp # for legendre polynomial weight and roots


# this is the function to be changed
def f(x):
	f = math.sin(math.sqrt(100*x))**2
	return f

# used in simpson rule
def leftpoint(a,b,N):
	sum, h = 0, (b-a)/N
	x = a
	for i in range(0,N-1):
		x += h
		sum += f(x) * h

	return sum

def rightpoint(a,b,N):
	sum, h = 0, (b-a)/N
	x = a + h
	for i in range(0,N-1):
		x += h
		sum += f(x) * h

	return sum

def midpoint(a,b,N):
	sum, h = 0, (b-a)/N
	x = a + h/2
	for i in range(0,N-1):
		x += h
		sum += f(x) * h

	return sum

def trapezoid(a,b,N):
        sum = (leftpoint(a,b,N) + rightpoint(a,b,N))/2
        return sum

def simpson(a,b,N):
        sum = trapezoid(a,b,N)/3 + 2*midpoint(a,b,N)/3
        return sum

def uf(a,b,u):
	ufunc = f(((b-a)*u+a+b)/2)
	return ufunc

def quadrature(a,b,N):
	roots, weights = sp.special.roots_legendre(N)
	sum = 0
	for i in range(0,N):
		sum += weights[i] * uf(a,b,roots[i])
		if i == N-1: sum *= (b-a)/2

	return sum

def usubtest(a,b,x):
	usub = (2*x-a-b)/(b-a)
	return usub

def answer(L,R,M,T,S,Q):
	print("\nThe correct value should be 1.0057025.\n")
	print("The result of the integral, with the left point method, is:", L)
	print("The result of the integral, with the right point method, is:", R)
	print("The result of the integral, with the mid point method, is:", M)
	print("The result of the integral, using the trapezoidal method, is:", T)
	print("The result of the integral, using Simpson's method, is:", S)
	print("The result of the integral, using the quadrature method, is:", Q)
	return

def init(a,b,N):
	L = leftpoint(a,b,N)
	R = rightpoint(a,b,N)
	M = midpoint(a,b,N)
	T = trapezoid(a,b,N)
	S = simpson(a,b,N)
	Q = quadrature(a,b,N)

	return L,R,M,T,S,Q

def methodcheck(a,b):
	N, correct, error, i = 1, 1.005702, 1, 0
	print("")
	while error > 0.0000001:
		val = simpson(a,b,N)
		error = correct - val
		print("N: ",N,", VALUE: ",f"{val:.{8}g}",", ERROR: ",f"{error:.{3}g}")
		i += 1
		N = 2 ** i

	return
