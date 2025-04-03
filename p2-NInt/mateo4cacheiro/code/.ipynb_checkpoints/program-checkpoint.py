import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sp


###############################################################################################################################################
#Location to define one mathematical function.
def function1(x):
    return((np.sin(np.sqrt(100*x)))**2) 
###############################################################################################################################################



###############################################################################################################################################
#Location to define a second mathematical function.
def function2(x):
    return((np.sin(np.sqrt(100*x)))**2)
###############################################################################################################################################


###############################################################################################################################################
#Defines a function that will take a mathematical function and its boundary points and return its integral using a left-point Riemann
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
#Defines a function that will take a mathematical function and its boundary points and return its integral using a midpoint Riemann
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
#Defines a function that will take a mathematical function and its boundary points and return its integral using a right-point Riemann
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
#Defines a function that will take a mathematical function and its boundary points and return its integral using a trapezoid Riemann    
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
#Defines a function that will take a mathematical function and its boundary points and return its integral using Simpson's rule
def Simp(f,a,b,N):
    I=1/3*trapezoid(f,a,b,N)+2/3*midpoint(f,a,b,N)
    return(I)
###############################################################################################################################################


###############################################################################################################################################
#Function used to express the Nth Legendre Polynomials as a function of x between -1 and 1.
def L(x,N):
    leg =legendre(N)
    P_N = leg(x)
    return(P_N)
###############################################################################################################################################


###############################################################################################################################################
#Function used to find the integral of the product of two Legendre Polynomials between a and b. 
def Ltrap(c,d,a,b,N):
    h = (b-a)/N #calculate width of box
    Sum= 0 #set starting sum to 0.
    f=legendre(c)*legendre(d) #c and d indicate the order of the individual Legendre polynomials.
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
#Integrates a function using Gaussian quadrature.    
def Gquad(f,a,b,N):
    roots, weights = sp.special.roots_legendre(N) #pull roots of Legendre polynomials and associated weights
    Sum =0 #Set sum to zero
    for i in range(N): #sum all N terms
        Sum += weights[i]*usub(f,a,b,roots[i]) #add the product of the weight and the value of f(u) at the root.
    Sum = Sum*((b-a)/(2)) #include du factor to final sum. 
    return(Sum)
###############################################################################################################################################



f,a,b,N= function1,0,2,1
ITE,IT=10000000000,0   #use caution to make sure 100000000 is very large relative to integral you wish to find. 
i=0
step = (b-a)/(10000)
print("The following values are found using trapezoid rule")
while(ITE>0.0000005):
    IT= trapezoid(f,a,b,N)
    diff=(((f(b-(step))-f(b))/(step))-((f(a)-f(a+(step)))/(step)))
    ITE=abs(-(b-a)**3/(12*N**2) * diff)
    print(ITE)
    print(f"| value: {IT:2.7f} | error: {ITE:2.7f} | subdivisions: {N}|")
    i+=1
    N = 2**i
    
xvals =  np.linspace(-1,1,10000)
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
#Uncomment the next line to make the code output the graphic. I have left this commented out because I have a saved version in the write-up and my computer really struggles to show the fig. 
#plt.show()
print(Sum)

print("Now using Gaussian Quadrature")
f,a1,b1,N =  function2,0,2,12
if( usubcheck(a1,b1,a1)==-1 and  usubcheck(a1,b1,b1)==1):
    print("u(x) successfully maps [a,b] to [-1,1]")
    Sum =  Gquad(f,a1,b1,N)
    print(Sum, "was found using ", N, " Sub-intervals")
else:
    print("failure: u(x) could not successfuly map [a,b] to [-1,1] and the integral could not be found using Guassian Quadrature.")
