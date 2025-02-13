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

def rightpoint(f,a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + (i+1)*h
		y = sin(x)
		sum += h*y
	return sum

def midpoint(f,a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i + h/2
		y = sin(x*x)
		sum += h*y
	return sum

def answer(sumL,sumR,sumM):
	print("\nThe result of the integral, with the left point method, is:", sumL)
	print("The result of the integral, with the right point method, is:", sumR)
	print("The result of the integral, with the mid point method, is:", sumM)
	return

def init(f,a,b,N):
	L = leftpoint(f,a,b,N)
	R = rightpoint(f,a,b,N)
	M = midpoint(f,a,b,N)
	return L,R,M

def plot(f,a,b,N):
	Nlist = [2,4,8,16,32,64,128,256,512,1024]
	anslist = [0] * 10

	for iN, N in enumerate(Nlist): anslist[iN] = leftpoint(f,a,b,N)

	py.plot(Nlist, anslist,'o-')
	py.xlabel('N, Number of Subintervals')
	py.ylabel('Integration Area')
	py.show(block=False)
	return

def logplot(f,a,b,N):
	Nlist = [2,4,8,16,32,64,128,256,512,1024]
	Nlistlog = [math.log(x) for x in Nlist]

	anslist = [0] * 10

	for iN, N in enumerate(Nlist): anslist[iN] = leftpoint(f,a,b,N)

	anslistlog = [math.log(np.abs(x-1)) for x in anslist]

	py.plot(Nlistlog, anslistlog,'o-')
	py.xlabel('Number of Subintervals')
	py.ylabel('Integration Area')
	py.show(block=False)
	return

# --- main function below --- #

N, a, b, f = int(input("\nN = ")), 0, 100, 1

L,R,M = init(f,a,b,N)
print("midpoint sum:",M)

#answer(L,R,M)
#logplot(f,a,b,N)


