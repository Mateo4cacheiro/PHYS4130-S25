# Author: Adam Grice
# Project: P1-DLA
# Date: 02-06-2025

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
import numba as nb

# Create grid
x = 1000
spawn_rad = 10
kill_rad = spawn_rad + 6
Nmax = 1000
N = 1
grid = np.zeros((x,x))
grid[x//2,x//2] = 1
i = 0

# @nb.njit
def generate_on_circle(spawn_rad, x0, y0):

    angle = np.random.rand() * 2*np.pi
    xval = round(spawn_rad * np.cos(angle)) + x0
    yval = round(spawn_rad * np.sin(angle)) + y0

    return xval, yval

# @nb.njit
def generate_particle(spawn_rad):
    s = np.random.randint(low=0, high=4) #choose integer from 0 to 3 to determine which side to generate particle on
    if(s == 0): #generate particle at top of grid
        x0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        y0 = spawn_rad
        return x0, y0
    elif(s == 1): #right side of grid
        x0 = spawn_rad
        y0 = np.random.randint(low = x//2 - spawn_rad, high = x//2 + spawn_rad)
        return x0, y0
    elif(s == 2): #bottom of grid
        x0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        y0 = spawn_rad
        return x0, y0
    elif(s == 3): #left side of grid
        x0 = x - spawn_rad
        y0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        return x0, y0


    

# determines whether there is a nonzero point in vicinity of another nonzero point
# @nb.njit
def get_coords(grid, x0, y0):
    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 0 ):
        return True
    else:
        return False


# takes in two coordinates and steps them in a random direction.
# @nb.njit
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 2)
    new_b = b + np.random.randint(low = -1, high = 2)
    return new_a, new_b

# @nb.njit
def check_neighbors(x, x_coord, y_coord, kill_rad, stuck, spawn_rad, N):
    while not stuck:
        x_coord, y_coord = step(x_coord, y_coord)
        dist = np.sqrt(((x//2) - x_coord)**2 + ((x//2) - y_coord)**2)
        if(dist > kill_rad):
            x_coord, y_coord = generate_on_circle(spawn_rad, x//2, x//2)
        stuck = get_coords(grid, x_coord, y_coord)
        
        if stuck:
            grid[x_coord, y_coord] = 1
            N += 1
            rad = np.sqrt(((x//2) - x_coord)**2 + ((x//2) - y_coord)**2)
            if(rad >= spawn_rad):
                spawn_rad = rad + 10
                kill_rad = spawn_rad + 6

while(N < Nmax):
    stuck = False
    x1, y1 = generate_on_circle(spawn_rad, x//2, x//2)
    check_neighbors(x, x1, y1, kill_rad, stuck, spawn_rad, N)


plt.imshow(grid)
plt.show()