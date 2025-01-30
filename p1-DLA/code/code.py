# Author: Adam Grice
# Project: P1-DLA
# Date: 01-29-2025

import numpy as np
import matplotlib.pyplot as plt


# Create grid
x = 11
y = 11
grid = np.zeros((x,y))
grid[x//2,y//2] = 1

# generate particle
def generate_particle():
    x0 = np.random.randint(low=0, high=10)
    y0 = np.random.randint(low=0,high=10)
    grid[x0, y0] = 1
    return x0, y0

# returns coordinates around a point in grid
def get_coords(grid, x0, y0):
    # print stuff just to see what's happening. Not necessary
    # -------------------------------------------------------
    print(grid[x0 - 1:x0 + 2, y0 - 1: y0 + 2])

    print(np.sum(grid[x0-1:x0+2]))

    print(np.sum(grid[y0-1:y0+2]))
    # -------------------------------------------------------

    if (np.sum(grid[x0-1:x0+2]) > 1 ) or (np.sum(grid[y0-1:y0+2]) > 1):
        return True
    else:
        return False


# takes in two coordinates and steps them in a random direction.
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 1)
    new_b = b + np.random.randint(low = -1, high = 1)
    return new_a, new_b

x0, y0 = generate_particle()
print(x0, y0)
x1, y1 = step(x0, y0)
print(x1,y1)