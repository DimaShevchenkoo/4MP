import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
fig, ax = plt.subplots()
x = [1.2, 1.5, 1.9, 2.4, 3.1]
y = [0.82, 1.38, 0.45, 2.67, 1.5]
spl = UnivariateSpline(x, y)
plt.title('Nice')
ax.plot(x, y, label = 'finally')
ax.legend()
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
xs = linspace(0, 4.5, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()