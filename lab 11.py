import matplotlib.pyplot as plt
from numpy import *
import sympy as sp
from math import *
def taylor(x):
    y = 0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    print(f'd1 = {d1}, d2 = {d2}, d3 = {d3}')
    y += f + d1 * x + d2 * (x - 0) ** 2 / 2 + d3 * (x - 0) ** 3 / 6
    print(f'y = {y}')
    return y
x = sp.symbols('x')
f = sp.cos(3 * x) - 3 * x + 3
taylor_x = taylor(x)
p1 = sp.plot(f, taylor_x, (x, -5, 5), label = 'Taylor')
p1.show()