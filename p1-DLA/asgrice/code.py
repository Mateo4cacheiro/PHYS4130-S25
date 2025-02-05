# Author: Adam Grice
# Project: P1-DLA
# Date: 02-05-2025

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# Create grid
x = 40
max_r = x - 10
Nmax = 30
N = 1
grid = np.zeros((x,x))
grid[x//2,x//2] = 1
i = 0


def generate_particle(max_r):
    s = np.random.randint(low=0, high=4) #choose integer from 0 to 3 to determine which side to generate particle on
    if(s == 0): #generate particle at top of grid
        x0 = np.random.randint(low = 0, high = max_r)
        y0 = 1
        return x0, y0
    elif(s == 1): #right side of grid
        x0 = max_r - 2
        y0 = np.random.randint(low=0,high=max_r)
        return x0, y0
    elif(s == 2): #bottom of grid
        x0 = np.random.randint(low=0,high=max_r)
        y0 = max_r - 2
        return x0, y0
    elif(s == 3): #left side of grid
        x0 = 1
        y0 = np.random.randint(low=0,high=max_r)
        return x0, y0


    

# determines whether there is a nonzero point in vicinity of another nonzero point
def get_coords(grid, x0, y0):
    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 1 ):
        return True
    else:
        return False


# takes in two coordinates and steps them in a random direction.
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 2)
    new_b = b + np.random.randint(low = -1, high = 2)
    return new_a, new_b

# Commenting this out to try something else
# while(N < Nmax):
#     x1, y1 = generate_particle(x)

#     while(i < 1000):
#         get_coords(grid, x1, y1)
#         if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#             grid[x1, y1] = 0
#             break
#         elif(get_coords(grid, x1, y1) == True):
#             N += 1
#             break
#         else:
#             grid[x1, y1] = 0 #zero current position
#             # print(x1, y1)
#             x1, y1 = step(x1, y1) #update position
#             #print(step(x1,y1))
#             #print(x1, y1)
#             if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#                 x1, y1 = generate_particle(x)
            
#             grid[x1, y1] = 1 #update value of new position
#             # plt.imshow(grid)
#             # plt.draw()
#             # plt.pause(0.0001)
#     i += 1



# grid = np.zeros((x,x))
# for m in range(1000):
#    x2, y2 = generate_particle(x)
#    grid[x2,y2] = 1
#    print(f'{x2},{y2}')


while(N < Nmax):
    stuck = False
    rad = max_r
    x1, y1 = generate_particle(rad)
    while not stuck:
        x1, y1 = step(x1, y1)
        stuck = get_coords(grid,x1,y1)
    if stuck:
        N+=1
        rad = np.sqrt((x1^2)+(y1^2))
        max_r = max((rad, max_r))
            