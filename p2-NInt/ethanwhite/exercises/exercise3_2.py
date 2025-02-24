# for exercise 3.2, according to Desmos, integral should be -4.8:
# a) An attempt was made LOL. I'm not really sure why my midpoint formula is wrong.
# b) Done (I did look at Adam's solution to this though to implement the data table.)
# c) Mateo told me the correct number for 6 digit precision is 3100 subintervals. My data table is wrong and inconsistent. :(
import numpy as np
import pylab as py
import pandas as pd
import math

def sin(x):
        f = math.sin(x)
        return f

def midpoint(f,a,b,N):
        sum, h = 0, (b-a)/N
        for i in range(0,N-1):
                x = a + h*i + h/2
                y = sin(x*x)
                sum += h*y
        return sum

N, a, b, f = int(input("\nN = ")), 0, 100, 1
integrate = [0] * 3200
number = [0] * 3200

print("midpoint sum:",midpoint(f,a,b,N))

for i in range(3200):
    integrate[i] = midpoint(f,a,b,i+1)
    number[i] = i

table = {
    'integration' : integrate,
    'subintervals' : number
}

df = pd.DataFrame(table)
print(df)

