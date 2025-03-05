import numpy as np
import pylab as py
import math as math
import time as time
import sys as sys
import scipy as sp
import matplotlib.pyplot as plt

def f(x):
	f = math.sin(math.sqrt(100*x))**2
	return f

def leftpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i
		y = f(x)
		sum += h*y
	return sum

def rightpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + (i+1)*h
		y = f(x)
		sum += h*y
	return sum

def midpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i + h/2
		y = f(x)
		sum += h*y
	return sum

def trapezoid(a,b,N):
        sum = (leftpoint(a,b,N) + rightpoint(a,b,N))/2
        return sum

def simpson(a,b,N):
        sum = trapezoid(a,b,N)/3 + 2*midpoint(a,b,N)/3
        return sum

def quadrature(a,b,N):
	roots, weights = sp.special.roots_legendre(N+1)
	sum = 0
	for i in range(0,N):
		sum += weights[i+1] * f((roots[i+1]*(b-a)+a+b))
	return sum

def verify(a,b,x):
	verify = (2*x-a-b)/(b-a)
	return verify

def p1(x):
	p1 = x
	return p1

def p2(x):
	p2 = (3*x**2-1)/2
	return p2

def p3(x):
	p3 = (5*x**3-3*x)/2
	return p3

def p4(x):
	p4 = (35*x**4-30*x**2+3)/8
	return p4

def legendreplot():
	x = np.linspace(-1,1,100)
	fig, axs = plt.subplots(4,4)

	y = np.array([p1(x),p2(x),p3(x),p4(x)])
	for i in range(0,4):
		for j in range(0,4):
			title = "P" + str(i+1) + ",P" + str(j+1) + ",P" + str(i+1) + " * P" + str(j+1)
			label1 = "P" + str(i+1)
			label2 = "P" + str(j+1)
			label3 = "P" + str(i+1) + " * P" + str(j+1)

			axs[i,j].plot(x,y[i],'tab:olive')
			axs[i,j].plot(x,y[j],'tab:cyan')
			axs[i,j].plot(x,y[i]*y[j],'tab:pink')
			axs[i,j].set_title(title)

	fig.tight_layout()
	fig.show()
	return

def answer(L,R,M,T,S,Q):
	printrainbow("\nThe correct value should be 0.4558235.\n")
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

def logplot(a,b,N):
	Nlist = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
	Nlistlog = [math.log(x) for x in Nlist]

	anslist = [0] * 20

	for iN, N in enumerate(Nlist): anslist[iN] = simpson(a,b,N)

	anslistlog = [math.log(np.abs(x-1)) for x in anslist]

	py.plot(Nlistlog, anslistlog,'o-')
	py.xlabel('Log(N)')
	py.ylabel('Log(Area)')
	py.show(block=False)
	return

def methodcheck(a,b):
	N, correct, error, i = 1, 0.455823, 1, 0
	while error > 0.0000005:
		val = simpson(a,b,N)
		error = correct - val
		i += 1
		N = 2 ** i

	print("\n",N)
	return

def printrainbow(text, delay=0.0001):
    colors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[94m",  # Blue
        "\033[95m"   # Magenta
    ]
    reset = "\033[0m"

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()
