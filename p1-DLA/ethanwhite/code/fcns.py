import numpy as np
import matplotlib.pyplot as plt
import random
import numba
import math
import time

@numba.jit
def program(shrub, n, num, size, spawnradius, deathradius, maxdis, t1):
	while np.sum(shrub[0:size,0:size]) < num:
		if np.sum(shrub[0:size,0:size]) % 500 == 0: print(np.sum(shrub[0:size,0:size]))
#			timekeeping(shrub,np.sum(shrub[0:size,0:size]),t1)
		n, x, y, distance, stick, shrub = spawn(shrub, size, spawnradius, n)

		while distance < deathradius and not stick:
			stick = stuck(shrub, x, y)
			if not stick:
				shrub, x, y, stick = move(shrub, x, y)
				distance = distance(x, y, size)
			if stick:
				if distance > maxdis:
					maxdis = distance
					spawnradius = 50 + maxdis
					deathradius = 10 + spawnradius
					print("maxdis updated to",maxdis)
		if distance >= deathradius:
			shrub[x,y] = 0
			n -= 1
	return shrub, maxdis, t1, num

def create(size):
	t = time.time()
	midpoint = int((size - 1)/2)
	shrub = np.zeros([size,size])
	shrub[midpoint,midpoint] = 1 # p self explanatory
	return shrub, 1, t # returns array and iteration variable set>

@numba.jit
def spawn(shrub, size, spawnradius, n):
	angle = np.random.uniform(0,2*math.pi)
	x = round(size/2 + spawnradius*math.cos(angle))
	y = round(size/2 + spawnradius*math.sin(angle))
	shrub[x,y] = 1
	n += 1
	stick = False
	return n, x, y, spawnradius, stick, shrub

@numba.jit
def stuck(shrub, x, y):
	bool = False
	if shrub[x+1,y] or shrub[x-1,y] or shrub[x,y+1] or shrub[x,y-1] == 1: bool = True
	return bool

@numba.jit
def distance(x, y, size):
	dis = math.sqrt((x-size/2)**2 + (y-size/2)**2)
#	rnddis = round(dis)
	return dis

@numba.jit
def rdir(n, x, y):
	if n == 1: x += 1
	if n == 2: x -= 1
	if n == 3: y += 1
	if n == 4: y -= 1
	return x, y

@numba.jit
def move(shrub, x1, y1):
	ran = random.randint(0,4)
	x2, y2 = rdir(ran, x1, y1)
	shrub[x1,y1] = 0
	shrub[x2, y2] = 1
	stick = stuck(shrub, x2, y2)
	return shrub, x2, y2, stick

def picture(shrub):
	plt.matshow(shrub,cmap='plasma')
	plt.show(block=False)
	return

def timekeeping(shrub,n,t1):
	t = round(time.time()-t1)
	print(n,"particles in shrub in",t,"seconds.\n")
#	picture(shrub)
	return
