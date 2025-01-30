# testing

import numpy as np
import matplotlib as plt
import random

def create(sidelength):
	midpoint = int((sidelength-1)/2)
	tree = np.zeros([sidelength,sidelength])
	tree[midpoint,midpoint] = 1
	return tree

def spawn(tree,sidelength): # spawns a particle on the edge of the grid
	num = random.randint(0,1000)
	r = num % sidelength
	s = num % 4

	if s == 0: # spawns on top row
		tree[0,r] = 1
		x = 0
		y = r
	elif s == 1: # spawns on leftmost column
		tree[r,0] = 1
		x = r
		y = 0
	elif s == 2: # spawns on bottom row
		tree[sidelength-1,r] = 1
		x = sidelength - 1
		y = r
	elif s == 3: # spawns on rightmost column
		tree[r,sidelength-1] = 1
		x = r
		y = sidelength - 1

	return tree, x, y

def direction(x,y): # function to randomly generate where the particle will go
	num = random.randint(1,4)
	newx = x
	newy = y

	if num == 1: newx = x - 1 # left
	if num == 2: newy = y + 1 # up
	if num == 3: newx = x + 1 # right
	if num == 4: newy = y - 1 # down

	return newx, newy

def move(tree,x,y,fax):
	fax = False
	newx, newy = direction(x,y)
	print("BEFORE IF")
	if 0 <= newx < tree.shape[0] and 0 <= newy < tree.shape[1]: # keeps in-bounds
		if tree[newx,newy] == 0: # is it empty?
			tree[newx,newy] = 1
			tree[x,y] = 0
			x, y = newx, newy
			return tree,x,y,fax


		else: return tree,x,y,not fax # if 1, just return

	else: move(tree,x,y,fax)

	print("AFTER ELSE")
	return tree,x,y,not fax

# ---------------- main function below ------------------

num = 1
sidelength = 7
tree = create(sidelength)

for i in range(1,num+1):
	fax = False
	tree, x, y = spawn(tree,sidelength)
	while fax == False: tree,x,y,fax = move(tree,x,y,fax)

print(tree[0:sidelength,0:sidelength])
