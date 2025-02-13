import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt


grid = np.array([[1,2,3], [9,8,7], [6,4,5]])
print(grid)

x, y = np.round(ndimage.center_of_mass(grid))
print(x, y)