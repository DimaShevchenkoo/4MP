import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = np.linspace(0.1, 1.1)
y = np.linspace(0.8, 0.48)


ax.plot(x, y)
ax.grid()
plt.title("---")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



x1 = np.linspace(0.9, 1.9)
y2 = np.linspace(1.7, 3.2)

ax.plot(x1, y2)
ax.grid()
plt.title('---')
plt.xlabel("x")
plt.ylabel("y")
plt.show()