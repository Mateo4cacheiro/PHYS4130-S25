import numpy as np
import math

def forward(x,h):
	p = (f(x+h)-f(x))/h
	e = secondderiv(x,h)*h/2
	return p, e

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
	p = 0
	e = 0
	return p, e

def secondderiv(x,h):
	p = (f(x+h)-2*f(x)+f(x-h))/(h*h)
	return p

def f(x):
	f = math.cos(x)*math.tanh(x)
	return f

x, h = float(2), float(input("h = "))

fval,ef = forward(x,h)
bval,eb = backward(x,h)
cval,ec = central(x,h)
tval,et = threepoint(x,h)
five,efive = fivepoint(x,h)
second = secondderiv(x,h)

print("forward: ",fval,"\nforward error: ",ef,"\n\nbackward: ",bval,"\nbackward error: ",eb,"\n\ncentral: ",cval,"\ncentral error: ",ec,"\n\nthree point: ",tval,"\nthree point error: ",et,"\n\nfive point: ",five,"\nfive point error: ",efive,"\n\nsecond: ",second)
