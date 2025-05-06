# Project 5--FEM
# Adam Grice
# 05-05-2025

from skfem import *
from skfem.models.poisson import unit_load
from skfem.helpers import dd, ddot, trace, eye
import numpy as np
import matplotlib.animation as animation

# m = (MeshTri
#      .init_symmetric()
#      .refined(3)
#      .with_defaults())



m = MeshTri.init_circle(2).refined(3).with_boundaries({'outer': lambda x: np.sqrt(x[0]**2 + x[1]**2) > 0.99})



basis = Basis(m, ElementTriMorley())

d = 0.001
E = 200e9
nu = 0.3



def C(T):
    return E / (1 + nu) * (T + nu / (1 - nu) * eye(trace(T), 2))


@BilinearForm
def bilinf(u, v, _):
    return d ** 3 / 12.0 * ddot(C(dd(u)), dd(v))


@LinearForm
def load(v, w):
    x, y =  w.x
    return v * (np.sin(np.pi * np.sqrt((x**2) + (y**2))))

K = bilinf.assemble(basis)
f = load.assemble(basis)



D = basis.get_dofs()



x = solve(*condense(K, f, D=D))


def visualize():
    from skfem.visuals.matplotlib import draw, plot
    ax = draw(m)
    return plot(basis,
                x,
                ax=ax,
                shading='gouraud',
                colorbar=True,
                nrefs=2)

if __name__ == "__main__":
    visualize().show()
    