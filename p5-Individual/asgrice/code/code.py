import matplotlib.pyplot as plt
import numpy as np

import skfem
from skfem.helpers import dot, grad
from skfem import *
import skfem.visuals.matplotlib

#********Playing around with tutorial stuff here*************

# mesh = skfem.MeshTri().refined(5)

# plt.subplots(figsize=(5,5))
# fem.visuals.matplotlib.draw(mesh, ax=plt.gca())

# plt.show()

# basis_p1 = skfem.Basis(mesh, skfem.ElementTriP1())
# fe_approx = basis_p1.zeros()

# fe_approx[:] = 1

# plt.subplots(figsize = (6,5))

# skfem.visuals.matplotlib.plot(basis_p1, fe_approx, vmin=0, vmax=2, ax=plt.gca(), colorbar = True)
# skfem.visuals.matplotlib.draw(mesh, ax=plt.gca())

# plt.show()

# def on_left_edge(x):
#     return x[0] < 0.1

# dof_subset_left_edge = basis_p1.get_dofs(facets=on_left_edge)
# fe_approx[dof_subset_left_edge] = 0

# dof_subset_top_edge = basis_p1.get_dofs(facets=lambda x: x[1] > 0.9)
# fe_approx[dof_subset_top_edge] = 3

# plt.subplots(figsize = (6,5))
# skfem.visuals.matplotlib.plot(basis_p1, fe_approx, vmin=0, vmax=3, ax=plt.gca(), colorbar = True, shading = 'gouraud')
# skfem.visuals.matplotlib.draw(mesh, ax=plt.gca())

# plt.show()

#****************** Attempt at 2D Euler-Bernoulli Beam*****************

m = MeshTri().refined(3).with_boundaries({"left": lambda x: x[0] == 0}) # define 1st-order triangular mesh
m = m.scaled([2.0, 1.0]) # scale to length 2, height 1
e = ElementTriHermite() # Hermite element, 3 DOF/vertex, 1 interior DOF
basis = Basis(m, e) # combines mesh and element I think


@BilinearForm
def bilinf(u, v, w):
    from skfem.helpers import dd, ddot
    return ddot(dd(u), dd(v)) # double dot product of Hessians of u and v
# Hessian is square matrix of 2nd order PDEs of a scalar field
# I think this part is the main "beam equation" stuff. I think it at least results in the
# 4th order PDEs needed

@LinearForm
def linf(v, w):
    return v*1.0

A = asm(bilinf, basis) # performs finite element assembly with bilinear form, whatever that means
f = asm(linf, basis) # does same with linear form

D = basis.get_dofs("left")

x = solve(*condense(A, f, D=D))

skfem.visuals.matplotlib.plot(basis, x, ax=plt.gca(), colorbar=True, shading='gouraud')

skfem.visuals.matplotlib.draw(m, ax=plt.gca())
plt.show()

# *************** Attempt at openFoam ****************
# mesh = MeshQuad().refined(4) 

# mesh = mesh.scaled([20.0, 20.0])

# basis = skfem.Basis(mesh, skfem.ElementQuad1())
# flow = basis.zeros()
# flow[:] = 0.1


# def plot_query_points(x, ax, style, label):
#     ax.plot(x[0], x[1], style, label=label)
#     return x[0] * 0

# basis.get_dofs(elements=lambda x: plot_query_points(x, plt.gca(), 'ob', 'elements'))
# skfem.visuals.matplotlib.plot(mesh, flow, ax=plt.gca(), colorbar=True, shading = 'gouraud')
# skfem.visuals.matplotlib.draw(mesh, ax=plt.gca())

# plt.show()

