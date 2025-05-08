# Project 5--FEM
# Adam Grice
# 06-05-2025

from skfem import *
from skfem.models.poisson import unit_load
from skfem.helpers import dd, ddot, trace, eye
import numpy as np
from skfem.visuals.matplotlib import draw, plot
import matplotlib.pyplot as plt

m = MeshTri.init_circle(2).refined(3).with_boundaries({'outer': lambda x: np.sqrt(x[0]**2 + x[1]**2) > 0.99}) # create mesh


basis = Basis(m, ElementTriMorley()) # create basis functions for this mesh using Morley element

d = 0.001
E = 200e9
nu = 0.3



def C(T):
    return E / (1 + nu) * (T + nu / (1 - nu) * eye(trace(T), 2)) 


@BilinearForm
def bilinf(u, v, _):
    return d ** 3 / 12.0 * ddot(C(dd(u)), dd(v)) # This is basically the 4th order derivative term


@LinearForm
def load(v, w):
    x, y =  w.x
    return v * (np.sin(np.pi * y)) # and this is the load function

K = bilinf.assemble(basis)
f = load.assemble(basis) # assemble both forms in the basis


D = basis.get_dofs().all() # gets degrees of freedom for mesh elements

x = solve(*condense(K, f, D=D)) # solves

fig, ax = plt.subplots(figsize=(6, 5))  
draw(basis.mesh, ax=ax)
plot(basis, x, ax=ax, shading='gouraud', colorbar = True)

ax.set_xlabel('x [m]')   
ax.set_ylabel('y [m]')   
ax.set_title('Plate Deflection')  
ax.axis('equal')         

plt.show()