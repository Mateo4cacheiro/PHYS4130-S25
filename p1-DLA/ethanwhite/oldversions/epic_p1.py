import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
from numba import jit

def create(size):
	t = time.time()
	midpoint = int((size - 1)/2)
	shrub = np.zeros([size,size])
	shrub[midpoint,midpoint] = 1 # p self explanatory
	spawnradius = round((size - midpoint)/1.2)
	deathradius = spawnradius + 5
	return shrub, spawnradius, deathradius, 1, t # returns array and iteration variable set to 1


def spawn(shrub, size, radius, n):
	angle = np.random.uniform(0,2*math.pi)
	x = round(size/2 + radius*math.cos(angle))
	y = round(size/2 + radius*math.sin(angle))
	shrub[x,y] = 1
	n += 1
	stick = False
	return n, x, y, radius, stick, shrub


def stuck(shrub, x, y):
	bool = False
	if shrub[x+1,y] or shrub[x-1,y] or shrub[x,y+1] or shrub[x,y-1] == 1: bool = True
	return bool

def distance(x, y, size):
	dis = math.sqrt((x-size/2)**2 + (y-size/2)**2)
	return dis

def attach(shrub, x, y):
	return

def rdir(n, x, y):
	if n == 1: x += 1
	if n == 2: x -= 1
	if n == 3: y += 1
	if n == 4: y -= 1
	return x, y

def timekeeping(n,t1):
	t = round(time.time()-t1)
	print(n,"particles in shrub in",t,"seconds.\n")
	return

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

num, size = 1000, 100 # initializes number of particles, array size
shrub, spawnradius, deathradius, n, t1 = create(size) # creates size * size array, sets midpoint to '1', returns creation and death radius, sets incremental psuedo-num to 1

while np.sum(shrub[0:size,0:size]) < num:
	if np.sum(shrub[0:size,0:size]) % 500 == 0: timekeeping(np.sum(shrub[0:size,0:size]),t1)
	n, x, y, dis, stick, shrub = spawn(shrub, size, round(spawnradius), n)
	while dis < deathradius and not stick:
		stick = stuck(shrub, x, y)
		if not stick:
			shrub, x, y, stick = move(shrub, x, y)
			dis = distance(x, y, size)
#			if dis >= step:
#				step += 1
#				spawnradius += 1
#				print(step)
#		else:
#			attach(shrub, x, y)
#			dis = distance(x, y, size)
#	if stick:
#		if round(distance(x, y, size) + 2) == spawnradius:
#			spawnradius = round(distance(x, y, size) + 2)
#			print(spawnradius)
	if dis >= deathradius:
		shrub[x,y] = 0
		n -= 1

#	if n == 1250 or n == 2500 or n == 5000 or n == 7500 or n == 10000: print(n)

#	if distance(x, y, size) >= deathradius: break # exit condition

print("total time elapsed:",round(time.time()-t1),"seconds")
print(np.sum(shrub[0:size,0:size]))
picture(shrub) # shows pretty picture
