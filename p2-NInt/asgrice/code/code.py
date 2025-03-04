# Author: Adam Grice
# Project: P2-NInt
# Date: 02-27-2025

import numpy as np
import scipy
import scipy.special
from tabulate import tabulate


def func(k):
    val = np.sin(np.sqrt(100*k))**2
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

def leg_p(n):
    return scipy.special.legendre(n)
    

#traprule(func, 0, 2, 1700000)

p1 = leg_p(1)
p2 = leg_p(2)
p3 = leg_p(3)
p4 = leg_p(4)

table = [['P', 'P', 'P', 'P'],
         [(p1, p1, p1*p1), (p1, p2, p1*p2), (p1, p3, p1*p3), (p1, p4, p1*p4)], 
         [(p2, p1, p2*p1), (p2, p2, p2*p2), (p2, p3, p2*p3), (p2, p4, p2*p4)],
         [(p3, p1, p3*p1), (p3, p2, p3*p2), (p3, p3, p3*p3), (p3, p4, p3*p4)],
         [(p4, p1, p4*p1), (p4, p2, p4*p2), (p4, p3, p4*p3), (p4, p4, p4*p4)] ]

print(table)