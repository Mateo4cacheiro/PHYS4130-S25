# Author: Adam Grice
# Project: P2-NInt
# Date: 03-04-2025

import numpy as np
import scipy
import scipy.special
from tabulate import tabulate
import matplotlib.pyplot as plt



def func(k,a,b):
    u = (k*((b-a)/2) + ((a+b)/2))
    val = (np.sin(np.sqrt(100*u)))**2
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
    i = 0
    I = 0
    du = (b-a)/2
    #roots, weights = scipy.special.roots_legendre(i+1)
    for i in range (N):
        roots, weights = scipy.special.roots_legendre(i+1)
        I += weights[i]*func(roots[i],0,2)
        i += 1

    return I*du
print(gauss_quad(1000, 0, 2))