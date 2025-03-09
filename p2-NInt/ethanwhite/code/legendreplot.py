import numpy as np
import matplotlib.pyplot as plt

def p1(x):
        p1 = x
        return p1

def p2(x):
        p2 = (3*x**2-1)/2
        return p2

def p3(x):
        p3 = (5*x**3-3*x)/2
        return p3

def p4(x):
        p4 = (35*x**4-30*x**2+3)/8
        return p4

def legendreplot():
        x = np.linspace(-1,1,100)
        fig, axs = plt.subplots(4,4)

        y = np.array([p1(x),p2(x),p3(x),p4(x)])
        for i in range(0,4):
                for j in range(0,4):
                        title = "P" + str(i+1) + ",P" + str(j+1) + ",P" + str(i+1) + " * P" + str(j+1)
                        label1 = "P" + str(i+1)
                        label2 = "P" + str(j+1)
                        label3 = "P" + str(i+1) + " * P" + str(j+1)

                        axs[i,j].plot(x,y[i],'tab:olive')
                        axs[i,j].plot(x,y[j],'tab:cyan')
                        axs[i,j].plot(x,y[i]*y[j],'tab:pink')
                        axs[i,j].set_title(title)

        fig.tight_layout()
        fig.show()
        return

legendreplot()
