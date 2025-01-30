# testing

import numpy as np
import matplotlib as plt
import random

def create(sidelength): # preferably odd sidelength
	midpoint = int((sidelength-1)/2)
	tree = np.zeros([sidelength,sidelength]) # making everything
	tree[midpoint,midpoint] = 1
	return tree

def spawn(tree,sidelength):
	num = random.randint(0,1000)
	r = num % sidelength
	s = num % 4

	if s == 0:
		tree[0,r] = 1
		x = 0
		y = r
	elif s == 1:
		tree[r,0] = 1
		x = r
		y = 0
	elif s == 2:
		tree[sidelength-1,r] = 1
		x = sidelength - 1
		y = r
	elif s == 3:
		tree[r,sidelength-1] = 1
		x = r
		y = sidelength - 1

#	print("the location of 1 is:",x,y)
#	print("and the value is: ",tree[x,y])

	return tree, x, y # this literally does not work but it somehow does

def move(tree,x,y):
	print("x =",x,"\ny =",y,"\n1.0 =",tree[x,y])

num = 1
sidelength = 7

tree = create(sidelength)

for i in range(1,num+1):
	tree, x, y = spawn(tree,sidelength)
	move(tree,x,y)

print(tree[0:sidelength,0:sidelength])
