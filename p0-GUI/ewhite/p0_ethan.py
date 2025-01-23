import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

fig, ax = plt.subplots()
ax.set_position([0.1, 0.4, 0.8, 0.5])

def submit(expression):
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

axsave = fig.add_axes([0.25, 0.05, 0.1, 0.075])
axload = fig.add_axes([0.45, 0.05, 0.1, 0.075])
axadd = fig.add_axes([0.65, 0.05, 0.1, 0.075])

bsave = Button(axsave, 'Save Values')
bload = Button(axload, 'Load Values')
badd = Button(axadd, 'Add Values')

# bsave.on_clicked()
# bload.on_clicked()
# badd.on_clicked()

axbox1 = fig.add_axes([0.1, 0.15, 0.8, 0.075])
axbox2 = fig.add_axes([0.1, 0.25, 0.8, 0.075])

box1 = TextBox(axbox1, "", textalignment="center")
box2 = TextBox(axbox2, "", textalignment="center")

box1.on_submit(submit)
box2.on_submit(submit)

box1.set_val("put an integer here")
box2.set_val("put another integer here")

plt.show()
