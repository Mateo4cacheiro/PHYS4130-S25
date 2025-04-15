# Finite Element Methods

## Introduction
The finite element method (FEM) is a method for numerically solving partial differential equations (PDEs), especially those in two or three dimensions. This method works by dividing the region over which the PDE is to be solved into a finite number of smaller regions, which together create a "mesh" approximating the original region. Once the initial and boundary conditions have been determined, the PDE is solved numerically for each piece of the mesh, allowing an aggregate solution for the original region to be approximated. This method is commonly used when either the original PDE or the geometry of the region do not allow an analytic solution to be found.

## The Plan
The scope of this project will be to gain some familiarity with an existing FEM python library, use it to create simple meshes, and then solve some PDE using that mesh structure. If time permits, different mesh geometries will be compared for the same problem. The first problem to tackle will be a beam deflection, as the geometry will be very simple. If this goes smoothly, the next step will be to adapt shallowWaterFoam from C++ to python. This project will be done using scikit-fem. The library appears to be well documented and many examples are available online.


https://scikit-fem.readthedocs.io/en/latest/index.html