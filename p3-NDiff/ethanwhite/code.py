import numpy as np
import matplotlib.pyplot as plt
import math

def forward(x,h):
	p = (f(x+h)-f(x))/h
	e = secondderiv(x,h)*h/2
	return p

def backward(x,h):
	p = (f(x)-f(x-h))/h
	e = -1*secondderiv(x,h)*h/2
	return p, e

def central(x,h):
	p = (f(x+h)-f(x-h))/(2*h)
	e = 0
	return p, e

def threepoint(x,h):
	p = (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)
	e = 0
	return p, e

def fivepoint(x,h):
	p = (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
	e = 0
	return p, e

def secondderiv(x,h):
	p = (f(x+h)-2*f(x)+f(x-h))/(h*h)
	return p

# Exercise 1
def loglogh(x):
	hvals = np.log([10**(-i) for i in range(1,7)])
	evalsFORWARD = np.log([secondderiv(x,10**(-i))*(10**(-i))/2 for i in range(1,7)])
#	evalsBACKWARD = np.log(np.abs([-secondderiv(x,10**(-i))*(10**(i))/2 for i in range(1,7)]))

	plt.plot(hvals,evalsFORWARD)
#	plt.plot(hvals,evalsBACKWARD)
	plt.show(block=False)

	slopeforward = (evalsFORWARD[5]-evalsFORWARD[0])/(hvals[5]-hvals[0])
	slopebackward = 1 #(evalsBACKWARD[5]-evalsBACKWARD[0])/(hvals[5]-hvals[0])
	print("Forward Slope: ",slopeforward,"\nBackward Slope: ",slopebackward)
	return

# Exercise 1, Machine Error
def errorbreak(x):
	hvals = np.log([10**(-i) for i in range(1,15)])
	evals = np.log([secondderiv(x,10**(-i))*(10**(-i))/2 for i in range(1,15)])

	plt.plot(hvals,evals)
	plt.show(block=False)
	return

# Exercise 3.2
# (third derivative w/ https://math.stackexchange.com/questions/3371195/numerical-derivative-at-order-3)
def loglogh2(x):
	hvals = 2*np.log([10**(-i) for i in range(1,6)])
	evals = np.log([(-f(x-3*(10**(-i)))+3*f(x-(10**(-i)))-3*f(x+(10**(-i)))+f(x+3*(10**(-i))))/(8*(10**(-i))**3)*(10**(-i))**2/6 for i in range(1,6)])

	plt.plot(hvals,evals)
	plt.show(block=False)

	slope = (evals[4]-evals[0])/(hvals[4]-hvals[0])
	print("Slope H2: ",slope)
	return

# Homework 3.2
def loglogh4(x):
	hvals = 4*np.log([10**(-i) for i in range(1,6)])
	evals = 0

	plt.plot(hvals,evals)

	slope = (evals[4]-evals[0])/(hvals[4]-hvals[0])
	print("Slope H4: ",slope)
# Homework 3.3
def secondderivgraph(h):
	a, b, p, i = 2, 5, 2, 0
	x, y = np.zeros([1+int((b-a)/h)]),np.zeros([1+int((b-a)/h)])
	while p <= b:
		y[i] = (fs(p+h)-2*fs(p)+fs(p-h))/(h*h)
		x[i] = p
		p += h
		i += 1

	plt.plot(x,y)
	plt.show(block=False)
	return

def fs(x):
	f = math.log(x)/math.cosh(x)
	return f

def f(x):
	f = math.cos(x)*math.tanh(x)
	return f

x, h = float(2), float(input("h = "))

fval,ef = forward(x,h), 1
bval,eb = backward(x,h)
cval,ec = central(x,h)
tval,et = threepoint(x,h)
five,efive = fivepoint(x,h)
second = secondderiv(x,h)

print("forward: ",fval,"\nforward error: ",ef,"\n\nbackward: ",bval,"\nbackward error: ",eb,"\n\ncentral: ",cval,"\ncentral error: ",ec,"\n\nthree point: ",tval,"\nthree point error: ",et,"\n\nfive point: ",five,"\nfive point error: ",efive,"\n\nsecond: ",second)

#loglogh(x)
#errorbreak(x)
#loglogh2(x)
secondderivgraph(h)
