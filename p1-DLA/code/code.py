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

# returns coordinates around a point in grid
def get_coords(grid, x0, y0):
    grid[0:10:1]
    return x0 + 1, x0 - 1, y0 + 1, y0 - 1

# takes in two coordinates and steps them in a random direction.
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 1)
    new_b = b + np.random.randint(low = -1, high = 1)
    return new_a, new_b