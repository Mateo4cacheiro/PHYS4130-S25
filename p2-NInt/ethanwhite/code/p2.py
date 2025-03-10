import fcns # Python file of main computational functions.
import legendreplot # Python file that spawns 4x4 Legendre polynomial plot.

N, a, b = int(input("\nN = ")), 0, 2 # Subinterval amount determined by user and setting the function bounds.
L,R,M,T,S,Q = fcns.init(a,b,N) # Finding the integral sum using all six methods and throwing them back here.

if fcns.usubtest(a,b,a) == -1 and fcns.usubtest(a,b,b) == 1: print("\n[a,b] maps to [-1,1].") # Just verifying the u-sub maps to [-1,1].

fcns.answer(L,R,M,T,S,Q) # Spits out the answer from the integrals found in line 5.
fcns.methodcheck(a,b) # Creates the N-table using Simpson's rule.
legendreplot.legendreplot() # Creates the 4x4 Legendre polynomial plot.
