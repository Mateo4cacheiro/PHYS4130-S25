# Author: Adam Grice
# Project: P2-NInt
# Date: 03-10-2025

import numpy as np
import scipy
import scipy.special
import matplotlib.pyplot as plt



def func(u,a,b):
    k = 0.5*(u*(b-a) + a + b)
    val = (np.sin(np.sqrt(100*k)))**2
    return val

def func1(u, a, b):
    k = 0.5*(u*(b-a) + a + b)
    val = 1/(k**2)
    return val

def traprule(f, a, b, N):
    h = (b - a)/N
    I = (h/2)*(f(a) + f(b))

    for i in range(N-1):
        x = (a + (i*h))
        I += f(x)*h

    error = np.abs(I - 1.005702542825726)
    print("Number of slices:", N)
    print("Value of Integral:", I)
    print("Error:", error)


def gauss_quad(N, a, b):
    I = 0
    dx = ((b - a)/2)
    roots, weights = scipy.special.roots_legendre(N+1)
    I = dx*sum(weights*func(roots, a, b))


    return I
print(gauss_quad(100, 0, 2))

fig, axs = plt.subplots(4, 4)

min = -1.0
max = 1.0
step = 0.05

x = np.arange(min, max + step, step)

P1 = scipy.special.legendre(1)
P2 = scipy.special.legendre(2)
P3 = scipy.special.legendre(3)
P4 = scipy.special.legendre(4)

y1 = P1(x)
y2 = P2(x)
y3 = P3(x)
y4 = P4(x)

#top row
axs[0,0].plot(x, y1)
axs[0,0].plot(x, y1)
axs[0,0].plot(x, y1*y1)

axs[0,1].plot(x, y1)
axs[0,1].plot(x, y2)
axs[0,1].plot(x, y1*y2)

axs[0,2].plot(x, y1)
axs[0,2].plot(x, y3)
axs[0,2].plot(x, y1*y3)

axs[0,3].plot(x, y1)
axs[0,3].plot(x, y4)
axs[0,3].plot(x, y1*y4)


#2nd row
axs[1,0].plot(x, y2)
axs[1,0].plot(x, y1)
axs[1,0].plot(x, y2*y1)

axs[1,1].plot(x, y2)
axs[1,1].plot(x, y2)
axs[1,1].plot(x, y2*y2)

axs[1,2].plot(x, y2)
axs[1,2].plot(x, y3)
axs[1,2].plot(x, y2*y3)

axs[1,3].plot(x, y2)
axs[1,3].plot(x, y4)
axs[1,3].plot(x, y2*y4)


#3rd row
axs[2,0].plot(x, y3)
axs[2,0].plot(x, y1)
axs[2,0].plot(x, y3*y1)

axs[2,1].plot(x, y3)
axs[2,1].plot(x, y2)
axs[2,1].plot(x, y3*y2)

axs[2,2].plot(x, y3)
axs[2,2].plot(x, y3)
axs[2,2].plot(x, y3*y3)

axs[2,3].plot(x, y3)
axs[2,3].plot(x, y4)
axs[2,3].plot(x, y3*y4)


#4th row
axs[3,0].plot(x, y4)
axs[3,0].plot(x, y1)
axs[3,0].plot(x, y4*y1)

axs[3,1].plot(x, y4)
axs[3,1].plot(x, y2)
axs[3,1].plot(x, y4*y2)

axs[3,2].plot(x, y4)
axs[3,2].plot(x, y3)
axs[3,2].plot(x, y4*y3)

axs[3,3].plot(x, y4)
axs[3,3].plot(x, y4)
axs[3,3].plot(x, y4*y4)

#plt.show()