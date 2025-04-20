---
    Author: Ethan White
    Project: Project 4, Differential Equations Solvers
    Date: 4/20/2025
    Class: PHYS 4130, Spring 2025
---
# Introduction


## Results (varying the damping parameter while using our Verlet integrator)

<figure align="center">
  <img src=Images/PositionsB.png>
  <figcaption align="center">Plot of varying dampening parameters' affect on position vs time, going from 0 to 1.0.</figcaption>
</figure>

<figure align="center">
  <img src=Images/HamiltoniansB.png>
  <figcaption align="center">Plot of varying dampening parameters' affect on hamiltonian vs time, going from 0 to 1.0.</figcaption>
</figure>

<figure align="center">
  <img src=Images/PhasesB.png>
  <figcaption align="center">Plot of varying dampening parameters' affect on the phase space diagram, going from 0 to 1.0.</figcaption>
</figure>

## Results (different solvers and their respective phase diagrams, hamiltonian plots, and position plots)

<figure align="center">
  <img src=Images/SolversPositions.png>
  <figcaption align="center">Plot of Verlet integration, RK4(5), and Adam's ODE methods' position plots, without dampening.</figcaption>
</figure>

<figure align="center">
  <img src=Images/SolversHamiltonian.png>
  <figcaption align="center">Plot of Verlet integration, RK4(5), and Adam's ODE methods' hamiltonian plots, without dampening.</figcaption>
</figure>

<figure align="center">
  <img src=Images/SolversPhases.png>
  <figcaption align="center">Plot of Verlet integration, RK4(5), and Adam's ODE methods' phase space diagrams, without dampening.</figcaption>
</figure>

## Extensions

### Attribution

[1] https://docs.scipy.org/doc/scipy/reference/integrate.html (used towards looking at other SciPy integrators)

[2] 

### Timekeeping

  I spent probably about 20 hours on this project, with 2-3 of which being the writeup. The most time was spent troubleshooting my Verlet solver and understanding how to use the solve_ivp function in the scipyintegrate library. 

### Languages, Libraries, and Lessons Learned

1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?

  I, once again, prioritized using Python since that's what I have done with everything else in the class. :P
  
2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

  I used the Python libraries numpy and math for array/math things, matplotlib.pyplot for plotting, and the scipyintegrate library for the solve_ivp function/different methods of solution.
