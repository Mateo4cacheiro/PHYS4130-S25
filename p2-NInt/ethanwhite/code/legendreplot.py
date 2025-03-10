import numpy as np
import matplotlib.pyplot as plt

def p1(x): # First-order Legendre polynomial
        p1 = x
        return p1

def p2(x): # Second-order Legendre polynomial
        p2 = (3*x**2-1)/2
        return p2

def p3(x): # Third-order Legendre polynomial
        p3 = (5*x**3-3*x)/2
        return p3

def p4(x): # Fourth-order Legendre polynomial
        p4 = (35*x**4-30*x**2+3)/8
        return p4

def legendreplot():
        x = np.linspace(-1,1,100) # Creating the x-axis (identical for all subplots).
        fig, axs = plt.subplots(4,4) # Creating the subplot.

        y = np.array([p1(x),p2(x),p3(x),p4(x)]) # Creating an array of y-values for x-axis.
        for i in range(0,4):
                for j in range(0,4): # Double array to fill in the square.
                        title = "P" + str(i+1) + ",P" + str(j+1) + ",P" + str(i+1) + " * P" + str(j+1) # Titles of individual plots.

                        axs[i,j].plot(x,y[i],'tab:olive') # Filling in the plot (one of the polynomials).
                        axs[i,j].plot(x,y[j],'tab:cyan') # Filling in the plot (another, polynomial).
                        axs[i,j].plot(x,y[i]*y[j],'tab:pink') # Filling in the plot with those two polynomials product.
                        axs[i,j].set_title(title) # Setting the title.

        fig.tight_layout() # No idea what this thing does LOL.
        fig.show() # Showing it.
        return

legendreplot() # Used for testing using ipython.
