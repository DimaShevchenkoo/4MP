import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
import sympy as sp

x = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5]
y = []
XX, YY, XX2, XY, a1, a0, i = 0, 0, 0, 0, 0, 0, 0
while i < len(x):
    y.append(x[i] * np.sin(x[i]))
    i += 1
i = 0
while i < (len(x) - 1):
    XX += x[i]
    YY += y[i]
    XX2 += (x[i]) / 2
    XY += x[i] * y[i]
    i += 1
XX /= len(x)
YY /= len(x)
XX2 /= len(x)
XY /= len(x)
print(f'X avg = {XX}, Y avg = {YY}, XY = {XY}, XX  2 = {XX2}')
a1 = (XY - XX * YY) / (XX2 - XX ** 2)
a0 = YY - a1 * XX
print(f'A1 = {a1}, A0 = {a0}')
def F(x):
    global a1, a0
    f = a0 + a1 * x
    return f
xs = np.array(linspace(0, 1))
f = vectorize(F)
plt.plot(x, y, 'ro', xs, f(xs))
plt.axis([0, 1, 0, 1])
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()