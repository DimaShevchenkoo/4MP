import numpy as np
import math
from math import factorial
from numpy import *
import matplotlib.pyplot as plt

x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
y = np.array([0.252, 0.293, 0.334, 0.375, 0.416, 0.457])

x1 = 0.1
x2 = 0.9
h = x[1] - x[0]
q = (x1 - 0) / h
q1 = (x2 - 1) / h


def func(y, j):
    mas = []
    for i in range(len(y)):
        mas.append(y[i] - y[i - 1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j -= 1
        return func(mas, j)


yx1 = y[0] - q1 * (func(y, 1)[0]) + (q1 * (q1 - 1) / factorial(2)) * (func(y, 2)[0]) + (
            q1 * (q1 - 1) * (q1 - 2) / factorial(3)) * (func(y, 3)[0]) + (
                  q1 * (q1 - 1) * (q1 - 2) * (q1 - 4) / factorial(4)) * (func(y, 4)[0]) + (
                  q1 * (q1 - 1) * (q1 - 2) * (q1 - 3) * (q1 - 4) / factorial(5)) * (func(y, 5)[0])
yx2 = y[5] - q * (func(y, 1)[4]) + (q * (q - 1) / factorial(2)) * (func(y, 2)[3]) + (
            q * (q - 1) * (q - 2) / factorial(3)) * (func(y, 3)[2]) + (
                  q * (q - 1) * (q - 2) * (q - 4) / factorial(4)) * (func(y, 4)[1]) + (
                  q * (q - 1) * (q - 2) * (q - 3) * (q - 4) / factorial(5)) * (func(y, 5)[0])
print(func(y, 1))

print("The first derivatative:", "\n", yx1)
print("The second derivatative:", "\n", yx2)
mas_x = linspace(0, 1, len(x))
mas_y = y
plt.plot(mas_x, mas_y, 'g-')
plt.scatter(linspace(0, 1, len(x)), y, marker='o')
plt.xticks(np.linspace(0, 1.3, 14))
plt.yticks(np.linspace(0, 7.2, 19))
plt.axis([0, 1.3, 0, 7.2])

plt.plot(x, y, 'o', linestyle='--')
plt.title('Newton interpolation')
plt.grid()
plt.show()
