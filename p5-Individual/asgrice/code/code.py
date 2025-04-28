import matplotlib.pyplot as plt
import numpy as np

import skfem
from skfem.helpers import dot, grad
import skfem.visuals.matplotlib

mesh = skfem.MeshTri().refined(1)

# plt.subplots(figsize=(5,5))
# fem.visuals.matplotlib.draw(mesh, ax=plt.gca())

# plt.show()

basis_p1 = skfem.Basis(mesh, skfem.ElementTriP1())
fe_approx = basis_p1.zeros()

fe_approx[:] = 1

plt.subplots(figsize = (6,5))

skfem.visuals.matplotlib.plot(basis_p1, fe_approx, vmin=0, vmax=2, ax=plt.gca(), colorbar = True)
skfem.visuals.matplotlib.draw(mesh, ax=plt.gca())

plt.show()

def on_left_edge(x):
    return x[0] < 0.1

dof_subset_left_edge = basis_p1.get_dofs(facets=on_left_edge)
fe_approx[dof_subset_left_edge] = 0

dof_subset_top_edge = basis_p1.get_dofs(facets=lambda x: x[1] > 0.9)
fe_approx[dof_subset_top_edge] = 3

plt.subplots(figsize = (6,5))
skfem.visuals.matplotlib.plot(basis_p1, fe_approx, vmin=0, vmax=3, ax=plt.gca(), colorbar = True, shading = 'gouraud')
skfem.visuals.matplotlib.draw(mesh, ax=plt.gca())

plt.show()