import math
from scipy import optimize

x0 = 0.1
y0 = 0.8


def f1(y):
    return  1 - math.sin(y) / 2
def f2(x):
    return 0.7 - math.cos(x - 1)
def idk(x, y ,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while abs(xn1- xn) >= e and abs(yn1 - yn) >= e:
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print(xn, yn, 0.0001)
idk(x0, y0, 0.0001)
def b(x):
    return math.sin(x[1]) + 2 * x[0] - 2, math.cos(x[0] - 1) + x[1] - 0.7
a = optimize.root(b, [0, 0], method = 'hybr')
print(a.x)