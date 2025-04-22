# Project 4: ODE
## Introduction
This project compares three different integrators used to solve a simple (undriven and undamped) harmonic oscillator problem. The system consists of a mass $m$ with a single force $F$ acting on it. This force $F$ is dependent only on the position of the mass and a constant $k$. Applying Newton's second law and Hooke's law gives $F = -kx = ma = m\frac{dv}{dt} = \frac{dp}{dt}$. The differential equation $ -kx = \frac{dp}{dt}$ is the one in question for this project. Three methods were used to solve it: Runge-Kutta order 4, Verlet, and scipy's odeint function, whch uses a linear multistep method.

## Results

Plots of momentum vs. time and position vs. time show that the Runge-Kutta method blows up very quickly, likely due to an error in the implementation. The Verlet and odeint methods behave as expected, producing sinusoidal plots. A plot of momentum vs. position using the linear multistep method produces an elliptic plot, as expected for a simple harmonic oscillator in motion. It is expected that the addition of a damping term will reduce the amplitude of oscillations over time. Due to time constraints this has not been implemented. All of these solvers show that the total mechanical energy grows over time.

## Attribution
I used wikipedia and docs.scipy.org.

## Timekeeping
Probably around 10-15 hours in total but I haven't paid close attention.