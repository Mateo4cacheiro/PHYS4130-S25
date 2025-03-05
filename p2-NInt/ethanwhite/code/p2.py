import fcns

N, a, b = int(input("\nN = ")), 0, 1
if fcns.verify(a,b,a) == -1 and fcns.verify(a,b,b) == 1: print("yep it maps [a,b] to [-1,1]")
L,R,M,T,S,Q = fcns.init(a,b,N)
fcns.answer(L,R,M,T,S,Q)

#fcns.logplot(a,b,N)
fcns.methodcheck(a,b)

fcns.legendreplot()
