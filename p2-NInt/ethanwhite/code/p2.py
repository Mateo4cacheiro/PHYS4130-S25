import fcns
import legendreplot

N, a, b = int(input("\nN = ")), 0, 2
L,R,M,T,S,Q = fcns.init(a,b,N)

if fcns.usubtest(a,b,a) == -1 and fcns.usubtest(a,b,b) == 1: print("\n[a,b] maps to [-1,1].")

fcns.answer(L,R,M,T,S,Q)
fcns.methodcheck(a,b)
legendreplot.legendreplot()
