import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as py
from scipy.special import legendre
import scipy as sp


###############################################################################################################################################
#Location to define one mathematical function.
def function(x):
    return((np.sin(np.sqrt(100*x)))**2) 
###############################################################################################################################################



###############################################################################################################################################
#Location to define a second mathematical function.
def function2(x):
    return((np.sin(np.sqrt(100*x)))**2)
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical fucntion and its boundary points and return its integral using a leftpoint riemann
def leftpoint(f,a,b,N):
    h = (b-a)/N #calculate width of box
    x = a #set starting left point as 0
    Sum = 0 #start sum as 0
    while x < b:
        Sum += f(x)*h #add area
        x += h #move left point
    return Sum   # Note that we need this to tell the code outside of the function about the result
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical fucntion and its boundary points and return its integral using a midpoint riemann
def midpoint(f,a,b,N):
    h = (b-a)/N #calculate width of box
    x = a+h/2 #set starting mid point as halfway through a rectangle
    Sum = 0 #start sum as 0
    while x < b:
        Sum += f(x)*h #add area
        x += h #move left point
    return Sum
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical fucntion and its boundary points and return its integral using a rightpoint riemann
def rightpoint(f,a,b,N):
    h = (b-a)/N #calculate width of box
    x = h #set starting right point as h
    Sum = 0 #start sum as 0
    while x <= b:
        Sum+=f(x)*h #add area
        x+=h #move right point
    return Sum   # Note that we need this to tell the code outside of the function about the result
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical fucntion and its boundary points and return its integral using a trapezoid riemann    
def trapezoid(f,a,b,N):
    h = (b-a)/N #calculate width of box
    Sum= 0 #set starting sum to 0.
    Sum+=(h/2)*(f(a)+f(b)) 
    i=1
    while i <= N-1:
        Sum+=(h*f(a+i*h))
        i+=1
    return Sum
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical fucntion and its boundary points and return its integral using simpson's rule
def Simp(f,a,b,N):
    I=1/3*trapezoid(f,a,b,N)+2/3*midpoint(f,a,b,N)
    return(I)
###############################################################################################################################################


###############################################################################################################################################
#Function used to express the Nth legendre Polynomials as a function of x between -1 and 1.
def L(x,N):
    leg =legendre(N)
    P_N = leg(x)
    return(P_N)
###############################################################################################################################################


###############################################################################################################################################
#Function used to find the integral of the product of two legendre Polynomials between a and b. 
def Ltrap(c,d,a,b,N):
    h = (b-a)/N #calculate width of box
    Sum= 0 #set starting sum to 0.
    f=legendre(c)*legendre(d) #c and d indicate the order of the individual legendre polynomials.
    Sum+=(h/2)*(f(a)+f(b)) 
    i=1
    while i <= N-1:
        Sum+=(h*f(a+i*h))
        i+=1
    return Sum
###############################################################################################################################################


###############################################################################################################################################
#A function used to map an x value to its corresponding u value using the u substitution that maps [a,b] to [-1,1]
def usubcheck(a,b,x):
    return((2*x-a-b)/(b-a))
###############################################################################################################################################


###############################################################################################################################################
#Given the function f(x) and u this returns "f(u)".
def usub(f,a,b,u):
    return(f((1/2)*((b-a)*u+a+b)))
###############################################################################################################################################


###############################################################################################################################################
#Integrates a function using guassian quadrature.    
def Gquad(f,a,b,N):
    roots, weights = sp.special.roots_legendre(N) #pull roots of legendre polynomials and associated weights
    Sum =0 #Set sum to zero
    for i in range(N): #sum all N terms
        Sum += weights[i]*usub(f,a,b,roots[i]) #add the product of the weight and the value of f(u) at the root.
    Sum = Sum*((b-a)/(2)) #include du factor to final sum. 
    return(Sum)
###############################################################################################################################################



f,a,b,N= function,0,2,1
correct_val=1.005702542825726
ITE,IT=100,0
i=0
print("The following values are found using trapezoid rule")
while(ITE>0.0000005):
    IT= trapezoid(f,a,b,N)
    ITE=abs(IT-correct_val)
    print(f"| value: {IT:2.7f} | error: {ITE:2.7f} | subdivisions: {N}|")
    i+=1
    N = 2**i
    
xvals =  np.linspace(-1,1,N)
Sum =  np.zeros([4,4])

fig = plt.figure(figsize=(10, 10))
outer_grid = fig.add_gridspec(4, 4, wspace=0.5, hspace=0.5)

for i in range(4):
    for j in range(4):
        # gridspec inside gridspec
        inner_grid = outer_grid[i, j].subgridspec(3, 1, wspace=1, hspace=1)
        axs = inner_grid.subplots()  # Create all subplots for the inner grid.
        axs[0].plot(xvals, L(xvals,i+1))
        axs[1].plot(xvals, L(xvals,j+1))
        axs[2].plot(xvals, L(xvals,i+1)* L(xvals,j+1))
        Sum[i,j]=((2*(j+1)+1)/2)* Ltrap((i+1),(j+1),-1,1,N)
        if Sum[i,j] < 0.00001:
            Sum[i,j]=0
        if abs(1-Sum[i,j])<0.00001:
            Sum[i,j]=1
plt.show()
print(Sum)

print("Now using Gaussian quadrature")
f,a,b,N =  function2,0,2,12
if( usubcheck(a,b,a)==-1 and  usubcheck(a,b,b)==1):
    print("u(x) successfully maps [a,b] to [-1,1]")
Sum =  Gquad(f,a,b,N)
print(Sum, "was found using ", N, " Subintervals")