# for exercise 3.1:
# a) See code below:
# b) See plot after running code.
# c) It is proportional to 1/N.
# d) See plot after running code.
# e) I think, since the leftpoint calculation has less error, it is superior.

import numpy as np
import pylab as py
import math

def sin(x):
	f = math.sin(x)
	return f

def leftpoint(f,a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i
		y = sin(x)
		sum += h*y
	return sum

def midpoint(f,a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i + h/2
		y = sin(x)
		sum += h*y
	return sum

def init(f,a,b,N):
	L = leftpoint(f,a,b,N)
#	R = rightpoint(f,a,b,N)
	M = midpoint(f,a,b,N)
	return L,M

def logplot(f,a,b,N):
	Nlist = [2,4,8,16,32,64,128,256,512,1024]
	Nlistlog = [math.log(x) for x in Nlist]

	anslist1 = [0] * 10
	anslist2 = [0] * 10

	for iN, N in enumerate(Nlist): anslist1[iN] = leftpoint(f,a,b,N)
	for iN, N in enumerate(Nlist): anslist2[iN] = midpoint(f,a,b,N)

	anslist1log = [math.log(np.abs(x-1)) for x in anslist1]
	anslist2log = [math.log(np.abs(x-1)) for x in anslist2]

	py.plot(Nlistlog, anslist1log,'o-', label = "Leftpoint")
	py.plot(Nlistlog, anslist2log,'o-', label = "Midpoint")
	py.legend()
	py.xlabel('Log(N)')
	py.ylabel('Error')
	py.show(block=False)
	return

# main fcn for exercise 3.1

N, a, b, f = int(input("\nN = ")), 0, math.pi/2, 1

L,M = init(f,a,b,N)
print("midpoint sum:",M)
logplot(f,a,b,N)
