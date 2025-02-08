import numpy as np
import random
import matplotlib.pyplot as plt
import time
#import numba

part_tot = 20000
size = 1001 #size of the grid, must be odd for a center

t0 = time.time()
tmid1 = t0
particles = 1
x0 = int((size - 1) / 2)
e_radius = 15 #edge radius
d_radius = 35 # death radius
tree = np.zeros([size, size]) # n X n array means array center is [(n-1)/2,(n-1)/2] when n is odd
tree[x0, x0] = 1
spawn_overlap = 0
i=0

def Spawn():
    rand1 = random.randrange(36000) / 100
    angle = rand1 * np.pi / 180
    if 90 > rand1 >= 0:
        x = -e_radius * np.cos(angle) - x0
        y = e_radius * np.sin(angle) - x0
    if 180 > rand1 >= 90:
        x = e_radius * np.cos(angle) - x0
        y = -e_radius * np.sin(angle) - x0
    if 270 > rand1 >= 180:
        x = -e_radius * np.cos(angle) - x0
        y = e_radius * np.sin(angle) - x0
    if 360 > rand1 >= 270:
        x = e_radius * np.cos(angle) - x0
        y = -e_radius * np.sin(angle) - x0
    return round(x), round(y)

while particles < part_tot:
    x, y = Spawn()
    if tree[x, y] != 1:
        while i < 1:
            if np.sqrt((x + x0)*(x + x0) + (y + x0)*(y + x0)) > d_radius: # Checking if particle is in death zone
                break
            elif (tree[x + 1, y] + tree[x - 1, y] + tree[x, y + 1] + tree[x, y - 1] + tree[x + 1, y + 1]  #Long statement checking if particle is near aggregate
                   + tree[x + 1, y - 1] + tree[x - 1, y + 1] + tree[x - 1, y - 1] > 0):
                tree[x, y] = 1
                particles += 1
                if (particles / 1000) == int(particles / 1000):
                    tmid2 = time.time()
                    print("N =", particles, "| Time since last checkpoint:", round(tmid2 - tmid1, 2), "| Time since start:", round(tmid2 - t0, 2))
                    tmid1 = tmid2
                if d_radius > np.sqrt((x + x0)*(x + x0) + (y + x0)*(y + x0)) > e_radius and d_radius < x0: #Radius increaser
                    e_radius += 1
                    d_radius += 1
                    if d_radius == x0 - 2:
                        print("*** DEATH RADIUS MAXXED ***")
                break
            else: #Mover
                randx = random.randrange(-1,2)
                randy = random.randrange(-1,2)
                x += randx
                y += randy
                
t1 = time.time()
hours = int((t1 - t0) / 3600)
minutes = int(((t1 - t0) / 3600 - hours) * 60)
seconds = int(((((t1 - t0) / 3600 - hours) * 60) - minutes) * 60)
print("*** TIME ELAPSED :", hours, "HOURS,", minutes, "MINUTES, AND", seconds, "SECONDS ***")
print("*** TOTAL PARTICLES =", particles, " ***")
plt.matshow(tree)