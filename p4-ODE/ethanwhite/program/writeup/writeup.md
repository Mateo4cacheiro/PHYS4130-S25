

---
    Author: Ethan White
    Project: Project 4, Differential Equations Solvers
    Date: 4/20/2025
    Class: PHYS 4130, Spring 2025
---


# Introduction

Ordinary differential equations are one of the most important concepts in physics. It would help, then, to understand how to model these objects computationally. In the previous project 4 notebooks, Euler's method and Runge-Kutta, order 2 (RK2), were explored. In this project, RK4(5) is explored, as well as a linear-multistep algorithm called Adams' backward differentiation formula (Adams-BDF) method. Both of these non-energy-conserving methods were utilized from the SciPy.integrate library. Since, in physics, we also want to conserve energy, symplectic integrators are useful to look at. Verlet integration was explored in this project as well using the Stormer method and some useful numerical differentiation facts. 

```mermaid
    graph TD
        A[Declaring initial conditions] --> B[Verlet function]
        B --> C[Create array of times] --> L[Finding dt from difference in each timestep] 
        B --> D[Creating array of positions]
        B --> E[Creating array of velocities]
        D --> F[Setting initial conditions]
        E --> F
        F --> G[Looping through every element in array]
        G --> H[Predicts the upcoming position using Stormer's method and kinematic equations]
        G --> J[Updates the current velocity uing numerical differentiation]
        H --> K[Arrays filled completely]
        J --> K
        K --> M[Finding potential energy array from the position array values]
        K --> N[Finding kinetic energy array from the velocity array values]
        M --> P[Calculating the Hamiltonian energy array as Potential array + Kinetic array]
        N --> P

        P --> T[Final return values (time, position, velocity, energy)]
        B --> T
        H --> T
        T --> B


```

## Results (varying the damping parameter while using our Verlet integrator)

<figure align="center">
  <img src=Images/PositionsB.png>
  <figcaption align="center">[Figure 1] Plot of varying dampening parameters' affect on position vs time, going from 0 to 1.0. Obviously, as dampening parameter increases, the amplitude of the wave decreases over time faster as well, whereas if there is no dampening, then the amplitude just doesn't decrease (blue wave). </figcaption>
</figure>

<p></p>

<figure align="center">
  <img src=Images/HamiltoniansB.png>
  <figcaption align="center">[Figure 2] Plot of varying dampening parameters' affect on hamiltonian vs time, going from 0 to 1.0. Since the hamiltonian isn't even dependent on the dampening parameter, it's no surprise that energy is lost from the system, so the Hamiltonian is not constant with a non-zero dampening parameter. Ofcourse, with higher dampening parameter, the energy loss is faster. </figcaption>
</figure>

<p></p>

<figure align="center">
  <img src=Images/PhasesB.png>
  <figcaption align="center">[Figure 3] Plot of varying dampening parameters' affect on the phase space diagram, going from 0 to 1.0. For nonzero dampening parameters, the resulting shape is a spiral inwards since the velocity is decreasing disproportionaly faster than the position. The resulting spiral goes to the center much faster for higher dampening parameters. </figcaption>
</figure>

## Results (different solvers and their respective phase diagrams, hamiltonian plots, and position plots)

<figure align="center">
  <img src=Images/SolversPosition.png>
  <figcaption align="center">[Figure 4] Plot of Verlet integration, RK4(5), and Adam's ODE methods' position plots, without dampening. RK4(5) and the Verlet integrator stayed very close in approximation with eachother, but there was a slight phase shift over a long period of time. The Adams' solver actually increased the amplitude of the wave over long periods of time. </figcaption>
</figure>

<p></p>

<figure align="center">
  <img src=Images/SolversHamiltonian.png>
  <figcaption align="center">[Figure 5] Plot of Verlet integration, RK4(5), and Adam's ODE methods' hamiltonian plots, without dampening. As expected, the Verlet solver method remained constant, so energy was not lost out of the system. The RK4(5) method lost energy slowly (not symplectic). The Adams' method did some crazy, non-sinusoidal, non-linear, non-quadratic funky stuff that I can't really conceptualize. This erratic behaviour is why I chose this solver method-- I thought the resulting phase diagram would be cool. </figcaption>
</figure>

<p></p>

<figure align="center">
  <img src=Images/SolversPhase.png>
  <figcaption align="center">[Figure 6] Plot of Verlet integration, RK4(5), and Adam's ODE methods' phase space diagrams, without dampening. The Adams' method slowly went further and further away from the center of the Verlet integrator circle. The RK4(5) method's phase diagram stayed close but also diverged from the Verlet method's phase diagram.</figcaption>
</figure>

## Extensions

### Attribution

[1] https://docs.scipy.org/doc/scipy/reference/integrate.html (used towards looking at other SciPy integrators)

[2] https://scicomp.stackexchange.com/questions/8393/confusion-regarding-the-adam-moulton-and-backwards-differentiation-formula-bdf

[3]

### Timekeeping

  I spent probably about 20 hours on this project, with 2-3 of which being the writeup. The most time was spent troubleshooting my Verlet solver and understanding how to use the solve_ivp function in the scipyintegrate library. 

### Languages, Libraries, and Lessons Learned

1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?

  I, once again, prioritized using Python since that's what I have done with everything else in the class. :P
  
2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

  I used the Python libraries numpy and math for array/math things, matplotlib.pyplot for plotting, and the scipyintegrate library for the solve_ivp function/different methods of solution.
