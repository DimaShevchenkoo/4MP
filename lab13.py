from scipy import integrate
from numpy import *
from math import sin
def f(x):
    return 1/sqrt(1.5 * x + 0.2)
s,err = integrate.quad(f, 1.4, 2.6)
print(f'Rectangle method = {s}')

def f3(x):
    return 1 / sqrt(0.5 + x / 2)

def tr(f3, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f3(a) + f3(b))
    for i in range(1, n + 1):
        sum += f3(a + i + h)
    return sum * h

print(f"Trapezoid = {tr(f3, 1.2, 2.4, 20)}")
s, err = integrate.quad(f3, 1.2, 2.4)
print(f'Trazepoid check = {s}')

def f2(x):
    return (sin(x / (2 - 0.4)))/ (x + 2)
def trf2(f2, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f2(a) + f3(b))
    for i in range(1, n + 1):
        sum += f2(a + i + h)
    return sum * h
print(f'Simpson = {trf2(f2, 0.8, 1.2, 8)}')
s, err = integrate.quad(f2, 0.8, 1.2)
print(f'Simpson check = {s}')