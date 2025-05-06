from skfem import *
from skfem.models.poisson import unit_load
from skfem.helpers import dd, ddot, trace, eye
import numpy as np
from skfem.visuals.matplotlib import plot, draw
import matplotlib.pyplot as plt

m = (MeshTri
     .init_symmetric()
     .refined(3)
     .with_defaults())
basis = Basis(m, ElementTriMorley())

d = 0.1
E = 200e9
nu = 0.3


def C(T):
    return E / (1 + nu) * (T + nu / (1 - nu) * eye(trace(T), 2))


@BilinearForm
def bilinf(u, v, _):
    return d ** 3 / 12.0 * ddot(C(dd(u)), dd(v))


@LinearForm
def load(v, _):
    return 1e6 * v


K = bilinf.assemble(basis)
f = load.assemble(basis)

D = np.hstack((
    basis.get_dofs("left"),
    basis.get_dofs({"right", "top"}).all("u"),
))
x = solve(*condense(K, f, D=D))



# def visualize():
#     from skfem.visuals.matplotlib import draw, plot
#     ax = draw(m)
#     return plot(basis,
#                 x,
#                 ax=ax,
#                 shading='gouraud',
#                 colorbar=True,
#                 nrefs=2)

# if __name__ == "__main__":
#     visualize().show()

fig, ax = plt.subplots(figsize=(6, 5))  
draw(basis.mesh, ax=ax)
plot(basis, x, ax=ax, shading='gouraud', colorbar = True)

ax.set_xlabel('x [m]')   
ax.set_ylabel('y [m]')   
ax.set_title('Plate Deflection')  
ax.axis('equal')         

plt.show()